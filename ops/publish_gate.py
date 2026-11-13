#!/usr/bin/env python3
"""Random-afternoon publish gate. launchd calls this every 15 minutes (12:00-18:45 KST); it decides whether ops/publish_daily.sh runs now.

State file (default ~/.ipe/queue/sunmeld/slot.json):
  {"date": "YYYY-MM-DD", "time": "HH:MM", "prev_date": ..., "prev_time": ..., "published": true|false}
Rules
  - date != today (KST): draw today's time uniformly from 12:00-17:59, never in the same hour as yesterday's time; yesterday goes to prev_*; published=false.
  - published already: nothing. now < time: nothing. Otherwise run publish_daily.sh.
  - published=true only when that run exited 0 AND its log shows a post is out ("publish_daily: pushed" or "already published today").
    SKIP / QUEUE_EMPTY / non-zero exit / "nothing to publish" keep published=false, so the next 15-minute tick retries.
Test hooks: SUNMELD_SLOT_FILE, SUNMELD_PUBLISH_SCRIPT, SUNMELD_NOW ("YYYY-MM-DD HH:MM", KST), SUNMELD_SLOT_SEED.
"""
import json
import os
import random
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
KST = timezone(timedelta(hours=9))
FIRST_HOUR, LAST_HOUR = 12, 17
OK_MARKERS = ("publish_daily: pushed ", "publish_post: already published today")


def now_kst():
    s = os.environ.get("SUNMELD_NOW")
    if s:
        return datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=KST)
    return datetime.now(KST)


def log(msg):
    print("[%s KST] publish_gate: %s" % (now_kst().strftime("%Y-%m-%d %H:%M:%S"), msg), flush=True)


def slot_path():
    return Path(os.environ.get("SUNMELD_SLOT_FILE") or Path.home() / ".ipe" / "queue" / "sunmeld" / "slot.json")


def load(path):
    try:
        d = json.loads(path.read_text())
        return d if isinstance(d, dict) else None
    except (OSError, ValueError):
        return None


def save(path, d):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    os.replace(tmp, path)


def draw_time(prev_time, rng):
    """HH:MM within 12:00-17:59, hour different from prev_time's hour."""
    prev_hour = None
    try:
        prev_hour = int(str(prev_time).split(":")[0])
    except (ValueError, IndexError):
        pass
    hours = [h for h in range(FIRST_HOUR, LAST_HOUR + 1) if h != prev_hour]
    return "%02d:%02d" % (rng.choice(hours), rng.randrange(60))


def main():
    now = now_kst()
    today = now.strftime("%Y-%m-%d")
    path = slot_path()
    st = load(path)
    if st is None:
        # first run: today counts as published (the 2026-11-13 post went out 21:15), the random schedule starts tomorrow
        st = {"date": today, "time": "21:15", "prev_date": today, "prev_time": "21:15", "published": True}
        save(path, st)
        log("created %s (today treated as published)" % path)
        return 0
    if st.get("date") != today:
        seed = os.environ.get("SUNMELD_SLOT_SEED")
        rng = random.Random(seed) if seed else random.Random()
        new = draw_time(st.get("time"), rng)
        st = {"date": today, "time": new, "prev_date": st.get("date"), "prev_time": st.get("time"), "published": False}
        save(path, st)
        log("new slot for %s: %s (yesterday %s)" % (today, new, st["prev_time"]))
    if st.get("published"):
        return 0
    if now.strftime("%H:%M") < st["time"]:
        log("not yet (slot %s)" % st["time"])
        return 0
    script = os.environ.get("SUNMELD_PUBLISH_SCRIPT") or str(HERE / "publish_daily.sh")
    log("slot %s reached — running %s" % (st["time"], script))
    r = subprocess.run(["/bin/bash", script], capture_output=True, text=True)
    out = (r.stdout or "") + (r.stderr or "")
    sys.stdout.write(out)
    if r.returncode == 0 and any(m in out for m in OK_MARKERS):
        st["published"] = True
        save(path, st)
        log("published — slot closed for %s" % today)
        return 0
    log("not published (exit %d) — will retry on the next tick" % r.returncode)
    return 0 if r.returncode == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
