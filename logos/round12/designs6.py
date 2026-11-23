"""Round 12: twenty more bold All Him marks (93-112)."""
import math, sys, os
os.chdir('/home/claude/logo'); sys.path.insert(0, '/home/claude/logo'); sys.path.insert(0, '/home/claude/royal')
from designs3 import F, HFont, knot, card, P, INK, CREAM
import parts
from parts import crown, laurel, ribbon, cipher, fleur

F.cinzel9 = HFont('fonts/Cinzel.ttf', {'wght': 900})
F.wide9 = HFont('fonts/Archivo.ttf', {'wght': 900, 'wdth': 125})
F.wide7 = HFont('fonts/Archivo.ttf', {'wght': 700, 'wdth': 125})
F.black = HFont('fonts/ArchivoBlack-Regular.ttf')


def K(S, cx, cy, ink, id_, w=0.23, g=0.095):
    return knot(S, cx, cy, w, g, ink, id_)[0]


def T(font, txt, size, track, cx, base, ink, stroke=0):
    d = font.line(txt, size, track, cx, base)
    st = f' stroke="{ink}" stroke-width="{stroke}" stroke-linejoin="round"' if stroke else ''
    return f'<path d="{d}" fill="{ink}"{st}/>'


def mid(font, size):  # baseline that centres caps on y
    return F.__dict__ and font.cap * size / 2


def star(cx, cy, r, ink):
    pts = [f"{cx + (r if i % 2 == 0 else r*.42) * math.sin(math.pi*i/5):.1f},{cy - (r if i % 2 == 0 else r*.42) * math.cos(math.pi*i/5):.1f}" for i in range(10)]
    return f'<polygon points="{" ".join(pts)}" fill="{ink}"/>'


# 93 Monogram Disc: AH reversed out of a solid circle
def d93(ink=INK, bg=CREAM, id_="d93"):
    return card(bg, f'<circle cx="500" cy="470" r="250" fill="{ink}"/>' + cipher(500, 560, 240, bg, ink)
                + T(F.wide9, "ALL HIM", 44, 16, 500, 820, ink))


# 94 Halo Knot: halo ring over the knot
def d94(ink=INK, bg=CREAM, id_="d94"):
    return card(bg, f'<ellipse cx="500" cy="255" rx="150" ry="38" fill="none" stroke="{ink}" stroke-width="20"/>'
                + K(150, 500, 500, ink, id_) + T(F.cinzel9, "ALL HIM", 70, 18, 500, 800, ink))


# 95 Chevron Badge: three chevrons under the knot (rank)
def d95(ink=INK, bg=CREAM, id_="d95"):
    ch = ''.join(f'<path d="M260 {560+i*70} L500 {450+i*70} L740 {560+i*70}" fill="none" stroke="{ink}" stroke-width="34" stroke-linejoin="miter"/>' for i in range(3))
    return card(bg, K(96, 500, 290, ink, id_) + ch + T(F.wide9, "ALL HIM", 40, 14, 500, 840, ink))


# 96 Script Swash: bold script with a swash and knot
def d96(ink=INK, bg=CREAM, id_="d96"):
    t = T(F.pinyon, "All Him", 230, 0, 500, 520, ink, stroke=7)
    sw = f'<path d="M230 600 C420 560 640 560 800 590" fill="none" stroke="{ink}" stroke-width="12" stroke-linecap="round"/>'
    return card(bg, t + sw + K(44, 500, 690, ink, id_) + T(F.wide9, "IT WAS NEVER ME", 24, 10, 500, 790, ink))


# 97 Ring Seal: name arched over the knot inside a heavy ring
def d97(ink=INK, bg=CREAM, id_="d97"):
    ring = f'<circle cx="500" cy="500" r="320" fill="none" stroke="{ink}" stroke-width="26"/><circle cx="500" cy="500" r="200" fill="none" stroke="{ink}" stroke-width="8"/>'
    arc = F.wide9.arc("ALL HIM", 52, 20, 500, 500, 238)
    s = star(310, 640, 18, ink) + star(690, 640, 18, ink) + star(500, 735, 18, ink)
    return card(bg, ring + P(arc, ink) + K(118, 500, 505, ink, id_) + s)


# 98 Hexagon Badge
def d98(ink=INK, bg=CREAM, id_="d98"):
    pts = " ".join(f"{500 + 330*math.cos(math.radians(30+60*i)):.1f},{500 + 330*math.sin(math.radians(30+60*i)):.1f}" for i in range(6))
    return card(bg, f'<polygon points="{pts}" fill="none" stroke="{ink}" stroke-width="26" stroke-linejoin="miter"/>'
                + K(126, 500, 440, ink, id_) + f'<rect x="300" y="610" width="400" height="8" fill="{ink}"/>' + T(F.wide9, "ALL HIM", 44, 14, 500, 690, ink))


