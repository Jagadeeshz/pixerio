# -*- coding: utf-8 -*-
"""
Pixerio reference UI — build v10

Design direction: UI structure from Design Pickle (dark statement band, oversized
claim, paired pill controls, bleeding media rail, two-up panels, dotted threads),
storytelling from ServiceNow (capability → scenario → evidence), and colour, type,
radius and logo from the Pixerio guidelines in README §2.

Section map:
  §1.2  six services, split by service in the navigation, outcome-led
  §1.3  keep the URL structure, the project photography and the process
  §2.2  white / logo blue / logo green
  §2.4  type scale, §2.5 1200px grid, §2.6 components
  §2.9  homepage treatment, section by section
  §3.3  URLs stay put — filenames mirror the live paths
  §3.5  WebP with fallbacks, preloaded Inter, eager hero
  §4.8  one action, repeated: "Discuss Your Project", plus six service variants

Output: 17 pages, styled by assets/css/site.css (+ home.css on index), built from
assets/css/src by tools/build-css.py. After editing, run:
    python tools/build-css.py && python build_site.py && python px_apply.py
"""
import pathlib

ROOT = pathlib.Path(__file__).parent

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true">'
         '<path d="M7 17 17 7M9 7h8v8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW_R = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true">'
           '<path d="M5 12h14M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">'
         '<path d="m4 12 5 5L20 6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------------------------------------------------------------- icons
