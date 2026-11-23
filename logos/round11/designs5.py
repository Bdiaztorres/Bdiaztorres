"""Round 11: eight more bold All Him marks (85-92)."""
import math, sys, os
os.chdir('/home/claude/logo'); sys.path.insert(0, '/home/claude/logo'); sys.path.insert(0, '/home/claude/royal')
from designs3 import F, HFont, knot, card, P, INK, CREAM, arc_bottom
import parts
from parts import crown, laurel, ribbon, key, cipher

F.cinzel9 = HFont('fonts/Cinzel.ttf', {'wght': 900})
F.wide9 = HFont('fonts/Archivo.ttf', {'wght': 900, 'wdth': 125})
F.wide7 = HFont('fonts/Archivo.ttf', {'wght': 700, 'wdth': 125})
SH = "M300 190 H700 V450 C700 620 610 705 500 775 C390 705 300 620 300 450 Z"


# 85 Ribbon Shield
def R85(ink=INK, bg=CREAM, id_="R85"):
    g, _ = knot(118, 500, 440, 0.22, 0.09, ink, id_)
    rb = ribbon(500, 770, 640, 30, 84, 'IT WAS NEVER ME', parts.CINZEL(900), 40, ink, bg, tail=ink, ls=.08)
    return card(bg, f'<path d="{SH}" fill="{bg}" stroke="{ink}" stroke-width="22" stroke-linejoin="miter"/>'
                    + P(F.wide9.line("ALL HIM", 34, 10, 500, 262), ink) + f'<rect x="300" y="290" width="400" height="9" fill="{ink}"/>' + g + rb)


# 86 Crown Roundel: crown, AH cipher, name around the bottom
def C86(ink=INK, bg=CREAM, id_="C86"):
    ring = (f'<circle cx="500" cy="500" r="310" fill="none" stroke="{ink}" stroke-width="22"/>'
            f'<circle cx="500" cy="500" r="262" fill="none" stroke="{ink}" stroke-width="7"/>')
    cr = crown(500, 268, 160, ink)
    ah = cipher(500, 600, 170, ink, bg)
    t = F.wide9.line("ALL HIM", 36, 12, 500, 692)
    e = F.wide7.line("EST. 2026", 20, 8, 500, 728)
    return card(bg, ring + cr + ah + f'<rect x="380" y="640" width="240" height="7" fill="{ink}"/>' + P(t, ink) + P(e, ink))


# 87 Varsity Arch: arched block name, knot, stars
def V87(ink=INK, bg=CREAM, id_="V87"):
    arch = F.varsity.arc("ALL HIM", 108, 10, 500, 640, 330)
    g, _ = knot(110, 500, 560, 0.23, 0.09, ink, id_)
    est = F.varsity.line("EST. 2026", 44, 6, 500, 790)
    def star(cx, cy, r):
        pts = [f"{cx + (r if i % 2 == 0 else r*.42) * math.sin(math.pi*i/5):.1f},{cy - (r if i % 2 == 0 else r*.42) * math.cos(math.pi*i/5):.1f}" for i in range(10)]
        return f'<polygon points="{" ".join(pts)}" fill="{ink}"/>'
    bold = lambda d: f'<path d="{d}" fill="{ink}" stroke="{ink}" stroke-width="7" stroke-linejoin="round"/>'
    return card(bg, bold(arch) + g + bold(est) + star(250, 560, 30) + star(750, 560, 30))


# 88 Keys of the Kingdom: crossed keys behind the knot (Matthew 16:19)
def K88(ink=INK, bg=CREAM, id_="K88"):
    Lk = 560; out = ''
    for rot, flip in ((-45, 1), (-135, -1)):
        out += f'<g transform="translate(500 470) rotate({rot}) scale(1 {flip}) translate({-Lk/2} 0)">{key(Lk, ink, bg)}</g>'
    disc = f'<circle cx="500" cy="470" r="122" fill="{bg}" stroke="{ink}" stroke-width="14"/>'
    g, _ = knot(84, 500, 474, 0.24, 0.10, ink, id_)
    t = F.cinzel9.line("ALL HIM", 60, 16, 500, 820)
    v = F.wide7.line("MT 16:19", 24, 8, 500, 870)
    return card(bg, out + disc + g + P(t, ink) + P(v, ink))


