"""Header language select = ipe_web_kit.langswitch (v0.7.2): one select per page in the header, all 12 languages, the page's own
language selected, same page in each language; privacy/terms only in the footer; no footer language row; dropped-language
addresses (pt zh ar hi ru) are redirect pages that are not in the sitemap."""
import re
import unittest

from helpers import REPO, bs

LANG_DIRS = [l for l in bs.LANGS if l != "en"]
SKIP = ("tests", "scripts", "docs", "ops", "content", "assets", "vendor") + tuple(bs.redirects.LEGACY_REDIRECTS)


def pages():
    out = []
    for p in REPO.rglob("index.html"):
        rel = p.relative_to(REPO).parts
        if rel[0] in SKIP:
            continue
        lang = rel[0] if rel[0] in LANG_DIRS else "en"
        out.append((lang, str(p.relative_to(REPO)), p.read_text(encoding="utf-8")))
    return out


class LangSelect(unittest.TestCase):
    def test_all_languages_have_pages(self):
        self.assertEqual({l for l, _, _ in pages()}, set(bs.LANGS))

    def test_one_select_in_the_header_with_all_languages(self):
        self.assertEqual(len(bs.LANGS), 12)
        for lang, f, h in pages():
            if "/privacy/" in "/" + f:
                continue  # privacy pages come from the kit privacy module with their own layout
            header = re.search(r"<header.*?</header>", h, re.S).group(0)
            self.assertEqual(header.count("<select"), 1, f)
            self.assertEqual(h.count("<select"), 1, f)
            sel = re.search(r"<select[^>]*>(.*?)</select>", header, re.S).group(1)
            opts = re.findall(r'<option value="([^"]*)" lang="([\w-]+)"( selected)?>', sel)
            self.assertEqual([l for _, l, _ in opts], list(bs.LANGS), f)
            self.assertEqual([l for _, l, s in opts if s], [lang], f)

    def test_select_values_are_the_same_page_in_each_language(self):
        for lang, f, h in pages():
            if "/privacy/" in "/" + f:
                continue
            for value, l, _ in re.findall(r'<option value="([^"]*)" lang="([\w-]+)"( selected)?>', h):
                self.assertTrue(value.startswith("/") and value.endswith("/"), (f, value))
                if l == "en":
                    self.assertFalse(value.startswith(tuple("/" + x + "/" for x in LANG_DIRS)), (f, value))
                else:
                    self.assertTrue(value.startswith("/" + l + "/"), (f, l, value))

    def test_privacy_and_terms_only_in_footer(self):
        for lang, f, h in pages():
            if "/privacy/" in "/" + f:
                continue
            nav = re.search(r'<header class="site-header".*?</header>', h, re.S).group(0)
            nav = re.sub(r'<div class="ipe-lang">.*?</div>', "", nav, flags=re.S)
            self.assertIsNone(re.search(r'href="[^"]*/(privacy|terms)/"', nav), f)
            foot = re.search(r'<nav class="foot-links".*?</nav>', h, re.S).group(0)
            self.assertIsNotNone(re.search(r'href="[^"]*/privacy/"', foot), f)
            self.assertIsNotNone(re.search(r'href="[^"]*/terms/"', foot), f)
            self.assertNotIn("foot-langs", h, f)

    def test_no_own_picker_left(self):
        css = (REPO / "assets" / "sunmeld.css").read_text(encoding="utf-8")
        for old in ("langsel", "langsw", "foot-langs"):
            self.assertNotIn(old, css)
        self.assertFalse((REPO / "assets" / "langpick.js").exists())
        self.assertFalse((REPO / "assets" / "sunmeld.js").exists())

    def test_ipe_lang_js_is_the_kit_file(self):
        self.assertEqual((REPO / "assets" / "ipe-lang.js").read_text(encoding="utf-8"), bs.langswitch.JS.read_text(encoding="utf-8"))

    def test_dropped_language_addresses_redirect(self):
        want = {"pt": "pt-BR/", "zh": "zh-Hant/", "ar": "", "hi": "", "ru": ""}
        for old, new in want.items():
            for rest in bs.LEGACY_PATHS:
                f = REPO / old / rest / "index.html"
                self.assertTrue(f.is_file(), f)
                h = f.read_text(encoding="utf-8")
                self.assertIn('http-equiv="refresh"', h)
                self.assertIn("noindex", h)
                if rest == "":
                    self.assertIn('rel="canonical" href="%s/%s"' % (bs.SITE, new), h)
        sm = (REPO / "sitemap.xml").read_text(encoding="utf-8")
        for old in want:
            self.assertNotIn("%s/%s/" % (bs.SITE, old), sm)


if __name__ == "__main__":
    unittest.main()
