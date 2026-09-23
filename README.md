# Cruxy website

A single-page, no-build static site (HTML + CSS + vanilla JS). No framework, no npm install,
no CMS. Copy and images are edited directly in the files below.

## How it's structured

```
index.html            ← the whole site (header, hero, services, CTA, contact form, footer)
css/style.css          ← styles + self-hosted Poppins @font-face declarations
js/site.js              ← footer year + the Klaviyo contact-form submission
fonts/                  ← self-hosted Poppins woff2 files (no Google Fonts dependency)
images/cruxy-logo.svg, cruxy-mark.svg   ← brand logo (header/footer) and favicon mark
images/hero-photo-PLACEHOLDER.jpg        ← swap this for a real hero photo
images/logos/                            ← Shopify / Klaviyo / Google Analytics logos shown in the services section
```

## Contact form → Klaviyo

The form in `#contact` posts directly to Klaviyo's public client API
(`https://a.klaviyo.com/client/subscriptions/`) with the public company/list keys hardcoded in
`js/site.js` (`KLAVIYO_PUBLIC_KEY`, `KLAVIYO_LIST_ID` — safe to expose, this is Klaviyo's
public/client-side key, not a private key). It captures two custom profile properties, `Store URL`
and `Goals`, and swaps the form for a "Thanks! We'll be in touch soon." confirmation on success.

## Hosting — GitHub Pages

This repo is already set up for GitHub Pages: **Settings → Pages → Source → Deploy from a
branch → `main` / `(root)`**. Any push to `main` redeploys automatically within a minute or two.

## Local preview

```
python3 -m http.server 8000
```
then open `http://localhost:8000`.

## Still placeholder

- `images/hero-photo-PLACEHOLDER.jpg` — replace with a real photo (same filename, or update the
  `<img src>` in the hero section of `index.html`).
