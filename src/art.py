# -*- coding: utf-8 -*-
"""Generative artwork. Each item gets its own deterministic SVG, drawn from its slug."""
import hashlib, math, random

PAL = {
    "gold":   ("#2b2215", "#C4A155", "#EBD7A0"),
    "ember":  ("#2b1711", "#C0603F", "#EDB08E"),
    "dusk":   ("#161b28", "#7088BC", "#BCC9E8"),
    "sage":   ("#142019", "#73A68B", "#BEDDC9"),
    "violet": ("#1e1828", "#9C7FC6", "#D6C6EC"),
    "teal":   ("#0f2120", "#52A6A2", "#A9DDD9"),
}

TAG_COLOR = {
    "urges": "ember", "porn": "ember", "habits": "gold", "discipline": "gold", "change": "gold",
    "mood": "dusk", "depression": "dusk", "energy": "dusk", "start here": "dusk",
    "attention": "teal", "phone": "teal", "focus": "teal",
    "mindfulness": "sage", "body": "sage", "calm": "sage", "connection": "sage",
    "meaning": "violet", "tradition": "violet", "values": "violet", "stoicism": "violet",
}

W, H = 480, 270


def color_for(tags, seed=""):
    for t in tags or []:
        c = TAG_COLOR.get(t.lower())
        if c:
            return c
    keys = sorted(PAL)
    return keys[int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(keys)]


def _f(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


def _ripples(r, mid, hi):
    cx, cy = r.uniform(.25, .75) * W, r.uniform(.3, .8) * H
    out = []
    for i in range(1, 16):
        rad = i * r.uniform(15, 19)
        op = max(.06, .7 - i * .045)
        out.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="%s"/>' % (
            _f(cx), _f(cy), _f(rad), mid if i % 3 else hi, _f(op), _f(1.4 if i % 3 else .8)))
    out.append('<circle cx="%s" cy="%s" r="5" fill="%s"/>' % (_f(cx), _f(cy), hi))
    return out


def _waves(r, mid, hi):
    out = []
    n = r.randint(9, 14)
    f = r.uniform(.012, .022)
    amp = r.uniform(14, 30)
    for k in range(n):
        base = H * (.18 + .68 * k / (n - 1))
        ph = k * r.uniform(.25, .5)
        pts = []
        for x in range(-10, W + 11, 10):
            y = base + amp * math.sin(f * x + ph) * (0.6 + 0.4 * math.sin(k * .5))
            pts.append("%s,%s" % (_f(x), _f(y)))
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="1.3"/>' % (
            " ".join(pts), hi if k == n // 2 else mid, _f(.25 + .5 * (1 - abs(k - n / 2) / (n / 2)))))
    return out


def _ridges(r, mid, hi):
    out = []
    sx, sy = r.uniform(.2, .8) * W, H * r.uniform(.25, .4)
    out.append('<circle cx="%s" cy="%s" r="%s" fill="%s" fill-opacity=".85"/>' % (_f(sx), _f(sy), _f(r.uniform(22, 34)), hi))
    layers = 5
    for k in range(layers):
        base = H * (.5 + .1 * k)
        pts = ["0,%d" % H]
        x = 0
        y = base
        while x <= W:
            y = base + r.uniform(-1, 1) * (34 - k * 5)
            pts.append("%s,%s" % (_f(x), _f(y)))
            x += r.uniform(30, 60)
        pts.append("%d,%s" % (W, _f(y)))
        pts.append("%d,%d" % (W, H))
        out.append('<polygon points="%s" fill="%s" fill-opacity="%s"/>' % (" ".join(pts), mid, _f(.18 + .16 * k)))
    return out


def _orbit(r, mid, hi):
    cx, cy = W * r.uniform(.4, .6), H * r.uniform(.4, .6)
    out = []
    rot = r.uniform(-30, 30)
    for i in range(1, 7):
        rx, ry = 40 + i * 30, 16 + i * 13
        out.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="%s" stroke-opacity="%s" transform="rotate(%s %s %s)"/>' % (
            _f(cx), _f(cy), rx, ry, mid, _f(.6 - i * .07), _f(rot), _f(cx), _f(cy)))
        a = r.uniform(0, 2 * math.pi)
        px = cx + rx * math.cos(a)
        py = cy + ry * math.sin(a)
        c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        dx, dy = px - cx, py - cy
        out.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(cx + dx * c - dy * s), _f(cy + dx * s + dy * c), _f(r.uniform(2.5, 5)), hi))
    for _ in range(40):
        out.append('<circle cx="%s" cy="%s" r="%s" fill="%s" fill-opacity="%s"/>' % (
            _f(r.uniform(0, W)), _f(r.uniform(0, H)), _f(r.uniform(.6, 1.6)), hi, _f(r.uniform(.2, .7))))
    out.append('<circle cx="%s" cy="%s" r="9" fill="%s"/>' % (_f(cx), _f(cy), hi))
    return out


def _bloom(r, mid, hi):
    cx, cy = W * r.uniform(.35, .65), H * r.uniform(.4, .65)
    n = r.choice([24, 32, 40, 48])
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n
        L = (60 + 50 * abs(math.sin(i * math.pi * 3 / n))) * r.uniform(.85, 1.1)
        out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-opacity="%s" stroke-width="1.2" stroke-linecap="round"/>' % (
            _f(cx + 18 * math.cos(a)), _f(cy + 18 * math.sin(a)), _f(cx + L * math.cos(a)), _f(cy + L * math.sin(a)),
            hi if i % 4 == 0 else mid, _f(.75 if i % 4 == 0 else .45)))
    for k in range(3):
        out.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-opacity=".35"/>' % (_f(cx), _f(cy), 120 + k * 26, mid))
    out.append('<circle cx="%s" cy="%s" r="10" fill="%s"/>' % (_f(cx), _f(cy), hi))
    return out


STYLES = {"ripples": _ripples, "waves": _waves, "ridges": _ridges, "orbit": _orbit, "bloom": _bloom}


def svg(seed, color="gold", style=None):
    r = random.Random(int(hashlib.sha1(seed.encode()).hexdigest()[:12], 16))
    deep, mid, hi = PAL[color]
    if not style:
        style = sorted(STYLES)[r.randrange(len(STYLES))]
    shapes = STYLES[style](r, mid, hi)
    gx, gy = _f(r.uniform(.2, .8) * 100), _f(r.uniform(.1, .5) * 100)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid slice">'
            '<defs><radialGradient id="g" cx="%s%%" cy="%s%%" r="85%%"><stop offset="0" stop-color="%s"/>'
            '<stop offset="1" stop-color="#0E0D0C"/></radialGradient></defs>'
            '<rect width="%d" height="%d" fill="url(#g)"/>%s</svg>') % (W, H, gx, gy, deep, W, H, "".join(shapes))
