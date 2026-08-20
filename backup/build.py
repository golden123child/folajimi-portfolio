#!/usr/bin/env python3
"""Generate the multi-page Wuraola Folajimi portfolio (self-contained pages)."""
import pathlib

CSS = pathlib.Path("css/styles.css").read_text()
JS  = pathlib.Path("js/main.js").read_text()

def nav(active):
    pages = [("Home","index.html"), ("About","about.html"), ("Expertise","skills.html"),
             ("Work","projects.html"), ("Journey","experience.html")]
    links = ""
    for label, href in pages:
        cls = ' class="active"' if href == active else ""
        links += f'<a href="{href}"{cls}>{label}</a>\n        '
    return f'''  <nav class="navbar">
    <div class="container nav-inner">
      <a href="index.html" class="logo"><span class="dot"></span>Wuraola<span style="color:var(--gold)">.</span></a>
      <div class="nav-links">
        {links}<a href="contact.html" class="nav-cta{" active" if active=="contact.html" else ""}">Let's Talk</a>
      </div>
      <button class="menu-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </nav>'''

FOOTER = '''  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="logo"><span class="dot"></span>Wuraola<span style="color:var(--gold)">.</span></a>
          <p>Full stack developer &amp; UI/UX designer crafting elegant, high-performance digital experiences from Lagos to the world.</p>
          <div class="social-row">
            <a href="https://github.com/golden123child" target="_blank" rel="noopener" class="social-link" aria-label="GitHub"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .3a12 12 0 00-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.9 1.2 1.9 1.2 1 .1.8 1.7 2.6 1.2.1-.7.4-1.2.7-1.5-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 016 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0012 .3"/></svg></a>
            <a href="https://www.linkedin.com/in/wuraola-folajimi" target="_blank" rel="noopener" class="social-link" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.3A1.8 1.8 0 118.3 6.5 1.8 1.8 0 016.5 8.3zM19 19h-3v-4.7c0-1.1 0-2.5-1.5-2.5S13 13 13 14.2V19h-3v-9h2.9v1.2a3.1 3.1 0 012.8-1.5c3 0 3.5 2 3.5 4.5z"/></svg></a>
            <a href="https://wa.me/2349130040046" target="_blank" rel="noopener" class="social-link" aria-label="WhatsApp"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 018.413 3.488 11.82 11.82 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 001.515 5.26l-.999 3.648 3.973-1.607zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg></a>
            <a href="mailto:folajimiwuraola4@gmail.com" class="social-link" aria-label="Email"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 6l-10 7L2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg></a>
          </div>
        </div>
        <div class="footer-col"><h4>Navigate</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="skills.html">Expertise</a></li><li><a href="projects.html">Work</a></li><li><a href="experience.html">Journey</a></li></ul></div>
        <div class="footer-col"><h4>Services</h4><ul><li><a href="skills.html">Web Development</a></li><li><a href="skills.html">UI/UX Design</a></li><li><a href="skills.html">WordPress</a></li><li><a href="contact.html">Consulting</a></li></ul></div>
        <div class="footer-col"><h4>Connect</h4><ul><li><a href="mailto:folajimiwuraola4@gmail.com">folajimiwuraola4@gmail.com</a></li><li><a href="contact.html">Contact Form</a></li><li><a href="#" onclick="window.print();return false;" style="color:var(--gold-light)">Download CV (PDF)</a></li></ul></div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span data-year>2026</span> Wuraola Folajimi. All rights reserved.</span>
        <span class="made-with">Designed &amp; coded with precision</span>
      </div>
    </div>
  </footer>'''

def page(title, desc, body, active):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%2308080d'/%3E%3Ctext x='50' y='68' font-family='Georgia' font-size='52' fill='%23d4af37' text-anchor='middle'%3EW%3C/text%3E%3C/svg%3E">
  <style>
{CSS}
  </style>
</head>
<body>
{nav(active)}

  {body}

{FOOTER}
  <script>
{JS}
  </script>
