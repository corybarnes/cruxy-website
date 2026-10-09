#!/usr/bin/env python3
"""Builds the Cruxy support section (support/**/index.html, search index, screenshot list).
Run from the repo root:  python3 scripts/build_support.py
A missing screenshot never stops the build: it becomes a placeholder and is listed in scripts/SCREENSHOTS.md."""
import html, json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from support_content import PAGES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOINDEX = True  # flip to False at launch, and add the pages to sitemap.xml
missing = []    # (page, section, alt, need)

def esc(s): return html.escape(s, quote=True)
def strip_tags(h): return re.sub(r'\s+([,.;:!?)])', r'\1', re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))).strip()

def fig(page, section, sh, prefix):
    path, alt, need = sh
    if path and os.path.exists(os.path.join(ROOT, 'images', path)):
        return '<figure><img src="%simages/%s" alt="%s" loading="lazy"></figure>' % (prefix, path, esc(alt))
    missing.append((page['title'], section[1], alt, need or alt, path))
    return ('<figure><div class="shot-missing" role="img" aria-label="%s"><strong>Screenshot coming</strong><span>%s</span></div></figure>'
            % (esc(alt), esc(alt)))

def nav_html(current, prefix):
    out = ['<nav class="snav" aria-label="Support topics"><div class="snav-title">Support</div><ul>']
    out.append('<li><a href="%ssupport/"%s>Support home</a></li>' % (prefix, ' aria-current="page"' if current is None else ''))
    for p in PAGES:
        cur = ' aria-current="page"' if current == p['slug'] else ''
        out.append('<li><a href="%ssupport/%s/"%s>%s</a></li>' % (prefix, p['slug'], cur, esc(p['nav'])))
    out.append('</ul></nav>')
    return ''.join(out)

def head(title, desc, canon, prefix):
    robots = '<meta name="robots" content="noindex, nofollow">\n' if NOINDEX else ''
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
%s<link rel="canonical" href="https://cruxy.io/%s">
<link rel="icon" type="image/svg+xml" href="%simages/cruxy-mark.svg">
<link rel="stylesheet" href="%scss/style.css">
<link rel="stylesheet" href="%scss/support.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a href="%sindex.html" class="logo-link" aria-label="Cruxy home"><img src="%simages/cruxy-logo.svg" alt="Cruxy"></a>
    <nav class="main-nav">
      <a href="%sindex.html#features" class="nav-link">Features</a>
      <a href="%sindex.html#pricing" class="nav-link">Pricing</a>
      <a href="%ssupport/" class="nav-link">Support</a>
      <a href="https://get.cruxy.io/signup" class="btn-book">Start Free</a>
    </nav>
  </div>
</header>
''' % (esc(title), esc(desc), robots, canon, prefix, prefix, prefix, prefix, prefix, prefix, prefix, prefix)

def foot(prefix):
    return '''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-about"><img src="%simages/cruxy-logo.svg" alt="Cruxy"><p>Free time tracking and invoicing for freelancers.</p></div>
      <div class="footer-cols">
        <div class="footer-col"><div class="footer-col-title">Product</div>
          <a href="%sindex.html#features">Features</a><a href="%sindex.html#pricing">Pricing</a><a href="%sindex.html#faq">FAQ</a></div>
        <div class="footer-col"><div class="footer-col-title">Support</div>
          <a href="%ssupport/">Help center</a><a href="mailto:support@cruxy.io">support@cruxy.io</a></div>
      </div>
    </div>
    <div class="footer-bottom"><span>&copy; Cruxy LLC. All rights reserved.</span>
      <div class="footer-legal"><a href="%sprivacy.html">Privacy Policy</a><a href="%sterms.html">Terms of Use</a><a href="%sdelete-account.html">Delete Account</a></div></div>
  </div>
</footer>
<script src="%ssupport/search.js" defer></script>
</body>
</html>
''' % ((prefix,) * 9)

def searchbox(prefix, big=False):
    return ('<div class="ssearch%s" data-index="%ssupport/search-index.json" data-base="%s">'
            '<label class="sr-only" for="q">Search the help center</label>'
            '<input id="q" type="search" placeholder="Search the help center" autocomplete="off">'
            '<div class="sresults" hidden></div></div>') % (' ssearch-big' if big else '', prefix, prefix)

def build_page(page, index):
    prefix = '../../'
    secs = page['sections']
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (s[0], esc(s[1])) for s in secs)
    body = []
    for n, sec in enumerate(secs, 1):
        sid, title, content, shots = sec[0], sec[1], sec[2], sec[3]
        kind = sec[4] if len(sec) > 4 else 'art'
        num = '<span class="step-num">%d</span>' % n if kind == 'step' else ''
        figs = ''.join(fig(page, sec, sh, prefix) for sh in shots)
        cls = 'sec' + (' sec-shots' if shots else '')
        body.append('<section class="%s" id="%s"><div class="sec-text">%s<h2>%s</h2>%s</div>%s</section>'
                    % (cls, sid, num, esc(title), content, ('<div class="sec-figs">%s</div>' % figs) if figs else ''))
        index.append(dict(url='support/%s/#%s' % (page['slug'], sid), page=page['title'], title=title,
                          text=strip_tags(content)))
    others = [p for p in PAGES if p['slug'] != page['slug']][:0]
    out = head('%s | Cruxy Support' % page['title'], page['desc'], 'support/%s/' % page['slug'], prefix)
    out += '''<main><div class="support-shell">
