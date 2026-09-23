// Cruxy landing page — footer year + Klaviyo contact form submission.

document.getElementById('year').textContent = new Date().getFullYear();

const KLAVIYO_PUBLIC_KEY = 'SKasJK';
const KLAVIYO_LIST_ID = 'YfTN2r';

// Bot protection: a hidden honeypot field (real visitors never see or fill it,
// since it's off-screen via CSS) plus a minimum-time check (scripted bots
// often submit instantly; a human takes at least a couple seconds to fill
// the form). Both checks fail silently with a fake success, so bots don't
// learn to adapt and real visitors are never affected.
const formLoadedAt = Date.now();
const MIN_SUBMIT_MS = 2000;

const form = document.getElementById('contactForm');
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
  submitBtn.textContent = isSubmitting ? 'Sending...' : 'Book a Discovery Call';
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

  const firstName = document.getElementById('firstName').value;
  const lastName = document.getElementById('lastName').value;
  const email = document.getElementById('email').value;
  const storeUrl = document.getElementById('storeUrl').value;
  const goals = document.getElementById('goals').value;

  if (!email) {
    setError('Email is required.');
    return;
  }

  setError('');
  setSubmitting(true);

  try {
    const res = await fetch(`https://a.klaviyo.com/client/subscriptions/?company_id=${KLAVIYO_PUBLIC_KEY}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'revision': '2024-10-15' },
      body: JSON.stringify({
        data: {
          type: 'subscription',
          attributes: {
            profile: {
              data: {
                type: 'profile',
                attributes: {
                  email,
                  first_name: firstName,
                  last_name: lastName,
                  properties: { 'Store URL': storeUrl, 'Goals': goals },
                },
              },
            },
          },
          relationships: { list: { data: { type: 'list', id: KLAVIYO_LIST_ID } } },
        },
      }),
    });

    if (!res.ok) throw new Error('Submission failed');

    formPanel.classList.add('hidden');
    successPanel.classList.add('visible');
  } catch (err) {
    setSubmitting(false);
    setError('Something went wrong. Please try again or email us directly.');
  }
});