# 99 Banner Wordmark: name in a folded ribbon banner
def d99(ink=INK, bg=CREAM, id_="d99"):
    b = (f'<path d="M150 470 L230 470 L230 590 L150 590 L190 530 Z" fill="{ink}"/><path d="M850 470 L770 470 L770 590 L850 590 L810 530 Z" fill="{ink}"/>'
         f'<rect x="220" y="440" width="560" height="120" fill="{ink}"/>')
    return card(bg, K(80, 500, 330, ink, id_) + b + T(F.cinzel9, "ALL HIM", 66, 18, 500, 524, bg) + T(F.wide9, "EST. 2026", 24, 10, 500, 650, ink))


# 100 Jersey 01: varsity numerals for Vol 01
def d100(ink=INK, bg=CREAM, id_="d100"):
    n = T(F.varsity, "01", 380, 10, 500, 700, ink, stroke=10)
    return card(bg, T(F.varsity, "ALL HIM", 70, 8, 500, 300, ink, stroke=5) + n + T(F.wide9, "VOL", 26, 12, 500, 790, ink))


# 101 Quartered Shield: knot, crown, cross, AH
def d101(ink=INK, bg=CREAM, id_="d101"):
    sh = "M300 200 H700 V460 C700 630 610 715 500 785 C390 715 300 630 300 460 Z"
    q = f'<rect x="300" y="430" width="400" height="16" fill="{ink}"/><rect x="492" y="200" width="16" height="585" fill="{ink}"/>'
    cross = f'<rect x="391" y="500" width="18" height="130" fill="{ink}"/><rect x="360" y="535" width="80" height="18" fill="{ink}"/>'
    return card(bg, f'<path d="{sh}" fill="none" stroke="{ink}" stroke-width="22"/>' + q + K(54, 400, 320, ink, id_)
                + crown(600, 265, 120, ink) + cross + T(F.cinzel9, "AH", 64, 2, 600, 590, ink))


# 102 Glory: knot with radiating rays
def d102(ink=INK, bg=CREAM, id_="d102"):
    rays = ''
    for i in range(24):
        a = math.radians(i * 15); r1, r2 = 160, (300 if i % 2 == 0 else 250)
        w = 7 if i % 2 == 0 else 5
        p1 = (500 + r1*math.cos(a - .05), 480 + r1*math.sin(a - .05)); p2 = (500 + r1*math.cos(a + .05), 480 + r1*math.sin(a + .05)); p3 = (500 + r2*math.cos(a), 480 + r2*math.sin(a))
        rays += f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="{ink}"/>'
    return card(bg, rays + K(118, 500, 484, ink, id_) + T(F.cinzel9, "ALL HIM", 60, 18, 500, 850, ink))


# 103 Horizontal Lockup: knot | ALL HIM
def d103(ink=INK, bg=CREAM, id_="d103"):
    return card(bg, K(92, 260, 500, ink, id_) + f'<rect x="372" y="410" width="10" height="180" fill="{ink}"/>'
                + f'<path d="{F.wide9.line("ALL HIM", 74, 6, 420, 500 + F.wide9.cap*74/2, "left")}" fill="{ink}"/>'
                + f'<path d="{F.wide7.line("IT WAS NEVER ME", 20, 9, 420, 590, "left")}" fill="{ink}"/>')


# 104 Tablet: arched tablet, Colossians 3:23
def d104(ink=INK, bg=CREAM, id_="d104"):
    tab = "M310 820 V360 A190 190 0 0 1 690 360 V820 Z"
    return card(bg, f'<path d="{tab}" fill="{ink}"/>' + K(110, 500, 380, bg, id_) + f'<rect x="360" y="530" width="280" height="8" fill="{bg}"/>'
                + T(F.cinzel9, "ALL HIM", 50, 12, 500, 620, bg) + T(F.wide9, "COL 3:23", 26, 8, 500, 740, bg))


# 105 Fleur Crest: fleur-de-lis over the name
def d105(ink=INK, bg=CREAM, id_="d105"):
    return card(bg, fleur(500, 170, 420, ink) + K(40, 500, 655, ink, id_) + T(F.cinzel9, "ALL HIM", 72, 18, 500, 800, ink))


# 106 Celtic Cross: ring cross with the knot at the centre
def d106(ink=INK, bg=CREAM, id_="d106"):
    c = (f'<rect x="440" y="140" width="120" height="740" fill="{ink}"/><rect x="250" y="320" width="500" height="120" fill="{ink}"/>'
         f'<circle cx="500" cy="380" r="150" fill="none" stroke="{ink}" stroke-width="34"/><circle cx="500" cy="380" r="86" fill="{bg}"/>')
    size = 44; cap = F.wide9.cap * size
    t = F.wide9.line("ALL HIM", size, 12, 0, cap / 2)
    return card(bg, c + K(64, 500, 382, ink, id_) + f'<path d="{t}" fill="{bg}" transform="translate(500 700) rotate(90)"/>')


