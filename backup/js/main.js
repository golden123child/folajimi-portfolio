/* ============================================================
   WURAOLA FOLAJIMI — PORTFOLIO ENGINE
   SPA Router + All Interactions (Enhanced Edition)
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- 01 · PRELOADER ---------- */
  const pre = document.createElement('div');
  pre.className = 'preloader';
  pre.innerHTML = '<div class="pre-inner"><div class="pre-mark">W</div><div class="pre-bar"><span></span></div><div class="pre-txt">Crafting the experience</div></div>';
  document.body.appendChild(pre);
  window.addEventListener('load', () => {
    setTimeout(() => {
      pre.classList.add('done');
      setTimeout(() => pre.remove(), 700);
      kickOff();
    }, 900);
  });
  // Fallback in case load already fired / stalls
  setTimeout(() => { if (document.body.contains(pre)) { pre.classList.add('done'); setTimeout(() => pre.remove(), 700); kickOff(); } }, 4000);

  /* ---------- (custom cursor removed) ---------- */

  /* ---------- (scroll progress bar removed) ---------- */

  /* ---------- 04 · BACK TO TOP ---------- */
  const btt = document.createElement('button'); btt.className = 'back-to-top';
  btt.setAttribute('aria-label', 'Back to top');
  btt.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"/></svg>';
  document.body.appendChild(btt);
  btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- 05 · SPA PAGE ROUTER ---------- */
  const pages = document.querySelectorAll('.spa-page');

  const showPage = (pageId) => {
    let target = document.getElementById('page-' + pageId);
    if (!target) { target = document.getElementById('page-home'); pageId = 'home'; }
    pages.forEach(p => p.classList.remove('active'));
    target.classList.add('active');
    window.scrollTo(0, 0);
    document.querySelectorAll('.nav-links a[data-page]').forEach(a => {
      a.classList.toggle('active', a.dataset.page === pageId);
    });
    requestAnimationFrame(() => {
      triggerReveals(target);
      initPageFeatures(target);
      initTilt(target);
    });
  };

  document.querySelectorAll('[data-page]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const page = link.dataset.page;
      history.pushState({ page }, '', '#' + page);
      showPage(page);
      if (navLinksEl) setMenuOpen(false);
    });
  });

  window.addEventListener('popstate', () => {
    showPage(location.hash.replace('#', '') || 'home');
  });

  /* ---------- 06 · NAVBAR + GLOBAL SCROLL ---------- */
  const navbar = document.querySelector('.navbar');
  const onScroll = () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    const pct = h > 0 ? (window.scrollY / h) * 100 : 0;
    if (navbar) navbar.classList.toggle('scrolled', window.scrollY > 40);
    btt.classList.toggle('show', window.scrollY > 600);
    const active = document.querySelector('.spa-page.active');
    if (active) triggerReveals(active);
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- 07 · MOBILE MENU ---------- */
  const toggle = document.querySelector('.menu-toggle');
  const navLinksEl = document.querySelector('.nav-links');
  const setMenuOpen = (isOpen) => {
    navLinksEl.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
  };
  if (toggle && navLinksEl) {
    toggle.addEventListener('click', () => setMenuOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    document.addEventListener('click', (event) => {
      if (!navLinksEl.contains(event.target) && !toggle.contains(event.target)) setMenuOpen(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenuOpen(false);
        toggle.focus();
      }
    });
  }

  /* ---------- 08 · REVEAL (IntersectionObserver — works on all screen sizes) ---------- */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

  const triggerReveals = (scope) => {
    scope.querySelectorAll('.reveal:not(.visible)').forEach(el => revealObserver.observe(el));
  };

  /* ---------- 09 · PAGE FEATURES (counters / skill bars) ---------- */
  const initPageFeatures = (scope) => {
    scope.querySelectorAll('[data-count]:not(.counted)').forEach(el => {
      el.classList.add('counted');
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const dec = el.dataset.decimal === 'true';
      const duration = 1700;
      const start = performance.now();
      const step = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        const val = target * eased;
        el.textContent = (dec ? val.toFixed(1) : Math.floor(val)) + suffix;
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      };
      requestAnimationFrame(step);
    });
    scope.querySelectorAll('.skill-fill[data-width]:not(.filled)').forEach(el => {
      el.classList.add('filled');
      requestAnimationFrame(() => { el.style.width = el.dataset.width + '%'; });
    });
  };

  /* ---------- 10 · TYPING EFFECT ---------- */
  const startTyping = () => {
    const typeEl = document.querySelector('[data-typing]');
    if (!typeEl || typeEl.dataset.started) return;
    typeEl.dataset.started = '1';
    const phrases = JSON.parse(typeEl.dataset.typing);
    let pi = 0, ci = 0, deleting = false;
    const cursor = '<span class="type-cursor"></span>';
    const tick = () => {
      const current = phrases[pi];
      if (deleting) {
        typeEl.innerHTML = current.substring(0, ci - 1) + cursor; ci--;
        if (ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; setTimeout(tick, 500); return; }
        setTimeout(tick, 40);
      } else {
        typeEl.innerHTML = current.substring(0, ci + 1) + cursor; ci++;
        if (ci === current.length) { deleting = true; setTimeout(tick, 2200); return; }
        setTimeout(tick, 70);
      }
    };
    typeEl.innerHTML = cursor;
    setTimeout(tick, 600);
  };

  /* ---------- 11 · 3D TILT ---------- */
  const initTilt = (scope) => {
    scope.querySelectorAll('.tilt:not(.tilted)').forEach(card => {
      card.classList.add('tilted');
      const strength = 10;
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width;
        const py = (e.clientY - r.top) / r.height;
        const rx = (py - 0.5) * -strength;
        const ry = (px - 0.5) * strength;
        card.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px)`;
        card.style.setProperty('--mx', px * 100 + '%');
        card.style.setProperty('--my', py * 100 + '%');
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  };

  /* ---------- 12 · TESTIMONIAL CAROUSEL ---------- */
  const initCarousel = () => {
    const track = document.querySelector('.tst-track');
    if (!track || track.dataset.bound) return;
    track.dataset.bound = '1';
    const slides = Array.from(track.children);
    const dotsWrap = document.querySelector('.tst-dots');
    let idx = 0, timer;
    slides.forEach((_, i) => {
      const d = document.createElement('button');
      d.className = 'tst-dot' + (i === 0 ? ' active' : '');
      d.addEventListener('click', () => go(i));
      dotsWrap.appendChild(d);
    });
    const dots = Array.from(dotsWrap.children);
    const go = (n) => {
      idx = (n + slides.length) % slides.length;
      track.style.transform = `translateX(-${idx * 100}%)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === idx));
    };
    const next = () => go(idx + 1);
    const start = () => { timer = setInterval(next, 5500); };
    const reset = () => { clearInterval(timer); start(); };
    document.querySelector('.tst-next')?.addEventListener('click', () => { go(idx + 1); reset(); });
    document.querySelector('.tst-prev')?.addEventListener('click', () => { go(idx - 1); reset(); });
    track.addEventListener('mouseenter', () => clearInterval(timer));
    track.addEventListener('mouseleave', start);
    start();
  };

  /* ---------- 13 · FAQ ACCORDION ---------- */
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ---------- 14 · PROJECT FILTER ---------- */
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      document.querySelectorAll('.project-card').forEach(card => {
        const cats = card.dataset.cat || '';
        card.style.display = (filter === 'all' || cats.includes(filter)) ? '' : 'none';
      });
    });
  });

  /* ---------- 15 · FORM HANDLER (real backend via FormSubmit) ---------- */
  const form = document.querySelector('form[data-contact]');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type=submit]');
      const original = btn.innerHTML;
      btn.disabled = true;
      btn.innerHTML = 'Sending&hellip;';
      try {
        const formData = new FormData(form);
        const res = await fetch('https://formsubmit.co/ajax/folajimiwuraola4@gmail.com', {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: formData
        });
        if (!res.ok) throw new Error('Network response was not ok');
        btn.innerHTML = '\u2713 Message Sent';
        btn.style.background = 'linear-gradient(135deg,#5eead4,#34d399)';
        btn.style.color = '#08080d';
        form.reset();
        setTimeout(() => { btn.innerHTML = original; btn.style.background = ''; btn.style.color = ''; btn.disabled = false; }, 4000);
      } catch (err) {
        btn.innerHTML = '\u26A0 Try email instead';
        btn.disabled = false;
        setTimeout(() => { btn.innerHTML = original; }, 4500);
      }
    });
  }

  /* ---------- 16 · MAGNETIC BUTTONS ---------- */
  document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      btn.style.transform = `translate(${x * 0.15}px,${y * 0.25 - 3}px)`;
    });
    btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
  });

  /* ---------- 17 · FOOTER YEAR ---------- */
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  /* ---------- 18 · KICKOFF (after preloader) ---------- */
  function kickOff() {
    showPage(location.hash.replace('#', '') || 'home');
    startTyping();
    initCarousel();
    onScroll();
  }
});
