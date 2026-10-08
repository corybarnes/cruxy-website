// Cruxy site-wide script: footer year, contact form (home page only), sticky header shadow.

const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const KLAVIYO_PUBLIC_KEY = 'SKasJK';
const KLAVIYO_LIST_ID = 'YfTN2r';
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

    // 2) Only if the visitor ticked the box: subscribe name, email and company
    // to Klaviyo. The message is never sent there. A Klaviyo failure never
    // affects the form, since the email already went through.
    if (optIn) {
      fetch(`https://a.klaviyo.com/client/subscriptions/?company_id=${KLAVIYO_PUBLIC_KEY}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'revision': '2024-10-15' },
        body: JSON.stringify({
          data: {
            type: 'subscription',
            attributes: {
              profile: { data: { type: 'profile', attributes: {
                email, first_name: firstName, last_name: lastName,
                properties: { 'Company': company, 'Source': 'Website contact form' },
              } } },
            },
            relationships: { list: { data: { type: 'list', id: KLAVIYO_LIST_ID } } },
          },
        }),
      }).catch(() => {});
    }

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
