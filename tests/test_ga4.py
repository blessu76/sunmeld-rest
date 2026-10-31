"""GA4: one snippet per generated page, and the privacy / support / llms.txt text that must match it."""
import re
import shutil
import unittest

from helpers import build, bs, make_site

GA_ID = "G-XG4BH800J0"
LANGS = ["en", "ko"]


class Ga4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = make_site()
        cls.ctx = build(cls.root)
        cls.pages = {str(p.relative_to(cls.root)): p.read_text(encoding="utf-8") for p in cls.root.rglob("*.html")
                     if not str(p.relative_to(cls.root)).startswith(("assets/", "content/"))}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, True)

    def page(self, lang, rel):
        return self.pages[(lang + "/" if lang != "en" else "") + rel + "index.html"]

    def test_constant_is_the_ipe_rest_property(self):
        self.assertEqual(bs.GA_MEASUREMENT_ID, GA_ID)

    def test_every_generated_page_has_the_snippet_once(self):
        self.assertIn("404.html", self.pages)
        self.assertGreater(len(self.pages), 14)
        for rel, text in self.pages.items():
            with self.subTest(rel):
                self.assertEqual(text.count(GA_ID), 1)
                self.assertEqual(text.count("googletagmanager.com/gtag/js"), 1)
                self.assertLess(text.index(GA_ID), text.index("</body>"))
                self.assertEqual(text.count("window.gtag('config',GA_ID)"), 1)

    def test_no_snippet_outside_html(self):
        for rel in ("assets/sunmeld.js", "assets/sunmeld.css"):
            self.assertNotIn(GA_ID, (self.root / rel).read_text(encoding="utf-8"))

    def test_privacy_matches_the_tracking(self):
        for lang in LANGS:
            text = self.page(lang, "privacy/")
            with self.subTest(lang):
                self.assertIn("Google Analytics", text)
                self.assertIn("_ga", text)
                self.assertIn("https://tools.google.com/dlpage/gaoptout", text)
                self.assertIn("sm-lang", text)
                self.assertIn(bs.EFFECTIVE, text)

    def test_privacy_sources_are_dated_with_effective(self):
        for lang in LANGS:
            src = (self.root / "content/pages" / lang / "privacy.md").read_text(encoding="utf-8")
            with self.subTest(lang):
                self.assertIn("updated: " + bs.EFFECTIVE, src)

    def test_terms_keep_their_own_effective_date(self):
        for lang in LANGS:
            self.assertIn(bs.TERMS_EFFECTIVE, self.page(lang, "terms/"))

    def test_no_stale_no_tracking_claims_about_the_site(self):
        stale = re.compile(r"uses no cookies|no analytics or advertising tags|do not collect your personal information|"
                           r"쿠키를 사용하지 않|분석 도구나 광고 태그를 넣지|웹사이트는 이용자의 개인정보를 수집하지", re.I)
        for rel in ("privacy/", "support/"):
            for lang in LANGS:
                with self.subTest(lang + rel):
                    self.assertIsNone(stale.search(self.page(lang, rel)))
        self.assertNotIn("No tracking", (self.root / "llms.txt").read_text(encoding="utf-8"))

    def test_support_faq_mentions_google_analytics(self):
        for lang in LANGS:
            with self.subTest(lang):
                self.assertIn("Google Analytics", self.page(lang, "support/"))

    def test_app_sentence_stays_app_only(self):
        self.assertIn("contains no advertising, analytics or tracking SDKs", self.page("en", "privacy/"))
        self.assertIn("추적 SDK가 포함되어 있지 않습니다", self.page("ko", "privacy/"))

    def test_llms_txt_says_so(self):
        text = (self.root / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("website collects only basic visit statistics through Google Analytics", text)


if __name__ == "__main__":
    unittest.main()