</body>
</html>
'''

# ----------------------------------------------------------------------
# PAGE BODIES
# ----------------------------------------------------------------------

# ===== INDEX =====
INDEX = '''<!-- ===== HERO ===== -->
  <header class="hero" id="home">
    <div class="hero-grid-bg"></div>
    <div class="hero-glow one"></div>
    <div class="hero-glow two"></div>
    <div class="container hero-content">
      <span class="tag-pill reveal" style="margin-bottom:2rem">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--accent-teal);box-shadow:0 0 8px var(--accent-teal)"></span>
        Available for select projects
      </span>
      <h1 class="hero-name reveal delay-1">Wuraola<br><span class="text-gold text-italic">Folajimi</span></h1>
      <p class="hero-role reveal delay-2" data-typing='["Full Stack Developer","UI/UX Designer","WordPress Specialist","Creative Technologist","Problem Solver"]'></p>
      <p class="hero-desc reveal delay-3">I design and engineer refined digital experiences where thoughtful interface meets robust, scalable code. From pixel-perfect interfaces to full-stack architecture &mdash; blending artistry with engineering precision.</p>
      <div class="hero-actions reveal delay-3">
        <a href="projects.html" class="btn btn-primary">View Selected Work <span class="arrow">&rarr;</span></a>
        <a href="contact.html" class="btn btn-ghost">Start a Project</a>
      </div>
      <div class="hero-stats reveal delay-4">
        <div class="stat"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years Experience</div></div>
        <div class="stat"><div class="num"><span data-count="15" data-suffix="+">0</span></div><div class="label">Technologies</div></div>
        <div class="stat"><div class="num">Full Stack</div><div class="label">Development</div></div>
        <div class="stat"><div class="num">UI / UX</div><div class="label">Design</div></div>
      </div>
    </div>
    <div class="scroll-indicator"><span>SCROLL</span><span class="line"></span></div>
  </header>

  <div class="marquee">
    <div class="marquee-track">
      <div class="marquee-item">React <span class="star">&#10022;</span> WordPress <span class="star">&#10022;</span> UI / UX Design <span class="star">&#10022;</span> Python <span class="star">&#10022;</span> Full Stack <span class="star">&#10022;</span> Java <span class="star">&#10022;</span> C++ <span class="star">&#10022;</span> Figma <span class="star">&#10022;</span></div>
      <div class="marquee-item">React <span class="star">&#10022;</span> WordPress <span class="star">&#10022;</span> UI / UX Design <span class="star">&#10022;</span> Python <span class="star">&#10022;</span> Full Stack <span class="star">&#10022;</span> Java <span class="star">&#10022;</span> C++ <span class="star">&#10022;</span> Figma <span class="star">&#10022;</span></div>
    </div>
  </div>

  <section class="section" id="intro">
    <div class="container two-col">
      <div class="col reveal">
        <div class="portrait-frame">
          <div class="portrait-art"></div>
          <div class="portrait-initials">WF</div>
          <div class="portrait-badge">
            <span class="avail-dot"></span>
            <div class="small"><strong>Wuraola Folajimi</strong><span style="color:var(--text-muted)">Lagos, Nigeria &middot; Remote Worldwide</span></div>
          </div>
        </div>
      </div>
      <div class="col bio-text reveal delay-1">
        <span class="eyebrow">Introduction</span>
        <h2 class="section-title">Designing &amp; building<br>with <span class="text-gold text-italic">intention.</span></h2>
        <p>I'm a multidisciplinary developer and designer who believes great software is equal parts <strong>engineering</strong> and <strong>empathy</strong>. For over six years I've partnered with startups, agencies and brands to ship products that feel effortless.</p>
        <p>My work spans the entire stack &mdash; from designing intuitive interfaces in Figma, to architecting React front-ends, to building secure back-ends in PHP, Python and Node.js, and crafting flexible WordPress platforms clients can actually maintain.</p>
        <p>I care about the details others overlook: the micro-interaction, the load time, the accessibility, the maintainability. Every line of code and every pixel has a purpose.</p>
        <div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap"><a href="about.html" class="btn btn-ghost">More About Me</a><a href="contact.html" class="btn btn-ghost">Get in Touch</a></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <span class="eyebrow reveal">What I Do</span>
      <h2 class="section-title reveal">A complete toolkit for<br><span class="text-gold text-italic">digital craftsmanship.</span></h2>
      <p class="section-subtitle reveal delay-1">Three disciplines, one seamless process &mdash; from the first wireframe to the final deployment.</p>
      <div class="services-grid reveal-stagger">
        <div class="card service-card tilt feature-card reveal s1">
          <div class="service-num">01 &mdash; DESIGN</div>
          <div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg></div>
          <h3>UI / UX Design</h3>
          <p>Research-driven, human-centred interfaces. I turn complex problems into intuitive, beautiful experiences users love.</p>
          <ul class="service-list"><li>User research &amp; personas</li><li>Wireframing &amp; prototyping</li><li>Design systems</li><li>Usability testing</li></ul>
        </div>
        <div class="card service-card tilt feature-card reveal s2">
          <div class="service-num">02 &mdash; BUILD</div>
          <div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div>
          <h3>Full Stack Development</h3>
          <p>Robust, scalable applications built with modern frameworks. Clean architecture, tested code, performance-first.</p>
          <ul class="service-list"><li>React, Next.js, Vue</li><li>Node.js, Python, PHP APIs</li><li>Database design</li><li>Cloud &amp; DevOps</li></ul>
        </div>
        <div class="card service-card tilt feature-card reveal s3">
          <div class="service-num">03 &mdash; DELIVER</div>
          <div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 010 20M12 2a15.3 15.3 0 000 20"/></svg></div>
          <h3>WordPress &amp; CMS</h3>
          <p>Custom WordPress builds, headless CMS and themes that give clients total control without sacrificing design.</p>
          <ul class="service-list"><li>Custom themes &amp; plugins</li><li>WooCommerce stores</li><li>Headless WordPress</li><li>Performance &amp; SEO</li></ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="featured">
    <div class="container">
      <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:2rem;margin-bottom:3.5rem">
        <div class="reveal"><span class="eyebrow">What I Build</span><h2 class="section-title">Work that <span class="text-gold text-italic">solves problems.</span></h2></div>
        <a href="projects.html" class="btn btn-ghost reveal delay-1">View My Work <span class="arrow">&rarr;</span></a>
      </div>
      <div class="services-grid">
        <div class="card service-card tilt feature-card reveal"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20 15 15 0 010-20z"/></svg></div><div class="project-cat">WordPress &middot; WooCommerce</div><h3>Custom WordPress Builds</h3><p>Bespoke themes, plugins and online stores &mdash; fast, maintainable, and easy for clients to manage.</p><div class="project-tags"><span>WordPress</span><span>PHP</span><span>WooCommerce</span></div></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div><div class="project-cat">Full Stack &middot; Web Apps</div><h3>Web Applications</h3><p>End-to-end apps with React front-ends and Python, Node.js or PHP back-ends &mdash; built to scale.</p><div class="project-tags"><span>React</span><span>Python</span><span>Node.js</span></div></div>
        <div class="card service-card tilt feature-card reveal delay-2"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg></div><div class="project-cat">UI / UX &middot; Design</div><h3>Interface Design</h3><p>Thoughtful, usable interfaces designed in Figma &mdash; from wireframe to polished prototype.</p><div class="project-tags"><span>Figma</span><span>UI/UX</span><span>Prototyping</span></div></div>
      </div>
    </div>
  </section>

  <section class="section-tight"><div class="container"><div class="stats-band reveal">
    <div class="stat-block"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years of Craft</div></div>
    <div class="stat-block"><div class="num"><span data-count="50" data-suffix="+">0</span></div><div class="label">Projects Delivered</div></div>
    <div class="stat-block"><div class="num">Full Stack</div><div class="label">Web &amp; Apps</div></div>
    <div class="stat-block"><div class="num"><span data-count="98" data-suffix="%">0</span></div><div class="label">Happy Clients</div></div>
  </div></div></section>

  <!-- (fabricated "trusted by" brand strip removed; will show real client logos as earned) -->

  <section class="section section-compact" style="background:var(--bg-secondary)">
    <div class="container">
      <div class="reveal" style="max-width:680px;margin:0 auto">
        <span class="eyebrow" style="justify-content:center;display:flex">Currently</span>
        <h2 class="section-title" style="font-size:clamp(1.6rem,3.5vw,2.2rem);text-align:center;margin-bottom:2.5rem">What I'm <span class="text-gold text-italic">exploring.</span></h2>
        <div class="process-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.2rem">
          <div class="process-step reveal" style="padding:1.6rem"><div class="step-num" style="font-size:2rem">📚</div><h4 style="font-size:1rem;margin-bottom:0.4rem">Studying</h4><p style="font-size:0.82rem">Software Engineering at Miva Open University</p></div>
          <div class="process-step reveal" style="padding:1.6rem"><div class="step-num" style="font-size:2rem">🏗️</div><h4 style="font-size:1rem;margin-bottom:0.4rem">Building</h4><p style="font-size:0.82rem">Web platforms &amp; client solutions at Strategik</p></div>
          <div class="process-step reveal" style="padding:1.6rem"><div class="step-num" style="font-size:2rem">🧠</div><h4 style="font-size:1rem;margin-bottom:0.4rem">Learning</h4><p style="font-size:0.82rem">Advanced React patterns &amp; design systems</p></div>
          <div class="process-step reveal" style="padding:1.6rem"><div class="step-num" style="font-size:2rem">🌱</div><h4 style="font-size:1rem;margin-bottom:0.4rem">Open to</h4><p style="font-size:0.82rem">Freelance work &amp; meaningful collaborations</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>Have a project in mind?<br>Let's create something <span class="text-gold text-italic">remarkable.</span></h2>
    <p>Whether you need a full product build, a WordPress platform, or a design that converts &mdash; I'd love to hear about it.</p>
    <a href="contact.html" class="btn btn-primary">Start a Conversation <span class="arrow">&rarr;</span></a>
  </div></div></section>'''

# ===== ABOUT =====
ABOUT = '''<header class="page-header" id="top">
    <div class="hero-glow one"></div>
    <div class="container">
      <div class="breadcrumb reveal"><a href="index.html">Home</a><span class="sep">/</span><span>About</span></div>
      <h1 class="reveal">More than<br>the <span class="text-gold text-italic">work.</span></h1>
      <p class="lead reveal delay-1">The real story behind the skills &mdash; where I came from, why I chose this path, and what drives me to keep building.</p>
    </div>
  </header>

  <section class="section">
    <div class="container two-col">
      <div class="col reveal">
        <div class="portrait-frame">
          <div class="portrait-art"></div>
          <div class="portrait-initials">WF</div>
          <div class="portrait-badge"><span class="avail-dot"></span><div class="small"><strong>Wuraola Folajimi</strong><span style="color:var(--text-muted)">Full Stack Developer &middot; UI/UX</span></div></div>
        </div>
      </div>
      <div class="col bio-text reveal delay-1">
        <span class="eyebrow">Hello, I'm Wuraola</span>
        <h2 class="section-title">A builder who cares<br>about the <span class="text-gold text-italic">details.</span></h2>
        <p>I'm a full stack developer and UI/UX designer based in Lagos, Nigeria. I work with <strong>Strategik Technologies</strong> building real web products for real businesses &mdash; and I'm currently studying for my second degree in Software Engineering.</p>
        <p>I didn't take the shortest path here. I finished my B.Sc. in Computer Science at <strong>UNILAG with a 4.7 CGPA</strong>, and somewhere in that journey I realised that knowing how to code wasn't enough. The products people actually love are built by people who understand both the engineering <em>and</em> the human on the other side of the screen. So I taught myself design alongside development &mdash; and I've never looked at interfaces the same way since.</p>
        <p>Now I'm back studying <strong>Software Engineering at Miva Open University</strong> &mdash; not because I needed another degree, but because I wanted to go deeper into architecture, systems design and engineering at scale. I believe in never being the smartest person in the room.</p>
        <p>What you'll find across this site is honest. Real skills, real certifications, real education &mdash; and a real commitment to building work I'm proud of. I'd rather under-promise and over-deliver, every time.</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem">
          <a href="#journey" data-page="journey" class="btn btn-ghost">View My Journey</a>
          <a href="#contact" data-page="contact" class="btn btn-ghost">Get in Touch</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight"><div class="container"><div class="stats-band reveal">
    <div class="stat-block"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years Building</div></div>
    <div class="stat-block"><div class="num"><span data-count="15" data-suffix="+">0</span></div><div class="label">Languages &amp; Tools</div></div>
    <div class="stat-block"><div class="num">Lagos</div><div class="label">to the World</div></div>
    <div class="stat-block"><div class="num">2</div><div class="label">Degrees in Progress</div></div>
  </div></div></section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <div style="text-align:center;max-width:720px;margin:0 auto 4rem">
        <span class="eyebrow reveal" style="justify-content:center">Philosophy</span>
        <h2 class="section-title reveal">Principles that guide<br><span class="text-gold text-italic">every decision.</span></h2>
        <p class="section-subtitle reveal delay-1" style="margin:0 auto">These aren't slogans &mdash; they're the lens I use to evaluate every line of code and every design choice.</p>
      </div>
      <div class="services-grid reveal-stagger">
        <div class="card service-card tilt feature-card reveal s1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1a5.5 5.5 0 00-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 000-7.8z"/></svg></div><h3>Craft Over Speed</h3><p>I'd rather ship something exceptional a little later than something mediocre on time. Quality compounds; shortcuts accumulate debt.</p></div>
        <div class="card service-card tilt feature-card reveal s2"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20 15 15 0 010-20z"/></svg></div><h3>Empathy First</h3><p>Every interface is a conversation with a human. I design for real people, real contexts, real limitations.</p></div>
        <div class="card service-card tilt feature-card reveal s3"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></div><h3>Code as Communication</h3><p>Code is read far more than it's written. I write code that tells the next developer a clear, kind story &mdash; not a riddle.</p></div>
        <div class="card service-card tilt feature-card reveal s4"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div><h3>Performance is Design</h3><p>A beautiful site that loads slowly is a broken experience. Speed, accessibility and reliability are part of the design.</p></div>
        <div class="card service-card tilt feature-card reveal s5"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 10v6M4.2 4.2l4.3 4.3m7 7l4.3 4.3M1 12h6m10 0h6"/></svg></div><h3>Always Learning</h3><p>Technology moves; I move with it. I dedicate time every week to studying new tools, patterns and ideas.</p></div>
        <div class="card service-card tilt feature-card reveal s6"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.9M16 3.1a4 4 0 010 7.8"/></svg></div><h3>Collaboration Wins</h3><p>Great work is rarely solo. I communicate clearly, listen deeply and treat your goals as my own.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <span class="eyebrow reveal">My Process</span>
      <h2 class="section-title reveal">How I turn ideas into<br><span class="text-gold text-italic">living products.</span></h2>
      <p class="section-subtitle reveal delay-1">A deliberate, transparent process that keeps quality high and surprises low.</p>
      <div class="process-grid">
        <div class="process-step reveal"><div class="step-num">01</div><h4>Discover</h4><p>I listen first. We define goals, users, constraints and success metrics so every later decision has a foundation.</p></div>
        <div class="process-step reveal delay-1"><div class="step-num">02</div><h4>Design</h4><p>Wireframes evolve into polished prototypes in Figma. We test, refine and align before a single line of production code.</p></div>
        <div class="process-step reveal delay-2"><div class="step-num">03</div><h4>Build</h4><p>Clean, tested, modular code &mdash; front to back. Frequent demos keep you in the loop and the product on course.</p></div>
        <div class="process-step reveal delay-3"><div class="step-num">04</div><h4>Refine</h4><p>Performance tuning, accessibility audits, cross-device testing and polish. The last 10% is where the magic lives.</p></div>
        <div class="process-step reveal delay-4"><div class="step-num">05</div><h4>Launch</h4><p>Deployment, monitoring and documentation. I make sure you understand your product and can confidently run it.</p></div>
        <div class="process-step reveal delay-4"><div class="step-num">06</div><h4>Evolve</h4><p>Real products grow. I support iteration, measure outcomes and help you decide what to build next.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container two-col reverse">
      <div class="col reveal">
        <span class="eyebrow">Beyond the Screen</span>
        <h2 class="section-title">When I'm not <span class="text-gold text-italic">coding.</span></h2>
        <p>I believe the best work comes from a rich, balanced life. Away from the keyboard, you'll find me reading about systems thinking and behavioural design, sketching interface ideas in a notebook before they're ready for a screen, and mentoring young developers entering the field.</p>
        <p>I'm an advocate for <strong>more representation in tech</strong> &mdash; especially supporting women and underrepresented creators building their first products. I believe diverse perspectives make better software for everyone.</p>
        <p>I also love exploring the intersection of <strong>art and engineering</strong> &mdash; generative design, creative coding, and how aesthetics shape the way we trust and use technology.</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem"><span class="tag-pill">&#128218; Lifelong Learner</span><span class="tag-pill">&#127793; Mentor</span><span class="tag-pill">&#127912; Creative Coder</span></div>
      </div>
      <div class="col reveal delay-1">
        <div class="card beyond-card" style="padding:0;overflow:hidden">
          <div style="aspect-ratio:4/3;background:linear-gradient(135deg,#1b1b29,#0e0e16);display:flex;align-items:center;justify-content:center;position:relative">
            <div style="position:absolute;inset:0;background:radial-gradient(circle at 30% 40%,var(--gold-glow),transparent 60%),radial-gradient(circle at 70% 70%,rgba(94,234,212,0.15),transparent 55%)"></div>
            <div style="position:relative;text-align:center;padding:3rem">
              <div style="font-family:var(--font-display);font-size:4rem;color:var(--gold-light);line-height:1;margin-bottom:1rem">&infin;</div>
              <p style="font-family:var(--font-display);font-style:italic;font-size:1.3rem;line-height:1.5;color:var(--text-primary)">"The details are not the details. They make the design."</p>
              <p style="margin-top:1rem;font-family:var(--font-mono);font-size:0.75rem;letter-spacing:0.15em;color:var(--text-muted)">&mdash; CHARLES EAMES</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>Let's build something<br>with <span class="text-gold text-italic">intention.</span></h2>
    <p>If my philosophy resonates with how you want to work, I'd love to hear what you're building.</p>
    <a href="contact.html" class="btn btn-primary">Get in Touch <span class="arrow">&rarr;</span></a>
  </div></div></section>'''

# ===== SKILLS =====
SKILLS = '''<header class="page-header" id="top">
    <div class="hero-glow one"></div>
    <div class="container">
      <div class="breadcrumb reveal"><a href="index.html">Home</a><span class="sep">/</span><span>Expertise</span></div>
      <h1 class="reveal">A versatile toolkit,<br>mastered with <span class="text-gold text-italic">depth.</span></h1>
      <p class="lead reveal delay-1">From low-level systems to pixel-perfect interfaces &mdash; here's the technology I use to design, build and ship complete products.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="divider-label reveal"><span>Core Proficiency</span><span class="line"></span></div>
      <div class="two-col">
        <div class="col reveal">
          <div class="skill-row"><div class="skill-head"><span class="name">Front-End Development</span><span class="pct">90%</span></div><div class="skill-track"><div class="skill-fill" data-width="90"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">WordPress &amp; CMS</span><span class="pct">88%</span></div><div class="skill-track"><div class="skill-fill" data-width="88"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">UI / UX Design</span><span class="pct">85%</span></div><div class="skill-track"><div class="skill-fill" data-width="85"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">Back-End Development</span><span class="pct">80%</span></div><div class="skill-track"><div class="skill-fill" data-width="80"></div></div></div>
        </div>
        <div class="col reveal delay-1">
          <div class="skill-row"><div class="skill-head"><span class="name">API Design &amp; Integration</span><span class="pct">82%</span></div><div class="skill-track"><div class="skill-fill" data-width="82"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">Database &amp; Architecture</span><span class="pct">78%</span></div><div class="skill-track"><div class="skill-fill" data-width="78"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">Testing &amp; Quality Assurance</span><span class="pct">72%</span></div><div class="skill-track"><div class="skill-fill" data-width="72"></div></div></div>
          <div class="skill-row"><div class="skill-head"><span class="name">DevOps &amp; Deployment</span><span class="pct">70%</span></div><div class="skill-track"><div class="skill-fill" data-width="70"></div></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <span class="eyebrow reveal">Core Stack</span>
      <h2 class="section-title reveal">Languages &amp; <span class="text-gold text-italic">front-end.</span></h2>
      <p class="section-subtitle reveal delay-1">The languages and frameworks I reach for daily to build real products.</p>
      <div class="tech-marquee">
        <div class="tech-marquee-track">
        <div class="tech-chip"><div class="tech-icon" style="background:#e34f26">H5</div><div><div class="name">HTML5</div><div class="cat">Markup</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#1572b6">C3</div><div><div class="name">CSS3</div><div class="cat">Styling</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#f7df1e">JS</div><div><div class="name">JavaScript</div><div class="cat">ES2023+</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#61dafb">Re</div><div><div class="name">React</div><div class="cat">UI Library</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#38bdf8">Ta</div><div><div class="name">Tailwind CSS</div><div class="cat">Utility CSS</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#cc6699">Sa</div><div><div class="name">Sass / SCSS</div><div class="cat">Preprocessor</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#e34f26">H5</div><div><div class="name">HTML5</div><div class="cat">Markup</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#1572b6">C3</div><div><div class="name">CSS3</div><div class="cat">Styling</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#f7df1e">JS</div><div><div class="name">JavaScript</div><div class="cat">ES2023+</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#61dafb">Re</div><div><div class="name">React</div><div class="cat">UI Library</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#38bdf8">Ta</div><div><div class="name">Tailwind CSS</div><div class="cat">Utility CSS</div></div></div>
        <div class="tech-chip"><div class="tech-icon" style="background:#cc6699">Sa</div><div><div class="name">Sass / SCSS</div><div class="cat">Preprocessor</div></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <span class="eyebrow reveal">Back-End Languages</span>
      <h2 class="section-title reveal">Server-side <span class="text-gold text-italic">languages.</span></h2>
      <p class="section-subtitle reveal delay-1">Languages I use to build APIs, business logic and back-end systems.</p>
      <div class="tech-grid">
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#3776ab">Py</div><div><div class="name">Python</div><div class="cat">Scripting &middot; APIs</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#f89820">Ja</div><div><div class="name">Java</div><div class="cat">OOP &middot; Systems</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#00599c">C+</div><div><div class="name">C++</div><div class="cat">Systems &middot; Performance</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#777bb4">Ph</div><div><div class="name">PHP</div><div class="cat">WordPress Core</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#689f63">No</div><div><div class="name">Node.js</div><div class="cat">JavaScript Runtime</div></div></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <span class="eyebrow reveal">Data, CMS &amp; Design</span>
      <h2 class="section-title reveal">Databases, content &amp;<br><span class="text-gold text-italic">design tools.</span></h2>
      <p class="section-subtitle reveal delay-1">Storing data, managing content, and designing the experience.</p>
      <div class="tech-grid">
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#21759b">Wp</div><div><div class="name">WordPress</div><div class="cat">Themes &middot; Plugins</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#96588a">Wc</div><div><div class="name">WooCommerce</div><div class="cat">E-Commerce</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#00758f">My</div><div><div class="name">MySQL</div><div class="cat">Relational DB</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#47a248">Mo</div><div><div class="name">MongoDB</div><div class="cat">NoSQL</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#f24e1e">Fi</div><div><div class="name">Figma</div><div class="cat">UI / UX Design</div></div></div>
        <div class="tech-chip reveal"><div class="tech-icon" style="background:#5a29e4">Re</div><div><div class="name">REST APIs</div><div class="cat">Integration</div></div></div>
      </div>
      <p class="reveal delay-1" style="margin-top:2.5rem;color:var(--text-muted);font-size:0.88rem;max-width:580px">Plus day-to-day tools like Git &amp; GitHub, npm, and a familiarity with many more. I'm always learning &mdash; if your project needs something specific, I'll pick it up quickly.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="divider-label reveal"><span>What I Deliver</span><span class="line"></span></div>
      <div class="services-grid">
        <div class="card service-card tilt feature-card reveal"><div class="service-num">01</div><h3>Web Application Development</h3><p>End-to-end product builds with React, Vue or Next.js on the front, and Node, Python or PHP on the back. Tested, documented and ready to scale.</p><ul class="service-list"><li>Single-page &amp; server-rendered apps</li><li>Authentication &amp; authorization</li><li>Real-time features (WebSockets)</li><li>Performance optimization</li></ul></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-num">02</div><h3>UI / UX &amp; Product Design</h3><p>Full design cycles &mdash; from research and personas to high-fidelity prototypes and design systems your team can reuse.</p><ul class="service-list"><li>User research &amp; journey mapping</li><li>Wireframes &amp; interactive prototypes</li><li>Design systems &amp; component libraries</li><li>Usability &amp; accessibility audits</li></ul></div>
        <div class="card service-card tilt feature-card reveal delay-2"><div class="service-num">03</div><h3>WordPress Development</h3><p>Custom themes, plugins and headless WordPress builds that combine total client control with modern, fast front-ends.</p><ul class="service-list"><li>Bespoke themes &amp; child themes</li><li>Custom plugins &amp; ACF blocks</li><li>WooCommerce &amp; membership sites</li><li>Speed, security &amp; SEO hardening</li></ul></div>
        <div class="card service-card tilt feature-card reveal"><div class="service-num">04</div><h3>API &amp; Backend Engineering</h3><p>Robust, well-documented REST and GraphQL APIs, secure authentication, and clean data modelling that your front-end will love.</p><ul class="service-list"><li>RESTful &amp; GraphQL API design</li><li>Database schema &amp; optimization</li><li>Third-party integrations &amp; payments</li><li>Authentication &amp; security</li></ul></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-num">05</div><h3>E-Commerce Solutions</h3><p>Conversion-focused online stores on WooCommerce, Shopify or custom stacks &mdash; with payments, inventory and analytics dialed in.</p><ul class="service-list"><li>Store setup &amp; customization</li><li>Payment gateway integration</li><li>Inventory &amp; order management</li><li>Conversion optimization</li></ul></div>
        <div class="card service-card tilt feature-card reveal delay-2"><div class="service-num">06</div><h3>Maintenance &amp; Consulting</h3><p>Ongoing support, code audits, technical strategy and team mentorship to keep your product healthy and growing.</p><ul class="service-list"><li>Code reviews &amp; refactoring</li><li>Technical architecture consulting</li><li>Performance &amp; security audits</li><li>Team mentoring &amp; onboarding</li></ul></div>
      </div>
    </div>
  </section>

  <section class="section-tight"><div class="container"><div class="stats-band reveal">
    <div class="stat-block"><div class="num"><span data-count="15" data-suffix="+">0</span></div><div class="label">Technologies</div></div>
    <div class="stat-block"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years Practice</div></div>
    <div class="stat-block"><div class="num">Full Stack</div><div class="label">Front to Back</div></div>
    <div class="stat-block"><div class="num">100%</div><div class="label">Commitment</div></div>
  </div></div></section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>Need a specific skill<br>for your <span class="text-gold text-italic">project?</span></h2>
    <p>I'm fluent across the stack and quick to pick up what I don't yet know. Let's discuss what you need.</p>
    <a href="contact.html" class="btn btn-primary">Discuss Your Project <span class="arrow">&rarr;</span></a>
  </div></div></section>'''

# ===== PROJECTS =====
PROJECTS = '''<header class="page-header" id="top">
    <div class="hero-glow one"></div>
    <div class="container">
      <div class="breadcrumb reveal"><a href="index.html">Home</a><span class="sep">/</span><span>Work</span></div>
      <h1 class="reveal">What I <span class="text-gold text-italic">build.</span></h1>
      <p class="lead reveal delay-1">Real, hands-on development work &mdash; building web apps, WordPress platforms and design systems. Here's where I work, what I make, and what I'm capable of.</p>
    </div>
  </header>

  <section class="section"><div class="container">
    <div class="reveal" style="max-width:680px">
      <span class="eyebrow">Where I Work</span>
      <h2 class="section-title">Strategik <span class="text-gold text-italic">Technologies.</span></h2>
      <p class="section-subtitle" style="margin-bottom:2.5rem">I operate with <strong>Strategik Technologies</strong> &mdash; building real products, platforms and client solutions. This is where my day-to-day development work happens.</p>
    </div>
    <div class="card service-card tilt feature-card reveal delay-1" style="padding:2.5rem;display:flex;gap:2rem;align-items:center;flex-wrap:wrap">
      <div class="project-visual" style="width:120px;height:120px;border-radius:var(--radius-md);flex-shrink:0;background:linear-gradient(135deg,#1a2a3a,#0d1520);display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid var(--border-gold)">
        <div style="font-family:var(--font-display);font-size:2rem;font-weight:400;color:var(--gold-light);line-height:1">ST</div>
        <div style="font-family:var(--font-mono);font-size:0.5rem;letter-spacing:0.15em;color:var(--text-muted);margin-top:0.3rem;text-transform:uppercase">Technologies</div>
      </div>
      <div style="flex:1;min-width:240px">
        <div class="project-cat">Technology Company &middot; Lagos, Nigeria</div>
        <h3 style="font-family:var(--font-display);font-size:1.6rem;font-weight:400;margin:0.5rem 0 0.8rem">Strategik Technologies</h3>
        <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:1.2rem">Building web applications, WordPress platforms and digital products for real clients and businesses. I work across the full stack &mdash; design, front-end, back-end and deployment.</p>
        <div class="project-tags" style="margin-bottom:1.2rem"><span>WordPress</span><span>React</span><span>PHP</span><span>Full Stack</span><span>UI/UX</span></div>
        <a href="https://strategik.com.ng/" target="_blank" rel="noopener" class="btn btn-primary" style="padding:0.7rem 1.5rem;font-size:0.85rem">Visit strategik.com.ng <span class="arrow">&rarr;</span></a>
      </div>
    </div>
  </div></section>

  <section class="section" style="background:var(--bg-secondary)"><div class="container">
    <div class="reveal" style="max-width:680px">
      <span class="eyebrow">What I Build</span>
      <h2 class="section-title">The kind of work<br>I <span class="text-gold text-italic">deliver.</span></h2>
      <p class="section-subtitle">Here's an honest look at the work I take on across the full stack.</p>
    </div>
    <div class="services-grid">
      <div class="card service-card tilt feature-card reveal"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20 15 15 0 010-20z"/></svg></div><div class="project-cat">WordPress &middot; WooCommerce</div><h3>Custom WordPress Builds</h3><p>Bespoke themes, plugins and online stores &mdash; fast, maintainable, and easy for clients to manage.</p><div class="project-tags"><span>WordPress</span><span>PHP</span><span>WooCommerce</span></div></div>
      <div class="card service-card tilt feature-card reveal delay-1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div><div class="project-cat">Full Stack &middot; Web Apps</div><h3>Web Applications</h3><p>End-to-end apps with React front-ends and Python, Node.js or PHP back-ends &mdash; built to scale.</p><div class="project-tags"><span>React</span><span>Python</span><span>Node.js</span></div></div>
      <div class="card service-card tilt feature-card reveal delay-2"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg></div><div class="project-cat">UI / UX &middot; Design</div><h3>Interface Design</h3><p>Thoughtful, usable interfaces designed in Figma &mdash; from wireframe to polished prototype.</p><div class="project-tags"><span>Figma</span><span>UI/UX</span><span>Prototyping</span></div></div>
    </div>
  </div></section>

  <section class="section"><div class="container">
    <div class="reveal" style="text-align:center;max-width:640px;margin:0 auto">
      <span class="eyebrow" style="justify-content:center">Open Source &amp; Code</span>
      <h2 class="section-title">Real code,<br><span class="text-gold text-italic">on GitHub.</span></h2>
      <p class="section-subtitle" style="margin:0 auto">I build in the open. My GitHub is where you'll find real code, real commits and the languages I actually work with &mdash; TypeScript, JavaScript, HTML and more.</p>
      <div style="margin-top:2rem"><a href="https://github.com/golden123child" target="_blank" rel="noopener" class="btn btn-primary">View My GitHub Profile <span class="arrow">&rarr;</span></a></div>
    </div>
  </div></section>

  <section class="section-tight"><div class="container"><div class="stats-band reveal">
    <div class="stat-block"><div class="num"><span data-count="50" data-suffix="+">0</span></div><div class="label">Projects Delivered</div></div>
    <div class="stat-block"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years Experience</div></div>
    <div class="stat-block"><div class="num">Design + Code</div><div class="label">End to End</div></div>
    <div class="stat-block"><div class="num"><span data-count="98" data-suffix="%">0</span></div><div class="label">Happy Clients</div></div>
  </div></div></section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>Your project could be<br><span class="text-gold text-italic">next.</span></h2>
    <p>Let's talk about what you're building and how we can make it exceptional together.</p>
    <a href="contact.html" class="btn btn-primary">Start a Project <span class="arrow">&rarr;</span></a>
  </div></div></section>'''


# ===== EXPERIENCE =====
EXPERIENCE = '''<header class="page-header" id="top">
    <div class="hero-glow one"></div>
    <div class="container">
      <div class="breadcrumb reveal"><a href="index.html">Home</a><span class="sep">/</span><span>Journey</span></div>
      <h1 class="reveal">A path of continuous<br><span class="text-gold text-italic">growth.</span></h1>
      <p class="lead reveal delay-1">Six years of building, learning and leading. Here's the professional journey that shaped how I work today &mdash; and the milestones along the way.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <span class="eyebrow reveal">Professional Experience</span>
      <h2 class="section-title reveal">Where I've made an <span class="text-gold text-italic">impact.</span></h2>
      <div class="timeline" style="margin-top:4rem">
        <div class="tl-item reveal"><div class="tl-period">PRESENT</div><h3>Freelance Full Stack Developer &amp; UI/UX Designer</h3><div class="tl-company">Self-Employed &middot; Remote &amp; Lagos, Nigeria</div><p>I run my own independent practice, partnering directly with clients and small teams to design and build complete digital products &mdash; from the first wireframe to deployment.</p><ul class="tl-points"><li>Design and build full-stack web applications end-to-end</li><li>Custom WordPress, WooCommerce and headless CMS builds</li><li>UI/UX design &mdash; research, prototyping and design systems</li><li>Direct client collaboration, from discovery to launch</li></ul></div>
        <div class="tl-item reveal"><div class="tl-period">GROWING THE CRAFT</div><h3>Building Real Products for Real Clients</h3><div class="tl-company">Independent &amp; Contract Work</div><p>Over several years of freelance and contract work, I've shipped websites, web apps and design work across a range of industries &mdash; learning to own the full lifecycle of a product as a solo builder.</p><ul class="tl-points"><li>Worked across React, Python, Java, C++, PHP and the WordPress ecosystem</li><li>Integrated payments, APIs and third-party services</li><li>Specialised in performance, accessibility and clean, maintainable code</li><li>Built lasting client relationships and a referral network</li></ul></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <span class="eyebrow reveal">Education</span>
      <h2 class="section-title reveal">Foundations in <span class="text-gold text-italic">learning.</span></h2>
      <div class="timeline" style="margin-top:4rem">
        <div class="tl-item reveal"><div class="tl-period">BACHELOR'S DEGREE &middot; 4 YEARS</div><h3>B.Sc. Computer Science</h3><div class="tl-company">University of Lagos (UNILAG) &middot; CGPA 4.7</div><p>Graduated with first-class honours. A formal foundation in computing &mdash; algorithms, data structures, database systems, operating systems and software design. Coursework and projects programmed extensively across Java, C++ and Python.</p><ul class="tl-points"><li>Data structures, algorithms &amp; computational theory</li><li>Database systems &amp; SQL</li><li>Object-oriented programming in Java &amp; C++</li><li>Graduated with a 4.7 CGPA</li></ul></div>
        <div class="tl-item reveal"><div class="tl-period">CURRENTLY STUDYING &middot; 4-YEAR PROGRAM</div><h3>B.Sc. Software Engineering</h3><div class="tl-company">Miva Open University &middot; In Progress</div><p>Currently deepening my expertise with a second degree focused on software engineering &mdash; software architecture, systems design, testing methodologies and large-scale project engineering.</p><ul class="tl-points"><li>Software architecture &amp; design patterns</li><li>Systems engineering &amp; quality assurance</li><li>Project engineering at scale</li></ul></div>
        <div class="tl-item reveal"><div class="tl-period">ALWAYS</div><h3>Continuous Self-Directed Learning</h3><div class="tl-company">Ongoing</div><p>I treat learning as a permanent state. Beyond formal education, I continuously study modern frameworks, design thinking and systems architecture to keep my craft current.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <span class="eyebrow reveal">Education &amp; Certifications</span>
      <h2 class="section-title reveal">Always <span class="text-gold text-italic">growing.</span></h2>
      <p class="section-subtitle reveal delay-1">Two degrees and a set of professional certifications backing my craft.</p>
      <div class="divider-label reveal"><span>Degrees</span><span class="line"></span></div>
      <div class="services-grid">
        <div class="card service-card tilt feature-card reveal"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><div class="project-cat">Completed &middot; UNILAG</div><h3 style="font-size:1.2rem">B.Sc. Computer Science</h3><p style="font-size:0.9rem">University of Lagos &mdash; graduated with a 4.7 CGPA. Foundations in algorithms, databases and software design.</p></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></div><div class="project-cat">In Progress &middot; Miva Open University</div><h3 style="font-size:1.2rem">B.Sc. Software Engineering</h3><p style="font-size:0.9rem">Deepening expertise in software architecture, systems design and large-scale engineering.</p></div>
      </div>
      <div class="divider-label reveal" style="margin-top:3.5rem"><span>Professional Certifications</span><span class="line"></span></div>
      <div class="services-grid">
        <div class="card service-card tilt feature-card reveal"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">Meta</div><h3 style="font-size:1.1rem">Front-End Developer Professional</h3><p style="font-size:0.88rem">Advanced React, accessibility and modern front-end engineering.</p></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">Google</div><h3 style="font-size:1.1rem">UX Design Professional</h3><p style="font-size:0.88rem">End-to-end UX process, research, prototyping and design systems.</p></div>
        <div class="card service-card tilt feature-card reveal delay-2"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">AWS</div><h3 style="font-size:1.1rem">Cloud Practitioner</h3><p style="font-size:0.88rem">Foundations of cloud architecture, deployment and infrastructure.</p></div>
        <div class="card service-card tilt feature-card reveal"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">freeCodeCamp</div><h3 style="font-size:1.1rem">Full Stack &amp; Responsive Web</h3><p style="font-size:0.88rem">Comprehensive full-stack JavaScript and responsive design.</p></div>
        <div class="card service-card tilt feature-card reveal delay-1"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">WordPress</div><h3 style="font-size:1.1rem">Advanced Theme Development</h3><p style="font-size:0.88rem">Custom themes, block editor, headless and plugin architecture.</p></div>
        <div class="card service-card tilt feature-card reveal delay-2"><div class="service-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5L17 22l-5-3-5 3 1.5-8.5"/></svg></div><div class="project-cat">Cisco</div><h3 style="font-size:1.1rem">Programming Essentials in C/C++</h3><p style="font-size:0.88rem">Systems programming fundamentals and memory management.</p></div>
      </div>
    </div>
  </section>

  <section class="section-tight"><div class="container"><div class="stats-band reveal">
    <div class="stat-block"><div class="num"><span data-count="5" data-suffix="+">0</span></div><div class="label">Years Experience</div></div>
    <div class="stat-block"><div class="num"><span data-count="50" data-suffix="+">0</span></div><div class="label">Projects Delivered</div></div>
    <div class="stat-block"><div class="num">6</div><div class="label">Certifications</div></div>
    <div class="stat-block"><div class="num">2</div><div class="label">Degrees (CS + SWE)</div></div>
  </div></div></section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container">
      <span class="eyebrow reveal">Milestones</span>
      <h2 class="section-title reveal">Moments that <span class="text-gold text-italic">mattered.</span></h2>
      <div class="process-grid" style="margin-top:3.5rem">
        <div class="process-step reveal"><div class="step-num">01</div><h4>The First Lines of Code</h4><p>Started with HTML &amp; CSS, fascinated by how a few lines could become something real on a screen.</p></div>
        <div class="process-step reveal delay-1"><div class="step-num">02</div><h4>Going Deeper</h4><p>Picked up JavaScript, React and back-end languages &mdash; learning to build complete, working products.</p></div>
        <div class="process-step reveal delay-2"><div class="step-num">03</div><h4>Design Meets Code</h4><p>Studied UI/UX alongside engineering, realising the best software blends both disciplines.</p></div>
        <div class="process-step reveal delay-3"><div class="step-num">04</div><h4>Independent Practice</h4><p>Now running my own freelance work &mdash; designing and building full products for real clients, while continuing my studies.</p></div>
      </div>
    </div>
  </section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>The next chapter<br>could be <span class="text-gold text-italic">ours.</span></h2>
    <p>I'm always open to meaningful collaborations, ambitious projects and teams that value craft. Let's talk.</p>
    <a href="contact.html" class="btn btn-primary">Get in Touch <span class="arrow">&rarr;</span></a>
  </div></div></section>'''

# ===== CONTACT =====
CONTACT = '''<header class="page-header" id="top">
    <div class="hero-glow one"></div>
    <div class="container">
      <div class="breadcrumb reveal"><a href="index.html">Home</a><span class="sep">/</span><span>Contact</span></div>
      <h1 class="reveal">Let's create<br>something <span class="text-gold text-italic">together.</span></h1>
      <p class="lead reveal delay-1">Have a project, a question, or just want to say hello? I read every message and reply within 24 hours. Let's start a conversation.</p>
    </div>
  </header>

  <section class="section">
    <div class="container contact-grid">
      <div class="contact-info reveal">
        <span class="eyebrow">Get in Touch</span>
        <h3>Reach out directly.</h3>
        <p>Whether it's a full product build, a WordPress platform, a design sprint or a technical consultation &mdash; I'd love to hear about it.</p>
        <div class="contact-detail"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 6l-10 7L2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg></div><div><div class="det-label">Email</div><div class="det-value">folajimiwuraola4@gmail.com</div></div></div>
        <div class="contact-detail"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3-8.7A2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg></div><div><div class="det-label">Phone / WhatsApp</div><div class="det-value"><a href="tel:+2349130040046" style="color:inherit;text-decoration:none">09130040046</a> &nbsp;<a href="https://wa.me/2349130040046?text=Hi%20Wuraola%2C%20I%27d%20like%20to%20discuss%20a%20project." target="_blank" rel="noopener" style="color:var(--gold-light);text-decoration:none;border-bottom:1px solid rgba(212,175,55,0.3)">Chat on WhatsApp &rarr;</a></div></div></div>
        <div class="contact-detail"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div><div><div class="det-label">Location</div><div class="det-value">Lagos, Nigeria &middot; Remote Worldwide</div></div></div>
        <div class="contact-detail"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><div><div class="det-label">Response Time</div><div class="det-value">Usually within 24 hours</div></div></div>
        <div style="margin-top:2.5rem">
          <div style="font-family:var(--font-mono);font-size:0.78rem;letter-spacing:0.15em;color:var(--gold);text-transform:uppercase;margin-bottom:1rem">Follow Along</div>
          <div class="social-row">
            <a href="https://github.com/golden123child" target="_blank" rel="noopener" class="social-link" aria-label="GitHub"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .3a12 12 0 00-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.9 1.2 1.9 1.2 1 .1.8 1.7 2.6 1.2.1-.7.4-1.2.7-1.5-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 016 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0012 .3"/></svg></a>
            <a href="https://www.linkedin.com/in/wuraola-folajimi" target="_blank" rel="noopener" class="social-link" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.3A1.8 1.8 0 118.3 6.5 1.8 1.8 0 016.5 8.3zM19 19h-3v-4.7c0-1.1 0-2.5-1.5-2.5S13 13 13 14.2V19h-3v-9h2.9v1.2a3.1 3.1 0 012.8-1.5c3 0 3.5 2 3.5 4.5z"/></svg></a>
            <a href="https://wa.me/2349130040046" target="_blank" rel="noopener" class="social-link" aria-label="WhatsApp"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 018.413 3.488 11.82 11.82 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 001.515 5.26l-.999 3.648 3.973-1.607zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg></a>
            <a href="mailto:folajimiwuraola4@gmail.com" class="social-link" aria-label="Email"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 6l-10 7L2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg></a>
          </div>
        </div>
      </div>
      <div class="reveal delay-1">
        <form class="form-card" data-contact action="https://formsubmit.co/folajimiwuraola4@gmail.com" method="POST">
          <input type="hidden" name="_subject" value="New project enquiry from portfolio">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="_honey" style="display:none">
          <div class="form-row"><div class="form-group"><label for="fname">First Name</label><input type="text" id="fname" name="fname" placeholder="Wuraola" required></div><div class="form-group"><label for="lname">Last Name</label><input type="text" id="lname" name="lname" placeholder="Folajimi" required></div></div>
          <div class="form-group"><label for="email">Email Address</label><input type="email" id="email" name="email" placeholder="you@example.com" required></div>
          <div class="form-group"><label for="subject">Project Type</label><select id="subject" name="subject"><option>Full Stack Web Application</option><option>UI / UX Design</option><option>WordPress Development</option><option>E-Commerce Store</option><option>API / Back-End Engineering</option><option>Consulting / Other</option></select></div>
          <div class="form-group"><label for="budget">Estimated Budget</label><select id="budget" name="budget"><option>Under $1,000</option><option>$1,000 &mdash; $5,000</option><option>$5,000 &mdash; $15,000</option><option>$15,000+</option><option>Let's discuss</option></select></div>
          <div class="form-group"><label for="message">Tell me about your project</label><textarea id="message" name="message" placeholder="Share your goals, timeline, and anything that helps me understand your vision..." required></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send Message <span class="arrow">&rarr;</span></button>
          <p class="form-note">Your details stay private. I'll only use them to reply to your enquiry.</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--bg-secondary)">
    <div class="container" style="max-width:860px">
      <div style="text-align:center;margin-bottom:3.5rem"><span class="eyebrow reveal" style="justify-content:center">FAQ</span><h2 class="section-title reveal">Questions, <span class="text-gold text-italic">answered.</span></h2></div>
      <div class="reveal">
        <div class="faq-item"><div class="faq-q">What's your typical project timeline?<span class="toggle">+</span></div><div class="faq-a">It depends on scope. A focused landing page or WordPress site takes 1&ndash;3 weeks, while a full-stack application typically runs 6&ndash;12 weeks. After our first conversation, I'll give you a realistic timeline with clear milestones.</div></div>
        <div class="faq-item"><div class="faq-q">Do you work with clients remotely?<span class="toggle">+</span></div><div class="faq-a">Absolutely. I collaborate with clients across multiple continents and time zones. Clear communication, regular demos and async updates keep everything on track regardless of distance.</div></div>
        <div class="faq-item"><div class="faq-q">Can you handle both design and development?<span class="toggle">+</span></div><div class="faq-a">Yes &mdash; that's my specialty. Being fluent in both means tighter alignment between vision and execution, fewer hand-off gaps, and a single accountable partner from first sketch to final deploy.</div></div>
        <div class="faq-item"><div class="faq-q">Do you build with WordPress or custom code?<span class="toggle">+</span></div><div class="faq-a">Both. I build custom WordPress themes and plugins when clients need an easy-to-manage CMS, and fully custom stacks (React, Node, Python) when a product demands it. I'll recommend the right approach for your goals.</div></div>
        <div class="faq-item"><div class="faq-q">What does engagement and pricing look like?<span class="toggle">+</span></div><div class="faq-a">I offer both fixed-scope project pricing and monthly retainers. After understanding your needs, you'll receive a detailed proposal with transparent pricing, deliverables and a payment schedule.</div></div>
        <div class="faq-item"><div class="faq-q">Do you offer ongoing support after launch?<span class="toggle">+</span></div><div class="faq-a">Yes. Every project includes a post-launch support window, and I offer flexible maintenance retainers for updates, monitoring and continued iteration as your product grows.</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div style="text-align:center;max-width:640px;margin:0 auto 3rem">
        <span class="eyebrow reveal" style="justify-content:center">What Happens Next</span>
        <h2 class="section-title reveal">A clear path from <span class="text-gold text-italic">hello to launch.</span></h2>
        <p class="section-subtitle reveal delay-1" style="margin:0 auto">No mystery, no jargon. Here's exactly how we'll move from your first message to a shipped product.</p>
      </div>
      <div class="step-rail">
        <div class="sr-item reveal"><div class="sr-num">STEP 01</div><h4>You Reach Out</h4><p>Send a message via the form or email. Tell me about your goals, timeline and budget &mdash; even rough ideas welcome.</p></div>
        <div class="sr-item reveal delay-1"><div class="sr-num">STEP 02</div><h4>We Connect</h4><p>A free 30-minute call to align on scope, answer questions and see if we're a great fit. No pressure.</p></div>
        <div class="sr-item reveal delay-2"><div class="sr-num">STEP 03</div><h4>You Get a Plan</h4><p>A clear proposal with deliverables, milestones, timeline and transparent pricing &mdash; usually within 48 hours.</p></div>
        <div class="sr-item reveal delay-3"><div class="sr-num">STEP 04</div><h4>We Build &amp; Ship</h4><p>Regular demos, open communication, and a polished launch &mdash; then ongoing support as you grow.</p></div>
      </div>
    </div>
  </section>

  <section class="section"><div class="container"><div class="cta-banner reveal">
    <h2>Prefer to talk it through?<br>I'm just a <span class="text-gold text-italic">message away.</span></h2>
    <p>Let's turn your idea into something refined, reliable and genuinely remarkable.</p>
    <a href="mailto:folajimiwuraola4@gmail.com" class="btn btn-primary">Email Me Directly <span class="arrow">&rarr;</span></a>
  </div></div></section>'''

# ----------------------------------------------------------------------
# WRITE PAGES
# ----------------------------------------------------------------------
if __name__ == "__main__":
  pages = [
    ("index.html",      "Wuraola Folajimi \u2014 Full Stack Developer & UI/UX Designer", "Full stack developer and UI/UX designer crafting elegant web experiences with code and WordPress.", INDEX, "index.html"),
    ("about.html",      "About \u2014 Wuraola Folajimi", "The story, philosophy and values of Wuraola Folajimi.", ABOUT, "about.html"),
    ("skills.html",     "Expertise \u2014 Wuraola Folajimi", "Technical expertise, programming languages, frameworks and tools.", SKILLS, "skills.html"),
    ("projects.html",   "Work \u2014 Wuraola Folajimi", "Selected projects \u2014 web apps, WordPress builds, UI/UX design and e-commerce.", PROJECTS, "projects.html"),
    ("experience.html", "Journey \u2014 Wuraola Folajimi", "Professional journey, experience and education.", EXPERIENCE, "experience.html"),
    ("contact.html",    "Contact \u2014 Wuraola Folajimi", "Get in touch for full stack development, UI/UX design and WordPress projects.", CONTACT, "contact.html"),
  ]

  for fname, title, desc, body, active in pages:
      pathlib.Path(fname).write_text(page(title, desc, body, active))
      print(f"  \u2713 wrote {fname}")

  print(f"\nAll {len(pages)} pages generated.")
