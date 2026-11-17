"""Rebuild the two CSS bundles from assets/css/src.  python tools/build-css.py

v10 composition:
  site.css  tokens.css (brand hues, focus, selection) + v10.css (the design system)
  home.css  v10-home.css (statement hero, six-service rail, home-only blocks)

The v9 sources (px.css, pagehead.css, site-motion.css, service.css, editorial.css,
backgrounds.css, hero7.css, home-motion.css, sequence.css, spine.css) stay on disk as
the previous record but are no longer part of either bundle.
"""
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "assets", "css")
SITE = ["tokens.css", "v10.css"]
HOME = ["v10-home.css"]
BANNER = "/* Pixerio bundle - generated from assets/css/src/*.css. Edit the sources. */\n\n"


def build(name, parts):
    body = BANNER + "\n".join(
        "/* ---- %s ---- */\n%s" % (p, open(os.path.join(BASE, "src", p), encoding="utf-8").read())
        for p in parts if os.path.exists(os.path.join(BASE, "src", p))
    )
    with open(os.path.join(BASE, name), "w", encoding="utf-8", newline="") as f:
        f.write(body)
    print("wrote", name, len(body) // 1024, "KB")


if __name__ == "__main__":
    build("site.css", SITE)
    build("home.css", HOME)
