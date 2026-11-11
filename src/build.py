# -*- coding: utf-8 -*-
"""Static site generator for imfeelinglost.org
   Run:  python3 build.py   ->  writes ./site
"""
import os, re, json, html, shutil
from urllib.parse import quote_plus
from content import *
from content2 import *
from content3 import *
import art
IDEAS = IDEAS + NEW_IDEAS
PRACTICES = PRACTICES + NEW_PRACTICES
PRODUCTS = [(n, items + EXTRA_BOOKS) if n == "Books" else (n, items) for n, items in PRODUCTS]

BASE = "https://imfeelinglost.org"
BUILD = "2026-11-10"
REVIEWED = "November 2026"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "site")
V = "20261110"
BRAND = "I’m Feeling Lost"

IDX = {i["slug"]: i for i in IDEAS}
PRX = {p["slug"]: p for p in PRACTICES}

def esc(s): return html.escape(s, quote=True)
def strip_tags(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()

def resolve(text):
    def rep(m):
        kind, slug, label = m.group(1), m.group(2), m.group(3)
        if kind == "idea":
            t, u = IDX[slug]["title"], "/ideas/%s/" % slug
        else:
            t, u = PRX[slug]["title"], "/practice/%s/" % slug
        return '<a href="%s">%s</a>' % (u, esc(label or t))
    return re.sub(r"\{(idea|practice):([a-z0-9-]+)(?:\|([^}]+))?\}", rep, text)

def add_ids(body):
    toc = []
    def rep(m):
        t = strip_tags(m.group(1))
        sid = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
        toc.append((sid, t))
        return '<h2 id="%s">%s</h2>' % (sid, m.group(1))
    return re.sub(r"<h2>(.*?)</h2>", rep, body, flags=re.S), toc

def amazon(q):
    return "https://www.amazon.com/s?k=%s&tag=%s" % (quote_plus(q), AMZ_TAG)

SEARCH = []   # search index
URLS = []     # sitemap

def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        full = os.path.join(full, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

NAV = [("Why", "/why/"), ("Practice", "/practice/"), ("Library", "/library/"), ("Mystics", "/mystics/"),
       ("Community", "/community/"), ("Journal", "/journal/"), ("Shop", "/shop/")]

MARK = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" '
        'stroke="currentColor" stroke-width="1.4" stroke-dasharray="40 16" stroke-linecap="round"/>'
        '<circle cx="12" cy="12" r="2.2" fill="currentColor"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E"
           "%3Crect width='24' height='24' rx='6' fill='%230E0D0C'/%3E"
           "%3Ccircle cx='12' cy='12' r='7' fill='none' stroke='%23C4A155' stroke-width='1.5' stroke-dasharray='32 12' stroke-linecap='round'/%3E"
           "%3Ccircle cx='12' cy='12' r='2' fill='%23C4A155'/%3E%3C/svg%3E")

def page(path, title, desc, body, section="", jsonld=None, og_type="website",
         search=None, noindex=False):
    url = BASE + path
    full_title = title if title.startswith(BRAND) else "%s · %s" % (title, BRAND)
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if n == section else "", n)
        for n, u in NAV)
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/")
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    if not noindex:
        URLS.append(path)
    if search:
        SEARCH.append(dict(search, url=path))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
{robots}
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0E0D0C" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#F6F1E7" media="(prefers-color-scheme: light)">
<link rel="icon" href="{FAVICON}">
<script>try{{var t=localStorage.getItem('ifl-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,200;0,300;0,400;0,500;0,600;1,300&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v={V}">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="/">{MARK}<span>{BRAND}</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="tools">
      <a class="icon-btn" href="/search/" aria-label="Search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg></a>
      <button class="icon-btn" id="theme" type="button" aria-label="Switch light or dark theme"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 019.5 4a8.5 8.5 0 1010.5 10.5z"/></svg></button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <p class="foot-brand">{MARK}<span>{BRAND}</span></p>
        <p class="muted">A free library for people who are low, scrolling too much, and stuck in habits they want out of.</p>
      </div>
      <div>
        <p class="foot-h">Explore</p>
        <ul><li><a href="/">Today</a></li><li><a href="/why/">Why</a></li><li><a href="/library/">Library</a></li><li><a href="/mystics/">Mystics</a></li><li><a href="/community/">Community</a></li><li><a href="/search/">Search</a></li></ul>
      </div>
      <div>
        <p class="foot-h">About</p>
        <ul><li><a href="/about/">About this site</a></li><li><a href="/help/">Need help now?</a></li><li><a href="/shop/">Recommended products</a></li></ul>
      </div>
    </div>
    <p class="fine">General information only, not medical or mental health advice. If you are in crisis, see <a href="/help/">help now</a>. The Shop page contains affiliate links. As an Amazon Associate I earn from qualifying purchases.</p>
  </div>
</footer>
<script src="/assets/site.js?v={V}" defer></script>
</body>
</html>
'''

def art_url(key, seed=None, color=None, style=None, tags=None):
    path = os.path.join(OUT, "assets", "art", key + ".svg")
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(art.svg(seed or key, color or art.color_for(tags, seed or key), style))
    return "/assets/art/%s.svg?v=%s" % (key, V)

def art_img(key, cls="art", **kw):
    return '<img class="%s" src="%s" alt="" loading="lazy" width="480" height="270">' % (cls, art_url(key, **kw))

IDEA_STYLES = ["ridges", "waves", "ripples", "bloom"]

def idea_art(i, cls="art"):
    n = [x["slug"] for x in IDEAS].index(i["slug"])
    return art_img("idea-" + i["slug"], cls=cls, tags=i["tags"], style=IDEA_STYLES[n % 4])

def practice_art(p, cls="art"):
    style = "ripples" if p.get("pacer") else ("bloom" if p["minutes"] >= 5 else "waves")
    return art_img("practice-" + p["slug"], cls=cls, style=style, tags=["calm"] if p.get("pacer") else None)

def vid_card(t, tags=("talk", "video")):
    key = "v-" + (t.get("id") or t.get("list"))
    bg = art_url(key, style="waves", color=art.color_for(None, key))
    data = ('data-id="%s"' % t["id"]) if t.get("id") else ('data-list="%s"' % t["list"])
    yt = ("https://www.youtube.com/watch?v=%s" % t["id"]) if t.get("id") else ("https://www.youtube.com/playlist?list=%s" % t["list"])
    meta = esc(t["who"]) + (" \u00b7 %d min" % t["min"] if t.get("min") else "")
    safety = ('<p class="note small" style="margin:10px 0">%s</p>' % esc(WIM_HOF_SAFETY)) if t.get("safety") else ""
    label = "Play playlist" if t.get("list") else "Play here"
    SEARCH.append(dict(title=t["title"], type="Watch", summary=t["who"] + ". " + t["note"], tags=list(tags), text="", url="/watch/"))
    return f"""
<article class="vid">
  <div class="vframe" {data} data-title="{esc(t["title"])}">
    <button class="vplay" type="button" aria-label="Play {esc(t["title"])}" style="background-image:url('{bg}')">
      <svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="rgba(0,0,0,.35)" stroke="currentColor" stroke-width="2"/><path d="M26 20l20 12-20 12z" fill="currentColor"/></svg>
      <span>{label}</span>
    </button>
  </div>
  <div class="vbody">
    <h3>{esc(t["title"])}</h3>
    <p class="muted small">{meta}</p>
    <p>{esc(t["note"])}</p>{safety}
    <p class="small"><a href="{yt}" target="_blank" rel="noopener">Open on YouTube</a></p>
  </div>
</article>"""

def idea_card(i):
    return ('<a class="card" href="/ideas/%s/" data-f="%s">' + idea_art(i) + '<span class="kicker">%s</span><h3>%s</h3><p>%s</p>'
            '<span class="meta">%d min read</span></a>') % (
        i["slug"], " ".join(re.sub(r"[^a-z0-9]+", "-", t.lower()) for t in i["tags"]),
        esc(i["tags"][0]), esc(i["title"]), esc(i["summary"]), i["read"])

def practice_card(p):
    bucket = "short" if p["minutes"] < 5 else ("mid" if p["minutes"] <= 10 else "long")
    return ('<a class="card" href="/practice/%s/" data-f="%s">' + practice_art(p) + '<span class="kicker">%d min</span><h3>%s</h3><p>%s</p>'
            '<span class="meta">%s</span></a>') % (
        p["slug"], bucket, p["minutes"], esc(p["title"]), esc(p["summary"]), esc(p["when"]))

# ===================================================================== HOME
def build_home():
    doors = [
        ("I feel flat or low", "Momentum when motivation is gone", "/ideas/low-mood-momentum/"),
        ("I can’t stop scrolling", "Doomscrolling and how to loosen it", "/ideas/doomscrolling/"),
        ("I’m fighting a porn urge", "Without shame, with a plan", "/ideas/porn-and-compulsive-use/"),
        ("I need to calm down", "Two minutes of paced breathing", "/breathe/"),
    ]
    door_html = "".join('<li><a href="%s"><b>%s</b><span>%s</span></a></li>' % (u, esc(a), esc(b)) for a, b, u in doors)
    feat = ["low-mood-momentum", "doomscrolling", "porn-and-compulsive-use", "retention-and-discipline", "habits", "urges"]
    ideas = "".join(idea_card(IDX[s]) for s in feat)
    urls = ",".join("/ideas/%s/" % i["slug"] for i in IDEAS)
    q0 = QUOTES[0]
    qjson = json.dumps([list(q) for q in QUOTES], ensure_ascii=False).replace("</", "<\\/")
    smalls = [PRX[s] for s in ["one-small-thing", "change-the-scene", "cyclic-sigh", "phone-out-of-bedroom", "phone-free-walk", "two-minute-start", "values-check", "worry-sort", "grounding-54321"]]
    sjson = json.dumps([dict(t=p["title"], s=p["summary"], u="/practice/%s/" % p["slug"]) for p in smalls], ensure_ascii=False).replace("</", "<\\/")
    body = f"""
<section class="hero">
  <canvas id="hero-field" aria-hidden="true"></canvas>
  <div class="wrap hero-in">
    <p class="kicker">Today</p>
    <blockquote style="margin:0">
      <p class="qbig" id="qtext">{esc(q0[0])}</p>
      <p class="qwho" id="qwho">{esc(q0[1])}</p>
      <p class="qsrc" id="qsrc">{esc(q0[2])}</p>
    </blockquote>
    <div class="row"><button class="btn" id="qnext" type="button">Another quote</button> <a class="btn" href="/mystics/">More from the mystics</a></div>
    <div class="today-card">
      <div><p class="kicker">One small thing for today</p><b id="small-title">One small thing</b><span class="muted small" id="small-sum">Pick one tiny action tied to something you care about.</span></div>
      <a class="btn primary" id="small-link" href="/practice/one-small-thing/">Try it</a>
    </div>
    <ul class="doors">{door_html}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap two-up">
    <div class="panel has-art">
      {art_img("home-why", cls="panel-art", style="ridges", color="gold")}
      <p class="kicker">Why</p>
      <h2>Live on purpose</h2>
      <p class="muted">Feeds, habits, and moods choose most of our days. Intention is the quiet decision to take some of them back, starting very small.</p>
      <p><a class="btn primary" href="/why/">Read why</a></p>
    </div>
    <div class="panel has-art">
      {art_img("home-for", cls="panel-art", style="ripples", color="dusk")}
      <p class="kicker">For anyone who feels stuck</p>
      <h2>You are not broken</h2>
      <p class="muted">Low mood, endless scrolling, and habits you wish you did not have are common, and they are workable. This library is free, with no account and no ads.</p>
      <p><a class="btn" href="/start/">Start here</a> <a class="btn" href="/help/">Need someone now?</a></p>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head"><div><p class="kicker">Ideas</p><h2>What is going on, and what helps</h2></div>
      <a href="/ideas/">All ideas →</a></div>
    <div class="grid">{ideas}</div>
    <p class="center" style="margin-top:26px"><button class="btn" id="random-idea" type="button" data-urls="{urls}">Surprise me with an idea</button></p>
  </div>
</section>

<section class="section">
  <div class="wrap two-up">
    <div class="panel has-art">
      {art_img("home-mystics", cls="panel-art", style="orbit", color="violet")}
      <p class="kicker">Mystics</p>
      <h2>Words that have lasted</h2>
      <p class="muted">Short passages and free readings from the Buddha, Lao Tzu, the Stoics, and other contemplatives.</p>
      <p><a class="btn" href="/mystics/">Open the mystics page</a></p>
    </div>
    <div class="panel has-art">
      {art_img("home-community", cls="panel-art", style="bloom", color="sage")}
      <p class="kicker">Community</p>
      <h2>You are not the only one</h2>
      <p class="muted">Subreddits like r/getdisciplined and r/nosurf, and other places where people work on the same things.</p>
      <p><a class="btn" href="/community/">Find your people</a></p>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head"><div><p class="kicker">Read</p><h2>Writers worth following</h2></div>
      <a href="/read/#writers">All writers \u2192</a></div>
    <div class="grid">{"".join(writer_card(w) for w in WRITERS[:3])}</div>
  </div>
</section>
<script type="application/json" id="quotes-data">{qjson}</script>
<script type="application/json" id="small-data">{sjson}</script>
"""
    write("/", page("/", BRAND + " — a free library for steadying yourself",
        "A free library for people who are low, scrolling too much, or stuck in habits they want out of. Ideas, practices, talks, and readings. No account, no ads.",
        body, section="Today", search=dict(title="Today", type="Page", summary="A daily quote and one small thing to try.", tags=[], text="")))

# ===================================================================== START
def build_start():
    five = ["feeling-lost", "discipline", "habits", "urges", "values"]
    li = "".join('<li><a href="/ideas/%s/"><b>%s</b></a><span>%s</span></li>' % (
        s, esc(IDX[s]["title"]), esc(IDX[s]["summary"])) for s in five)
    body = f'''
<div class="wrap narrow page-head">
  <p class="kicker">Start here</p>
  <h1>You do not need a plan.</h1>
  <p class="lede">You need one small thing you can do in the next ten minutes. Here is a way to find it.</p>
</div>
<div class="wrap narrow prose" style="padding-bottom:64px">
  <ol class="steps">
    <li><b>Settle your body.</b> Two minutes of slow breathing takes the edge off almost anything. Your thinking gets better when your body is calmer.
      <p><a class="btn primary" href="/breathe/">Breathe for two minutes</a></p></li>
    <li><b>Pick one small thing.</b> If you know what you are avoiding, shrink the first step with <a href="/practice/two-minute-start/">the two-minute start</a>. If you do not know what you want, try <a href="/practice/values-check/">a five-minute values check</a>.</li>
    <li><b>Read one idea.</b> Not all of them. Just the one that sounds closest to where you are today.</li>
  </ol>
  <h2>If you only read five things</h2>
  <ul class="reslist">{li}</ul>
  <p class="note">If this feels bigger than lost, if you are hopeless, or if you are thinking about hurting yourself, please reach out to a person today. The <a href="/help/">help page</a> lists free, confidential lines.</p>
</div>
'''
    write("/start/", page("/start/", "Start here", "A gentle ten-minute path for anyone who feels lost: settle your body, pick one small thing, read one idea.",
        body, search=dict(title="Start here", type="Page", summary="A gentle ten-minute path for when you feel lost.", tags=["start"], text="")))

# ===================================================================== IDEAS
def build_ideas():
    tagcount = {}
    for i in IDEAS:
        for t in i["tags"]:
            tagcount[t] = tagcount.get(t, 0) + 1
    tags = sorted(tagcount, key=lambda t: (-tagcount[t], t))
    chips = '<button class="chip" type="button" data-v="all" aria-pressed="true">All</button>' + "".join(
        '<button class="chip" type="button" data-v="%s" aria-pressed="false">%s</button>' % (
            re.sub(r"[^a-z0-9]+", "-", t.lower()), esc(t)) for t in tags)
    cards = "".join(idea_card(i) for i in sorted(IDEAS, key=lambda x: x["title"].lower()))
    urls = ",".join("/ideas/%s/" % i["slug"] for i in IDEAS)
    body = f'''
<div class="wrap page-head">
  <p class="kicker">Ideas</p>
  <h1>How change actually works</h1>
  <p class="lede">Plain-language explanations of the research and the old wisdom behind discipline, habits, motivation, and meaning. Every page cites its sources and says where the evidence is mixed.</p>
</div>
<div class="wrap" style="padding-bottom:64px">
  <div class="chips" data-target="#grid" role="group" aria-label="Filter by topic">{chips}</div>
  <div class="grid" id="grid">{cards}</div>
  <p class="center"><button class="btn" id="random-idea" type="button" data-urls="{urls}">Surprise me</button></p>
</div>
'''
    write("/ideas/", page("/ideas/", "Ideas", "Plain-language articles on discipline, habits, urges, values, procrastination, and self-compassion, with sources.",
        body, section="Library", search=dict(title="Ideas", type="Page", summary="All articles.", tags=[], text="")))

    for i in IDEAS:
        main, toc = add_ids(resolve(i["body"]))
        glance = "".join("<li>%s</li>" % esc(x) for x in i["short"])
        tocli = "".join('<li><a href="#%s">%s</a></li>' % (a, esc(b)) for a, b in toc)
        tagl = "".join('<a class="tag" href="/ideas/#%s">%s</a>' % (re.sub(r"[^a-z0-9]+", "-", t.lower()), esc(t)) for t in i["tags"])
        tr = PRX[i["try"]]
        rel_i = "".join('<li><a href="/ideas/%s/">%s</a></li>' % (s, esc(IDX[s]["title"])) for s in i["related"] if s != i["slug"])
        rel_p = "".join('<li><a href="/practice/%s/">%s</a> <span class="muted">(%d min)</span></li>' % (s, esc(PRX[s]["title"]), PRX[s]["minutes"]) for s in i["practices"])
        srcs = "".join("<li>%s</li>" % esc(s) for s in i["sources"])
        body = f'''
<article>
<div class="wrap page-head">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/ideas/">Ideas</a> / {esc(i["title"])}</nav>
  <p class="kicker">Idea</p>
  <h1>{esc(i["title"])}</h1>
  <p class="lede">{esc(i["summary"])}</p>
  <p class="byline">{i["read"]} min read · Reviewed {REVIEWED}</p>
  {idea_art(i, "banner")}
</div>
<div class="wrap layout">
  <aside class="infobox" aria-label="At a glance">
    <h2>At a glance</h2>
    <ul>{glance}</ul>
    <h2>Try this</h2>
    <p><a class="btn primary" href="/practice/{tr["slug"]}/">{esc(tr["title"])}</a></p>
    <h2>On this page</h2>
    <ul class="toc">{tocli}<li><a href="#sources">Sources</a></li></ul>
    <div class="tags">{tagl}</div>
  </aside>
  <div class="prose">
    {main}
    <h2 id="see-also">See also</h2>
    <ul>{rel_i}{rel_p}</ul>
    <h2 id="sources">Sources</h2>
    <ul class="sources">{srcs}</ul>
    <p class="note">General information, not medical or mental health advice. If you are struggling, you do not have to figure it out alone. See <a href="/help/">help now</a>.</p>
  </div>
</div>
</article>
'''
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": i["title"], "description": i["summary"],
              "dateModified": BUILD, "datePublished": BUILD, "inLanguage": "en",
              "author": {"@type": "Organization", "name": "I’m Feeling Lost"},
              "publisher": {"@type": "Organization", "name": "I’m Feeling Lost"},
              "mainEntityOfPage": "%s/ideas/%s/" % (BASE, i["slug"])}
        write("/ideas/%s/" % i["slug"], page("/ideas/%s/" % i["slug"], i["title"], i["summary"], body, section="Library",
              jsonld=ld, og_type="article",
              search=dict(title=i["title"], type="Idea", summary=i["summary"], tags=i["tags"], text=strip_tags(main)[:1800])))

# ===================================================================== PRACTICE
def build_practice():
    chips = ('<button class="chip" type="button" data-v="all" aria-pressed="true">All</button>'
             '<button class="chip" type="button" data-v="short" aria-pressed="false">Under 5 minutes</button>'
             '<button class="chip" type="button" data-v="mid" aria-pressed="false">5 to 10 minutes</button>'
             '<button class="chip" type="button" data-v="long" aria-pressed="false">Longer</button>')
    cards = "".join(practice_card(p) for p in sorted(PRACTICES, key=lambda x: (x["minutes"], x["title"])))
    body = f'''
<div class="wrap page-head">
  <p class="kicker">Practice</p>
  <h1>Small things you can do right now</h1>
  <p class="lede">Exercises you can try in a few minutes: breathing, grounding, planning, reflection. Each one says when to use it and why it works.</p>
</div>
<div class="wrap" style="padding-bottom:64px">
  <div class="chips" data-target="#grid" role="group" aria-label="Filter by length">{chips}</div>
  <div class="grid" id="grid">{cards}</div>
  <div class="panel" style="margin-top:34px">
    <h2 style="margin-top:0">Want a guide?</h2>
    <p class="muted">The <a href="/breathe/">breathing pacer</a> and the <a href="/meditate/">meditation timer and guided readings</a> do the timing for you.</p>
  </div>
</div>
'''
    write("/practice/", page("/practice/", "Practice", "Short, evidence-informed exercises for calming down, getting started, and finding direction.",
        body, section="Practice", search=dict(title="Practice", type="Page", summary="All practices.", tags=[], text="")))

    for p in PRACTICES:
        steps = "".join("<li>%s</li>" % esc(s) for s in p["steps"])
        extras = ""
        if p.get("pacer"):
            extras += '<a class="btn primary" href="/breathe/?p=%s">Open the breathing pacer</a> ' % p["pacer"]
        if p.get("guided"):
            extras += '<a class="btn primary" href="/meditate/#%s">Open the guided reading</a> ' % p["guided"]
        if p["minutes"] >= 5 and not p.get("pacer"):
            extras += '<a class="btn" href="/meditate/?m=%d">Start a %d-minute timer</a>' % (p["minutes"], p["minutes"])
        rel = "".join('<li><a href="/ideas/%s/">%s</a></li>' % (s, esc(IDX[s]["title"])) for s in p["ideas"])
        src = '<p class="small muted">Source: %s</p>' % esc(p["source"]) if p.get("source") else ""
        body = f'''
<article>
<div class="wrap narrow page-head">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/practice/">Practice</a> / {esc(p["title"])}</nav>
  <p class="kicker">Practice · {p["minutes"]} min</p>
  <h1>{esc(p["title"])}</h1>
  <p class="lede">{esc(p["summary"])}</p>
  {practice_art(p, "banner")}
</div>
<div class="wrap narrow prose" style="padding-bottom:64px">
  <p class="note"><b>When to use it.</b> {esc(p["when"])}</p>
  <h2>Steps</h2>
  <ol class="steps">{steps}</ol>
  <div class="btn-row">{extras}</div>
  <h2>Why it works</h2>
  <p>{esc(p["why"])}</p>
  {src}
  <h2>Read more</h2>
  <ul>{rel}</ul>
  <p class="note small">General information, not medical or mental health advice. Stop any breathing exercise if you feel dizzy. If you are struggling, see <a href="/help/">help now</a>.</p>
</div>
</article>
'''
        ld = {"@context": "https://schema.org", "@type": "HowTo", "name": p["title"], "description": p["summary"],
              "totalTime": "PT%dM" % p["minutes"],
              "step": [{"@type": "HowToStep", "position": n + 1, "text": s} for n, s in enumerate(p["steps"])]}
        write("/practice/%s/" % p["slug"], page("/practice/%s/" % p["slug"], p["title"], p["summary"], body, section="Practice",
              jsonld=ld, search=dict(title=p["title"], type="Practice", summary=p["summary"], tags=[], text=" ".join(p["steps"])[:1200])))

# ===================================================================== BREATHE
def build_breathe():
    body = f'''
<div class="wrap narrow page-head center">
  <p class="kicker">Breathe</p>
  <h1>Follow the circle.</h1>
  <p class="lede" style="margin-inline:auto">Slow breathing with a long exhale tends to settle the body. Pick a pattern, press start, and let the circle set the pace.</p>
</div>
<div class="wrap narrow pacer" id="pacer" style="padding-bottom:64px">
  <div class="stage" id="stage">
    <div class="orb" id="orb"></div>
    <div class="txt" aria-live="polite"><b id="plabel">Ready</b><span id="pcount"></span></div>
  </div>
  <div class="chips center" id="patterns" role="group" aria-label="Breathing pattern"></div>
  <p class="muted center" id="pnote"></p>
  <div class="chips center" id="lengths" role="group" aria-label="Session length">
    <button class="chip" type="button" data-m="1" aria-pressed="false">1 min</button>
    <button class="chip" type="button" data-m="2" aria-pressed="true">2 min</button>
    <button class="chip" type="button" data-m="3" aria-pressed="false">3 min</button>
    <button class="chip" type="button" data-m="5" aria-pressed="false">5 min</button>
  </div>
  <p class="center"><button class="btn primary big" id="pstart" type="button">Start</button></p>
  <hr class="sep">
  <h2>Breathe along with a guide</h2>
  <p class="muted">A stronger, energizing practice. Read the safety note before you start.</p>
  <div class="vgrid one">{vid_card(BREATH_VIDEOS[0], ('breathing',))}</div>
  <p class="note small">If you feel dizzy, tingly, or uncomfortable, stop and breathe normally. If holding your breath feels bad, skip the holds. This is general wellness information, not medical advice, and may not suit everyone, especially people with breathing, heart, or anxiety conditions. Ask a clinician if unsure.</p>
</div>
'''
    write("/breathe/", page("/breathe/", "Breathing pacer", "A simple visual breathing pacer with box breathing, cyclic sighing, and longer-exhale patterns.",
        body, section="Library", search=dict(title="Breathing pacer", type="Tool", summary="Paced breathing: box, cyclic sigh, 4-7-8, even breathing.", tags=["calm", "breathing"], text="calm down anxiety breathing exercise stress"),
        ))

# ===================================================================== MEDITATE
def build_meditate():
    scripts_json = json.dumps(SCRIPTS, ensure_ascii=False).replace("</", "<\\/")
    sc = ""
    for s in SCRIPTS:
        paras = "".join("<p>%s</p>" % esc(l) for l in s["lines"])
        sc += f'''
<details class="script" id="{s["id"]}">
  <summary><span><b>{esc(s["title"])}</b><small>{esc(s["minutes"])}</small></span></summary>
  <div class="script-body">
    <p><button class="btn primary" type="button" data-guide="{s["id"]}">Guide me, one line at a time</button></p>
    {paras}
  </div>
</details>'''
    links = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s</span></li>' % (
        m["url"], esc(m["title"]), esc(m["note"])) for m in MEDITATE_LINKS)
    body = f'''
<div class="wrap narrow page-head center">
  <p class="kicker">Meditate</p>
  <h1>Sit for a few minutes.</h1>
  <p class="lede" style="margin-inline:auto">A quiet timer with a soft bell, guided readings you can follow line by line, and links to free guided audio.</p>
</div>
<div class="wrap narrow" style="padding-bottom:64px">
  <section aria-labelledby="t-h">
    <h2 id="t-h" class="center">Silent timer</h2>
    <div class="timer" id="timer">
      <svg viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="90"/><circle class="fg" id="tfg" cx="100" cy="100" r="90" stroke-dasharray="565.49" stroke-dashoffset="0"/></svg>
      <div class="read" id="tread" role="timer" aria-live="off">10:00</div>
    </div>
    <div class="chips center" id="tlen" role="group" aria-label="Timer length">
      <button class="chip" type="button" data-m="3" aria-pressed="false">3</button>
      <button class="chip" type="button" data-m="5" aria-pressed="false">5</button>
      <button class="chip" type="button" data-m="10" aria-pressed="true">10</button>
      <button class="chip" type="button" data-m="15" aria-pressed="false">15</button>
      <button class="chip" type="button" data-m="20" aria-pressed="false">20</button>
    </div>
    <p class="center"><button class="btn primary big" id="tstart" type="button">Begin</button> <button class="btn" id="treset" type="button">Reset</button></p>
    <p class="muted center small" id="tmsg">A soft bell sounds at the start and the end. Sit however is comfortable. When the mind wanders, and it will, return to the breath.</p>
  </section>

  <hr class="sep">

  <section aria-labelledby="g-h">
    <h2 id="g-h">Guided readings</h2>
    <p class="muted">Read them yourself, or press the guide button and each line appears at a slow pace.</p>
    {sc}
  </section>

  <hr class="sep">

  <section aria-labelledby="l-h">
    <h2 id="l-h">Listen to a guide</h2>
    <p class="muted">Free recordings from trusted sources.</p>
    <div class="vgrid one" style="margin-bottom:16px">{"".join(vid_card(v, ("meditation",)) for v in MEDITATION_VIDEOS)}</div>
    <ul class="reslist">{links}</ul>
  </section>
</div>

<div class="guide" id="guide" hidden role="dialog" aria-modal="true" aria-label="Guided reading">
  <div class="guide-top"><span id="guide-title"></span><button class="btn" type="button" id="guide-x">Close</button></div>
  <div class="guide-body"><p id="guide-line" aria-live="polite"></p></div>
  <div class="guide-bar"><div id="guide-prog"></div></div>
  <div class="guide-ctl"><button class="btn" type="button" id="guide-pause">Pause</button></div>
</div>
<script type="application/json" id="scripts-data">{scripts_json}</script>
'''
    write("/meditate/", page("/meditate/", "Meditate", "A silent meditation timer, guided readings you can follow line by line, and links to free guided audio.",
        body, section="Library", search=dict(title="Meditate", type="Tool", summary="Silent timer, guided body scan, loving-kindness, and noting practices.", tags=["meditation", "mindfulness"], text="meditation timer body scan loving kindness noting mindfulness")))

# ===================================================================== WATCH
def build_watch():
    vids = "".join(vid_card(t) for t in TALKS)
    breath = "".join(vid_card(t, ("breathing", "meditation")) for t in BREATH_VIDEOS + MEDITATION_VIDEOS)
    teach = "".join(vid_card(t, ("teacher", "mystic")) for t in TEACHER_VIDEOS)
    longl = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s%s</span></li>' % (
        t["url"], esc(t["title"]), esc(t["who"]) + (" · %d min. " % t["min"] if t["min"] else ". "), esc(t["note"])) for t in LONG_TALKS)
    chans = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s</span></li>' % (
        c["url"], esc(c["title"]), esc(c["note"])) for c in CHANNELS)
    body = f'''
<div class="wrap page-head">
  <p class="kicker">Watch</p>
  <h1>Talks worth your time</h1>
  <p class="lede">A short, curated shelf. Videos load from YouTube only when you press play, using YouTube’s privacy-enhanced mode.</p>
</div>
<div class="wrap" style="padding-bottom:64px">
  <h2>Talks to start with</h2>
  <div class="vgrid">{vids}</div>
  <h2 style="margin-top:46px">Breathe and meditate along</h2>
  <div class="vgrid">{breath}</div>
  <h2 style="margin-top:46px">Teachers</h2>
  <div class="vgrid">{teach}</div>
  <p class="note" style="margin-top:30px">Talks reflect their speakers’ views, and research keeps moving. Treat them as starting points, not final answers.</p>
  <h2 style="margin-top:46px">Longer listens</h2>
  <ul class="reslist">{longl}</ul>
  <h2 style="margin-top:36px">Channels worth following</h2>
  <ul class="reslist">{chans}</ul>
</div>
'''
    write("/watch/", page("/watch/", "Watch", "A short, curated shelf of talks on procrastination, stress, grit, vulnerability, mindfulness, and meaning.",
        body, section="Library", search=dict(title="Watch", type="Page", summary="Curated talks.", tags=[], text="")))

# ===================================================================== READ
def writer_card(w):
    name, who, url, what = w
    key = "w-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40]
    SEARCH.append(dict(title=name, type="Writer", summary=who + ". " + what, tags=["writer", "substack"], text="", url="/read/"))
    return ('<a class="card" href="%s" target="_blank" rel="noopener">%s<span class="kicker">%s</span><h3>%s</h3><p>%s</p>'
            '<span class="meta">Read on Substack \u2197</span></a>') % (url, art_img(key, style="orbit"), esc(who), esc(name), esc(what))

def build_read():
    books = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span class="by">%s</span><span>%s</span></li>' % (
        b["url"], esc(b["title"]), esc(b["who"]), esc(b["note"])) for b in FREE_BOOKS)
    for b in FREE_BOOKS:
        SEARCH.append(dict(title=b["title"], type="Read", summary=b["who"] + ". " + b["note"], tags=["book", "free"], text="", url="/read/"))
    enc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (e["url"], esc(e["title"])) for e in ENCYCLOPEDIA)
    writers = "".join(writer_card(w) for w in WRITERS)
    body = f'''
<div class="wrap page-head">
  <p class="kicker">Read</p>
  <h1>Writers and old books</h1>
  <p class="lede">Living writers worth following, and old books that still read like good advice. Read a page, not a chapter, and pick one line to try today.</p>
</div>
<div class="wrap" style="padding-bottom:64px">
  <h2 id="writers">Living writers</h2>
  <p class="muted">Independent newsletters on Substack about feelings, rest, meaning, and practice. Free to read, with optional paid tiers.</p>
  <div class="grid">{writers}</div>
  <h2 id="classics" style="margin-top:46px">Free classics</h2>
  <ul class="reslist big-list">{books}</ul>
  <h2 style="margin-top:46px">Background reading</h2>
  <p class="muted">Encyclopedia articles for going deeper on the ideas behind this library.</p>
  <ul class="plain">{enc}</ul>
  <p class="note" style="margin-top:30px">Looking for newer books? The <a href="/shop/">Shop page</a> lists a few favorites, and your public library probably has them for free.</p>
</div>
'''
    write("/read/", page("/read/", "Read", "Free classic texts on Stoicism, habit, and the power of thought, plus background reading on the ideas behind this library.",
        body, section="Library", search=dict(title="Read", type="Page", summary="Free classic texts.", tags=[], text="")))

# ===================================================================== SHOP
def build_shop():
    free = "".join("<li><b>%s</b><span>%s</span></li>" % (esc(f["title"]), esc(f["note"])) for f in FREE_FIRST)
    sections = ""
    for name, items in PRODUCTS:
        cards = ""
        for title, by, q, why in items:
            cards += (f'<div class="card pcard"><h3>{esc(title)}</h3><p class="muted small">{esc(by)}</p><p>{esc(why)}</p>'
                      f'<a class="btn" href="{amazon(q)}" target="_blank" rel="sponsored noopener">Find on Amazon</a></div>')
            SEARCH.append(dict(title=title, type="Shop", summary=by + ". " + why, tags=[name.lower()], text="", url="/shop/"))
        sections += f'<h2 style="margin-top:40px">{esc(name)}</h2><div class="grid">{cards}</div>'
    acc = "".join(('<div class="card pcard"><h3>%s</h3><p class="muted small">%s</p><p>%s</p>'
                    '<a class="btn" href="%s" target="_blank" rel="noopener">%s</a></div>') % (
        esc(a["title"]), esc(a["who"]), esc(a["why"]), a["url"], esc(a["btn"])) for a in ACCOUNTABILITY)
    sections += '<h2 style="margin-top:40px">Blocking and accountability</h2><div class="grid">%s</div>' % acc
    st = SOUNDS_TRUE
    sections += (f'<h2 style="margin-top:40px">Courses and audio</h2><div class="grid"><div class="card pcard"><h3>{esc(st["title"])}</h3>'
                 f'<p class="muted small">{esc(st["who"])}</p><p>{esc(st["why"])}</p>'
                 f'<a class="btn" href="{st["url"]}" target="_blank" rel="sponsored noopener">Visit Sounds True</a></div></div>')
    SEARCH.append(dict(title="Sounds True", type="Shop", summary=st["why"], tags=["courses"], text="", url="/shop/"))
    body = f'''
<div class="wrap page-head">
  <p class="kicker">Shop</p>
  <h1>Things we would buy</h1>
  <p class="lede">The only page on this site that earns anything. Nothing here is required, and none of it will fix you. These are books and simple tools that people in this field tend to recommend.</p>
</div>
<div class="wrap" style="padding-bottom:64px">
  <p class="note"><b>Disclosure.</b> Amazon and Sounds True links on this page are affiliate links. If you buy through them, this site may earn a small commission at no extra cost to you. As an Amazon Associate I earn from qualifying purchases. Amazon links go to a search for the item, so check the edition and price before you buy.</p>
  <h2 style="margin-top:36px">Free first</h2>
  <ul class="reslist">{free}</ul>
  {sections}
</div>
'''
    write("/shop/", page("/shop/", "Recommended products", "Books and simple tools recommended for discipline, focus, and steadiness. Affiliate links are disclosed.",
        body, section="Shop", search=dict(title="Recommended products", type="Page", summary="Books and tools. Affiliate links disclosed.", tags=[], text="")))

# ===================================================================== ABOUT / HELP
def build_about():
    body = '''
<div class="wrap narrow page-head">
  <p class="kicker">About</p>
  <h1>About this site</h1>
  <p class="lede">A free, independent library for people who feel low, scattered, or stuck, who scroll more than they want to, or who are trying to change habits like porn use, and want practical help that respects their intelligence.</p>
</div>
<div class="wrap narrow prose" style="padding-bottom:64px">
  <h2>What this is</h2>
  <p>Think of it as a small encyclopedia of self-help, motivation, and discipline. It collects ideas from psychology and from older traditions like Stoicism, explains them in plain language, and pairs them with short practices you can try today. It also curates talks and free readings worth your time.</p>
  <h2>How we write</h2>
  <ul>
    <li>Pages cite their sources, and we say when the evidence is mixed or the research has been criticized.</li>
    <li>We prefer small, doable steps over big promises.</li>
    <li>We do not shame. Slips are information, not verdicts.</li>
    <li>Free options come first. The Shop page is clearly separated and clearly labeled.</li>
  </ul>
  <h2>What this is not</h2>
  <p>This site is general information. It is not therapy, medical advice, or a substitute for a professional who knows you. If you are dealing with depression, anxiety, addiction, trauma, or thoughts of hurting yourself, please talk to a doctor, therapist, or support line. The <a href="/help/">help page</a> lists places to start.</p>
  <h2>How it pays for itself</h2>
  <p>The <a href="/shop/">Shop</a> page contains affiliate links. If you buy through them, the site may earn a small commission at no cost to you. There are no ads on the rest of the site, and nothing is sold on the pages that teach.</p>
  <h2>Privacy</h2>
  <p>There are no accounts, no ads, and no analytics scripts on this site. Your light or dark theme choice, and anything you write in the journal, is saved only in your own browser. Fonts load from Google Fonts. Embedded videos load from YouTube only when you press play, in privacy-enhanced mode, and outbound links go to other sites with their own policies.</p>
</div>
'''
    write("/about/", page("/about/", "About", "What this library is, how it is written, how it pays for itself, and what it is not.",
        body, search=dict(title="About this site", type="Page", summary="What this library is and is not.", tags=[], text="")))

def build_help():
    body = '''
<div class="wrap narrow page-head">
  <p class="kicker">Help now</p>
  <h1>If you need a person today</h1>
  <p class="lede">Feeling lost is common. Feeling hopeless, or thinking about ending your life, is different, and you deserve real support. These lines are free and confidential.</p>
</div>
<div class="wrap narrow prose" style="padding-bottom:64px">
  <p class="note"><b>If you or someone else is in immediate danger,</b> call your local emergency number now (911 in the United States).</p>
  <h2>United States</h2>
  <ul>
    <li><b>988 Suicide &amp; Crisis Lifeline.</b> Call or text <b>988</b>, or chat at <a href="https://988lifeline.org/" rel="noopener">988lifeline.org</a>. Free, 24/7, open to anyone in distress. Spanish: press 2 when you call, or text AYUDA to 988.</li>
    <li><b>Crisis Text Line.</b> Text <b>HOME</b> to <b>741741</b>.</li>
    <li><b>SAMHSA National Helpline.</b> <b>1-800-662-4357</b> (HELP). Free, 24/7 referrals for mental health and substance use.</li>
  </ul>
  <h2>Canada</h2>
  <ul><li><b>9-8-8 Suicide Crisis Helpline.</b> Call or text <b>988</b>.</li></ul>
  <h2>United Kingdom and Ireland</h2>
  <ul><li><b>Samaritans.</b> Call <b>116 123</b>, free, 24/7.</li></ul>
  <h2>Anywhere else</h2>
  <p><a href="https://findahelpline.com/" rel="noopener">findahelpline.com</a> lists crisis and support lines in more than 170 countries.</p>
  <h2>If it is not a crisis but you want support</h2>
  <ul>
    <li>Talk to your doctor or a licensed therapist. Many offer sliding-scale fees.</li>
    <li>Look for a peer support group for what you are facing. Meeting others who have been there helps.</li>
    <li>Tell one person you trust how you have been feeling. Say it plainly. You do not need the right words.</li>
  </ul>
  <p class="small muted">Numbers and services change. If a line does not connect, search for your local crisis line or ask a doctor or pharmacist.</p>
</div>
'''
    write("/help/", page("/help/", "Help now", "Crisis lines and support resources if you are in distress or having thoughts of ending your life.",
        body, search=dict(title="Help now", type="Page", summary="Crisis lines and support.", tags=["crisis", "help"], text="crisis suicide hopeless 988 emergency support helpline")))

def build_search():
    body = '''
<div class="wrap narrow page-head">
  <p class="kicker">Search</p>
  <h1>Search the library</h1>
  <form class="search" action="/search/" role="search" style="max-width:none">
    <label class="sr" for="sq">Search</label>
    <input id="sq" name="q" type="search" placeholder="Try “procrastination”, “breathing”, “Stoic”" autocomplete="off" autofocus>
    <button class="btn primary" type="submit">Search</button>
  </form>
</div>
<div class="wrap narrow" style="padding-bottom:64px">
  <p class="muted" id="rstatus" aria-live="polite"></p>
  <ol class="results" id="results"></ol>
</div>
'''
    write("/search/", page("/search/", "Search", "Search ideas, practices, talks, and readings.", body, noindex=True))

def build_404():
    body = '''
<div class="wrap narrow page-head center" style="padding-block:90px">
  <p class="kicker">404</p>
  <h1>That page wandered off.</h1>
  <p class="lede" style="margin-inline:auto">Funny, for a site about being lost. Try the search, or start from the beginning.</p>
  <p><a class="btn primary" href="/">Go home</a> <a class="btn" href="/search/">Search</a></p>
</div>
'''
    html_ = page("/404/", "Page not found", "Page not found.", body, noindex=True)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html_)

# ===================================================================== WHY
def build_why():
    main, toc = add_ids(resolve(WHY_BODY))
    body = f"""
<div class="wrap narrow page-head">
  <p class="kicker">Why</p>
  <h1>Living on purpose</h1>
  <p class="lede">{esc(WHY_LEDE)}</p>
</div>
<div class="wrap narrow prose" style="padding-bottom:64px;max-width:none">
  {main}
  <div class="btn-row"><a class="btn primary" href="/practice/one-small-thing/">Try one small thing</a> <a class="btn" href="/practice/values-check/">Do a values check</a> <a class="btn" href="/help/">Need help now?</a></div>
</div>
"""
    write("/why/", page("/why/", "Why live on purpose", WHY_LEDE, body, section="Why",
        search=dict(title="Why live on purpose", type="Page", summary=WHY_LEDE, tags=["intention", "purpose"], text=strip_tags(main)[:1500])))

# ===================================================================== LIBRARY HUB
def build_library():
    items = [
        ("Ideas", "/ideas/", "%d plain-language articles on habits, urges, mood, attention, and meaning." % len(IDEAS)),
        ("Practice", "/practice/", "%d short exercises you can try in minutes." % len(PRACTICES)),
        ("Breathe", "/breathe/", "A visual pacer for box breathing, cyclic sighing, and longer exhales."),
        ("Meditate", "/meditate/", "A silent timer, guided readings, and free guided audio."),
        ("Watch", "/watch/", "A short shelf of well-regarded talks."),
        ("Read", "/read/", "Living writers on Substack, plus free classics on Stoicism and habit."),
        ("Mystics", "/mystics/", "Short passages and free texts from contemplatives."),
        ("Community", "/community/", "Subreddits and groups where others work on the same things."),
    ]
    hub_style = {"Ideas": "ridges", "Practice": "bloom", "Breathe": "ripples", "Meditate": "ripples", "Watch": "waves",
                 "Read": "orbit", "Mystics": "orbit", "Community": "bloom"}
    hub_color = {"Ideas": "gold", "Practice": "sage", "Breathe": "teal", "Meditate": "violet", "Watch": "ember",
                 "Read": "dusk", "Mystics": "violet", "Community": "gold"}
    cards = "".join('<a class="card" href="%s">%s<h3>%s</h3><p>%s</p></a>' % (
        u, art_img("hub-" + n.lower(), style=hub_style[n], color=hub_color[n]), n, esc(d)) for n, u, d in items)
    body = f"""
<div class="wrap page-head">
  <p class="kicker">Library</p>
  <h1>Everything in one place</h1>
  <p class="lede">Browse by format. Or <a href="/search/">search</a> for what you are dealing with.</p>
</div>
<div class="wrap" style="padding-bottom:64px"><div class="grid">{cards}</div></div>
"""
    write("/library/", page("/library/", "Library", "Ideas, practices, breathing, meditation, talks, readings, mystics, and communities.", body, section="Library",
        search=dict(title="Library", type="Page", summary="Everything in one place.", tags=[], text="")))

# ===================================================================== MYSTICS
def build_mystics():
    intro = "".join("<p>%s</p>" % esc(p) for p in MYSTIC_INTRO)
    qc = "".join('<figure class="qcard" style="margin:0 0 16px"><p>“%s”</p><footer><b>%s</b>%s</footer></figure>' % (esc(t), esc(a), esc(s)) for t, a, s in QUOTES)
    texts = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span class="by">%s</span><span>%s</span></li>' % (
        t["url"], esc(t["title"]), esc(t["who"]), esc(t["note"])) for t in MYSTIC_TEXTS)
    people = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s</span></li>' % (u, esc(n), esc(d)) for n, u, d in MYSTIC_PEOPLE)
    body = f"""
<div class="wrap page-head">
  <p class="kicker">Mystics</p>
  <h1>Words that have lasted</h1>
  <div class="prose" style="max-width:62ch;grid-column:auto">{intro}</div>
</div>
<div class="wrap" style="padding-bottom:64px">
  <h2>Passages</h2>
  <p class="muted">Short quotations from public-domain translations, with their sources.</p>
  <div class="qgrid">{qc}</div>
  <h2 style="margin-top:46px">Listen</h2>
  <p class="muted">Full talks from teachers in the contemplative tradition.</p>
  <div class="vgrid">{"".join(vid_card(v, ("teacher", "mystic")) for v in TEACHER_VIDEOS)}</div>
  <h2 style="margin-top:46px">Free texts to read</h2>
  <ul class="reslist">{texts}</ul>
  <h2 style="margin-top:46px">Meet the mystics</h2>
  <p class="muted">Starting points on Wikipedia. Follow the references from there.</p>
  <ul class="reslist" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr))">{people}</ul>
  <p class="note" style="margin-top:34px">Take what helps and leave the rest. Mystic writing can steady you, but it works best beside sleep, movement, good friends, and professional care when you need it. If things feel heavy, see <a href="/help/">help now</a>.</p>
</div>
"""
    for t, a, s in QUOTES:
        SEARCH.append(dict(title=a + ": " + t[:70], type="Quote", summary=s, tags=["quote", "mystic"], text=t, url="/mystics/"))
    write("/mystics/", page("/mystics/", "Mystics", "Short passages, free texts, and starting points from mystics and contemplatives across traditions.", body, section="Mystics",
        search=dict(title="Mystics", type="Page", summary="Passages, texts, and teachers.", tags=["mystic", "quotes", "wisdom"], text="mystics buddha lao tzu stoics rumi yogananda ram dass quotes wisdom")))

# ===================================================================== COMMUNITY
def build_community():
    intro = "".join("<p>%s</p>" % esc(p) for p in COMMUNITY_INTRO)
    cau = "".join("<li>%s</li>" % esc(c) for c in COMMUNITY_CAUTIONS)
    groups = ""
    for name, items in SUBREDDITS:
        li = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s</span></li>' % (u, esc(n), esc(d)) for n, u, d in items)
        groups += '<h2 style="margin-top:36px">%s</h2><ul class="reslist">%s</ul>' % (esc(name), li)
        for n, u, d in items:
            SEARCH.append(dict(title=n, type="Community", summary=d, tags=["reddit", "community"], text="", url="/community/"))
    other = "".join('<li><a href="%s" target="_blank" rel="noopener"><b>%s</b></a><span>%s</span></li>' % (u, esc(n), esc(d)) for n, u, d in OTHER_SUPPORT)
    body = f"""
<div class="wrap page-head">
  <p class="kicker">Community</p>
  <h1>You are not the only one</h1>
  <div class="prose" style="max-width:62ch;grid-column:auto">{intro}</div>
</div>
<div class="wrap" style="padding-bottom:64px">
  <div class="note" style="margin-top:0"><b>Read these with care.</b><ul style="margin:.6em 0 0;padding-left:1.2em">{cau}</ul></div>
  {groups}
  <h2 style="margin-top:46px">Beyond Reddit</h2>
  <ul class="reslist">{other}</ul>
  <p class="note small" style="margin-top:34px">These links go to other sites with their own rules and policies. Communities change over time.</p>
</div>
"""
    write("/community/", page("/community/", "Community", "Subreddits and groups for discipline, quitting porn, cutting back on scrolling, and personal growth, with notes on how to use them well.", body, section="Community",
        search=dict(title="Community", type="Page", summary="Subreddits and support groups.", tags=["reddit", "support"], text="reddit subreddit getdisciplined selfimprovement selfhelp nosurf nofap pornfree support group")))

# ===================================================================== JOURNAL
def build_journal():
    pj = json.dumps(JOURNAL_PROMPTS, ensure_ascii=False).replace("</", "<\\/")
    body = f"""
<div class="wrap narrow page-head">
  <p class="kicker">Journal</p>
  <h1>Write it down</h1>
  <p class="lede">A few lines can loosen a heavy day. Entries stay in this browser only. Nothing is sent anywhere.</p>
</div>
<div class="wrap narrow" style="padding-bottom:64px">
  <p class="kicker" style="margin-bottom:.4em">A prompt</p>
  <p id="jprompt" style="font-size:1.25rem;font-weight:300"></p>
  <p><button class="btn" id="jnew" type="button">Another prompt</button></p>
  <label class="sr" for="jtext">Your entry</label>
  <textarea class="jtext" id="jtext" placeholder="Write whatever is true."></textarea>
  <p><button class="btn primary" id="jsave" type="button">Save entry</button></p>
  <p class="note small">Saved in this browser on this device. Clearing your browser data erases it, and it will not appear on another device. Use Export to keep a copy. Do not use a shared or public computer.</p>
  <hr class="sep">
  <div class="section-head"><h2>Your entries</h2><div><button class="btn" id="jexport" type="button">Export</button> <button class="btn" id="jclear" type="button">Clear all</button></div></div>
  <p class="muted" id="jempty">No entries yet.</p>
  <div id="jlist"></div>
</div>
<script type="application/json" id="prompts-data">{pj}</script>
"""
    write("/journal/", page("/journal/", "Journal", "A private journal that stays in your browser, with gentle prompts.", body, section="Journal",
        search=dict(title="Journal", type="Tool", summary="A private journal with prompts. Stays in your browser.", tags=["journal", "writing"], text="journal writing prompts reflect")))

# ===================================================================== ASSETS
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
JS = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()

def build_assets():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "style.css"), "w", encoding="utf-8") as f: f.write(CSS)
    with open(os.path.join(OUT, "assets", "site.js"), "w", encoding="utf-8") as f: f.write(JS)
    idx = [dict(t=s["title"], u=s["url"], y=s["type"], s=s["summary"], g=s["tags"], x=s["text"]) for s in SEARCH]
    with open(os.path.join(OUT, "search.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, separators=(",", ":"))
    urls = "".join("  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (BASE, u, BUILD) for u in sorted(set(URLS)))
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /search/\n\nSitemap: %s/sitemap.xml\n" % BASE)
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("imfeelinglost.org\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()

if __name__ == "__main__":
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_home(); build_start(); build_ideas(); build_practice(); build_breathe(); build_meditate()
    build_why(); build_library(); build_mystics(); build_community(); build_journal(); build_watch(); build_read(); build_shop(); build_about(); build_help(); build_search(); build_404()
    build_assets()
    print("built", len(URLS), "pages ->", OUT)
