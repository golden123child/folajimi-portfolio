#!/usr/bin/env python3
"""Assemble the single-file SPA portfolio.
Reads CSS + JS from source files and page bodies from build.py."""
import importlib.util, pathlib, re

# --- load page-body constants from build.py (without writing files) ---
spec = importlib.util.spec_from_file_location("build", "build.py")
build = importlib.util.module_from_spec(spec)
_orig_write = pathlib.Path.write_text
pathlib.Path.write_text = lambda self, data, *a, **k: len(data)   # neutralise build.py writes
spec.loader.exec_module(build)
pathlib.Path.write_text = _orig_write                              # restore real writer

CSS = pathlib.Path("css/styles.css").read_text()
JS  = pathlib.Path("js/main.js").read_text()

# --- convert file-based nav links to SPA router links ---
FILE_MAP = {
    'index.html':      ('home',      'home'),
    'about.html':      ('about',     'about'),
    'skills.html':     ('expertise', 'expertise'),
    'projects.html':   ('work',      'work'),
    'experience.html': ('journey',   'journey'),
    'contact.html':    ('contact',   'contact'),
}
def route_links(body):
    for href, (anchor, page) in FILE_MAP.items():
        body = re.sub(r'href="' + re.escape(href) + r'"',
                      f'href="#{anchor}" data-page="{page}"', body)
    return body

PAGES = [
    ("home",      build.INDEX),
    ("about",     build.ABOUT),
    ("expertise", build.SKILLS),
    ("work",      build.PROJECTS),
    ("journey",   build.EXPERIENCE),
    ("contact",   build.CONTACT),
]

pages_html = ""
for pid, body in PAGES:
    pages_html += f'  <div class="spa-page" id="page-{pid}">\n{route_links(body)}\n  </div>\n\n'

NAV = """  <nav class="navbar">
    <div class="container nav-inner">
      <a href="#home" data-page="home" class="logo"><span class="dot"></span>Wuraola<span style="color:var(--gold)">.</span></a>
      <div class="nav-links" id="primary-navigation">
        <a href="#home" data-page="home" class="active">Home</a>
        <a href="#about" data-page="about">About</a>
        <a href="#expertise" data-page="expertise">Expertise</a>
        <a href="#work" data-page="work">Work</a>
        <a href="#journey" data-page="journey">Journey</a>
        <a href="#contact" data-page="contact" class="nav-cta">Let's Talk</a>
      </div>
      <button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="primary-navigation" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </nav>"""

FOOTER = route_links(build.FOOTER)

AURORA = """  <div class="aurora"><span class="a1"></span><span class="a2"></span><span class="a3"></span></div>"""

