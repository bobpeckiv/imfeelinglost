/* I'm Feeling Lost: small, dependency-free helpers */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function store(k, v) {
    try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; }
  }
  function dayIndex() { var d = new Date(); return Math.floor((d - new Date(d.getFullYear(), 0, 0)) / 864e5) + d.getFullYear(); }
  function json(id) { var e = document.getElementById(id); try { return e ? JSON.parse(e.textContent) : null; } catch (x) { return null; } }

  /* theme */
  var tb = $('#theme');
  if (tb) tb.addEventListener('click', function () {
    var el = document.documentElement, cur = el.getAttribute('data-theme') ||
      (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    var next = cur === 'dark' ? 'light' : 'dark';
    el.setAttribute('data-theme', next); store('ifl-theme', next);
  });

  /* random idea */
  var ri = $('#random-idea');
  if (ri) ri.addEventListener('click', function () {
    var u = (ri.getAttribute('data-urls') || '').split(',').filter(Boolean);
    if (u.length) location.href = u[Math.floor(Math.random() * u.length)];
  });

  /* chips filter */
  $$('.chips[data-target]').forEach(function (box) {
    var grid = $(box.getAttribute('data-target'));
    if (!grid) return;
    function apply(v) {
      $$('.chip', box).forEach(function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-v') === v)); });
      $$('.card', grid).forEach(function (card) {
        var f = (card.getAttribute('data-f') || '').split(' ');
        card.hidden = !(v === 'all' || f.indexOf(v) > -1);
      });
    }
    box.addEventListener('click', function (e) {
      var b = e.target.closest('.chip'); if (b) apply(b.getAttribute('data-v'));
    });
    var h = location.hash.slice(1);
    if (h && $('.chip[data-v="' + h + '"]', box)) apply(h);
  });

  /* quote of the day */
  var qs = json('quotes-data'), qb = $('#qtext');
  if (qs && qb) {
    var qi = dayIndex() % qs.length;
    var showQ = function () {
      var q = qs[qi];
      qb.textContent = q[0]; $('#qwho').textContent = q[1]; $('#qsrc').textContent = q[2];
    };
    showQ();
    var qn = $('#qnext');
    if (qn) qn.addEventListener('click', function () { qi = (qi + 1) % qs.length; showQ(); });
  }

  /* one small thing */
  var sm = json('small-data');
  if (sm && $('#small-title')) {
    var s = sm[dayIndex() % sm.length];
    $('#small-title').textContent = s.t; $('#small-sum').textContent = s.s;
    $('#small-link').setAttribute('href', s.u);
  }

  /* hero particle field */
  var cv = $('#hero-field');
  if (cv && cv.getContext) {
    var cx = cv.getContext('2d'), W, H, P = [], col = '196,161,85', run = true, raf;
    var size = function () {
      var dpr = Math.min(window.devicePixelRatio || 1, 2), r = cv.getBoundingClientRect();
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; cx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var a = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim();
      var m = /^#([0-9a-f]{6})$/i.exec(a);
      if (m) col = [parseInt(m[1].substr(0, 2), 16), parseInt(m[1].substr(2, 2), 16), parseInt(m[1].substr(4, 2), 16)].join(',');
      var n = Math.round(Math.min(110, W * H / 9000)); P = [];
      for (var i = 0; i < n; i++) P.push({ x: Math.random() * W, y: Math.random() * H, r: Math.random() * 1.6 + .4,
        vx: (Math.random() - .5) * .15, vy: -(Math.random() * .25 + .05), a: Math.random() * .5 + .15, p: Math.random() * 6 });
    };
    var draw = function (t) {
      cx.clearRect(0, 0, W, H);
      for (var i = 0; i < P.length; i++) {
        var p = P[i];
        if (!reduce) { p.x += p.vx; p.y += p.vy; if (p.y < -4) { p.y = H + 4; p.x = Math.random() * W; } if (p.x < -4) p.x = W + 4; if (p.x > W + 4) p.x = -4; }
        var al = p.a * (0.6 + 0.4 * Math.sin(t / 1400 + p.p));
        cx.beginPath(); cx.arc(p.x, p.y, p.r, 0, 6.2832);
        cx.fillStyle = 'rgba(' + col + ',' + al.toFixed(3) + ')'; cx.fill();
      }
      if (!reduce && run) raf = requestAnimationFrame(draw);
    };
    size(); draw(0);
    window.addEventListener('resize', function () { size(); if (reduce) draw(0); });
    document.addEventListener('visibilitychange', function () {
      run = !document.hidden; if (run && !reduce) { cancelAnimationFrame(raf); raf = requestAnimationFrame(draw); }
    });
  }

  /* video: load on click, privacy-enhanced */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.vplay'); if (!b) return;
    var f = b.parentNode, id = f.getAttribute('data-id');
    var ifr = document.createElement('iframe');
    ifr.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
    ifr.title = f.getAttribute('data-title') || 'Video';
    ifr.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture; fullscreen';
    ifr.setAttribute('allowfullscreen', ''); ifr.referrerPolicy = 'strict-origin-when-cross-origin';
    f.replaceChild(ifr, b);
  });

  /* breathing pacer */
  var pc = $('#pacer');
  if (pc) {
    var PAT = {
      box:  { n: 'Box', note: 'Four counts in, hold, out, hold. Steady and focusing.', ph: [['Breathe in', 4, 1], ['Hold', 4, 1], ['Breathe out', 4, .6], ['Hold', 4, .6]] },
      sigh: { n: 'Cyclic sigh', note: 'Two quick breaths in through the nose, then a long slow breath out. Often used for fast calming.', ph: [['Breathe in', 2, .85], ['Sip in more', 1, 1], ['Long breath out', 6, .6]] },
      s478: { n: '4-7-8', note: 'In for four, hold for seven, out for eight. Skip the hold if it feels uncomfortable.', ph: [['Breathe in', 4, 1], ['Hold', 7, 1], ['Breathe out', 8, .6]] },
      long: { n: 'Longer exhale', note: 'In for four, out for six. A gentle everyday pace.', ph: [['Breathe in', 4, 1], ['Breathe out', 6, .6]] }
    };
    var cur = 'box', mins = 2, going = false, timer = null, tick = null, end = 0, idx = 0;
    var orb = $('#orb'), lab = $('#plabel'), cnt = $('#pcount'), btn = $('#pstart'), note = $('#pnote'), pats = $('#patterns');
    var qp = /[?&]p=(box|sigh|s478|long)/.exec(location.search); if (qp) cur = qp[1];
    Object.keys(PAT).forEach(function (k) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'chip'; b.textContent = PAT[k].n;
      b.setAttribute('data-k', k); b.setAttribute('aria-pressed', String(k === cur)); pats.appendChild(b);
    });
    var setNote = function () { note.textContent = PAT[cur].note; };
    setNote();
    pats.addEventListener('click', function (e) {
      var b = e.target.closest('.chip'); if (!b || going) return; cur = b.getAttribute('data-k');
      $$('.chip', pats).forEach(function (c) { c.setAttribute('aria-pressed', String(c === b)); }); setNote();
    });
    $('#lengths').addEventListener('click', function (e) {
      var b = e.target.closest('.chip'); if (!b || going) return; mins = +b.getAttribute('data-m');
      $$('#lengths .chip').forEach(function (c) { c.setAttribute('aria-pressed', String(c === b)); });
    });
    var stop = function (msg) {
      going = false; clearTimeout(timer); clearInterval(tick);
      btn.textContent = 'Start'; lab.textContent = msg || 'Ready'; cnt.textContent = '';
      orb.style.transition = 'transform 1.2s ease-in-out'; orb.style.transform = 'scale(.6)';
    };
    var phase = function () {
      if (!going) return;
      var p = PAT[cur].ph[idx];
      if (idx === 0 && Date.now() >= end) { stop('Well done'); return; }
      lab.textContent = p[0]; var left = p[1]; cnt.textContent = left;
      orb.style.transition = reduce ? 'none' : 'transform ' + p[1] + 's ease-in-out'; orb.style.transform = 'scale(' + p[2] + ')';
      clearInterval(tick);
      tick = setInterval(function () { left--; if (left > 0) cnt.textContent = left; }, 1000);
      timer = setTimeout(function () { idx = (idx + 1) % PAT[cur].ph.length; phase(); }, p[1] * 1000);
    };
    btn.addEventListener('click', function () {
      if (going) { stop('Stopped'); return; }
      going = true; idx = 0; end = Date.now() + mins * 60000; btn.textContent = 'Stop'; phase();
    });
  }

  /* meditation timer + guided readings */
  var tr = $('#timer');
  if (tr) {
    var TOT = 565.49, total = 600, remain = 600, tint = null, tend = 0, ac = null;
    var rd = $('#tread'), fg = $('#tfg'), ts = $('#tstart'), msg = $('#tmsg');
    var mm = /[?&]m=(\d+)/.exec(location.search);
    var fmt = function (s) { s = Math.max(0, Math.ceil(s)); return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); };
    var paint = function () { rd.textContent = fmt(remain); fg.style.strokeDashoffset = String(TOT * (1 - remain / total)); };
    var setLen = function (m) {
      total = remain = m * 60; paint();
      $$('#tlen .chip').forEach(function (c) { c.setAttribute('aria-pressed', String(+c.getAttribute('data-m') === m)); });
    };
    if (mm && $('#tlen .chip[data-m="' + mm[1] + '"]')) setLen(+mm[1]); else setLen(10);
    var bell = function () {
      try {
        ac = ac || new (window.AudioContext || window.webkitAudioContext)();
        [528, 1056].forEach(function (f, i) {
          var o = ac.createOscillator(), g = ac.createGain(), t = ac.currentTime;
          o.type = 'sine'; o.frequency.value = f; g.gain.setValueAtTime(0.0001, t);
          g.gain.exponentialRampToValueAtTime(i ? 0.06 : 0.3, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + 5);
          o.connect(g); g.connect(ac.destination); o.start(t); o.stop(t + 5.2);
        });
      } catch (e) {}
    };
    var tstop = function () { clearInterval(tint); tint = null; ts.textContent = 'Begin'; };
    $('#tlen').addEventListener('click', function (e) {
      var b = e.target.closest('.chip'); if (b && !tint) setLen(+b.getAttribute('data-m'));
    });
    ts.addEventListener('click', function () {
      if (tint) { tstop(); msg.textContent = 'Paused. Press Begin to continue.'; return; }
      if (remain <= 0) setLen(total / 60);
      bell(); tend = Date.now() + remain * 1000; ts.textContent = 'Pause'; msg.textContent = 'Sit comfortably. When the mind wanders, return to the breath.';
      tint = setInterval(function () {
        remain = (tend - Date.now()) / 1000; paint();
        if (remain <= 0) { remain = 0; paint(); tstop(); bell(); msg.textContent = 'Done. Take a breath before you move.'; }
      }, 250);
    });
    $('#treset').addEventListener('click', function () { tstop(); setLen(total / 60); msg.textContent = 'A soft bell sounds at the start and the end.'; });

    var sc = json('scripts-data') || [], g = $('#guide'), gl = $('#guide-line'), gp = $('#guide-prog'), gt = $('#guide-title');
    var gi = 0, gcur = null, gtm = null, gpause = false;
    var gstep = function () {
      if (gpause) return;
      if (gi >= gcur.lines.length) { gl.textContent = 'Take a breath. You can stop here.'; gp.style.width = '100%'; return; }
      var line = gcur.lines[gi];
      gl.style.opacity = 0;
      setTimeout(function () { gl.textContent = line; gl.style.opacity = 1; }, reduce ? 0 : 350);
      gp.style.width = ((gi + 1) / gcur.lines.length * 100) + '%';
      gi++; gtm = setTimeout(gstep, 3400 + line.length * 65);
    };
    document.addEventListener('click', function (e) {
      var b = e.target.closest('[data-guide]');
      if (b) {
        gcur = sc.filter(function (s) { return s.id === b.getAttribute('data-guide'); })[0]; if (!gcur) return;
        gi = 0; gpause = false; $('#guide-pause').textContent = 'Pause'; gt.textContent = gcur.title; g.hidden = false; gstep(); return;
      }
      if (e.target.closest('#guide-x')) { g.hidden = true; clearTimeout(gtm); }
      if (e.target.closest('#guide-pause')) {
        gpause = !gpause; $('#guide-pause').textContent = gpause ? 'Resume' : 'Pause';
        if (!gpause) gstep(); else clearTimeout(gtm);
      }
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !g.hidden) { g.hidden = true; clearTimeout(gtm); } });
    if (location.hash) { var d = document.getElementById(location.hash.slice(1)); if (d && d.tagName === 'DETAILS') d.open = true; }
  }

  /* journal: stays in this browser */
  var jt = $('#jtext');
  if (jt) {
    var prompts = json('prompts-data') || [], pi = dayIndex() % Math.max(prompts.length, 1), jl = $('#jlist');
    var load = function () { try { return JSON.parse(store('ifl-journal') || '[]'); } catch (e) { return []; } };
    var save = function (a) { store('ifl-journal', JSON.stringify(a)); };
    var showP = function () { $('#jprompt').textContent = prompts[pi] || 'Write whatever is on your mind.'; };
    var render = function () {
      var a = load(); jl.innerHTML = '';
      $('#jempty').hidden = a.length > 0;
      a.slice().reverse().forEach(function (en, ri) {
        var i = a.length - 1 - ri, d = document.createElement('div'); d.className = 'entry';
        var t = document.createElement('time'); t.textContent = new Date(en.t).toLocaleString([], { dateStyle: 'medium', timeStyle: 'short' });
        var q = document.createElement('div'); q.className = 'q'; q.textContent = en.q || '';
        var p = document.createElement('p'); p.textContent = en.x;
        var x = document.createElement('button'); x.type = 'button'; x.textContent = 'Delete';
        x.addEventListener('click', function () { var b = load(); b.splice(i, 1); save(b); render(); });
        d.appendChild(t); if (en.q) d.appendChild(q); d.appendChild(p); d.appendChild(x); jl.appendChild(d);
      });
    };
    showP(); render();
    $('#jnew').addEventListener('click', function () { pi = (pi + 1) % prompts.length; showP(); });
    $('#jsave').addEventListener('click', function () {
      var v = jt.value.trim(); if (!v) return;
      var a = load(); a.push({ t: new Date().toISOString(), q: $('#jprompt').textContent, x: v }); save(a); jt.value = ''; render();
    });
    $('#jexport').addEventListener('click', function () {
      var a = load(); if (!a.length) return;
      var txt = a.map(function (e) { return new Date(e.t).toLocaleString() + '\n' + (e.q ? e.q + '\n' : '') + e.x; }).join('\n\n---\n\n');
      var l = document.createElement('a'); l.href = URL.createObjectURL(new Blob([txt], { type: 'text/plain' }));
      l.download = 'my-journal.txt'; document.body.appendChild(l); l.click(); l.remove();
    });
    $('#jclear').addEventListener('click', function () {
      if (load().length && confirm('Delete every entry on this device? This cannot be undone.')) { save([]); render(); }
    });
  }

  /* search */
  var rs = $('#results');
  if (rs) {
    var inp = $('#sq'), st = $('#rstatus'), data = null;
    var go = function () {
      var q = inp.value.trim().toLowerCase(); rs.innerHTML = '';
      if (!q) { st.textContent = 'Type to search ideas, practices, talks, and readings.'; return; }
      if (!data) { st.textContent = 'Loading…'; return; }
      var terms = q.split(/\s+/).filter(Boolean);
      var out = data.map(function (d) {
        var s = 0, ti = d.t.toLowerCase(), tg = d.g.join(' ').toLowerCase(), su = d.s.toLowerCase(), tx = (d.x || '').toLowerCase();
        for (var i = 0; i < terms.length; i++) {
          var w = terms[i], hit = false;
          if (ti.indexOf(w) > -1) { s += 10; hit = true; }
          if (tg.indexOf(w) > -1) { s += 5; hit = true; }
          if (su.indexOf(w) > -1) { s += 3; hit = true; }
          if (tx.indexOf(w) > -1) { s += 1; hit = true; }
          if (!hit) return null;
        }
        return { d: d, s: s };
      }).filter(Boolean).sort(function (a, b) { return b.s - a.s; }).slice(0, 40);
      st.textContent = out.length ? out.length + ' result' + (out.length > 1 ? 's' : '') : 'Nothing found. Try a simpler word, like “habit” or “calm”.';
      out.forEach(function (r) {
        var li = document.createElement('li'), a = document.createElement('a'); a.href = r.d.u;
        var ty = document.createElement('span'); ty.className = 'ty'; ty.textContent = r.d.y;
        var b = document.createElement('b'); b.textContent = r.d.t;
        var s = document.createElement('span'); s.className = 's'; s.textContent = r.d.s;
        a.appendChild(ty); a.appendChild(b); a.appendChild(s); li.appendChild(a); rs.appendChild(li);
      });
    };
    var qm = /[?&]q=([^&]*)/.exec(location.search);
    if (qm) inp.value = decodeURIComponent(qm[1].replace(/\+/g, ' '));
    inp.addEventListener('input', function () {
      go(); if (history.replaceState) history.replaceState(null, '', '?q=' + encodeURIComponent(inp.value));
    });
    go();
    fetch('/search.json').then(function (r) { return r.json(); }).then(function (j) { data = j; go(); })
      .catch(function () { st.textContent = 'Search is unavailable right now.'; });
  }
})();
