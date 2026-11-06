# sunmeld-rest

Sunmeld (F-020) official site, https://sunmeld.ipe.rest. Static, GitHub Pages, generator `scripts/build_site.py` (stdlib only, Python 3.8+ compatible).
- 공통 웹 킷 ipe_web_kit 은 비공개라 소스를 커밋하지 않는다 — `vendor/ipe_web_kit.lock` 만 커밋, 설치는 `python3 scripts/kit_lock.py sync --kit <킷 클론>`(README).

- Never hand-edit generated files (`index.html`, `about/`, `privacy/`, `support/`, `terms/`, `releases/`, `journal/`, `ko/`, `sitemap.xml`, `robots.txt`, `llms.txt`, `404.html`). Edit `content/` or the generator, then run `python3 scripts/build_site.py`.
- Green gate before every commit: `bash scripts/check.sh` must print GREEN. UI check: `tests/ui_check.js` (see README).
- Bump `ASSET_V` in `build_site.py` when `assets/sunmeld.css` or `sunmeld.js` change; bump `SITE_UPDATED` when home/releases/404 text changes; each page's "Last updated" is its front matter `updated:`.
- Content rules: game facts only from SUNMELD_DOCS core rules, kept generic (shared tub, turns, same-stage stones merge from dust to sun, merger scores, overflow loses for the last placer, AI opponents with own habits, in development for iOS/Android, free to try + one purchase + no ads). No price, no release date, no opponent names, no numbers for turn timers or counts, no ratings, no emoji, never the words Suika / 수박게임 / Watermelon game (the build rejects them).
- Privacy / terms / support derive from iltonggi-rest with the app name swapped; do not add new clauses without the owner's decision.
- Journal publishes daily at 18:00 KST via `ops/` (template only; launchd is installed by the maintainer, never by this repo). GA4 is on (measurement ID G-XG4BH800J0, same property as ipe.rest; one `GA_SNIPPET` in `build_site.py` inserted into every page by `render()`). The privacy policy section 2, the support FAQ and llms.txt are written to match — change them together with the snippet. The app itself has no analytics: keep app sentences app-only.
- No `docs/` folder and no planning markdown in this repo.
