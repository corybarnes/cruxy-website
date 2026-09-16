// Cruxy — content renderer
// Fetches /content/<page>.json and populates the page shell.
// Editing that JSON file (by hand, or via the /admin CMS) updates the live site — no HTML edits needed.

const ICONS = {
  store: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l1-5h16l1 5"/><path d="M4 9v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9"/><path d="M9 21V13h6v8"/></svg>',
  mail: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>'
};

async function loadContent(page) {
  const res = await fetch(`content/${page}.json`);
  if (!res.ok) throw new Error(`Could not load content/${page}.json`);
  return res.json();
}

function el(tag, opts = {}, children = []) {
  const node = document.createElement(tag);
  if (opts.class) node.className = opts.class;
  if (opts.html) node.innerHTML = opts.html;
  if (opts.text) node.textContent = opts.text;
  children.forEach(c => c && node.appendChild(c));
  return node;
}

function statBlock(num, label, cls = 'stat') {
  return el('div', { class: cls }, [
    el('div', { class: 'stat-num', text: num }),
    el('div', { class: 'stat-label', text: label })
  ]);
}

/* ---------- Home ---------- */
function renderHome(data) {
  document.getElementById('hero-badge').textContent = data.hero.badge;
  document.getElementById('hero-headline').textContent = data.hero.headline;
  document.getElementById('hero-lead').textContent = data.hero.lead;
  document.getElementById('hero-cta-label').textContent = data.hero.cta_label;

  const marks = document.getElementById('trust-marks');
  data.hero.trust_marks.forEach(m => marks.appendChild(el('span', { text: m })));

  const statsBar = document.getElementById('stats-bar');
  data.stats.forEach(s => statsBar.appendChild(statBlock(s.num, s.label)));

  document.getElementById('spec-heading').textContent = data.specializations.heading;
  document.getElementById('spec-lead').textContent = data.specializations.lead;
  const grid = document.getElementById('spec-grid');
  data.specializations.items.forEach(item => {
    const bullets = el('ul', {}, item.bullets.map(b => el('li', { text: b })));
    grid.appendChild(el('div', { class: 'card' }, [
      el('div', { class: 'card-icon', html: ICONS[item.icon] || '' }),
      el('h3', { text: item.title }),
      el('p', { text: item.desc }),
      bullets
    ]));
  });

  document.getElementById('feature-img').src = data.feature.image;
  document.getElementById('feature-stat-num').textContent = data.feature.stat_num;
  document.getElementById('feature-stat-label').textContent = data.feature.stat_label;
  document.getElementById('feature-heading').textContent = data.feature.heading;
  document.getElementById('feature-body').textContent = data.feature.body;
  document.getElementById('feature-link').textContent = data.feature.link_label + ' →';

  document.getElementById('testimonial-quote').textContent = `"${data.testimonial.quote}"`;
  document.getElementById('testimonial-name').textContent = data.testimonial.name;
  document.getElementById('testimonial-role').textContent = data.testimonial.role;

  document.getElementById('cta-heading').textContent = data.cta.heading;
  document.getElementById('cta-body').textContent = data.cta.body;
  document.getElementById('cta-primary').textContent = data.cta.primary;
  document.getElementById('cta-secondary').textContent = data.cta.secondary;
}

/* ---------- Solutions ---------- */
function renderSolutions(data) {
  document.getElementById('hero-badge').textContent = data.hero.badge;
  document.getElementById('hero-heading').textContent = data.hero.heading;
  document.getElementById('hero-lead').textContent = data.hero.lead;

  const grid = document.getElementById('disciplines-grid');
  data.disciplines.forEach(d => {
    const bullets = el('ul', {}, d.bullets.map(b => el('li', { text: b })));
    grid.appendChild(el('div', { class: 'card' }, [
      el('span', { class: 'card-num', text: d.num }),
      el('h3', { text: d.title }),
      el('p', { text: d.desc }),
      bullets
    ]));
  });

  document.getElementById('engage-heading').textContent = data.engage.heading;
  document.getElementById('engage-lead').textContent = data.engage.lead;
  const pricing = document.getElementById('pricing-grid');
  data.engage.tiers.forEach(t => {
    pricing.appendChild(el('div', { class: 'price-card' }, [
      el('h3', { text: t.title }),
      el('div', { class: 'price', text: t.price }),
      el('p', { text: t.desc })
    ]));
  });

  document.getElementById('cta-heading').textContent = data.cta.heading;
  document.getElementById('cta-body').textContent = data.cta.body;
  document.getElementById('cta-primary').textContent = data.cta.primary;
}

