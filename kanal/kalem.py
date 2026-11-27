"""Defter tarzı: dokulu kâğıt, kalemin ucuyla çizme ve yazma, taramalı boyama (video 3'ten itibaren).
Kullanım: class X(Defter): theme = "gece" | "defter"; self.ciz(m1, m2) ve self.yaz(t) say() adımı olarak verilir."""
import numpy as np
from manim import *

from tahta import FONT, P, THEMES, Tahta, sketch, text

THEMES["gece"] = dict(bg="#101b2d", ink="#eef0e6", red="#ff7a66", blue="#6ec6ff", yellow="#ffd166", green="#8fd694", gray="#7d8aa0")
THEMES["defter"] = dict(bg="#f5eedb", ink="#2b2a28", red="#c8412f", blue="#2a62b8", yellow="#d99a00", green="#2e8b57", gray="#8b8678")
UZAK = P(40, 0)                      # boştaki kalem ekran dışında bekler


def kagit(theme):
    """Dokulu zemin: defterde kareli kâğıt ve kenar çizgisi, gecede lifli lacivert ve nokta ızgarası."""
    h, w = 900, 1600
    rng = np.random.default_rng(7)
    base = np.array(ManimColor(THEMES[theme]["bg"]).to_rgb()) * 255
    kaba = np.kron(rng.normal(0, 1, (h // 10, w // 10)), np.ones((10, 10)))
    img = base + (rng.normal(0, 2.2, (h, w)) + kaba * 1.4)[..., None]
    if theme == "defter":
        mavi = np.array([150, 180, 205])
        for maske in (np.s_[::50, :], np.s_[:, ::50]):
            img[maske] = img[maske] * .72 + mavi * .28
        img[:, 70:73] = img[:, 70:73] * .4 + np.array([215, 110, 100]) * .6
    else:
        for dy in (0, 1):
            for dx in (0, 1):
                img[25 + dy::50, 25 + dx::50] += 28
    y, x = np.mgrid[0:h, 0:w]
    vin = 1 - .16 * (((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2) ** 1.5 / 2.8
    rgb = np.clip(img * vin[..., None], 0, 255).astype(np.uint8)
    m = ImageMobject(np.dstack([rgb, np.full((h, w), 255, np.uint8)]))
    m.height = 9.0
    return m.move_to(P(0, -.5)).set_z_index(-100)


def kalem(theme):
    """Uç (0,0) noktasında. Defterde kurşun kalem, gecede tebeşir."""
    def cok(pts, renk):
        return Polygon(*[P(*q) for q in pts], stroke_color="#20201e", stroke_width=2).set_fill(renk, 1)
    if theme == "defter":
        parts = [cok([(0, 0), (.13, .30), (.30, .13)], "#e8c79a"), cok([(0, 0), (.05, .11), (.11, .05)], "#333333"),
                 cok([(.13, .30), (.30, .13), (1.05, .88), (.88, 1.05)], "#f2b705"),
                 cok([(.88, 1.05), (1.05, .88), (1.2, 1.03), (1.03, 1.2)], "#e0707a")]
    else:
        parts = [cok([(0, 0), (.02, .17), (.17, .02)], "#d9d9d2"), cok([(.02, .17), (.17, .02), (.85, .70), (.70, .85)], "#f4f4ee")]
    return VGroup(*parts).set_z_index(50)


class Ciz(Animation):
    """Nesneleri sırayla, kalemin ucunu izleyerek çizer. Metinde harfleri soldan sağa yazar."""

    def __init__(self, mob, metin=False, **kw):
        self.metin, self.adim_sn, self.uc = metin, 1.0, None
        super().__init__(mob, introducer=True, rate_func=linear, **kw)

    def begin(self):
        self.yaprak = self.mobject.family_members_with_points()
        self.asil = [m.copy() for m in self.yaprak]
        if self.metin:
            boy = [m.width + .12 for m in self.asil]
        else:
            boy = [float(np.linalg.norm(np.diff(m.points, axis=0), axis=1).sum()) / 1.6 + .15 for m in self.asil]
        self.boy = np.array(boy)
        self.bas = np.concatenate([[0], np.cumsum(self.boy)[:-1]])
        self.top = float(self.boy.sum())
        self.cizim_sn = float(np.clip(self.top * (.16 if self.metin else .11), .5, 3.2))   # uzun cümlede bile elle çizim hızı
        super().begin()

    def interpolate_mobject(self, alpha):
        ilerleme = min(1.0, alpha * max(self.adim_sn, .01) / self.cizim_sn) if alpha < 1 else 1.0
        a, self.uc = ilerleme * self.top, None
        for m, o, L, b in zip(self.yaprak, self.asil, self.boy, self.bas):
            t = float(np.clip((a - b) / L, 0, 1))
            t = 1.0 if t > .999 else t                  # kayan nokta artığı son harfte kontur bırakmasın
            m.pointwise_become_partial(o, 0, t)
            dolgu = o.get_fill_opacity() * float(np.clip(t * 2 - 1, 0, 1))
            m.set_fill(opacity=dolgu, family=False)
            if self.metin:
                m.set_stroke(o.get_fill_color(), width=0 if t >= 1 else 1.6, opacity=1, family=False)
            if 0 < t < 1:
                if self.metin:
                    x = o.get_left()[0] + t * o.width
                    self.uc = P(x, o.get_center()[1] + .35 * o.height * np.sin(t * 3 * PI))
                else:
                    self.uc = o.point_from_proportion(t)


class Defter(Tahta):
    theme = "gece"

    def setup(self):
        super().setup()
        self.zemin = kagit(self.theme)
        self.add(self.zemin)
        self.kalem = kalem(self.theme).shift(UZAK)
        self.kalem_ucu = UZAK.copy()

    # ---- kalem ----
    def _kalemli(self, anim):
        def izle(k, alpha):
            hedef = anim.uc if (anim.uc is not None and alpha < 1) else UZAK
            k.shift(hedef - self.kalem_ucu)
            self.kalem_ucu = np.array(hedef, dtype=float)
        grup = AnimationGroup(anim, UpdateFromAlphaFunc(self.kalem, izle, rate_func=linear))
        grup.adim = lambda sn: setattr(anim, "adim_sn", sn)
        return grup

    def ciz(self, *mobs):
        return self._kalemli(Ciz(mobs[0] if len(mobs) == 1 else VGroup(*mobs)))

    def yaz(self, *mobs):
        return self._kalemli(Ciz(mobs[0] if len(mobs) == 1 else VGroup(*mobs), metin=True))

    # ---- hazır öğeler ----
    def baslik(self, s, saat=None):
        """Sol üstte başlık + fosforlu kalem şeridi; sağ üstte isteğe bağlı zaman damgası. (başlık, damga) döner."""
        t = text(s, self.c["ink"], 38)
        t.move_to(P(-6.5 + t.width / 2, 3.38))
        serit = Rectangle(width=t.width + .35, height=.34, stroke_width=0).set_fill(self.c["yellow"], .28).move_to(P(t.get_center()[0], 3.12))
        serit.set_z_index(-1)
        d = None
        if saat:
            y = text(saat, self.c["red"], 32)
            kutu = sketch(RoundedRectangle(width=y.width + .5, height=.78, corner_radius=.2, color=self.c["red"], stroke_width=4))
            d = VGroup(kutu, y.move_to(kutu)).move_to(P(6.6 - kutu.width / 2, 3.38))
        return VGroup(serit, t), d

    def tara(self, r, pos, renk, ara=.17, aci=PI / 4, w=5, op=.75):
        """Dairenin içini kalemle tarayarak boyar (zikzak çizgiler)."""
        yon, dik = P(np.cos(aci), np.sin(aci)), P(-np.sin(aci), np.cos(aci))
        out = VGroup()
        for k, d in enumerate(np.arange(-r + ara / 2, r, ara)):
            yari = np.sqrt(max(r * r - d * d, 0)) * .96
            a, b = pos + d * dik - yari * yon, pos + d * dik + yari * yon
            if k % 2:
                a, b = b, a
            out.add(Line(a, b, color=self.c[renk], stroke_width=w, stroke_opacity=op))
        return out

    def daire(self, r, pos, renk="ink", w=5):
        return sketch(Circle(r, color=self.c[renk], stroke_width=w), min(.018, r * .04)).move_to(pos)

    def dunya(self, r, pos):
        kitalar = [[(-.55, .35), (-.2, .62), (.1, .4), (-.05, .1), (-.35, .05)], [(.15, -.05), (.55, .1), (.62, -.3), (.3, -.62), (.1, -.35)],
                   [(.35, .55), (.6, .4), (.45, .3)]]
        kara = VGroup(*[sketch(Polygon(*[pos + r * P(*q) for q in k], color=self.c["green"], stroke_width=4).set_fill(self.c["green"], .75))
                        for k in kitalar])
        return VGroup(self.tara(r, pos, "blue", max(.14, r * .13), op=.55), kara, self.daire(r, pos, "blue", 6))

    def ay(self, r, pos):
        krater = VGroup(*[self.daire(r * s, pos + r * P(x, y), "gray", 3) for x, y, s in [(-.35, .3, .22), (.3, -.1, .16), (-.1, -.45, .12), (.35, .45, .09)]])
        return VGroup(self.tara(r, pos, "gray", max(.13, r * .14), aci=PI / 3, op=.5), krater, self.daire(r, pos, "ink", 5))

    def yildizlar(self, n, seed, x=(-6.8, 6.8), y=(-2.8, 2.6)):
        rng = np.random.default_rng(seed)
        g = VGroup()
        for _ in range(n):
            d = Dot(P(rng.uniform(*x), rng.uniform(*y)), radius=rng.uniform(.015, .04), color=self.c["ink"])
            faz = rng.uniform(0, TAU)
            d.t = 0.0

            def kirp(m, dt, faz=faz):                    # hafif göz kırpma
                m.t += dt
                m.set_opacity(.55 + .4 * np.sin(2.2 * m.t + faz))
            d.add_updater(kirp)
            g.add(d)
        return g

    def end(self):
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.zemin and m is not self.kalem], run_time=.6)
