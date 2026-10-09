// Cruxy site-wide script: footer year, contact form (home page only), sticky header shadow.

const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const CONTACT_ENDPOINT = 'https://iztknzqbkouknleqjyug.supabase.co/functions/v1/contact-form';

// Bot protection: a hidden honeypot field (real visitors never see or fill it,
// since it's off-screen via CSS) plus a minimum-time check (scripted bots
// often submit instantly; a human takes at least a couple seconds to fill
// the form). Both checks fail silently with a fake success, so bots don't
// learn to adapt and real visitors are never affected.
const formLoadedAt = Date.now();
const MIN_SUBMIT_MS = 2000;

const form = document.getElementById('contactForm');

// Everything below only applies on pages that actually have the contact
// form (currently just the home page) — skip entirely elsewhere so this
// shared script doesn't error out on other pages.
if (form) {
const honeypot = document.getElementById('website');
const submitBtn = document.getElementById('submitBtn');
const formError = document.getElementById('formError');
const formPanel = document.getElementById('formPanel');
const successPanel = document.getElementById('successPanel');

function setError(msg) {
  if (msg) {
    formError.textContent = msg;
    formError.classList.add('visible');
  } else {
    formError.textContent = '';
    formError.classList.remove('visible');
  }
}

function setSubmitting(isSubmitting) {
  submitBtn.disabled = isSubmitting;
  submitBtn.style.opacity = isSubmitting ? '0.6' : '1';
  submitBtn.textContent = isSubmitting ? 'Sending...' : 'Submit';
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Bot check: honeypot filled in, or submitted too fast to be a real person.
  // Show the normal success state without actually sending anything to Klaviyo.
  if (honeypot.value || (Date.now() - formLoadedAt) < MIN_SUBMIT_MS) {
    formPanel.classList.add('hidden');
    successPanel.classList.add('visible');
    return;
  }

  const firstName = document.getElementById('firstName').value.trim();
  const lastName = document.getElementById('lastName').value.trim();
  const email = document.getElementById('email').value.trim();
  const company = document.getElementById('company').value.trim();
  const goals = document.getElementById('goals').value.trim();
  const optIn = document.getElementById('optIn').checked;

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    setError('Please enter a valid email.');
    return;
  }
  if (!goals) {
    setError('Please tell us how we can help.');
    return;
  }

  setError('');
  setSubmitting(true);

  try {
    // 1) The message always goes to us by email, independent of Klaviyo.
    const res = await fetch(CONTACT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ firstName, lastName, email, company, message: goals, optIn }),
    });
    if (!res.ok) throw new Error('Submission failed');

    // The server also saves name, email and company to Klaviyo, and sends
    // marketing consent only when the box is ticked.

    formPanel.classList.add('hidden');
    successPanel.classList.add('visible');
  } catch (err) {
    setSubmitting(false);
    setError('Something went wrong. Please try again or email us directly.');
  }
});
} // end if (form)

// Sticky header shadow on scroll
(function () {
  var header = document.querySelector('header.site-header');
  if (!header) return;
  function updateHeaderShadow() {
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', updateHeaderShadow, { passive: true });
  updateHeaderShadow();
})();

// "What It Does" tabs: one feature at a time. Advances by itself every 6 seconds until the visitor
// taps, swipes or uses the keyboard (or hovers, which only pauses it). Stays still for people who
// prefer reduced motion, and while off-screen.
(function () {
  const root = document.getElementById('feature-tabs');
  if (!root) return;
  const tabs = Array.from(root.querySelectorAll('.ft-tab'));
  const panels = Array.from(root.querySelectorAll('.ft-panel'));
  let current = 0;
  let stopped = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let hovering = false;
  let visible = false;

  function show(i) {
    current = (i + tabs.length) % tabs.length;
    tabs.forEach((t, n) => {
      const on = n === current;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      panels[n].classList.toggle('is-active', on);
    });
    const tab = tabs[current];
    const row = tab.parentElement;
    row.scrollTo({ left: tab.offsetLeft - (row.clientWidth - tab.offsetWidth) / 2, behavior: 'smooth' });
  }
  function userShow(i) { stopped = true; show(i); }

  tabs.forEach((t, n) => {
    t.addEventListener('click', () => userShow(n));
    t.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      e.preventDefault();
      userShow(current + (e.key === 'ArrowRight' ? 1 : -1));
      tabs[current].focus();
    });
  });

  let startX = null;
  const area = root.querySelector('.ft-panels');
  area.addEventListener('touchstart', (e) => { startX = e.touches[0].clientX; }, { passive: true });
  area.addEventListener('touchend', (e) => {
    if (startX === null) return;
    const dx = e.changedTouches[0].clientX - startX;
    startX = null;
    if (Math.abs(dx) > 50) userShow(current + (dx < 0 ? 1 : -1));
  }, { passive: true });

  root.addEventListener('mouseenter', () => { hovering = true; });
  root.addEventListener('mouseleave', () => { hovering = false; });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver((entries) => { visible = entries[0].isIntersecting; }, { threshold: 0.4 }).observe(root);
  } else {
    visible = true;
  }
  setInterval(() => { if (!stopped && !hovering && visible) show(current + 1); }, 6000);
})();