/* ---------- Case studies ---------- */
function renderCaseStudies(data) {
  document.getElementById('hero-badge').textContent = data.hero.badge;
  document.getElementById('hero-heading').textContent = data.hero.heading;
  document.getElementById('hero-lead').textContent = data.hero.lead;

  document.getElementById('feature-img').src = data.feature.image;
  document.getElementById('feature-eyebrow').textContent = data.feature.eyebrow;
  document.getElementById('feature-heading').textContent = data.feature.heading;
  document.getElementById('feature-body').textContent = data.feature.body;

  const list = document.getElementById('case-list');
  data.cases.forEach(c => {
    const statsRow = el('div', { class: 'case-stats' }, c.stats.map(s => statBlock(s.num, s.label)));
    list.appendChild(el('div', { class: 'case-card' }, [
      el('div', {}, [
        el('span', { class: 'case-tag', text: c.name + ' — ' + c.tag }),
        el('h3', { text: c.title }),
        el('p', { text: c.body })
      ]),
      statsRow
    ]));
  });

  document.getElementById('cta-heading').textContent = data.cta.heading;
  document.getElementById('cta-body').textContent = data.cta.body;
  document.getElementById('cta-primary').textContent = data.cta.primary;
  document.getElementById('cta-secondary').textContent = data.cta.secondary;
}

/* ---------- About ---------- */
function renderAbout(data) {
  document.getElementById('hero-badge').textContent = data.hero.badge;
  document.getElementById('hero-heading').textContent = data.hero.heading;
  document.getElementById('hero-lead').textContent = data.hero.lead;

  const statsBar = document.getElementById('stats-bar');
  data.stats.forEach(s => statsBar.appendChild(statBlock(s.num, s.label)));

  document.getElementById('operate-heading').textContent = data.operate.heading;
  document.getElementById('operate-lead').textContent = data.operate.lead;
  const principles = document.getElementById('principles-grid');
  data.operate.principles.forEach(p => {
    principles.appendChild(el('div', { class: 'card' }, [
      el('h3', { text: p.title }),
      el('p', { text: p.desc })
    ]));
  });

  document.getElementById('process-heading').textContent = data.process.heading;
  document.getElementById('process-lead').textContent = data.process.lead;
  const process = document.getElementById('process-grid');
  data.process.steps.forEach(s => {
    process.appendChild(el('div', { class: 'process-step' }, [
      el('span', { class: 'card-num', text: s.num }),
      el('h3', { text: s.title }),
      el('p', { text: s.desc })
    ]));
  });

  document.getElementById('team-heading').textContent = data.team.heading;
  document.getElementById('team-lead').textContent = data.team.lead;
  const team = document.getElementById('team-grid');
  data.team.members.forEach(m => {
    team.appendChild(el('div', { class: 'team-card' }, [
      el('div', { class: 'team-photo' }),
      el('div', { class: 'name', text: m.name }),
      el('div', { class: 'role', text: m.role })
    ]));
  });

  document.getElementById('cta-heading').textContent = data.cta.heading;
  document.getElementById('cta-body').textContent = data.cta.body;
  document.getElementById('cta-primary').textContent = data.cta.primary;
}

const RENDERERS = {
  home: renderHome,
  solutions: renderSolutions,
  'case-studies': renderCaseStudies,
  about: renderAbout
};

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.page;
  const renderer = RENDERERS[page];
  if (!renderer) return;
  loadContent(page).then(renderer).catch(err => console.error(err));
});
