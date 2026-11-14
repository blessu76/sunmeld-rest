"""Header language <select> and footer legal links: on every built page the nav has no privacy/terms link,
the footer has both, the language select lists all languages with the page's own one selected, and the
old footer language row is gone (the same choice is in the select, with a noscript link list in the header)."""
import re
import unittest

from helpers import REPO, bs
from test_langpicker import pages


class LangSelect(unittest.TestCase):
    def test_privacy_and_terms_only_in_footer(self):
        for lang, f, h in pages():
            nav = re.search(r'<nav class="nav".*?</nav>', h, re.S).group(0).split('<span class="langsel"')[0]
            self.assertIsNone(re.search(r'href="[^"]*/(privacy|terms)/"', nav), f)
            foot = re.search(r'<nav class="foot-links".*?</nav>', h, re.S).group(0)
            self.assertIsNotNone(re.search(r'href="[^"]*/privacy/"', foot), f)
            self.assertIsNotNone(re.search(r'href="[^"]*/terms/"', foot), f)

    def test_language_select_has_all_languages_and_current_selected(self):
        self.assertEqual(len(bs.LANGS), 12)
        for lang, f, h in pages():
            sel = re.search(r'<span class="langsel" hidden><select aria-label="[^"]+">(.*?)</select></span>', h, re.S)
            self.assertIsNotNone(sel, f)
            opts = re.findall(r'<option value="([^"]*)" data-lang="([\w-]+)"( selected)?>', sel.group(1))
            self.assertEqual(len(opts), 12, f)
            self.assertEqual([d for _, d, _ in opts], list(bs.LANGS), f)
            self.assertEqual([d for _, d, s in opts if s], [lang], f)

    def test_select_values_are_the_same_page_in_each_language(self):
        for lang, f, h in pages():
            sel = re.search(r'<select aria-label="[^"]+">(.*?)</select>', h, re.S).group(1)
            for value, l in re.findall(r'<option value="([^"]*)" data-lang="([\w-]+)"', sel):
                self.assertTrue(value.startswith("/") and value.endswith("/"), (f, value))
                if l == "en":
                    self.assertFalse(value.startswith(tuple("/" + x + "/" for x in bs.LANGS if x != "en")), (f, value))
                else:
                    self.assertTrue(value.startswith("/" + l + "/"), (f, l, value))

    def test_no_footer_language_row(self):
        for lang, f, h in pages():
            self.assertNotIn("foot-langs", h, f)
        self.assertNotIn("foot-langs", (REPO / "assets" / "sunmeld.css").read_text(encoding="utf-8"))

    def test_noscript_link_list_keeps_language_links(self):
        for lang, f, h in pages():
            ns = re.search(r'<noscript><span class="langsw".*?</noscript>', h, re.S).group(0)
            self.assertEqual(len(re.findall(r'<a href="[^"]*" hreflang="[\w-]+"', ns)), 12, f)


if __name__ == "__main__":
    unittest.main()