<aside>%s</aside>
<article class="support-main">
<p class="crumbs"><a href="%sindex.html">Cruxy</a> / <a href="../">Support</a> / %s</p>
%s
<h1>%s</h1>
<p class="support-lead">%s</p>
<nav class="toc" aria-label="On this page"><div class="toc-title">On this page</div><ol>%s</ol></nav>
%s
<div class="still-stuck">Still stuck? Email us at <a href="mailto:support@cruxy.io">support@cruxy.io</a>.</div>
</article></div></main>
''' % (nav_html(page['slug'], prefix), prefix, esc(page['title']), searchbox(prefix), esc(page['title'] if page['slug'] != 'get-started' else 'Get started with Cruxy'),
       esc(page['intro']), toc, '\n'.join(body))
    out += foot(prefix)
    d = os.path.join(ROOT, 'support', page['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(out)

def build_home():
    prefix = '../'
    cards = ''.join('<a class="topic" href="%s/"><strong>%s</strong><span>%s</span></a>' % (p['slug'], esc(p['title']), esc(p['intro'])) for p in PAGES if p['slug'] not in ('get-started', 'contact'))
    popular = [('get-started', 'first-invoice', 'Send your first invoice'), ('time', 'timer', 'Use the timer'),
               ('alerts', 'client-reminders', 'Automatic reminders to your clients'), ('billing', 'cancel', 'Cancel Pro'),
               ('troubleshooting', 'email-missing', "An invoice email didn't arrive"), ('free-vs-pro', 'compare', 'What Free and Pro include')]
    pop = ''.join('<li><a href="%s/#%s">%s</a></li>' % (a, b, esc(c)) for a, b, c in popular)
    out = head('Help Center | Cruxy Support', 'Help for Cruxy, the free time tracking and invoicing app for freelancers: getting started, logging time, invoices, alerts, plans and billing.', 'support/', prefix)
    out += '''<main><div class="support-home">
<div class="home-hero"><h1>How can we help?</h1>%s</div>
<div class="wrap-s">
<a class="start-card" href="get-started/"><div><strong>New to Cruxy?</strong><span>Set up in about five minutes: account, first client, first time, first invoice.</span></div><em>Get started &rarr;</em></a>
<h2>Browse by topic</h2>
<div class="topics">%s</div>
<h2>Popular questions</h2>
<ul class="pop">%s</ul>
<div class="still-stuck">Can't find it? Email us at <a href="mailto:support@cruxy.io">support@cruxy.io</a>.</div>
</div></div></main>
''' % (searchbox(prefix, True), cards, pop)
    out += foot(prefix)
    open(os.path.join(ROOT, 'support', 'index.html'), 'w').write(out)

def main():
    index = []
    for p in PAGES:
        build_page(p, index)
    build_home()
    os.makedirs(os.path.join(ROOT, 'support'), exist_ok=True)
    json.dump(index, open(os.path.join(ROOT, 'support', 'search-index.json'), 'w'), separators=(',', ':'))
    lines = ['# Screenshots still needed', '', 'Generated by scripts/build_support.py. Each item renders as a "Screenshot coming" placeholder on the page.', '']
    cur = None
    for page, sec, alt, need, path in missing:
        if page != cur:
            lines += ['', '## ' + page]; cur = page
        lines.append('- [ ] %s: %s' % (sec, need))
    lines += ['', '## Existing screenshots to retake or check when refreshing the set',
              '- [ ] settings-invoicing.png, settings-profile.png, settings-tasks.png: the Settings tab row now has an Alerts tab',
              '- [ ] client-details.png and client-invoices.png: check against the current client modal (gear icon for details, Reminders tab)',
              '- [ ] app/import-pick.jpg, app/import-review.png, app/invoices-list.png, app/retainers-progress.png: older shots, check they match the current app',
              '- [ ] Retake all with one consistent demo workspace and device frame once the client-reminders work is merged']
    open(os.path.join(ROOT, 'scripts', 'SCREENSHOTS.md'), 'w').write('\n'.join(lines) + '\n')
    print('pages: %d + home, sections: %d, missing screenshots: %d' % (len(PAGES), len(index), len(missing)))

main()
