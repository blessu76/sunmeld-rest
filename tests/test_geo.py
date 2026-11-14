"""GEO/SEO checks on the real generated site: JSON-LD, FAQ, sitemap, feeds, llms.txt, robots.txt (reads the repo as committed)."""
import json
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from helpers import REPO
import build_site as bs

LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
POST_FIELDS = ("headline", "author", "datePublished", "dateModified", "inLanguage", "image", "mainEntityOfPage", "about", "description", "url")


def post_pages():
    for slug_dir in sorted((REPO / "journal").glob("*/index.html")) + sorted((REPO / "ko" / "journal").glob("*/index.html")):
        if slug_dir.parent.name == "page":
            continue
        yield slug_dir


def graph_of(path):
    blocks = LD.findall(path.read_text(encoding="utf-8"))
    assert len(blocks) == 1, "%s: expected one JSON-LD block, got %d" % (path, len(blocks))
    return json.loads(blocks[0].replace("<\\/", "</"))["@graph"]


class JsonLd(unittest.TestCase):
    def test_every_html_page_parses(self):
        n = 0
        for f in REPO.rglob("*.html"):
            if {"vendor", ".git", "assets", "content"} & set(f.relative_to(REPO).parts) or f.name == "404.html" or f.relative_to(REPO).parts[0] in bs.redirects.LEGACY_REDIRECTS:  # legacy redirect pages carry no JSON-LD
                continue
            graph_of(f)
            n += 1
        self.assertGreater(n, 50)

    def test_posts_have_blogposting_with_game(self):
        pages = list(post_pages())
        self.assertGreaterEqual(len(pages), 26)
        for f in pages:
            node = next((x for x in graph_of(f) if x["@type"] == "BlogPosting"), None)
            self.assertIsNotNone(node, f)
            for k in POST_FIELDS:
                self.assertTrue(node.get(k), "%s: missing %s" % (f, k))
            about = node["about"]
            self.assertEqual(about["@type"], "VideoGame")
            for k in ("name", "genre", "gamePlatform"):
                self.assertTrue(about.get(k), "%s: about.%s" % (f, k))
            self.assertRegex(node["dateModified"], r"^\d{4}-\d{2}-\d{2}")
            self.assertGreaterEqual(node["dateModified"][:10], node["datePublished"][:10])

    def test_posts_have_unique_title_description_canonical_hreflang(self):
        seen = {"t": set(), "d": set(), "c": set()}
        for f in post_pages():
            h = f.read_text(encoding="utf-8")
            t = re.search(r"<title>(.*?)</title>", h).group(1)
            d = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
            c = re.search(r'<link rel="canonical" href="(.*?)">', h).group(1)
            for key, v in (("t", t), ("d", d), ("c", c)):
                self.assertNotIn(v, seen[key], f)
                seen[key].add(v)
            self.assertIn('hreflang="x-default"', h)
            self.assertIn('hreflang="en"', h)
            self.assertIn('hreflang="ko"', h)
            for needle in ('property="og:title"', 'property="og:image"', 'name="twitter:card"'):
                self.assertIn(needle, h, f)

    def test_every_post_has_faq_section_and_faqpage(self):
        for f in post_pages():
            g = graph_of(f)
            faq = next((x for x in g if x["@type"] == "FAQPage"), None)
            self.assertIsNotNone(faq, "%s: no FAQ section (H2 FAQ / 자주 묻는 질문 with H3 questions)" % f)
            self.assertGreaterEqual(len(faq["mainEntity"]), 2, f)
            for q in faq["mainEntity"]:
                self.assertTrue(q["name"] and q["acceptedAnswer"]["text"], f)
            self.assertIn("<h2>", f.read_text(encoding="utf-8"))

    def test_first_paragraph_names_game_and_platform(self):
        for src in sorted((REPO / "content" / "journal").glob("*/*.md")):
            _, body = bs.parse_front(src.read_text(encoding="utf-8"))
            first = body.split("\n\n")[0]
            self.assertRegex(first, r"Sunmeld|썬멜드|サンメルド", src)
            self.assertIn("iOS", first, src)


