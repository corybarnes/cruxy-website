// Client-side search for the Cruxy help center. Reads support/search-index.json (built by scripts/build_support.py).
(function () {
  var box = document.querySelector('.ssearch');
  if (!box) return;
  var input = box.querySelector('input'), out = box.querySelector('.sresults');
  var base = box.getAttribute('data-base') || '', docs = null, loading = null, active = -1;

  function norm(s) { return s.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim(); }
  function words(s) { return norm(s).split(' ').filter(Boolean); }
  function lev1(a, b) { // true when edit distance <= 1
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0, j = 0, edits = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++edits > 1) return false;
      if (a.length > b.length) i++; else if (a.length < b.length) j++; else { i++; j++; }
    }
    return edits + (a.length - i) + (b.length - j) <= 1;
  }
  function matches(q, w) { return w === q || (q.length >= 2 && w.indexOf(q) === 0) || (q.length >= 5 && lev1(q, w)); }
  function prep(d) { d._t = words(d.title); d._p = words(d.page); d._x = words(d.text); return d; }
  function score(d, qs) {
    var total = 0;
    for (var i = 0; i < qs.length; i++) {
      var q = qs[i], s = 0, k;
      for (k = 0; k < d._t.length; k++) if (matches(q, d._t[k])) { s += 6; break; }
      for (k = 0; k < d._p.length; k++) if (matches(q, d._p[k])) { s += 2; break; }
      var hits = 0; for (k = 0; k < d._x.length; k++) if (matches(q, d._x[k])) hits++;
      if (hits) s += 1 + Math.min(hits, 4) * 0.4;
      if (!s) return 0;
      total += s;
    }
    return total;
  }
  function snippet(d, qs) {
    var t = d.text, low = t.toLowerCase(), at = -1;
    for (var i = 0; i < qs.length && at < 0; i++) at = low.indexOf(qs[i]);
    var start = Math.max(0, (at < 0 ? 0 : at) - 40), s = t.substr(start, 150);
    if (start > 0) s = '…' + s; if (start + 150 < t.length) s += '…';
    return s;
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function mark(s, qs) {
    var h = esc(s);
    qs.forEach(function (q) { if (q.length > 1) h = h.replace(new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
    return h;
  }
  function load() {
    if (docs) return Promise.resolve();
    if (!loading) loading = fetch(box.getAttribute('data-index')).then(function (r) { return r.json(); }).then(function (j) { docs = j.map(prep); });
    return loading;
  }
  function render() {
    var qs = words(input.value); active = -1;
    if (!qs.length || !docs) { out.hidden = true; return; }
    var res = docs.map(function (d) { return { d: d, s: score(d, qs) }; }).filter(function (r) { return r.s > 0; })
      .sort(function (a, b) { return b.s - a.s; }).slice(0, 8);
    if (!res.length) out.innerHTML = '<div class="none">No results. Try different words, or email <a href="mailto:support@cruxy.io">support@cruxy.io</a>.</div>';
    else out.innerHTML = res.map(function (r) {
      return '<a href="' + base + r.d.url + '"><b>' + mark(r.d.title, qs) + '</b><small>' + esc(r.d.page) + '</small><p>' + mark(snippet(r.d, qs), qs) + '</p></a>';
    }).join('');
    out.hidden = false;
  }
  input.addEventListener('focus', load);
  input.addEventListener('input', function () { load().then(render); });
  input.addEventListener('keydown', function (e) {
    var items = out.querySelectorAll('a');
    if (e.key === 'Escape') { out.hidden = true; return; }
    if (!items.length || out.hidden) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); active = (active + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
      items.forEach(function (a, i) { a.classList.toggle('on', i === active); });
    } else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); items[active].click(); }
    else if (e.key === 'Enter' && items.length) { e.preventDefault(); items[0].click(); }
  });
  document.addEventListener('click', function (e) { if (!box.contains(e.target)) out.hidden = true; });
})();
