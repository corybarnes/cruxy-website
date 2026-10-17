#!/usr/bin/env python3
"""Builds the Cruxy support section (support/**/index.html, search index, screenshot list).
Run from the repo root:  python3 scripts/build_support.py
A missing screenshot never stops the build: it becomes a placeholder and is listed in scripts/SCREENSHOTS.md."""
import html, json, os, re, sys
from html.parser import HTMLParser
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from support_content import PAGES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOINDEX = False  # True adds noindex and leaves Support out of sitemap.xml / llms.txt
SITE = 'https://cruxy.io/'
PUBLISHED = '2026-10-09'
MODIFIED = '2026-10-14'
SOCIAL_IMG = SITE + 'images/hero/og-share-2.png'
SEO_TITLES = {
    'get-started': 'Get started with Cruxy: set up in 5 minutes',
    'time': 'Log time in Cruxy: timer, entries and timesheet',
    'clients-projects': 'Clients and projects in Cruxy',
    'invoices': 'Create, email and track invoices in Cruxy',
    'alerts': 'Cruxy alerts and overdue invoice reminders',
    'budgets-retainers': 'Project budgets and retainers in Cruxy',
    'free-vs-pro': 'Cruxy Free vs Pro: what each plan includes',
    'billing': 'Cruxy billing: upgrade, cancel and manage Pro',
    'account': 'Your Cruxy account: profile, sign-in, install',
    'troubleshooting': 'Cruxy troubleshooting: common fixes',
    'contact': 'Contact Cruxy support',
}
missing = []    # (page, section, alt, need)

def esc(s): return html.escape(s, quote=True)
def strip_tags(h): return re.sub(r'\s+([,.;:!?)])', r'\1', re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))).strip()

def fig(page, section, sh, prefix):
    path, alt, need = sh
    if path and os.path.exists(os.path.join(ROOT, 'images', path)):
        w, h = Image.open(os.path.join(ROOT, 'images', path)).size
        return '<figure><img src="%simages/%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></figure>' % (prefix, path, esc(alt), w, h)
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

def jsonld(*objs):
    data = [dict({'@context': 'https://schema.org'}, **o) for o in objs]
    return '<script type="application/ld+json">%s</script>\n' % json.dumps(data, ensure_ascii=False).replace('</', '<\\/')

def head(title, desc, canon, prefix, extra=''):
    robots = ('<meta name="robots" content="noindex, nofollow">\n' if NOINDEX else
              '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n')
    url = SITE + canon
    robots += ('<meta property="og:type" content="website">\n<meta property="og:site_name" content="Cruxy">\n'
               '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
               '<meta property="og:url" content="%s">\n<meta property="og:image" content="%s">\n'
               '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="%s">\n'
               '<meta name="twitter:description" content="%s">\n<meta name="twitter:image" content="%s">\n'
               '<meta name="theme-color" content="#FFC60B">\n') % (esc(title), esc(desc), url, SOCIAL_IMG, esc(title), esc(desc), SOCIAL_IMG)
    robots += extra
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
          <a href="%ssupport/">Help Center</a><a href="mailto:support@cruxy.io">support@cruxy.io</a></div>
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


class MD(HTMLParser):
    """Small HTML to Markdown converter for the support article bodies."""
    def __init__(self):
        super().__init__(); self.out = []; self.lists = []; self.href = None; self.row = None; self.cell = None; self.rows = []
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ('strong', 'b'): self.out.append('**')
        elif t == 'em': self.out.append('*')
        elif t == 'code': self.out.append('`')
        elif t == 'a': self.href = a.get('href', ''); self.out.append('[')
        elif t in ('ul', 'ol'): self.lists.append([t, 0])
        elif t == 'li':
            l = self.lists[-1]; l[1] += 1
            self.out.append('\n' + ('- ' if l[0] == 'ul' else '%d. ' % l[1]))
        elif t == 'p': self.out.append('\n\n')
        elif t == 'br': (self.cell.append(' ') if self.cell is not None else self.out.append('\n'))
        elif t == 'tr': self.row = []
        elif t in ('td', 'th'): self.cell = []
    def handle_endtag(self, t):
        if t in ('strong', 'b'): self.out.append('**')
        elif t == 'em': self.out.append('*')
        elif t == 'code': self.out.append('`')
        elif t == 'a':
            h = self.href or ''
            if h.startswith('../') or h.startswith('#'): h = absurl(h)
            self.out.append('](%s)' % h)
        elif t in ('ul', 'ol'): self.lists.pop(); self.out.append('\n')
        elif t in ('td', 'th'): self.row.append(re.sub(r'\s+', ' ', ''.join(self.cell)).strip()); self.cell = None
        elif t == 'tr': self.rows.append(self.row); self.row = None
        elif t == 'table':
            r = self.rows; self.rows = []
            if r:
                self.out.append('\n\n| ' + ' | '.join(r[0]) + ' |\n|' + '---|' * len(r[0]) + '\n')
                for x in r[1:]: self.out.append('| ' + ' | '.join(x) + ' |\n')
    def handle_data(self, d):
        d = re.sub(r'\s+', ' ', d)
        if self.cell is not None: self.cell.append(d)
        else: self.out.append(d)