class FaqParser(unittest.TestCase):
    def test_pairs(self):
        body = "Intro.\n\n## What\n\ntext\n\n## FAQ\n\n### Q1?\n\nA **one**.\n\nmore\n\n### Q2?\n\n- a\n\n## After\n\n### not a question\n\nx\n"
        self.assertEqual(bs.faq_pairs(body), [("Q1?", "A one. more"), ("Q2?", "a")])
        self.assertEqual(bs.faq_pairs("## What\n\n### Q?\n\nA\n"), [])

    def test_sss_heading_is_faq(self):
        self.assertEqual(bs.faq_pairs("## SSS\n\n### Q?\n\nA\n"), [("Q?", "A")])

    def test_updated_front_matter_sets_date_modified(self):
        import helpers
        root = helpers.make_site(posts=(("alpha-post", "2026-11-01T18:00+09:00"),))
        f = root / "content" / "journal" / "alpha-post" / "en.md"
        f.write_text(f.read_text(encoding="utf-8").replace("category: devlog\n", "category: devlog\nupdated: 2026-11-02\n", 1), encoding="utf-8")
        posts, errs = bs.load_posts(root, now=helpers.NOW)
        self.assertEqual(errs, [])
        self.assertEqual(posts[0]["updated"], "2026-11-02")


class SiteFiles(unittest.TestCase):
    def test_sitemap_has_journal_and_every_post_in_both_languages(self):
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        root = ET.parse(REPO / "sitemap.xml").getroot()
        locs = {u.find("s:loc", ns).text: u.find("s:lastmod", ns).text for u in root.findall("s:url", ns)}
        self.assertIn(bs.SITE + "/journal/", locs)
        self.assertIn(bs.SITE + "/ko/journal/", locs)
        for d in (REPO / "content" / "journal").iterdir():
            for l in ("en", "ko"):
                self.assertIn(bs.url(bs.path_post(l, d.name)), locs)
        for v in locs.values():
            self.assertRegex(v, r"^\d{4}-\d{2}-\d{2}$")

    def test_feeds_are_valid_rss_with_all_posts(self):
        n = len(list((REPO / "content" / "journal").iterdir()))
        for rel in ("journal/feed.xml", "ko/journal/feed.xml"):
            root = ET.parse(REPO / rel).getroot()
            self.assertEqual(root.tag, "rss")
            items = root.findall("./channel/item")
            self.assertEqual(len(items), n, rel)
            for it in items:
                for tag in ("title", "link", "guid", "pubDate", "description"):
                    self.assertTrue((it.findtext(tag) or "").strip(), "%s %s" % (rel, tag))

    def test_feed_alternate_links(self):
        for rel in ("index.html", "journal/index.html", "ko/index.html", "ko/journal/index.html", "de/index.html"):
            h = (REPO / rel).read_text(encoding="utf-8")
            self.assertRegex(h, r'<link rel="alternate" type="application/rss\+xml"[^>]*href="/(ko/)?journal/feed\.xml"', rel)

    def test_home_and_about_link_to_journal(self):
        for rel in ("index.html", "about/index.html", "ko/index.html", "ko/about/index.html"):
            h = (REPO / rel).read_text(encoding="utf-8")
            self.assertRegex(h, r'href="/(ko/)?journal/"', rel)

    def test_llms_txt_lists_journal(self):
        t = (REPO / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("/journal/", t)
        self.assertIn("/journal/feed.xml", t)
        for d in (REPO / "content" / "journal").iterdir():
            self.assertIn("/journal/%s/" % d.name, t)

    def test_robots_does_not_block_ai_crawlers(self):
        t = (REPO / "robots.txt").read_text(encoding="utf-8")
        self.assertNotRegex(t, r"(?im)^\s*Disallow:\s*/\s*$")
        for bot in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"):
            m = re.search(r"User-agent: %s\n((?:(?!User-agent).*\n?)*)" % bot, t)
            self.assertIsNotNone(m, bot)
            self.assertIn("Allow: /", m.group(1))
            self.assertNotIn("Disallow", m.group(1))
        self.assertIn("Sitemap: https://sunmeld.ipe.rest/sitemap.xml", t)


if __name__ == "__main__":
    unittest.main()
