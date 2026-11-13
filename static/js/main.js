// Technology on Wheels: vanilla JS
(function () {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');
  $('#yr').textContent = new Date().getFullYear();

  // mobile menu
  const burger = $('.burger'), links = $('#links');
  burger.addEventListener('click', () => burger.setAttribute('aria-expanded', links.classList.toggle('open')));

  // scroll reveal (IntersectionObserver)
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
    $$('.reveal').forEach(el => io.observe(el));
  } else $$('.reveal').forEach(el => el.classList.add('in'));

  // hero fallback when CSS scroll-driven animations are not supported
  const hero = $('#hero');
  if (hero && !reduce && !CSS.supports('animation-timeline: scroll()')) {
    hero.classList.add('js-scroll');
    let tick = false;
    const update = () => { hero.style.setProperty('--p', Math.min(1, Math.max(0, scrollY / (innerHeight * 1.2))).toFixed(3)); tick = false; };
    addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  // gallery filter + lightbox
  const chips = $$('.chip'), projs = $$('.proj');
  chips.forEach(c => c.addEventListener('click', () => {
    chips.forEach(x => x.classList.toggle('active', x === c));
    projs.forEach(p => p.hidden = c.dataset.f !== 'all' && p.dataset.cat !== c.dataset.f);
  }));
  const lb = $('#lb');
  if (lb) {
    let last;
    const open = p => {
      last = p; const d = p.dataset;
      $('#lb-media').innerHTML = d.img ? `<img alt="${d.title}" src="${d.img}">` : `<div class="ph">${d.icon}</div>`;
      $('#lb-t').textContent = d.title; $('#lb-d').textContent = d.desc; $('#lb-m').textContent = d.cat || p.dataset.cat + ' · ' + d.team;
      lb.hidden = false; $('.lb-x').focus();
    };
    const close = () => { lb.hidden = true; last && last.focus(); };
    projs.forEach(p => { p.addEventListener('click', () => open(p)); p.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(p); } }); });
    $('.lb-x').addEventListener('click', close);
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    addEventListener('keydown', e => { if (e.key === 'Escape' && !lb.hidden) close(); });
  }

  // form validation
  const form = $('#form');
  if (form) {
    const msg = { valueMissing: 'This field is required.', typeMismatch: 'Enter a valid value.' };
    const show = (name, text) => { const e = $(`.err[data-for="${name}"]`, form); if (e) e.textContent = text; };
    form.addEventListener('submit', e => {
      let ok = true;
      $$('input,textarea,select', form).forEach(f => {
        if (f.type === 'radio') return;
        const bad = !f.checkValidity(); show(f.name, bad ? (f.validity.valueMissing ? msg.valueMissing : msg.typeMismatch) : ''); if (bad) ok = false;
      });
      if ($('.stars', form) && !$('input[name=rating]:checked', form)) { show('rating', 'Please choose a rating.'); ok = false; }
      if (!ok) { e.preventDefault(); $('.err:not(:empty)', form)?.scrollIntoView({ block: 'center' }); }
    });
  }
  setTimeout(() => $$('.toast').forEach(t => t.remove()), 6000);
})();
