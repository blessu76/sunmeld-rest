"""Web kit (vendor/ipe_web_kit) — the copy is untouched, pinned to a tag, and imported from vendor/ (indexnow only)."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import indexnow  # noqa: E402  (the shim puts vendor/ on sys.path)
from ipe_web_kit import __version__ as KIT_VERSION, indexnow as kit_indexnow  # noqa: E402


class KitVendor(unittest.TestCase):
    def test_vendor_copy_is_unmodified(self):
        r = subprocess.run([sys.executable, str(ROOT / "vendor" / "ipe_web_kit" / "vendor.py"), "verify", str(ROOT)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_pinned_tag(self):
        stamp = (ROOT / "vendor" / "ipe_web_kit" / "KIT_VERSION").read_text(encoding="utf-8").split()
        self.assertEqual(stamp[0], "v" + KIT_VERSION)
        self.assertRegex(stamp[1], r"^[0-9a-f]{40}$")

    def test_imports_come_from_vendor(self):
        self.assertTrue(Path(kit_indexnow.__file__).resolve().is_relative_to((ROOT / "vendor").resolve()))
        self.assertEqual(indexnow.find_key.__module__, "ipe_web_kit.indexnow")


if __name__ == "__main__":
    unittest.main()