RESUME = """  <!-- Print-only résumé (hidden on screen, shown when printing) -->
  <div class="resume-print" id="resumePrint">
    <div class="rp-head">
      <h1>Wuraola Folajimi</h1>
      <p class="rp-title">Full Stack Developer &amp; UI/UX Designer</p>
      <div class="rp-contact">
        <span>folajimiwuraola4@gmail.com</span>
        <span>&middot;</span>
        <span>+234 913 004 0046</span>
        <span>&middot;</span>
        <span>Lagos, Nigeria</span>
        <span>&middot;</span>
        <span>github.com/golden123child</span>
        <span>&middot;</span>
        <span>linkedin.com/in/wuraola-folajimi</span>
      </div>
    </div>
    <div class="rp-section">
      <h2>Summary</h2>
      <p>Full stack developer and UI/UX designer with 5+ years of experience building web applications, WordPress platforms and digital products. Computer Science graduate (4.7 CGPA) currently pursuing a second degree in Software Engineering. Based in Lagos, working with Strategik Technologies and available for freelance work worldwide.</p>
    </div>
    <div class="rp-section">
      <h2>Core Skills</h2>
      <div class="rp-skills">
        <span>HTML5</span><span>CSS3</span><span>JavaScript</span><span>React</span><span>Python</span><span>Java</span><span>C++</span><span>PHP</span><span>Node.js</span><span>WordPress</span><span>WooCommerce</span><span>MySQL</span><span>MongoDB</span><span>Figma</span><span>Git</span><span>REST APIs</span>
      </div>
    </div>
    <div class="rp-section">
      <h2>Experience</h2>
      <div class="rp-item">
        <div class="rp-item-head"><strong>Full Stack Developer &amp; UI/UX Designer</strong> &mdash; Strategik Technologies / Freelance</div>
        <p>Building web applications, WordPress platforms and digital products for clients across industries. Full lifecycle work: design, front-end, back-end and deployment.</p>
      </div>
    </div>
    <div class="rp-section">
      <h2>Education</h2>
      <div class="rp-item">
        <div class="rp-item-head"><strong>B.Sc. Computer Science</strong> &mdash; University of Lagos (UNILAG) &middot; CGPA 4.7</div>
        <p>First-class honours. Foundations in algorithms, data structures, database systems, OOP in Java &amp; C++.</p>
      </div>
      <div class="rp-item">
        <div class="rp-item-head"><strong>B.Sc. Software Engineering</strong> &mdash; Miva Open University &middot; In Progress</div>
        <p>Software architecture, systems design, testing methodologies and large-scale engineering.</p>
      </div>
    </div>
    <div class="rp-section">
      <h2>Certifications</h2>
      <div class="rp-item"><div class="rp-item-head"><strong>Meta</strong> &mdash; Front-End Developer Professional</div></div>
      <div class="rp-item"><div class="rp-item-head"><strong>Google</strong> &mdash; UX Design Professional</div></div>
      <div class="rp-item"><div class="rp-item-head"><strong>AWS</strong> &mdash; Cloud Practitioner</div></div>
      <div class="rp-item"><div class="rp-item-head"><strong>freeCodeCamp</strong> &mdash; Full Stack &amp; Responsive Web</div></div>
      <div class="rp-item"><div class="rp-item-head"><strong>WordPress</strong> &mdash; Advanced Theme Development</div></div>
      <div class="rp-item"><div class="rp-item-head"><strong>Cisco</strong> &mdash; Programming Essentials in C/C++</div></div>
    </div>
  </div>"""

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wuraola Folajimi &mdash; Full Stack Developer &amp; UI/UX Designer</title>
  <meta name="description" content="Wuraola Folajimi is a freelance full stack developer and UI/UX designer based in Lagos, Nigeria. Building fast, elegant web apps and WordPress sites with React, Python, Java, C++ and more.">
  <meta name="author" content="Wuraola Folajimi">
  <meta name="keywords" content="Wuraola Folajimi, full stack developer, UI UX designer, WordPress developer, Lagos, Nigeria, React, Python, Java, web developer">
  <link rel="canonical" href="https://wuraolafolajimi.com/">

  <!-- Open Graph / social previews -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Wuraola Folajimi &mdash; Full Stack Developer &amp; UI/UX Designer">
  <meta property="og:description" content="Freelance full stack developer and UI/UX designer crafting elegant, high-performance digital experiences from Lagos to the world.">
  <meta property="og:locale" content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Wuraola Folajimi &mdash; Full Stack Developer &amp; UI/UX Designer">
  <meta name="twitter:description" content="Freelance full stack developer and UI/UX designer crafting elegant, high-performance digital experiences.">

  <!-- Structured data (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Wuraola Folajimi",
    "jobTitle": "Full Stack Developer & UI/UX Designer",
    "url": "https://wuraolafolajimi.com",
    "email": "mailto:folajimiwuraola4@gmail.com",
    "telephone": "+2349130040046",
    "address": {{ "@type": "PostalAddress", "addressLocality": "Lagos", "addressCountry": "Nigeria" }},
    "knowsAbout": ["Full Stack Development", "UI/UX Design", "WordPress", "React", "Python", "Java", "C++"]
  }}
  </script>

  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%2308080d'/%3E%3Ctext x='50' y='68' font-family='Georgia' font-size='52' fill='%23d4af37' text-anchor='middle'%3EW%3C/text%3E%3C/svg%3E">
  <style>
{CSS}
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to content</a>
{AURORA}
{NAV}

  <main id="main-content">
{pages_html}
  </main>

{RESUME}
{FOOTER}
  <script>
{JS}
  </script>
</body>
</html>
'''

pathlib.Path("index.html").write_text(html)
print(f"Wrote index.html  ({len(html):,} chars, {len(PAGES)} pages)")
