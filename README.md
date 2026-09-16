# Cruxy website

A plain, no-build static site (HTML + CSS + vanilla JS) that reproduces the Lovable prototype.
No framework, no npm install, no lock-in. All the copy lives in `/content/*.json` — edit those
files (by hand, or through the `/admin` editor) and the site updates. The HTML/CSS never needs
to change for a copy edit.

## How it's structured

```
index.html, solutions.html, case-studies.html, about.html   ← page shells (rarely touched)
css/style.css                                                ← one shared design system
js/site.js                                                   ← fetches content/*.json and fills in the page
content/*.json                                                ← all the editable text/stats/cards
images/                                                        ← photos (replace aura-labs.jpg with a real shot)
admin/                                                         ← the in-browser content editor (Sveltia CMS)
```

Each page fetches its own JSON file over `fetch()` at load time, so this only works when served
over http(s) — opening `index.html` directly with `file://` will fail the fetch. Any static host
handles this fine.

## 1. Host it for free — GitHub Pages

1. Create a new **public** GitHub repo, e.g. `cruxy-website`.
2. Push everything in this folder to the repo's `main` branch.
3. In the repo: **Settings → Pages → Source → Deploy from a branch → `main` / `(root)`**.
4. Your site is live at `https://YOUR-USERNAME.github.io/cruxy-website/` within a minute or two.
5. Optional — point `cruxy.io` at it: **Settings → Pages → Custom domain**, enter `cruxy.io`,
   and add the DNS records GitHub shows you (an `A` record to GitHub's IPs, or a `CNAME` if
   you're using a subdomain). GitHub issues the SSL certificate automatically.

(Cloudflare Pages is an equally good free alternative if you'd rather build off your existing
Cloudflare account — same idea, connect the repo, no build command needed since there's no
framework to compile.)

## 2. Turn on the content editor (`/admin`)

The `/admin` folder is [Sveltia CMS](https://github.com/sveltia/sveltia-cms) — free, open source,
actively maintained, and a drop-in for the Decap CMS approach we talked about, just with a more
modern editing UI. It edits your GitHub repo directly: no database, no third-party host for your
content.

**One-time setup (about 5 minutes):**

1. **Edit `admin/config.yml`** — set `repo:` to your actual `username/cruxy-website`.
2. **Create a GitHub OAuth App** (GitHub → Settings → Developer settings → OAuth Apps → New OAuth App):
   - Homepage URL: `https://cruxy.io` (or your GitHub Pages URL)
   - Authorization callback URL: `https://YOUR-OAUTH-WORKER.workers.dev/callback` (from the next step)
   - Save the generated **Client ID** and **Client Secret**.
3. **Deploy the OAuth relay as a Cloudflare Worker** — GitHub Pages has no server, so the CMS
   needs a tiny relay to complete the login handshake. This is exactly the kind of Worker you
   already built for the `cruxy-github-push` pipeline, so the pattern will be familiar:
   - Use [`sveltia-cms-auth`](https://github.com/sveltia/sveltia-cms-auth) — a ready-made
     Cloudflare Worker for precisely this.
   - `wrangler deploy` it, then set the `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` secrets to
     the values from step 2.
   - Update `admin/config.yml`'s `base_url` to the Worker's URL.
4. Push the updated `config.yml`, visit `https://cruxy.io/admin/`, and log in with GitHub.

From then on, editing is: open `/admin`, click a page, change the text, hit **Save** — Sveltia
commits the JSON change straight to GitHub, and GitHub Pages redeploys automatically in under a
minute. No code, no terminal.

**Skip the CMS entirely if you want** — since content is just JSON, you can also edit
`content/home.json` etc. directly in GitHub's web editor (press `.` on any repo page to open the
github.dev editor) any time you don't want to set up the OAuth flow.

## 3. Local preview before you push

Any local static server works, e.g. from this folder:

```
python3 -m http.server 8000
```

then open `http://localhost:8000`.

## What's still placeholder

- `images/aura-labs.jpg` is a generated placeholder — swap in a real client/product photo (same
  filename, or update the `image` field in `content/home.json` and `content/case-studies.json`).
- The four team member photos on the About page are empty gray boxes (`.team-photo`) — add
  `<img>` tags there once you have real headshots, or keep them as intentional negative space.
- Nav "Start a project" and footer social links point to `#` — wire these up to your real contact
  flow (mailto, Calendly, socials) in the HTML files' `<nav>` and `<footer>`.