# 89 Laurel Roundel: wreath, knot, ribbon name
def L89(ink=INK, bg=CREAM, id_="L89"):
    wr = laurel(500, 470, 280, 300, ink, n=10, a0=100, step=14.2, L=92, W=34, stem=11)
    g, _ = knot(128, 500, 450, 0.22, 0.09, ink, id_)
    rb = ribbon(500, 800, 820, 24, 98, 'ALL HIM', parts.CINZEL(900), 58, ink, bg, tail=ink, ls=.16)
    return card(bg, wr + g + rb)


# 90 Diamond Patch: diamond outline, name band, knot, John 3:30
def D90(ink=INK, bg=CREAM, id_="D90"):
    d = "M500 170 L830 500 L500 830 L170 500 Z"
    band = f'<path d="M222 448 H778 L830 500 L778 552 H222 L170 500 Z" fill="{ink}"/>'
    t = F.wide9.line("ALL HIM", 52, 10, 500, 500 + F.wide9.cap * 52 / 2)
    g, _ = knot(64, 500, 340, 0.24, 0.10, ink, id_)
    v = F.wide9.line("JN 3:30", 30, 8, 500, 660)
    return card(bg, f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="24" stroke-linejoin="miter"/>' + band + P(t, bg) + g + P(v, ink))


# 91 Stacked: ALL / knot / HIM, John 3:30 ("He must increase, but I must decrease")
def S91(ink=INK, bg=CREAM, id_="S91"):
    a = F.anton.line("ALL", 300, 14, 500, 425)
    h = F.anton.line("HIM", 300, 14, 500, 835)
    g, _ = knot(40, 500, 505, 0.24, 0.10, ink, id_)
    rules = f'<rect x="300" y="500" width="140" height="10" fill="{ink}"/><rect x="560" y="500" width="140" height="10" fill="{ink}"/>'
    v = F.wide9.line("JN 3:30", 26, 10, 500, 905)
    return card(bg, P(a, ink) + rules + g + P(h, ink) + P(v, ink))


# 92 Dog Tag: ball chain, tag, stamped lines
def T92(ink=INK, bg=CREAM, id_="T92"):
    tag = f'<rect x="330" y="230" width="340" height="600" rx="80" fill="none" stroke="{ink}" stroke-width="22"/>'
    hole = f'<circle cx="500" cy="300" r="26" fill="none" stroke="{ink}" stroke-width="12"/>'
    chain = ''
    for sx in (-1, 1):
        for i in range(1, 12):
            t = i / 11; x = 500 + sx * (14 + 170 * t); y = 280 - 230 * t + 40 * t * (1 - t)
            chain += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{ink}"/>'
    lines = ''.join(P(F.mono.line(s, 40, 4, 500, y), ink) for s, y in (("ALL HIM", 420), ("IT WAS", 490), ("NEVER ME", 560), ("JN 3:30", 630)))
    g, _ = knot(52, 500, 730, 0.24, 0.10, ink, id_)
    return card(bg, chain + tag + hole + lines + g)


NEW5 = [("85", "ribbon-shield", "Ribbon Shield", R85), ("86", "crown-roundel", "Crown Roundel", C86),
        ("87", "varsity-arch", "Varsity Arch", V87), ("88", "keys", "Keys of the Kingdom", K88),
        ("89", "laurel-roundel", "Laurel Roundel", L89), ("90", "diamond-patch", "Diamond Patch", D90),
        ("91", "stacked", "Stacked", S91), ("92", "dog-tag", "Dog Tag", T92)]

if __name__ == "__main__":
    os.makedirs("round11", exist_ok=True)
    for num, slug, _, fn in NEW5:
        open(f"round11/{num}-{slug}.svg", "w").write(fn())
        open(f"round11/{num}-{slug}-dark.svg", "w").write(fn(CREAM, INK, id_=fn.__name__ + "d"))
    print("ok")