# 107 Pennant
def d107(ink=INK, bg=CREAM, id_="d107"):
    pen = "M210 330 L860 500 L210 670 Z"
    pole = f'<rect x="180" y="250" width="22" height="540" rx="6" fill="{ink}"/>'
    return card(bg, pole + f'<path d="{pen}" fill="{ink}"/>' + K(66, 300, 500, bg, id_)
                + f'<path d="{F.wide9.line("ALL HIM", 50, 8, 380, 500 + F.wide9.cap*50/2, "left")}" fill="{bg}"/>')


# 108 Stamp: perforated postage stamp, VOL 01
def d108(ink=INK, bg=CREAM, id_="d108"):
    x0, y0, w, h, r = 280, 210, 440, 580, 16
    holes = ''.join(f'<circle cx="{x0 + w*i/12:.1f}" cy="{y}" r="{r}" fill="{bg}"/>' for i in range(13) for y in (y0, y0 + h))
    holes += ''.join(f'<circle cx="{x}" cy="{y0 + h*i/16:.1f}" r="{r}" fill="{bg}"/>' for i in range(17) for x in (x0, x0 + w))
    inner = f'<rect x="{x0+44}" y="{y0+44}" width="{w-88}" height="{h-88}" fill="none" stroke="{bg}" stroke-width="8"/>'
    return card(bg, f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{ink}"/>' + holes + inner + K(110, 500, 440, bg, id_)
                + T(F.wide9, "ALL HIM", 38, 10, 500, 640, bg) + T(F.wide9, "VOL 01", 26, 10, 500, 700, bg))


# 109 Interlock AH: varsity A over H
def d109(ink=INK, bg=CREAM, id_="d109"):
    h = F.varsity.line("H", 380, 0, 560, 700); a = F.varsity.line("A", 380, 0, 430, 610)
    return card(bg, f'<path d="{h}" fill="{ink}" stroke="{ink}" stroke-width="10"/>'
                + f'<path d="{a}" fill="{bg}" stroke="{bg}" stroke-width="26" stroke-linejoin="round"/><path d="{a}" fill="{ink}" stroke="{ink}" stroke-width="10"/>'
                + T(F.wide9, "ALL HIM", 30, 12, 500, 820, ink))


# 110 Crowned H
def d110(ink=INK, bg=CREAM, id_="d110"):
    return card(bg, crown(500, 150, 220, ink) + T(F.cinzel9, "H", 420, 0, 500, 680, ink)
                + T(F.wide9, "ALL HIM", 36, 14, 500, 780, ink) + K(40, 500, 860, ink, id_))


# 111 Wreath Monogram: laurel around AH
def d111(ink=INK, bg=CREAM, id_="d111"):
    wr = laurel(500, 480, 270, 290, ink, n=10, a0=100, step=14.2, L=88, W=32, stem=10)
    return card(bg, wr + cipher(500, 560, 200, ink, bg) + K(40, 500, 820, ink, id_))


# 112 Motto Block: stacked motto in a box with the knot
def d112(ink=INK, bg=CREAM, id_="d112"):
    box = f'<rect x="230" y="240" width="540" height="520" fill="none" stroke="{ink}" stroke-width="22"/>'
    lines = ''.join(T(F.black, s, 74, 2, 500, y, ink) for s, y in (("IT WAS", 370), ("NEVER", 465), ("ME.", 560)))
    return card(bg, box + lines + f'<rect x="230" y="610" width="540" height="150" fill="{ink}"/>' + K(56, 380, 685, bg, id_)
                + f'<path d="{F.wide9.line("ALL HIM", 40, 8, 450, 685 + F.wide9.cap*40/2, "left")}" fill="{bg}"/>')


NEW6 = [("93", "monogram-disc", "Monogram Disc", d93), ("94", "halo-knot", "Halo Knot", d94), ("95", "chevron-badge", "Chevron Badge", d95),
        ("96", "script-swash", "Script Swash", d96), ("97", "ring-seal", "Ring Seal", d97), ("98", "hexagon-badge", "Hexagon Badge", d98),
        ("99", "banner-wordmark", "Banner Wordmark", d99), ("100", "jersey-01", "Jersey 01", d100), ("101", "quartered-shield", "Quartered Shield", d101),
        ("102", "glory", "Glory", d102), ("103", "horizontal-lockup", "Horizontal Lockup", d103), ("104", "tablet", "Tablet", d104),
        ("105", "fleur-crest", "Fleur Crest", d105), ("106", "celtic-cross", "Celtic Cross", d106), ("107", "pennant", "Pennant", d107),
        ("108", "stamp", "Stamp", d108), ("109", "interlock-ah", "Interlock AH", d109), ("110", "crowned-h", "Crowned H", d110),
        ("111", "wreath-monogram", "Wreath Monogram", d111), ("112", "motto-block", "Motto Block", d112)]

if __name__ == "__main__":
    os.makedirs("round12", exist_ok=True)
    for num, slug, _, fn in NEW6:
        open(f"round12/{num}-{slug}.svg", "w").write(fn())
        open(f"round12/{num}-{slug}-dark.svg", "w").write(fn(CREAM, INK, id_=fn.__name__ + "d"))
    print("ok")
