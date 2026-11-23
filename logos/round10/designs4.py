"""Round 10: eight bold, embroidery-ready All Him marks (77-84)."""
import math, sys
sys.path.insert(0, '/home/claude/royal')
from designs3 import F, HFont, knot, card, P, INK, CREAM
from parts import crown

F.cinzel9 = HFont('fonts/Cinzel.ttf', {'wght': 900})
F.wide9 = HFont('fonts/Archivo.ttf', {'wght': 900, 'wdth': 125})
F.wide7 = HFont('fonts/Archivo.ttf', {'wght': 700, 'wdth': 125})

SH = "M300 210 H700 V470 C700 640 610 725 500 795 C390 725 300 640 300 470 Z"


def fit(font, txt, size, track, maxw):
    w = font.width(txt, size, track)
    return size * min(1, maxw / w)


# 77 AH Shield: monogram in the heavy shield
def M77(ink=INK, bg=CREAM, id_="M77"):
    t = F.cinzel9.line("AH", 210, 4, 500, 540)
    g, _ = knot(46, 500, 650, 0.24, 0.10, ink, id_)
    return card(bg, f'<path d="{SH}" fill="none" stroke="{ink}" stroke-width="24" stroke-linejoin="miter"/>'
                    + f'<rect x="300" y="300" width="400" height="10" fill="{ink}"/>'
                    + P(F.wide9.line("ALL HIM", 34, 10, 500, 272), ink) + P(t, ink) + g)


# 78 Wax Seal: scalloped seal, name around, knot centre
def S78(ink=INK, bg=CREAM, id_="S78"):
    cx, cy, n = 500, 500, 30
    pts = []
    for i in range(n * 8):
        a = 2 * math.pi * i / (n * 8)
        r = 300 + 14 * math.cos(n * a)
        pts.append(f"{cx + r * math.cos(a):.1f} {cy + r * math.sin(a):.1f}")
    seal = "M" + " L".join(pts) + " Z"
    txt = "ALL HIM · IT WAS NEVER ME · "
    size, R = 34, 236
    nat = F.wide9.width(txt, size, 0); m = len(F.wide9.shape(txt))
    track = (2 * math.pi * R - nat) / m
    ring = F.wide9.arc(txt, size, track, cx, cy, R)
    g, _ = knot(120, cx, cy + 6, 0.22, 0.09, bg, id_)
    return card(bg, f'<path d="{seal}" fill="{ink}"/>'
                    f'<circle cx="{cx}" cy="{cy}" r="196" fill="none" stroke="{bg}" stroke-width="10"/>' + P(ring, bg) + g)


# 79 Crowned Knot
def C79(ink=INK, bg=CREAM, id_="C79"):
    cr = crown(500, 170, 250, ink)
    g, _ = knot(132, 500, 520, 0.22, 0.09, ink, id_)
    t = F.cinzel9.line("ALL HIM", 66, 16, 500, 790)
    return card(bg, cr + g + P(t, ink))


# 80 Cornerstone: keystone with Psalm 118:22
def K80(ink=INK, bg=CREAM, id_="K80"):
    stone = "M300 200 L700 200 L620 800 L380 800 Z"
    t = F.wide9.line("ALL HIM", 46, 8, 500, 290)
    g, _ = knot(96, 500, 500, 0.24, 0.10, bg, id_)
    v = F.wide7.line("PS 118:22", 26, 6, 500, 720)
    return card(bg, f'<path d="{stone}" fill="{ink}" stroke="{ink}" stroke-width="16" stroke-linejoin="round"/>'
                    f'<rect x="330" y="322" width="340" height="8" fill="{bg}"/><rect x="398" y="664" width="204" height="8" fill="{bg}"/>'
                    + P(t, bg) + g + P(v, bg))


# 81 Alpha Omega: A, knot, Omega (Revelation 22:13)
def A81(ink=INK, bg=CREAM, id_="A81"):
    a = F.cinzel9.line("A", 230, 0, 260, 560)
    o = F.cinzel9.line("Ω", 230, 0, 740, 560)
    g, _ = knot(112, 500, 470, 0.22, 0.09, ink, id_)
    t = F.wide9.line("ALL HIM", 40, 18, 500, 712)
    r = F.wide7.line("REV 22:13", 22, 8, 500, 770)
    return card(bg, P(a, ink) + P(o, ink) + g + f'<rect x="150" y="620" width="700" height="9" fill="{ink}"/>' + P(t, ink) + P(r, ink))


# 82 Gothic: blackletter name, knot as the dot, motto bar
def G82(ink=INK, bg=CREAM, id_="G82"):
    t = F.goth.line("All Him", 196, 0, 500, 540)
    g, _ = knot(52, 500, 300, 0.24, 0.10, ink, id_)
    m = F.wide9.line("IT WAS NEVER ME", 26, 10, 500, 676)
    return card(bg, g + P(t, ink) + f'<rect x="230" y="604" width="540" height="10" fill="{ink}"/>' + P(m, ink))


# 83 Cross Knot: heavy cross outline, knot at the crossing, name down the stem
def X83(ink=INK, bg=CREAM, id_="X83"):
    cross = ("M420 160 H580 V300 H740 V460 H580 V840 H420 V460 H260 V300 H420 Z")
    g, _ = knot(62, 500, 380, 0.24, 0.10, ink, id_)
    size = 40; cap = F.wide9.cap * size
    t = F.wide9.line("ALL HIM", size, 10, 0, cap / 2)
    return card(bg, f'<path d="{cross}" fill="none" stroke="{ink}" stroke-width="22" stroke-linejoin="miter"/>' + g
                    + f'<path d="{t}" fill="{ink}" transform="translate(500 652) rotate(90)"/>')


# 84 Box Logo: name reversed out of a solid bar
def B84(ink=INK, bg=CREAM, id_="B84"):
    size = fit(F.wide9, "ALL HIM", 118, 4, 540)
    cap = F.wide9.cap * size
    t = F.wide9.line("ALL HIM", size, 4, 500, 500 + cap / 2)
    m = F.wide7.line("IT WAS NEVER ME", 24, 10, 500, 656)
    g, _ = knot(40, 500, 345, 0.24, 0.10, ink, id_)
    return card(bg, g + f'<rect x="190" y="410" width="620" height="180" fill="{ink}"/>' + P(t, bg) + P(m, ink))


NEW4 = [("77", "ah-shield", "AH Shield", M77), ("78", "wax-seal", "Wax Seal", S78),
        ("79", "crowned-knot", "Crowned Knot", C79), ("80", "cornerstone", "Cornerstone", K80),
        ("81", "alpha-omega", "Alpha & Omega", A81), ("82", "gothic-bar", "Gothic Bar", G82),
        ("83", "cross-knot", "Cross Knot", X83), ("84", "box-logo", "Box Logo", B84)]

if __name__ == "__main__":
    import os
    os.makedirs("round10", exist_ok=True)
    for num, slug, _, fn in NEW4:
        open(f"round10/{num}-{slug}.svg", "w").write(fn())
        open(f"round10/{num}-{slug}-dark.svg", "w").write(fn(CREAM, INK, id_=fn.__name__ + "d"))
        open(f"round10/{num}-{slug}-transparent.svg", "w").write(fn(INK, "none", id_=fn.__name__ + "t"))
        open(f"round10/{num}-{slug}-transparent-cream.svg", "w").write(fn(CREAM, "none", id_=fn.__name__ + "c"))
    print("ok")
