# -*- coding: utf-8 -*-
"""Post-build chrome pass — run after build_site.py.

Per page (idempotent: safe to re-run, and a no-op on a page build_site.py has
just written):
  * drops every stylesheet the v9 layer used and ensures assets/css/site.css
    (plus home.css on the homepage)
  * replaces the <header> block with the one navigation used sitewide
  * ensures the progress bar and the four scripts the pages rely on
  * removes app.js / hero-belt.js / hero-*.js if an older page still carries them

Content, sections, copy, images and links inside <main> are never touched.
The header is imported from build_site, so the navigation exists once.
"""
import pathlib
import re

import build_site

ROOT = pathlib.Path(__file__).parent
PAGES = sorted(p.name for p in ROOT.glob("*.html"))

ACTIVE = {
    "pixerio-portfolio.html": "work",
    "blog.html": "insights",
    "about-us.html": "about",
    "contact-us.html": "contact",
}

HEADER_MARK = "<!-- px:header -->"
LEGACY_CSS = ("px.css", "motion.css", "system.css", "hero-belt.css")
LEGACY_JS = ("app", "hero-belt", "hero7", "hero-bg", "hero", "hero-gl", "hero-enter",
             "spine", "sequence", "home-motion", "contact", "site-motion")
SCRIPTS = ["px.js", "pagehead.js", "motion.js"]


def header(page):
    return HEADER_MARK + build_site.header(ACTIVE.get(page, "")) + "\n<!-- /px:header -->"


def transform(html, page):
    # 1. stylesheets: the v10 bundle only
    for legacy in LEGACY_CSS:
        html = re.sub(r'\s*<link rel="stylesheet" href="assets/css/%s(?:\?[^"]*)?">\s*'
                      % re.escape(legacy), "\n", html)
    if "assets/css/site.css" not in html:
        html = html.replace("</head>", '<link rel="stylesheet" href="assets/css/site.css">\n</head>', 1)
    wants_home = page == "index.html"
    has_home = "assets/css/home.css" in html
    if wants_home and not has_home:
        html = re.sub(r'(<link rel="stylesheet" href="assets/css/site\.css[^"]*">)',
                      r'\1\n<link rel="stylesheet" href="assets/css/home.css">', html, count=1)
    if not wants_home and has_home:
        html = re.sub(r'\s*<link rel="stylesheet" href="assets/css/home\.css(?:\?[^"]*)?">\s*', "\n", html)

    # 2. header: one navigation, marked so the swap stays idempotent
    head_pat = re.compile(
        r'(?:<!-- px:header -->)?\s*<header class="site-header">.*?</header>\s*(?:<!-- /px:header -->)?',
        re.S)
    if head_pat.search(html):
        html = head_pat.sub(lambda m: header(page), html, count=1)
    else:
        html = html.replace('<main id="main">', header(page) + '\n<main id="main">', 1)

    # 3. scroll-progress bar
    if 'class="progress"' not in html:
        html = re.sub(r'(<a class="skip" href="#main">Skip to content</a>)',
                      r'\1\n<div class="progress" aria-hidden="true"></div>', html, count=1)

    # 4. scripts: the four the pages need, nothing else
    html = re.sub(r'\s*<script src="assets/js/(%s)\.js"[^>]*></script>' % "|".join(LEGACY_JS), "", html)
    for js in SCRIPTS:
        if "assets/js/%s" % js not in html:
            html = html.replace("</body>", '<script src="assets/js/%s" defer></script>\n</body>' % js, 1)
    return html


def main():
    changed = 0
    for page in PAGES:
        p = ROOT / page
        src = p.read_text(encoding="utf-8")
        out = transform(src, page)
        if out != src:
            p.write_text(out, encoding="utf-8")
            changed += 1
            print("updated", page)
    print("%d/%d pages updated" % (changed, len(PAGES)))


if __name__ == "__main__":
    main()
