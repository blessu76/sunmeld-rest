"""ops/publish_gate.py: random afternoon slot, hour rotation, retry rules (publish_daily.sh replaced by a stub)."""
import json
import os
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from helpers import REPO

GATE = REPO / "ops" / "publish_gate.py"
sys.path.insert(0, str(REPO / "ops"))
import publish_gate  # noqa: E402


class Gate(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="sunmeld-gate-"))
        self.slot = self.tmp / "q" / "slot.json"
        self.stub = self.tmp / "stub.sh"
        self.calls = self.tmp / "calls"
        self.set_stub("echo '[x] publish_daily: pushed some-slug'")

    def set_stub(self, body, rc=0):
        self.stub.write_text("echo run >> %s\n%s\nexit %d\n" % (self.calls, body, rc))

    def run_gate(self, now, seed="1"):
        env = {**os.environ, "SUNMELD_SLOT_FILE": str(self.slot), "SUNMELD_PUBLISH_SCRIPT": str(self.stub),
               "SUNMELD_NOW": now, "SUNMELD_SLOT_SEED": seed}
        return subprocess.run([sys.executable, str(GATE)], env=env, capture_output=True, text=True)

    def state(self):
        return json.loads(self.slot.read_text())

    def write(self, **kw):
        self.slot.parent.mkdir(parents=True, exist_ok=True)
        self.slot.write_text(json.dumps(kw))

    def ran(self):
        return self.calls.read_text().count("run") if self.calls.exists() else 0

    def test_first_run_creates_published_today(self):
        self.run_gate("2026-11-13 22:00")
        s = self.state()
        self.assertEqual((s["date"], s["time"], s["published"]), ("2026-11-13", "21:15", True))
        self.assertEqual(self.ran(), 0)

    def test_new_day_draws_slot_in_window_and_excludes_yesterdays_hour(self):
        for i in range(60):   # repeat: 12:00-17:59 and never yesterday's hour
            prev_hour = 12 + i % 6
            self.write(date="2026-11-13", time="%02d:30" % prev_hour, prev_date=None, prev_time=None, published=True)
            self.run_gate("2026-11-14 00:05", seed=str(i))
            s = self.state()
            h = int(s["time"].split(":")[0])
            self.assertTrue(12 <= h <= 17, s)
            self.assertNotEqual(h, prev_hour, s)
            self.assertEqual((s["date"], s["prev_date"], s["prev_time"], s["published"]),
                             ("2026-11-14", "2026-11-13", "%02d:30" % prev_hour, False))

    def test_draw_time_after_late_evening_slot_any_hour(self):
        hours = {int(publish_gate.draw_time("21:15", random.Random(i)).split(":")[0]) for i in range(200)}
        self.assertEqual(hours, set(range(12, 18)))

    def test_date_rollover_resets_published(self):
        self.write(date="2026-11-14", time="13:00", prev_date="2026-11-13", prev_time="21:15", published=True)
        self.run_gate("2026-11-15 12:00")
        s = self.state()
        self.assertEqual((s["date"], s["prev_time"], s["published"]), ("2026-11-15", "13:00", False))

    def test_already_published_is_ignored(self):
        self.write(date="2026-11-14", time="13:00", prev_date=None, prev_time=None, published=True)
        self.run_gate("2026-11-14 18:00")
        self.assertEqual(self.ran(), 0)
        self.assertTrue(self.state()["published"])

    def test_before_slot_time_does_not_publish(self):
        self.write(date="2026-11-14", time="15:20", prev_date=None, prev_time=None, published=False)
        self.run_gate("2026-11-14 15:15")
        self.assertEqual(self.ran(), 0)
        self.assertFalse(self.state()["published"])

    def test_at_or_after_slot_publishes_and_marks(self):
        self.write(date="2026-11-14", time="15:20", prev_date=None, prev_time=None, published=False)
        self.run_gate("2026-11-14 15:30")
        self.assertEqual(self.ran(), 1)
        self.assertTrue(self.state()["published"])
        self.run_gate("2026-11-14 15:45")   # closed: no second run
        self.assertEqual(self.ran(), 1)

    def test_failure_keeps_unpublished_then_retry_succeeds(self):
        self.write(date="2026-11-14", time="15:20", prev_date=None, prev_time=None, published=False)
        self.set_stub("echo '[x] publish_daily: FAIL — green gate'", rc=1)
        r = self.run_gate("2026-11-14 15:30")
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(self.state()["published"])
        self.set_stub("echo '[x] publish_daily: pushed s'")
        self.run_gate("2026-11-14 15:45")
        self.assertTrue(self.state()["published"])
        self.assertEqual(self.ran(), 2)

    def test_skip_and_queue_empty_do_not_mark_published(self):
        self.write(date="2026-11-14", time="15:20", prev_date=None, prev_time=None, published=False)
        for line in ("publish_daily: SKIP — working tree is not clean", "publish_daily: QUEUE_EMPTY — no post left"):
            self.set_stub("echo '[x] %s'" % line)
            self.run_gate("2026-11-14 16:00")
            self.assertFalse(self.state()["published"], line)

    def test_already_published_today_by_hand_closes_slot(self):
        self.write(date="2026-11-14", time="15:20", prev_date=None, prev_time=None, published=False)
        self.set_stub("echo 'publish_post: already published today (2026-11-14 10:00) — nothing to do'")
        self.run_gate("2026-11-14 16:00")
        self.assertTrue(self.state()["published"])


if __name__ == "__main__":
    unittest.main()