_cur_slug = ['']
def absurl(h):
    if h.startswith('#'): return SITE + 'support/%s/%s' % (_cur_slug[0], h)
    return SITE + 'support/' + h.replace('../', '', 1)

def to_md(h):
    m = MD(); m.feed(h)
    t = ''.join(m.out)
    t = re.sub(r'\n{3,}', '\n\n', t).strip()
    return re.sub(r' +\n', '\n', t)

def page_md(page):
    _cur_slug[0] = page['slug']
    lines = ['# %s' % (page['title'] if page['slug'] != 'get-started' else 'Get started with Cruxy'), '',
             '> %s' % page['intro'], '', 'Source: %ssupport/%s/ (updated %s)' % (SITE, page['slug'], MODIFIED), '']
    for sec in page['sections']:
        lines += ['## %s' % sec[1], '', to_md(sec[2]), '']
    lines += ['---', 'Still stuck? Email support@cruxy.io and you\'ll get a quick response from a real person.', '']
    return '\n'.join(lines)

def page_schema(page):
    url = SITE + 'support/%s/' % page['slug']
    pub = {'@type': 'Organization', 'name': 'Cruxy', 'url': SITE, 'logo': {'@type': 'ImageObject', 'url': SITE + 'images/cruxy-mark.svg'}}
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Cruxy', 'item': SITE},
        {'@type': 'ListItem', 'position': 2, 'name': 'Support', 'item': SITE + 'support/'},
        {'@type': 'ListItem', 'position': 3, 'name': page['title'], 'item': url}]}
    art = {'@type': 'TechArticle', 'headline': SEO_TITLES[page['slug']], 'description': page['desc'], 'url': url,
           'mainEntityOfPage': url, 'inLanguage': 'en', 'datePublished': PUBLISHED, 'dateModified': MODIFIED,
           'author': pub, 'publisher': pub, 'image': SOCIAL_IMG,
           'about': {'@type': 'SoftwareApplication', 'name': 'Cruxy', 'url': SITE, 'applicationCategory': 'BusinessApplication'},
           'isPartOf': {'@type': 'CollectionPage', 'name': 'Cruxy Help Center', 'url': SITE + 'support/'}}
    objs = [art, crumbs]
    secs = page['sections']
    if page['slug'] == 'get-started':
        objs.append({'@type': 'HowTo', 'name': 'Get started with Cruxy', 'description': page['intro'], 'totalTime': 'PT5M',
                     'tool': [{'@type': 'HowToTool', 'name': 'A phone or computer'}],
                     'step': [{'@type': 'HowToStep', 'position': i, 'name': sec[1], 'url': url + '#' + sec[0], 'text': strip_tags(sec[2])}
                              for i, sec in enumerate(secs, 1)]})
    if page['slug'] == 'troubleshooting':
        objs.append({'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': sec[1], 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(sec[2])}} for sec in secs]})
    if page['slug'] == 'contact':
        objs[0]['@type'] = 'ContactPage'
        objs.append({'@type': 'Organization', 'name': 'Cruxy', 'url': SITE, 'contactPoint': {'@type': 'ContactPoint', 'contactType': 'customer support', 'email': 'support@cruxy.io', 'availableLanguage': 'English'}})
    return jsonld(*objs)