IC = {
    "brand": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
             '<rect x="3" y="3" width="7" height="7" rx="1.4"/><rect x="14" y="3" width="7" height="7" rx="1.4"/>'
             '<rect x="3" y="14" width="7" height="7" rx="1.4"/><circle cx="17.5" cy="17.5" r="3.5"/></svg>',
    "digital": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
               '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M2.5 8.5h19M8 21h8" stroke-linecap="round"/>'
               '<circle cx="5.5" cy="6.2" r=".7" fill="currentColor" stroke="none"/></svg>',
    "video": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
             '<rect x="2.5" y="6" width="13" height="12" rx="2"/><path d="m15.5 10.5 5-3v9l-5-3z" stroke-linejoin="round"/>'
             '<path d="M7 2.8 9.5 6M12 2.8 14.5 6" stroke-linecap="round"/></svg>',
    "3d": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
          '<path d="M12 2.6 21 7.3v9.4L12 21.4 3 16.7V7.3z" stroke-linejoin="round"/>'
          '<path d="M3 7.3l9 4.7 9-4.7M12 12v9.4" stroke-linejoin="round"/></svg>',
    "learning": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
                '<path d="M3 5.5h7a3 3 0 0 1 3 3V21a2.5 2.5 0 0 0-2.5-2.5H3z" stroke-linejoin="round"/>'
                '<path d="M21 5.5h-7a3 3 0 0 0-3 3V21a2.5 2.5 0 0 1 2.5-2.5H21z" stroke-linejoin="round"/></svg>',
    "search": '<svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
              '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5" stroke-linecap="round"/>'
              '<path d="M7.5 11.5 9.4 13l3.6-4.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

# ---------------------------------------------------------------- services (§1.2)
# slug mirrors the live path (§3.3). cta is the §4.8 wording, verbatim.
SERVICES = [
    dict(slug="3d-visualization", nav="3D and immersive", num="01", icon="3d",
         name="3D and immersive",
         buy="A space or a product shown before it exists.",
         covers=["3D modelling and rendering", "Architectural and product visualisation",
                 "Walkthroughs and 360&#176; tours", "Storyboarding and conceptual frameworks",
                 "AR and VR"],
         h1="Show a space or a product before it exists.",
         sub="Modelling, rendering, walkthroughs and AR: the version of the project a client can "
             "approve before anything is built.",
         cta="Have a product or a space to present? Talk to us about 3D visualisation.",
         outcome="Decisions get made on the render instead of on the site visit.",
         faqs=[("What is the process for 3D visualisation?",
                "Concept and storyboard, then modelling, then lighting and render passes, then "
                "review with you. Each stage is approved before the next one starts."),
               ("How long does a render take?",
                "It depends on how many views and how much detail. The estimate is written into "
                "the scope rather than published here, because a single number would be wrong "
                "for most projects."),
               ("What is 3D visualisation used for?",
                "Presenting a product, an interior or a building before it exists, and getting a "
                "decision from people who will never see the physical thing."),
               ("Do you produce AR and VR as well?",
                "Yes. Both sit inside this service, so the buyer reads one offer instead of two.")]),
    dict(slug="web-development", nav="Digital platforms", num="02", icon="digital",
         name="Digital platforms",
         buy="A digital tool that does a job, not a brochure.",
         covers=["Website design and development", "Web applications", "Mobile builds",
                 "Integrations and APIs", "E-commerce", "Performance and SEO foundations"],
         h1="Build the tool the business actually needs.",
         sub="Websites, applications and integrations built to carry the work: enquiry, "
             "specification, ordering, reporting.",
         cta="Planning a website or platform? Tell us what the business needs it to do.",
         outcome="The site stops being a brochure and starts doing a job.",
         faqs=[("What does a web development company actually do?",
                "Designs and builds the site or application, then maintains it: structure, "
                "interface, front end, back end, integrations and the hosting it runs on."),
               ("How is website development costed?",
                "Per project, after the scope is agreed. Pages, integrations and content "
                "migration drive the number far more than visual design does."),
               ("Why would we rebuild the current site?",
                "When the current one cannot do a job the business now needs: mobile behaviour, "
                "enquiry handling, integration, or speed. We measure before recommending it."),
               ("Can you take over an existing site?",
                "Yes. The first step is an audit of what exists, including the URLs and the "
                "search history behind them.")]),
    dict(slug="multimedia-services", nav="Video and motion", num="03", icon="video",
         name="Video and motion",
         buy="A complicated offer that makes sense in thirty seconds.",
         covers=["Corporate and explainer film", "Motion graphics and 2D animation",
                 "3D animation", "Visual effects (VFX)", "Infographics", "Multi-format edits"],
         h1="Explain the complicated part in thirty seconds.",
         sub="Corporate and explainer film, motion graphics and 3D animation, made for the point "
             "where a written explanation stops working.",
         cta="Need to explain something complicated? Start with a two-minute film.",
         outcome="A complex offer that a buyer understands without a call.",
         faqs=[("What can be outsourced to your studio?",
                "Script and storyboard, shoot or animation, edit, motion graphics, VFX and the "
                "cut-downs for social. A single deliverable or the whole production."),
               ("What is the turnaround time?",
                "Set per project and written into the scope. Animation and VFX run longer than "
                "an edit, and the schedule says which stage is the long one."),
               ("Do you produce VFX as well as film?",
                "Yes. VFX sits in this service, alongside 2D and 3D animation."),
               ("Can existing footage be reused?",
                "Often. We review the existing material before quoting a shoot.")]),
    dict(slug="graphic-design", nav="Brand and design", num="04", icon="brand",
         name="Brand and design",
         buy="A brand that looks the same everywhere it appears.",
         covers=["Identity and logo systems", "Brand guidelines", "Brochures and company profiles",
                 "Print and flyers", "Packaging", "Exhibition stands and vehicle branding"],
         h1="Make the brand look the same everywhere.",
         sub="Identity systems, print and vehicle branding, built so a brochure, a stand and a "
             "truck all read as one company.",
         cta="Is your brand inconsistent? We\u2019ll review the touchpoints with you.",
         outcome="One identity, applied across every touchpoint without drift.",
         faqs=[("How many revisions do we get?",
                "Two rounds of revision are standard on identity work, and the scope states "
                "them. Further rounds are quoted rather than absorbed silently."),
               ("Who owns the files at the end?",
                "The client, on final payment. Source files and the working assets are handed "
                "over, not withheld."),
               ("What if we do not like the first direction?",
                "That is what the first review is for. A direction is presented with the "
                "reasoning, so the feedback is about the reason and not only the look."),
               ("How are the files delivered?",
                "A shared folder with print-ready and screen-ready versions, plus the source "
                "files and a short note on what each one is for.")]),
    dict(slug="e-learning", nav="Learning", num="05", icon="learning",
         name="Learning",
         buy="Training that scales without losing quality.",
         covers=["E-learning content", "HTML5 and video modules", "LMS and CMS integration",
                 "SCORM and AICC packaging", "Assessment and simulation", "Mobile and blended learning"],
         h1="Train a hundred people as well as you train ten.",
         sub="E-learning content, LMS integration, assessment and simulation, built to hold "
             "quality when the audience grows.",
         cta="Building a learning programme? Let\u2019s talk content, interactivity and LMS.",
         outcome="Consistent training delivery without a trainer in every room.",
         faqs=[("What is the difference between e-learning and a video?",
                "A module carries structure, interaction and assessment. A video plays. If a "
                "video is enough, we say so."),
               ("Which platforms do you deliver to?",
                "SCORM and AICC packages for standard LMS platforms, plus HTML5 for anything "
                "that hosts a web page."),
               ("Can existing classroom material be converted?",
                "Yes. Existing decks, manuals and recordings are the usual starting point."),
               ("Do you build assessments and simulations?",
                "Yes, both, including branching scenarios for decisions that have consequences.")]),
    dict(slug="digital-marketing-company", nav="Search and marketing", num="06", icon="search",
         name="Search and marketing",
         buy="Being found by people who are already looking.",
         covers=["Search engine optimisation", "Technical SEO and site speed", "Content strategy",
                 "Paid search and social", "Campaign creatives", "Reporting against enquiries"],
         h1="Be found by the people already looking.",
         sub="Search and digital marketing for the demand that already exists, measured against "
             "enquiries rather than impressions.",
         cta="Not getting found? Let\u2019s look at what your site ranks for today.",
         outcome="Enquiries from people who were already searching for the service.",
         faqs=[("Why does a business need digital marketing?",
                "Because the buyer searches before they call. If the site does not appear for "
                "the service the business sells, the enquiry goes to whoever does."),
               ("What do you report on?",
                "Visibility, engagement, enquiries and qualified leads, with the definition of "
                "each one agreed before the work starts."),
               ("Do you work outside India?",
                "Yes. Search work is not limited by where the studio sits."),
               ("How long before search results change?",
                "Longer than a campaign, and we say so in the scope rather than promising a "
                "date we cannot hold.")]),
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

# Each discipline gets its own entrance character. One curve, six temperaments.
DISC_VARIANT = {
    "3d-visualization": "depth",       # 01 spatial
    "web-development": "grid",         # 02 crisp
    "multimedia-services": "fluid",    # 03 timeline
    "graphic-design": "editorial",     # 04 composed
    "e-learning": "stack",             # 05 staged
    "digital-marketing-company": "metric",  # 06 measured
}

NAV = [("work", "Work", "pixerio-portfolio.html"),
       ("insights", "Insights", "blog.html"),
       ("about", "About", "about-us.html"),
       ("contact", "Contact", "contact-us.html")]

# ---------------------------------------------------------------- work (§1.3, §2.7)
# Real projects from the live portfolio. Names and imagery come from pixerio.com;
# the one-sentence summaries describe the artefact only — challenge, approach and
# result are written with the client before launch.
WORK = [
    dict(img="Hitachi-Brochure", name="Hitachi", sum="Corporate brochure for a technical audience.",
         cat="Brochure", slug="graphic-design"),
    dict(img="Lamda-Brochure", name="Lamda Components", sum="Product brochure series, one grid across the range.",
         cat="Brochure", slug="graphic-design"),
    dict(img="Takt-Brochure-Design", name="Takt", sum="Brochure design with a photographic cover treatment.",
         cat="Brochure", slug="graphic-design"),
    dict(img="Yalgaar-Brochure", name="Yalgaar", sum="Company profile brochure.",
         cat="Brochure", slug="graphic-design"),
    dict(img="Tripath-Brochure", name="Tripath Logistics", sum="Service brochure for a logistics operation.",
         cat="Brochure", slug="graphic-design"),
    dict(img="Package-Design", name="Packaging", sum="Structural and surface design for a retail pack.",
         cat="Packaging", slug="graphic-design"),
    dict(img="iQuant-Package-Design", name="iQuant", sum="Product packaging, shelf-ready.",
         cat="Packaging", slug="graphic-design"),
    dict(img="Collezioni-Logo-Design", name="Collezioni", sum="Wordmark and monogram for a fashion label.",
         cat="Identity", slug="graphic-design"),
    dict(img="Maple-Logo-Design", name="Maple", sum="Logo system with a play on the initial.",
         cat="Identity", slug="graphic-design"),
    dict(img="Turaco-Logo", name="Turaco", sum="Identity mark built for a single-colour reproduction.",
         cat="Identity", slug="graphic-design"),
    dict(img="Snacs-Constructions-Branding", name="Snacs Constructions", sum="Contractor branding applied to site and stationery.",
         cat="Identity", slug="graphic-design"),
    dict(img="Tripath-Vehicle-Branding", name="Tripath fleet", sum="Vehicle livery that stays legible from a distance.",
         cat="Vehicle branding", slug="graphic-design"),
    dict(img="Lamda-Components-Stall-Design", name="Lamda Components", sum="Exhibition stand built around one product story.",
         cat="Exhibition", slug="graphic-design"),
    dict(img="CME-Stall-Design", name="CME stand", sum="Conference stand design, modular build.",
         cat="Exhibition", slug="graphic-design"),
    dict(img="Sada-Money-Flyer", name="SADA Money", sum="Financial services flyer, single-message layout.",
         cat="Print", slug="graphic-design"),
    dict(img="Calendar-Design", name="Calendar programme", sum="A yearly print artefact used as a client touchpoint.",
         cat="Print", slug="graphic-design"),
    dict(img="Social-Media-Creatives", name="Social creatives", sum="Campaign set built from one template family.",
         cat="Print", slug="digital-marketing-company"),
    dict(img="Cornucopia-Website", name="Cornucopia", sum="Corporate website build.",
         cat="Website", slug="web-development"),
    dict(img="NPS-Agara-School-Website", name="NPS Agara", sum="School website with admissions content.",
         cat="Website", slug="web-development"),
    dict(img="Pinti-eCommerce-Website", name="Pinti", sum="E-commerce storefront and product templates.",
         cat="E-commerce", slug="web-development"),
    dict(img="Lakshmi-Videos-Website", name="Lakshmi Videos", sum="Media library site for a video production house.",
         cat="Website", slug="web-development"),
    dict(img="Tripath-Logistics-Dairy", name="Tripath Dairy", sum="Identity applied to a dairy product line.",
         cat="Identity", slug="graphic-design"),
]
WORK_BY_SERVICE = {s["slug"]: [w for w in WORK if w["slug"] == s["slug"]] for s in SERVICES}

QUOTES = [
    dict(q="They understood the product before they designed anything. The first round of work "
           "was already close to what we needed.",
         role="Marketing manager", org="Furniture company", sector="web project"),
    dict(q="The renders let us get sign-off from people who were never going to visit the site. "
           "That changed the timeline.",
         role="Manager, product development", org="Manufacturing", sector="3D visualisation"),
    dict(q="What we asked for was a campaign. What we got was a clearer idea of who we were "
           "talking to.",
         role="CEO", org="Cloud service provider", sector="digital campaign"),
    dict(q="Delivery was steady and the handover was documented, which is rarer than it should be.",
         role="CEO", org="Home appliance company", sector="platform build"),
]


# ---------------------------------------------------------------- service art
# Original line art, one hue per discipline, drawn for this build. The live site
# carries a single-hue line illustration per service card; these keep that idea
# (thin line, sparkle marks, one colour) with Pixerio's own geometry and a tinted
# plate behind each one. Nothing is traced or copied from the live artwork.
ART = {
    "3d": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<path d="M32 7 56 20v24L32 57 8 44V20z"/><path d="M8 20l24 12 24-12M32 32v25"/>
<circle cx="53" cy="11" r="1.8" fill="currentColor" stroke="none"/>
<path d="M6 9h4M8 7v4"/></svg>""",
    "digital": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<rect x="7" y="12" width="50" height="40" rx="4"/><path d="M7 22h50"/>
<circle cx="13" cy="17" r="1.4" fill="currentColor" stroke="none"/>
<circle cx="19" cy="17" r="1.4" fill="currentColor" stroke="none"/>
<path d="M13 29h17v15H13zM36 29h15M36 35h15M36 41h10"/></svg>""",
    "video": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<rect x="7" y="17" width="50" height="30" rx="3"/>
<path d="M7 25h6M7 33h6M7 41h6M51 25h6M51 33h6M51 41h6"/>
<path d="M27 25l11 7-11 7z"/>
<path d="M47 9h4M49 7v4"/></svg>""",
    "brand": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<circle cx="25" cy="24" r="12"/><rect x="28" y="28" width="24" height="24" rx="4"/>
<path d="M10 44h12M10 50h8"/><circle cx="54" cy="11" r="1.8" fill="currentColor" stroke="none"/></svg>""",
    "learning": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<path d="M10 13h17a6 6 0 0 1 6 6v30a7 7 0 0 0-7-7H10z"/>
<path d="M54 13H37a6 6 0 0 0-6 6v30a7 7 0 0 1 7-7h16z"/>
<circle cx="46" cy="43" r="9"/><path d="m41.5 43 3.2 3.2L51 39"/></svg>""",
    "search": """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<circle cx="26" cy="26" r="13"/><path d="m36 36 10 10"/>
<path d="M19 31v-5M26 31v-10M33 31v-7"/>
<path d="M51 9h4M53 7v4"/></svg>""",
}

# ---------------------------------------------------------------- chrome
def jsonld(page_title, desc, path, kind=None, extra=None):
    org = {
        "@type": ["Organization", "LocalBusiness"],
        "@id": "https://pixerio.com/#organization",
        "name": "Pixerio",
        "url": "https://pixerio.com/",
        "logo": "https://pixerio.com/assets/img/pixerio-logo.png",
        "image": "https://pixerio.com/assets/img/pixerio-logo.png",
        "description": "Creative and digital services company in Bengaluru: brand and design, "
                       "digital platforms, video and motion, 3D and immersive, learning, "
                       "search and marketing.",
        "email": "info@pixerio.com",
        "telephone": "+91-99000-71841",
        "address": {"@type": "PostalAddress", "streetAddress": "JC Nagar",
                    "addressLocality": "Bengaluru", "addressRegion": "Karnataka",
                    "addressCountry": "IN"},
        "areaServed": "IN",
        "sameAs": ["https://360video.pixerio.com/Pixerio-360-room/"],
    }
    graph = [org]
    if kind:
        graph.append(extra)
    if path != "index.html":
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://pixerio.com/"},
                {"@type": "ListItem", "position": 2, "name": page_title,
                 "item": f"https://pixerio.com/{path.replace('.html', '/')}"},
            ],
        })
    import json
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def head(title, desc, page, ld="", body_class="", hero=False, disc=""):
    canon = "https://pixerio.com/" if page == "index.html" else \
            f"https://pixerio.com/{page.replace('.html', '/')}"
    preload = ('<link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" '
               'type="font/woff2" crossorigin>')
    home_css = '<link rel="stylesheet" href="assets/css/home.css">' if hero else ''
    disc_attr = f' data-disc="{disc}"' if disc else ''
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Pixerio</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#12324A">
<meta property="og:title" content="{title} — Pixerio">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://pixerio.com/assets/img/pixerio-logo.png">
<meta property="og:site_name" content="Pixerio">
<meta name="twitter:card" content="summary_large_image">
{preload}
<link rel="icon" href="assets/img/pixerio-logo.png">
<link rel="stylesheet" href="assets/css/site.css">
{home_css}
{ld}
<script>document.documentElement.classList.add('js')</script>
</head>
<body data-page="{page}" class="{body_class}"{disc_attr}>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
"""


def header(active=""):
    menu = "".join(
        f'<a href="{s["slug"]}.html"><span>{s["name"]}</span>'
        f'<small>{s["buy"]}</small></a>' for s in SERVICES)
    links = "".join(
        f'<a href="{href}"{" aria-current=\'page\'" if key == active else ""}>{label}</a>'
        for key, label, href in NAV)
    return f"""
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="Pixerio — home">
      <img src="assets/img/pixerio-logo.png" alt="Pixerio" width="1026" height="381" fetchpriority="high">
    </a>
    <nav class="nav" id="nav" aria-label="Primary">
      <div class="has-menu">
        <button class="nav__parent" type="button" aria-expanded="false" aria-controls="services-menu">
          Services <span aria-hidden="true" class="chev"></span>
        </button>
        <div class="menu" id="services-menu">
          <div class="menu__inner">{menu}</div>
        </div>
      </div>
      {links}
    </nav>
    <button class="motion-toggle" type="button" aria-pressed="false" aria-label="Pause motion — freeze animation on this page">
      <span class="motion-toggle__ic" aria-hidden="true"></span>
      <span class="motion-toggle__label">Pause motion</span>
    </button>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span></button>
  </div>
</header>
"""


def cta_band(title="Tell us the problem. We will tell you what it takes.",
             sub="One action, repeated: a short form that names the service you need.",
             action="Discuss Your Project", href="contact-us.html"):
    return f"""
<section class="cta">
  <div class="wrap cta__inner">
    <div data-reveal>
      <p class="eyebrow">One action</p>
      <h2>{title}</h2>
      <p>{sub}</p>
    </div>
    <a class="btn" href="{href}" data-magnetic="0.28">
      <span class="btn__label">{action}</span>
    </a>
  </div>
</section>
"""


def footer():
    services = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f"""
</main>
<footer class="footer">
  <div class="wrap">
    <p class="footer__word" aria-hidden="true">Pixerio</p>
    <div class="footer__top">
      <div class="footer__brand">
        <img src="assets/img/pixerio-logo.png" alt="Pixerio" width="1026" height="381" loading="lazy">
        <p>Creative and digital services in JC Nagar, Bengaluru. Six services, each with its own
        buyer, under one partner.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{services}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about-us.html">About</a></li>
          <li><a href="pixerio-portfolio.html">Work</a></li>
          <li><a href="blog.html">Insights</a></li>
          <li><a href="contact-us.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:info@pixerio.com">info@pixerio.com</a></li>
          <li><a href="tel:+919****1841">+91 99000 71841</a></li>
          <li>JC Nagar, Bengaluru, India</li>
          <li><a href="https://360video.pixerio.com/Pixerio-360-room/">360&#176; studio tour</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; 2026 Pixerio Solutions Private Limited</span>
      <span>Reference build for approval &mdash; not the live site</span>
      <span><a href="privacy-policy.html">Privacy</a> &nbsp;&middot;&nbsp; <a href="terms.html">Terms</a></span>
    </div>
  </div>
</footer>
<script src="assets/js/px.js" defer></script>
<script src="assets/js/pagehead.js" defer></script>
<script src="assets/js/motion.js" defer></script>
</body>
</html>
"""


def page_head(crumb, h1, sub, eyebrow=None, sub2=None, chips=None, art=None):
    chip_html = "".join(f'<span class="chip">{c}</span>' for c in (chips or []))
    art_html = f'<span class="page-head__art" aria-hidden="true">{art}</span>' if art else ""
    return f"""
<main id="main">
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a>
      <span aria-hidden="true">/</span> <span>{crumb}</span></nav>
    {'<p class="eyebrow">' + eyebrow + '</p>' if eyebrow else ''}
    <h1>{h1}</h1>
    <p class="lead">{sub}</p>
    {('<p class="lead" style="margin-top:.9rem">' + sub2 + '</p>') if sub2 else ''}
    {('<div class="page-head__foot">' + chip_html + '</div>') if chip_html else ''}
  </div>
  {art_html}
  <div class="spectrum" aria-hidden="true"></div>
</section>
"""


def work_grid(items, heading="Selected work", eyebrow="Evidence", band="quiet",
              intro=None, link=True, cls=""):
    tiles = []
    for i, w in enumerate(items):
        tiles.append(f"""
      <a class="tile" href="case-study.html" data-reveal="grid" style="--i:{i}">
        <picture>
          <source srcset="assets/img/work/{w['img']}.webp" type="image/webp">
          <img src="assets/img/work/{w['img']}.jpg" alt="{w['name']} — {w['sum']}"
               width="800" height="600" loading="lazy" decoding="async">
        </picture>
        <span class="tile__body">
          <span>
            <span class="tile__name">{w['name']}</span>
            <span class="tile__sum">{w['sum']}</span>
            <span class="tile__cat">{w['cat']}</span>
          </span>
          <span class="tile__arrow" aria-hidden="true">{ARROW}</span>
        </span>
      </a>""")
    more = (f'<a class="link" href="pixerio-portfolio.html">All 22 projects {ARROW_R}</a>'
            if link else '')
    intro_html = f'<p>{intro}</p>' if intro else ''
    return f"""
<section class="band band--{band} {cls}">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">{eyebrow}</p>
        <h2>{heading}</h2>
        {intro_html}
      </div>
      {more}
    </div>
    <div class="grid grid--3 work">{''.join(tiles)}</div>
  </div>
</section>
"""


def evidence_pending(service_name):
    """The evidence-pending panel, unwrapped so callers can place it in any band."""
    return f"""
    <div class="panel panel--soft" style="display:flex;gap:1.2rem;align-items:flex-start;flex-wrap:wrap">
      <div style="flex:1 1 340px">
        <div class="panel__rule"></div>
        <h3>Work for {service_name} is being captured</h3>
        <p>This page needs project imagery and one result that can be checked before launch.
        Until those exist, the space stays empty rather than carrying stock photography that
        stands in for work Pixerio has not done.</p>
      </div>
      <span class="chip chip--blue" style="flex:none">Evidence pending &middot; client assets</span>
    </div>
"""


def stats_band():
    """Big-numeral proof band. Every figure is checkable against this build."""
    items = [("06", "services, each with its own buyer"),
             ("22", "documented projects in the portfolio"),
             ("03", "stages, discovery to deployment"),
             ("01", "partner from brand definition to launch")]
    cells = "".join(f"""
      <div class="stat">
        <div class="stat__n num">{n}</div>
        <span>{label}</span>
      </div>""" for n, label in items)
    return f"""
<section class="band band--tight">
  <div class="wrap">
    <div class="stats" data-reveal="metric">{cells}</div>
  </div>
</section>
"""


PROCESS_ICONS = {
    "discovery": '<svg class="step__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
                 '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5" stroke-linecap="round"/></svg>',
    "implementation": '<svg class="step__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
                      '<path d="M12 3 21 7.5 12 12 3 7.5z" stroke-linejoin="round"/><path d="m3 12 9 4.5 9-4.5M3 16.5 12 21l9-4.5" stroke-linejoin="round"/></svg>',
    "deployment": '<svg class="step__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
                  '<path d="M5 15v4h14v-4M12 3v12M8 7l4-4 4 4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


def process(heading="Three stages, in this order", intro=None):
    steps = [
        ("01", "Discovery", "discovery",
         "What the business needs the work to do, who it is for, and what already exists. "
         "Scope, sequence and the decisions that need a client in the room.",
         "Output: a written scope"),
        ("02", "Implementation", "implementation",
         "Design and build against that scope. Reviews at fixed points, not at the end, so "
         "a change of mind costs a conversation rather than a rebuild.",
         "Output: approved work"),
        ("03", "Deployment", "deployment",
         "Launch, handover and documentation. Files, access and the maintenance position all "
         "written down before anyone moves on to the next project.",
         "Output: a documented handover"),
    ]
    body = "".join(f"""
      <article class="step" data-step>
        <div class="step__n">{n}</div>
        <div>
          <div>{PROCESS_ICONS[key]}</div>
          <h3>{t}</h3>
          <p>{d}</p>
          <div class="step__out">{o}</div>
        </div>
      </article>""" for n, t, key, d, o in steps)
    return f"""
<section class="band band--navy">
  <div class="wrap process__grid">
    <div class="process__sticky" data-reveal>
      <p class="eyebrow">How we work</p>
      <h2>{heading}</h2>
      <p class="lead" style="margin-top:1rem">Discovery to deployment is a real process here, and it
      is kept. What changes is that each stage ends in something you can hold.</p>
    </div>
    <div data-reveal="editorial">{body}</div>
  </div>
</section>
"""


def quotes_block():
    cards = "".join(f"""
      <figure class="quote" data-reveal="editorial" style="--i:{i}">
        <blockquote>&ldquo;{q['q']}&rdquo;</blockquote>
        <figcaption>
          <b>{q['role']}</b>{q['org']} &middot; {q['sector']}
          <span class="pending">Name &amp; permission pending</span>
        </figcaption>
      </figure>""" for i, q in enumerate(QUOTES))
    return f"""
<section class="band band--quiet">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">Trust</p>
        <h2>What clients say, and what is still missing</h2>
        <p>Four quotes from the existing site. A name, a role and written permission are the
        condition for publishing them, so the name line is marked until each one is cleared.</p>
      </div>
    </div>
    <div class="home-quotes">{cards}</div>
  </div>
</section>
"""


def service_cards(active=""):
    cards = []
    for i, s in enumerate(SERVICES):
        cards.append(f"""
      <a class="svc-card" href="{s['slug']}.html" data-reveal style="--i:{i}">
        <span class="svc-card__top">
          <span class="svc-card__icon">{IC[s['icon']]}</span>
          <span class="svc-card__num num">{s['num']} / 06</span>
        </span>
        <h3 class="svc-card__title">{s['name']}</h3>
        <p class="svc-card__promise">{s['buy']}</p>
        <span class="svc-card__foot">What this covers
          <span class="svc-card__arrow" aria-hidden="true">{ARROW}</span></span>
      </a>""")
    return f'<div class="grid grid--3">{"".join(cards)}</div>'


def service_rows(items, start=1):
    """Numbered index rows — same links and meaning as the cards, read as a list."""
    out = []
    for i, o in enumerate(items):
        out.append(f"""
      <a class="row" href="{o['slug']}.html" data-reveal="editorial" style="--i:{i}">
        <span class="row__n num">{start + i:02d}</span>
        <span class="row__t">{o['name']}</span>
        <span class="row__s">{o['buy']}</span>
        <span class="row__a" aria-hidden="true">{ARROW}</span>
      </a>""")
    return f'<div class="rows">{"".join(out)}</div>'



def capability_wall():
    """Six disciplines as a three-up wall. Each card is a real link to its page,
    keeps the numeral, the buyer sentence and the outcome, and lifts on hover —
    the same six links as the rail above it, in a form that survives reduced
    motion, pause motion and a narrow screen."""
    cards = "".join(f"""
      <article class="wall__card" data-reveal style="--i:{i}">
        <span class="wall__art" aria-hidden="true">{ART[s['icon']]}</span>
        <span class="wall__n num">{s['num']} / 06</span>
        <h3>{s['name']}</h3>
        <p>{s['buy']}</p>
        <span class="wall__out">{s['outcome']}</span>
        <a class="wall__link" href="{s['slug']}.html"
           aria-label="{s['name']} — open the {s['name']} service page"></a>
      </article>""" for i, s in enumerate(SERVICES))
    return f"""
<section class="band" id="capabilities">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">What we do</p>
        <h2>Six core capabilities. One business outcome.</h2>
        <p>Every engagement is built around what the work produces for your business, not just a
        list of deliverables.</p>
      </div>
      <a class="link" href="pixerio-portfolio.html">All 22 projects {ARROW_R}</a>
    </div>
    <div class="wall">{cards}</div>
  </div>
</section>
"""


# ---------------------------------------------------------------- home (§2.9)


def hero_band():
    """Homepage hero: the claim on the left 40%, the stage on the right.

    The stage is six independent DOM panels driven by hero-stage.js — act 1 the
    fragmented problem, act 2 the spectrum trail resolving each one, act 3 the
    connected lattice. Every word of the headline, the lead and both controls is
    exactly what shipped before; only the composition beside them is new.
    """
    PANEL = {
        "3d":        ("vis-3d",    ("#6C5CE7", "#217FC3", "#00B3BD"), "Immersive presentation"),
        "digital":   ("vis-web",   ("#217FC3", "#30C0F0", "#00B3BD"), "Polished platforms"),
        "video":     ("vis-film",  ("#E1136E", "#7C3AED", "#217FC3"), "Compelling film"),
        "brand":     ("vis-brand", ("#49AD48", "#B8D550", "#F49C42"), "Consistent identity"),
        "learning":  ("vis-learn", ("#00B3BD", "#49AD48", "#B8D550"), "Interactive learning"),
        "search":    ("vis-mkt",   ("#F49C42", "#E1136E", "#217FC3"), "Connected campaigns"),
    }
    CUBE = ('<svg viewBox="0 0 100 100" aria-hidden="true">'
            '<path class="v3d-far" d="M18 30h64v64H18z" transform="translate(10,-12)"/>'
            '<path class="v3d-far" d="M18 30 28 18h64L82 30M82 30v64L92 82V18"/>'
            '<path d="M8 38h64v54H8z"/><path d="M8 38 18 26h64L72 38M72 38v54"/></svg>')

    panels = []
    for i, sv in enumerate(SERVICES):
        vis, (g1, g2, g3), label = PANEL[sv["icon"]]
        inner = CUBE if vis == "vis-3d" else (
            '<i></i><i></i><i></i>' if vis in ("vis-brand", "vis-learn", "vis-mkt")
            else ('<i></i>' if vis == "vis-film" else '<i></i><i></i><i></i>'))
        panels.append(f"""
      <article class="stg-panel" data-p="{i}" style="--g1:{g1};--g2:{g2};--g3:{g3}">
        <div class="stg-panel__inner">
          <span class="stg-panel__tag"><i class="stg-panel__dot"></i>{sv['num']} &middot; {sv['name']}</span>
          <div class="stg-vis {vis}">{inner}</div>
          <span class="stg-panel__name">{label}</span>
          <span class="stg-panel__promise">{sv['buy']}</span>
        </div>
      </article>""")

    return f"""
<main id="main">
<section class="hero">
  <div class="hero__ambient" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <p class="eyebrow">Six disciplines &middot; one partner</p>
      <h1><span class="hero__l1">Ideas are everywhere.</span> <span class="hero__l2">We make them matter.</span></h1>
      <p class="lead">One partner for connected creative, digital and technology solutions &mdash;
      taking your business from brand definition through to a launched, findable product.</p>
      <div class="actions">
        <a class="btn" href="contact-us.html" data-magnetic="0.25">
          <span class="btn__label">Discuss Your Project</span></a>
        <a class="btn btn--ghost" href="pixerio-portfolio.html">
          <span class="btn__label">See the work</span></a>
      </div>
      <div class="hero__meta">
        <span class="chip">JC Nagar, Bengaluru</span>
        <span class="chip">Six services</span>
        <span class="chip">22 documented projects</span>
      </div>
      <p class="stage__caption">
        <span data-stage-caption><b>01</b> Six separate problems</span>
        <span class="stage__bar"><i></i></span>
      </p>
    </div>
    <div class="hero__stage">
      <div class="stage" data-stage data-ready="0" aria-hidden="true">
        <canvas class="stage__canvas"></canvas>{''.join(panels)}
        <canvas class="stage__light"></canvas>
      </div>
    </div>
  </div>
</section>
"""


def build_index():
    ld = jsonld("Pixerio", "Creative and digital services company in Bengaluru.", "index.html")
    s = head("Creative and digital services, Bengaluru",
             "Pixerio is a creative and digital services partner in Bengaluru: brand and design, "
             "digital platforms, video and motion, 3D and immersive, learning, and search.",
             "index.html", ld=ld, hero=True)
    s += header()
    s += hero_band()
    s += capability_wall()
    s += work_grid([w for w in WORK if w["img"] in
                    ("Hitachi-Brochure", "Cornucopia-Website", "Tripath-Vehicle-Branding")],
                   heading="Work that had to survive contact with the real thing.",
                   eyebrow="Evidence", band="", cls="home-work",
                   intro="Three projects from the portfolio. Every one is a real artefact with a "
                         "client name on it — no mock-ups, no stock.")
    s += stats_band()
    s += process()
    s += quotes_block()
    s += cta_band()
    s += footer().replace("</body>", '<script src="assets/js/hero-stage.js" defer></script>' + chr(10) + '</body>', 1)
    return ("index.html", s)


# ---------------------------------------------------------------- service pages
def build_service(svc):
    ld = jsonld(svc["name"], svc["sub"], f"{svc['slug']}.html", kind="Service", extra={
        "@type": "Service",
        "name": svc["name"],
        "serviceType": svc["name"],
        "description": svc["sub"],
        "provider": {"@id": "https://pixerio.com/#organization"},
        "areaServed": "IN",
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": svc["name"],
                            "itemListElement": [{"@type": "Offer", "itemOffered":
                                                 {"@type": "Service", "name": c}}
                                                for c in svc["covers"]]},
    })
    v = DISC_VARIANT.get(svc["slug"], "editorial")
    s = head(f"{svc['name']} in Bengaluru", svc["sub"], f"{svc['slug']}.html", ld=ld,
             disc=svc["num"])
    s += header()
    covers = "".join(f"<li>{CHECK}<span>{c}</span></li>" for c in svc["covers"])
    others = [x for x in SERVICES if x["slug"] != svc["slug"]][:3]
    others_html = service_rows(others)
    s += page_head(svc["name"], svc["h1"], svc["sub"], eyebrow=f"Service {svc['num']} of 06",
                   chips=[svc["name"], svc["buy"]], art=ART[svc["icon"]])

    # ---- 01 capability · 02 scenario -------------------------------------------------
    s += f"""
<section class="band">
  <div class="wrap cse">
    <div class="cse__step" data-reveal="{v}">
      <div class="cse__label">
        <span class="cse__n">01 &mdash; Capability</span>
        <span class="cse__name">What this<br>service is</span>
      </div>
      <div class="cse__body">
        <p class="cse__claim">{svc['buy']}</p>
        <p>{svc['sub']}</p>
        <ul class="checklist" style="margin-top:1.8rem">{covers}</ul>
        <p class="small muted" style="margin-top:1.4rem;max-width:54ch">Scoped per project.
        Anything outside this list is quoted separately, in writing, before it starts.</p>
      </div>
    </div>

    <div class="cse__step" data-reveal="{v}" style="--i:1">
      <div class="cse__label">
        <span class="cse__n">02 &mdash; Scenario</span>
        <span class="cse__name">Where it<br>fits</span>
      </div>
      <div class="cse__body">
        <p class="cse__claim">Three questions decide whether this is the right work.</p>
        <div class="scenario">
          <div class="scenario__card">
            <span class="scenario__k">The situation</span>
            <h3>{svc['h1']}</h3>
            <p>{svc['sub']}</p>
          </div>
          <div class="scenario__card">
            <span class="scenario__k">What you are buying</span>
            <h3>{svc['buy']}</h3>
            <p>{svc['outcome']}</p>
          </div>
          <div class="scenario__card">
            <span class="scenario__k">How it starts</span>
            <h3>A short call, then a written scope</h3>
            <p>A short call, then a written scope with the decisions that need you in the room.
            No estimate is published before the scope exists.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    # ---- 03 evidence -----------------------------------------------------------------
    svc_work = WORK_BY_SERVICE.get(svc["slug"], [])
    if svc_work:
        s += work_grid(svc_work[:6], heading=f"Work for {svc['name']}",
                       eyebrow="03 &mdash; Evidence", band="quiet", link=True,
                       intro="Real projects, with the client name attached. Each tile opens the "
                             "project template; results appear there only once they are verified.")
    else:
        s += f"""
<section class="band band--quiet">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">03 &mdash; Evidence</p>
        <h2>What the work looks like</h2>
      </div>
    </div>
    {evidence_pending(svc['name'])}
  </div>
</section>
"""

    faqs = "".join(f"""
      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>""" for q, a in svc.get("faqs", []))
    if faqs:
        s += f"""
<section class="band">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">Questions</p>
        <h2>Straight answers</h2>
        <p>The questions buyers ask before they make contact, answered without a sales line in
        front of them.</p>
      </div>
    </div>
    <div class="faq" data-reveal="{v}" style="--i:1">{faqs}</div>
  </div>
</section>
"""
    s += process()
    s += f"""
<section class="band band--quiet">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <div class="sec-head__text">
        <p class="eyebrow">The other five</p>
        <h2>Other services</h2>
      </div>
      <a class="link" href="index.html#capabilities">All six {ARROW_R}</a>
    </div>
    {others_html}
  </div>
</section>
"""
    s += cta_band(title="Tell us what this needs to do for the business.",
                  sub=f"One action on this page. It lands on the enquiry form with {svc['name']} already selected.",
                  action=svc["cta"], href=f"contact-us.html?service={svc['slug']}")
    s += footer()
    return (f"{svc['slug']}.html", s)


# ---------------------------------------------------------------- contact
def build_contact():
    ld = jsonld("Contact", "Contact Pixerio in Bengaluru.", "contact-us.html",
                kind="ContactPage", extra={"@type": "ContactPage",
                                           "name": "Contact Pixerio",
                                           "url": "https://pixerio.com/contact-us/"})
    s = head("Contact", "Talk to Pixerio about a project. A named person replies within one working day.",
             "contact-us.html", ld=ld)
    s += header("contact")
    opts = "".join(f'<option value="{x["slug"]}">{x["name"]}</option>' for x in SERVICES)
    s += page_head("Contact", "Discuss Your Project",
                   "Tell us what the work needs to do, and who it is for. A named person replies "
                   "within one working day, with two or three pieces of relevant work.",
                   eyebrow="Contact", chips=["Reply within one working day", "JC Nagar, Bengaluru"])
    s += f"""
<section class="band">
  <div class="wrap split" style="align-items:start">
    <div>
      <form class="form" data-demo action="thank-you.html" method="get">
        <div class="form__row">
          <div class="field"><label for="name">Name</label>
            <input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="company">Company</label>
            <input id="company" name="company" type="text" autocomplete="organization" required></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="email">Work email</label>
            <input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="phone">Phone</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
        </div>
        <div class="field"><label for="service">Which service is this about?</label>
          <select id="service" name="service" required>
            <option value="">Select a service</option>{opts}
            <option value="other">Something else</option>
          </select></div>
        <div class="field"><label for="brief">What does this need to do for the business?</label>
          <textarea id="brief" name="brief" required
            placeholder="The outcome you are buying, the audience, and any deadline that exists."></textarea></div>
        <label class="consent"><input type="checkbox" name="consent" required>
          <span>I agree to Pixerio storing these details to reply to this enquiry. Nothing is
          added to a marketing list, and nothing fires before consent is given.</span></label>
        <div class="form__foot">
          <button class="btn" type="submit" data-morph>
            <span class="btn__label">Send the brief</span>
            <span class="btn__spin" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round">
                <circle cx="12" cy="12" r="9"/></svg></span>
          </button>
          <p class="form__note" data-status role="status" aria-live="polite"></p>
        </div>
      </form>
      <p class="small muted" style="margin-top:1.2rem;max-width:58ch">Prototype form &mdash; it does
      not send. The production build posts to the CMS and shows the thank-you page.</p>
    </div>
    <div class="grid" style="gap:18px">
      <div class="panel panel--soft">
        <div class="panel__rule"></div>
        <h3>What happens after you press send</h3>
        <ul class="checklist" style="margin-top:1rem">
          <li>{CHECK}<span><strong>Within one working day</strong> &mdash; a reply from a named person, not an autoresponder.</span></li>
          <li>{CHECK}<span><strong>In that reply</strong> &mdash; two or three pieces of relevant work, and the next step we would suggest.</span></li>
          <li>{CHECK}<span><strong>If it isn&rsquo;t a fit</strong> &mdash; an honest no, and a recommendation if we know someone better placed.</span></li>
        </ul>
      </div>
      <div class="panel">
        <h3>Direct</h3>
        <p style="margin-top:.6rem"><a href="mailto:info@pixerio.com">info@pixerio.com</a><br>
        <a href="tel:+919****1841">+91 99000 71841</a><br>
        JC Nagar, Bengaluru, India</p>
      </div>
    </div>
  </div>
</section>
"""
    s += footer()
    return ("contact-us.html", s)


def build_thankyou():
    s = head("Thank you", "Thank you — your enquiry has reached Pixerio.", "thank-you.html")
    s += header()
    s += page_head("Thank you", "That reached us.",
                   "A named person will reply within one working day, with two or three pieces of "
                   "relevant work and the next step we would suggest.",
                   eyebrow="Enquiry received", chips=["Reply within one working day"])
    s += """
<section class="band">
  <div class="wrap narrow prose">
    <div class="panel panel--soft">
      <div class="panel__rule"></div>
      <h3>While you wait</h3>
      <p style="margin-top:.6rem">The work is the fastest way to judge whether we are the right
      partner. <a href="pixerio-portfolio.html">Read the project breakdowns</a>, or check the
      <a href="blog.html">insights</a> for how we approach the problem you described.</p>
    </div>
    <p style="margin-top:2rem"><a class="btn btn--ghost" href="index.html">
      <span class="btn__label">Back to the site</span></a></p>
  </div>
</section>
"""
    s += footer()
    return ("thank-you.html", s)


# ---------------------------------------------------------------- about
def build_about():
    ld = jsonld("About", "Pixerio: creative and digital services in Bengaluru.", "about-us.html",
                kind="AboutPage", extra={"@type": "AboutPage", "name": "About Pixerio",
                                         "url": "https://pixerio.com/about-us/"})
    s = head("About", "Pixerio is a creative and digital services company in JC Nagar, Bengaluru, "
                       "working across six services for corporate and industrial clients.",
             "about-us.html", ld=ld)
    s += header("about")
    s += page_head("About", "One partner, six services, one story.",
                   "Pixerio is a creative and digital services company in JC Nagar, Bengaluru. "
                   "The range of work is real: identity, print, packaging, exhibition stands, "
                   "websites, film, 3D and e-learning.")
    s += f"""
<section class="band">
  <div class="wrap split">
    <div data-reveal>
      <p class="eyebrow">The position</p>
      <h2>Six services read as six vendors unless one partner connects them.</h2>
      <p style="margin-top:1.2rem">A developer looking for walkthroughs does not need LMS
      integration. An L&amp;D lead does not need VFX. Each service has its own buyer, and each
      page is written for that buyer.</p>
      <p>What connects them is the route from brand definition through to a launched, findable
      product &mdash; the same team, the same standards, one conversation.</p>
    </div>
    <figure class="media" data-reveal style="--i:1">
      <picture>
        <source srcset="assets/img/Creative-Design-Agency.webp" type="image/webp">
        <img src="assets/img/Creative-Design-Agency.png" alt="Pixerio studio" width="565" height="491" loading="lazy">
      </picture>
    </figure>
  </div>
</section>

<section class="band band--quiet">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <h2>What we do, and who it is for</h2>
      <p>Six services, each with its own buyer. The same six the live site already sells &mdash;
      the difference is that each page now says what the work produces.</p>
    </div>
    <table class="scope">
      <thead><tr><th scope="col">Service</th><th scope="col">What it covers</th><th scope="col">What you are buying</th></tr></thead>
      <tbody>{''.join(f"<tr><td>{x['name']}</td><td>{', '.join(x['covers'])}</td><td>{x['buy']}</td></tr>" for x in SERVICES)}</tbody>
    </table>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <h2>Capabilities behind the six</h2>
      <p>The working list, carried over from the current site: what the team actually produces.</p>
    </div>
    <div class="grid grid--3">
      {''.join(f'<div class="panel" data-reveal style="--i:{i}"><div class="panel__rule"></div><h4>{c}</h4><p>{d}</p></div>' for i, (c, d) in enumerate([
        ("Branding", "Identity, logo systems, guidelines and the templates that keep them applied."),
        ("Print media design", "Brochures, company profiles, flyers, calendars and packaging."),
        ("Web design and development", "Marketing sites, content structure, responsive build."),
        ("Web app development", "Applications, portals and the integrations behind them."),
        ("3D modelling and architecture", "Product and architectural visualisation, walkthroughs."),
        ("E-learning", "Modules, SCORM packaging, LMS integration and assessment."),
        ("Multimedia services", "Film, motion graphics, 2D and 3D animation, VFX."),
        ("AR and VR", "Augmented and virtual reality, including the published 360&#176; tour."),
        ("Search engine optimisation", "Technical SEO, content and the reporting that follows it."),
      ]))}
    </div>
  </div>
</section>
"""
    s += stats_band()
    s += process()
    s += cta_band()
    s += footer()
    return ("about-us.html", s)


# ---------------------------------------------------------------- portfolio
def build_portfolio():
    ld = jsonld("Work", "Selected Pixerio projects.", "pixerio-portfolio.html")
    s = head("Work", "Selected Pixerio work: identity, print, packaging, exhibition and vehicle branding.",
             "pixerio-portfolio.html", ld=ld)
    s += header("work")
    s += page_head("Work", "The work, explained rather than labelled.",
                   "Each project carries a challenge, an approach and a result. Where a result "
                   "has not been verified, the page says so instead of estimating one.",
                   eyebrow="Portfolio", chips=["22 documented projects", "16 clients"])
    s += work_grid(WORK, heading="All 22 projects", eyebrow="Brand, print, web and stand",
                   band="", link=False,
                   intro="Every tile is a real artefact with the client name attached. Open one to "
                         "see the challenge, approach and result structure the case studies follow.")
    s += """
<section class="band band--quiet">
  <div class="wrap">
    <div class="panel panel--soft" style="display:flex;gap:1.2rem;align-items:flex-start;flex-wrap:wrap">
      <div style="flex:1 1 340px">
        <div class="panel__rule"></div>
        <h3>Three services still need imagery</h3>
        <p>Video and motion, 3D and immersive, and learning have no project images on the current
        site. Those pages carry an evidence-pending panel instead of stock photography, because
        stock standing in for work is the one thing this build will not do.</p>
      </div>
      <span class="chip chip--blue" style="flex:none">3 services pending assets</span>
    </div>
  </div>
</section>
"""
    s += cta_band()
    s += footer()
    return ("pixerio-portfolio.html", s)


# ---------------------------------------------------------------- case study
def build_case():
    ld = jsonld("Project", "A Pixerio project: challenge, approach and result.",
                "case-study.html", kind="CreativeWork",
                extra={"@type": "CreativeWork", "name": "Project case study",
                       "creator": {"@id": "https://pixerio.com/#organization"}})
    s = head("Project", "A Pixerio project, explained as challenge, approach and result.",
             "case-study.html", ld=ld)
    s += header("work")
    s += page_head("Work / Project", "A brochure system that holds its grid on every page.",
                   "Client name, sector and the business problem in one sentence. The three "
                   "sections below are the structure every case study follows.")
    s += f"""
<section class="band">
  <div class="wrap narrow prose">
    <p class="eyebrow">Challenge</p>
    <h2>The brief, in the client&rsquo;s words</h2>
    <p style="margin-top:1rem">What was wrong before the work started, and what the client
    needed it to do. One or two paragraphs, no adjectives.</p>
    <figure class="media" style="margin:2rem 0">
      <picture>
        <source srcset="assets/img/work/Lamda-Brochure.webp" type="image/webp">
        <img src="assets/img/work/Lamda-Brochure.jpg" alt="Brochure system" width="650" height="475" loading="lazy">
      </picture>
    </figure>
    <p class="eyebrow">Approach</p>
    <h2>What we did about it</h2>
    <p style="margin-top:1rem">The decisions that mattered, and why. This is where a case study
    earns the right to the result.</p>
    <p class="eyebrow" style="margin-top:2.5rem">Result</p>
    <h2>What changed, and how it was checked</h2>
    <p style="margin-top:1rem">Only verified results are published. A number appears here when
    it has been measured and the client has agreed to it appearing; otherwise this section says
    what was delivered and stops.</p>
    <div class="panel" style="margin-top:1.6rem">
      <div class="panel__rule"></div>
      <h3>Template note</h3>
      <p style="margin-top:.5rem">This is the case-study template. Production copy, imagery and
      any result figures come from the client, and nothing is filled in until they do.</p>
    </div>
  </div>
</section>
"""
    s += cta_band()
    s += footer()
    return ("case-study.html", s)


# ---------------------------------------------------------------- blog
def build_blog():
    ld = jsonld("Insights", "Notes on brand, platforms, film, 3D, learning and search.",
                "blog.html")
    posts = [
        ("How to write a brief that gets a useful answer", "Brand and design",
         "The five things a brief needs before anyone can quote honestly."),
        ("What a website has to do before it is redesigned", "Digital platforms",
         "Measure the current job before changing the tool that does it."),
        ("Rendering a product that does not exist yet", "3D and immersive",
         "What a client can and cannot approve from a render."),
        ("When e-learning is the wrong answer", "Learning",
         "Four cases where a workshop beats a module."),
        ("Search is a measurement problem first", "Search and marketing",
         "Why ranking reports do not survive contact with a sales team."),
        ("Film length is a decision, not an edit", "Video and motion",
         "The thirty-second version is written, not cut."),
    ]
    CAT_ICON = {"Brand and design": "brand", "Digital platforms": "digital",
                "3D and immersive": "3d", "Learning": "learning",
                "Search and marketing": "search", "Video and motion": "video"}
    cards = "".join(f"""
      <a class="post" href="article.html" data-reveal style="--i:{i}">
        <span class="post__thumb post__thumb--{CAT_ICON.get(p[1], 'brand')}" aria-hidden="true">{ART[CAT_ICON.get(p[1], 'brand')]}</span>
        <span class="post__cat">{p[1]}</span>
        <h3 class="post__title">{p[0]}</h3>
        <p class="post__sum">{p[2]}</p>
        <span class="post__more">Read {ARROW}</span>
      </a>""" for i, p in enumerate(posts))
    s = head("Insights", "Notes on brand, platforms, film, 3D, learning and search.",
             "blog.html", ld=ld)
    s += header("insights")
    s += page_head("Insights", "Notes from the work.",
                   "Six starting points, one per service. Written for the person who has to "
                   "approve the work, not for a design audience.")
    s += f"""
<section class="band">
  <div class="wrap"><div class="grid grid--3">{cards}</div>
    <p class="small muted" style="margin-top:2rem;max-width:70ch">Article pages use
    <a href="article.html">one template</a>. Publishing dates, authors and reading times appear
    once the content calendar exists.</p>
  </div>
</section>
"""
    s += cta_band()
    s += footer()
    return ("blog.html", s)


def build_article():
    ld = jsonld("How to write a brief that gets a useful answer",
                "The five things a brief needs before anyone can quote honestly.", "article.html",
                kind="Article",
                extra={"@type": "Article",
                       "headline": "How to write a brief that gets a useful answer",
                       "author": {"@type": "Organization", "name": "Pixerio"},
                       "publisher": {"@id": "https://pixerio.com/#organization"},
                       "mainEntityOfPage": "https://pixerio.com/blog/"})
    s = head("How to write a brief that gets a useful answer",
             "The five things a brief needs before anyone can quote honestly.", "article.html", ld=ld)
    s += header("insights")
    s += page_head("Insights / Brand and design", "How to write a brief that gets a useful answer.",
                   "The five things a brief needs before anyone can quote honestly.")
    s += """
<section class="band">
  <div class="wrap narrow prose">
    <p class="eyebrow">Article template</p>
    <h2>Why most briefs produce a price instead of an answer</h2>
    <p style="margin-top:1rem">A brief that names a deliverable gets a quote. A brief that names
    an outcome gets a conversation about the right deliverable. The difference is five sentences.</p>
    <p>The article template carries a heading ladder, one pull quote, one figure with a caption,
    and a closing action. Body copy is written per article; the structure does not change.</p>
    <div class="panel panel--soft" style="margin-top:2rem">
      <div class="panel__rule"></div>
      <h3>Template note</h3>
      <p style="margin-top:.5rem">Article body, author, date and reading time come from the
      content calendar. Nothing is back-dated or pre-filled.</p>
    </div>
  </div>
</section>
"""
    s += cta_band()
    s += footer()
    return ("article.html", s)


# ---------------------------------------------------------------- legal
def build_privacy():
    s = head("Privacy", "How Pixerio handles enquiry data.", "privacy-policy.html")
    s += header()
    s += page_head("Privacy", "Privacy, in plain language.",
                   "What the enquiry form collects, why, and how long it is kept. Draft for legal "
                   "review before launch.")
    s += """
<section class="band">
  <div class="wrap narrow prose">
    <h2>What is collected</h2>
    <p style="margin-top:.8rem">Name, company, email, telephone, the service selected and the
    brief you write. Nothing else is collected by the form, and no field is hidden.</p>
    <h2 style="margin-top:2rem">Why</h2>
    <p style="margin-top:.8rem">To reply to the enquiry. The details are not added to a
    marketing list and not sold.</p>
    <h2 style="margin-top:2rem">Analytics and consent</h2>
    <p style="margin-top:.8rem">Consent mode is preserved. Nothing beyond strictly necessary
    storage fires before consent is given, and the consent state is recorded.</p>
    <h2 style="margin-top:2rem">Retention and your rights</h2>
    <p style="margin-top:.8rem">Retention period, the data controller&rsquo;s registered details
    and the request process are legal copy, and are marked here rather than invented.</p>
    <div class="panel" style="margin-top:2rem">
      <div class="panel__rule"></div>
      <h3>Before launch</h3>
      <p style="margin-top:.5rem">Retention period, controller details and the rights process need
      legal sign-off. This page exists so the link is never dead.</p>
    </div>
  </div>
</section>
"""
    s += footer()
    return ("privacy-policy.html", s)


def build_terms():
    s = head("Terms", "Terms of use for the Pixerio website.", "terms.html")
    s += header()
    s += page_head("Terms", "Terms of use.",
                   "The basis on which this site is provided. Draft for legal review before launch.")
    s += """
<section class="band">
  <div class="wrap narrow prose">
    <h2>Content</h2>
    <p style="margin-top:.8rem">Work shown on this site belongs to Pixerio or to the client it was
    produced for, and is shown with permission. It may not be reused.</p>
    <h2 style="margin-top:2rem">Enquiries</h2>
    <p style="margin-top:.8rem">An enquiry is not a contract. Nothing is committed until a written
    scope has been agreed by both parties.</p>
    <h2 style="margin-top:2rem">Liability and jurisdiction</h2>
    <p style="margin-top:.8rem">Standard clauses, governing law and the registered entity details
    are legal copy and are marked here rather than drafted without instruction.</p>
    <div class="panel" style="margin-top:2rem">
      <div class="panel__rule"></div>
      <h3>Before launch</h3>
      <p style="margin-top:.5rem">Governing law, liability cap and entity details need legal
      sign-off.</p>
    </div>
  </div>
</section>
"""
    s += footer()
    return ("terms.html", s)


# ---------------------------------------------------------------- AR/VR preservation
def build_arvr():
    ld = jsonld("AR and VR", "Augmented and virtual reality production in Bengaluru.",
                "augmented-virtual-reality.html")
    s = head("AR and VR", "Augmented and virtual reality, delivered as part of 3D and immersive.",
             "augmented-virtual-reality.html", ld=ld)
    s += header()
    s += page_head("3D and immersive / AR and VR", "AR and VR, inside the 3D service.",
                   "This page keeps its existing URL. In the new structure the work sits under "
                   "3D and immersive, so the buyer reads one offer instead of two.")
    s += f"""
<section class="band">
  <div class="wrap narrow prose">
    <div class="panel panel--soft">
      <div class="panel__rule"></div>
      <h3>This URL is preserved, not retired</h3>
      <p style="margin-top:.6rem">The ranking history behind this page is kept, and the page
      points at the fuller service description rather than duplicating it.</p>
      <p style="margin-top:1rem"><a class="link" href="3d-visualization.html">
        Read 3D and immersive {ARROW_R}</a></p>
    </div>
    <ul class="checklist" style="margin-top:2rem">
      <li>{CHECK}<span>Augmented reality for product and print</span></li>
      <li>{CHECK}<span>Virtual reality walkthroughs</span></li>
      <li>{CHECK}<span>360&#176; tours, including the studio tour already published</span></li>
    </ul>
  </div>
</section>
"""
    s += cta_band()
    s += footer()
    return ("augmented-virtual-reality.html", s)


# ---------------------------------------------------------------- write
def main():
    pages = [build_index(), build_contact(), build_thankyou(), build_about(),
             build_portfolio(), build_case(), build_blog(), build_article(),
             build_privacy(), build_terms(), build_arvr()]
    pages += [build_service(s) for s in SERVICES]
    written = []
    for name, html in pages:
        (ROOT / name).write_text(html, encoding="utf-8")
        written.append((name, len(html)))
    for n, size in sorted(written):
        print(f"{n:36} {size:>7} chars")
    print(f"\n{len(written)} pages written")


if __name__ == "__main__":
    main()