def alt_md(slug):
    return '<link rel="alternate" type="text/markdown" href="%ssupport/%s/index.md" title="Markdown version">\n' % (SITE, slug)

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
    out = head('%s | Cruxy Help Center' % SEO_TITLES[page['slug']], page['desc'], 'support/%s/' % page['slug'], prefix, page_schema(page) + alt_md(page['slug']))
    out += '''<main><div class="support-shell">
<aside>%s</aside>
<article class="support-main">
<p class="crumbs"><a href="%sindex.html">Cruxy</a> / <a href="../">Support</a> / %s</p>
%s
<h1>%s</h1>
<p class="support-lead">%s</p>
<p class="updated">Updated <time datetime="%s">October 14, 2026</time></p>
<nav class="toc" aria-label="On this page"><div class="toc-title">On this page</div><ol>%s</ol></nav>
%s
<div class="still-stuck">Still stuck? Email us at <a href="mailto:support@cruxy.io">support@cruxy.io</a>.</div>
</article></div></main>
''' % (nav_html(page['slug'], prefix), prefix, esc(page['title']), searchbox(prefix), esc(page['title'] if page['slug'] != 'get-started' else 'Get started with Cruxy'),
       esc(page['intro']), MODIFIED, toc, '\n'.join(body))
    out += foot(prefix)
    d = os.path.join(ROOT, 'support', page['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(out)
    open(os.path.join(d, 'index.md'), 'w').write(page_md(page))

def build_home():
    prefix = '../'
    cards = ''.join('<a class="topic" href="%s/"><strong>%s</strong><span>%s</span></a>' % (p['slug'], esc(p['title']), esc(p['intro'])) for p in PAGES if p['slug'] not in ('get-started', 'contact'))
    popular = [('get-started', 'first-invoice', 'Send your first invoice'), ('time', 'timer', 'Use the timer'),
               ('alerts', 'client-reminders', 'Automatic reminders to your clients'), ('billing', 'cancel', 'Cancel Pro'),
               ('troubleshooting', 'email-missing', "An invoice email didn't arrive"), ('free-vs-pro', 'compare', 'What Free and Pro include')]
    pop = ''.join('<li><a href="%s/#%s">%s</a></li>' % (a, b, esc(c)) for a, b, c in popular)
    hdesc = 'Help for Cruxy, the free time tracking and invoicing app for freelancers: getting started, logging time, invoices, alerts, plans and billing.'
    hurl = SITE + 'support/'
    pub = {'@type': 'Organization', 'name': 'Cruxy', 'url': SITE}
    hs = jsonld({'@type': 'CollectionPage', 'name': 'Cruxy Help Center', 'url': hurl, 'description': hdesc, 'inLanguage': 'en', 'dateModified': MODIFIED, 'publisher': pub,
                 'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i, 'name': p['title'], 'url': hurl + p['slug'] + '/'} for i, p in enumerate(PAGES, 1)]}},
                {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Cruxy', 'item': SITE}, {'@type': 'ListItem', 'position': 2, 'name': 'Support', 'item': hurl}]})
    out = head('Cruxy Help Center: guides, billing and troubleshooting', hdesc, 'support/', prefix, hs)
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


def update_between(path, start, end, block, fallback_anchor, before=True):
    t = open(path).read()
    t = re.sub(re.escape(start) + r'.*?' + re.escape(end) + r'\n?', '', t, flags=re.S)
    if block:
        i = t.index(fallback_anchor)
        t = t[:i] + start + '\n' + block + end + '\n' + t[i:] if before else t[:i + len(fallback_anchor)] + start + '\n' + block + end + '\n' + t[i + len(fallback_anchor):]
    open(path, 'w').write(t)

def write_discovery():
    pages = [('support/', 'Help Center')] + [('support/%s/' % p['slug'], p['title']) for p in PAGES]
    sm = ''.join('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n' % (SITE, u, MODIFIED) for u, _ in pages) if not NOINDEX else ''
    update_between(os.path.join(ROOT, 'sitemap.xml'), '  <!-- support:start -->', '  <!-- support:end -->', sm, '</urlset>')
    llms = ''
    if not NOINDEX:
        llms = '\n## Help Center (step-by-step guides)\n' + '\n'.join(
            '- [%s](%s%s): %s' % (p['title'], SITE, 'support/%s/' % p['slug'], p['intro']) for p in PAGES) + \
            '\n- [Help Center home](%ssupport/): search and browse every topic\n- [All support articles as one text file](%sllms-full.txt)\n- Support email: support@cruxy.io (a real person replies quickly)\n' % (SITE, SITE)
    update_between(os.path.join(ROOT, 'llms.txt'), '<!-- support:start -->', '<!-- support:end -->', llms, '## Links\n', before=True)
    if NOINDEX:
        full = ''
    else:
        full = '# Cruxy Help Center (full text)\n\n> Step-by-step help for Cruxy, the free time tracking and invoicing app for freelancers. Each article also has its own page at %ssupport/.\n\n' % SITE
        for p in PAGES:
            full += page_md(p).replace('\n# ', '\n# ', 1) + '\n\n'
    path = os.path.join(ROOT, 'llms-full.txt')
    if full: open(path, 'w').write(full)
    elif os.path.exists(path): os.remove(path)

def main():
    index = []
    for p in PAGES:
        build_page(p, index)
    build_home()
    write_discovery()
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
              '- [ ] app/import-pick.jpg, app/import-review.jpg, app/invoices-list.jpg, app/retainers-progress.jpg: older shots, check they match the current app',
              '- [ ] Retake all with one consistent demo workspace and device frame once the client-reminders work is merged']
    open(os.path.join(ROOT, 'scripts', 'SCREENSHOTS.md'), 'w').write('\n'.join(lines) + '\n')
    print('pages: %d + home, sections: %d, missing screenshots: %d' % (len(PAGES), len(index), len(missing)))

main()
