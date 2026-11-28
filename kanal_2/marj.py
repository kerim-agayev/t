"""Mind Margins tarzı: çizgili defter, solda kenar boşluğu (izleyicinin notu), çıpa motifi.
Kullanım: class X(Marj): ... Tarz denemesi için ortam değişkeni MARJ_TARZ = kenar | kraft | gece."""
import os
import textwrap
from pathlib import Path

import manimpango
import numpy as np
from manim import *
from mutagen.mp3 import MP3

import kalem
import tahta
from tahta import P, sketch

HERE = Path(__file__).parent
for f in ("PatrickHand-Regular.ttf", "PatrickHandSC-Regular.ttf"):
    manimpango.register_font(str(HERE / "fonts" / f))

TARZ = os.environ.get("MARJ_TARZ", "kenar")
tahta.FONT = {"kenar": "Patrick Hand", "kraft": "Ink Free", "gece": "Patrick Hand SC"}[TARZ]

# renk adları: ink (mürekkep), teal (ana vurgu), orange (çıpa/dikkat), red, gray, card (kart içi), rule (satır)
tahta.THEMES["kenar"] = dict(bg="#F5EEDB", ink="#1F2A44", teal="#1F8A80", orange="#E2741A", red="#C0432F", gray="#7F7B6E",
                             card="#FFFBEF", rule="#A9C3C0")
tahta.THEMES["kraft"] = dict(bg="#C9A97C", ink="#1C1913", teal="#0C514B", orange="#9C3A06", red="#8E1F14", gray="#4F4232",
                             card="#EFE3CB", rule="#A98B62")
tahta.THEMES["gece"] = dict(bg="#0F3836", ink="#F5EEDB", teal="#6FD6C8", orange="#F6A04D", red="#FF8270", gray="#9DB8B2",
                            card="#174845", rule="#2A5C57")
KENAR_X = -5.2                      # kenar boşluğu çizgisi
NOT_X = -6.6                        # kenar notlarının merkezi


def zemin(tarz):
    h, w = 900, 1600
    c = tahta.THEMES[tarz]
    rng = np.random.default_rng(11)
    img = np.array(ManimColor(c["bg"]).to_rgb()) * 255 + rng.normal(0, 1.8 if tarz != "kraft" else 5, (h, w))[..., None]
    kaba = np.kron(rng.normal(0, 1, (h // 20, w // 20)), np.ones((20, 20)))
    img = img + (kaba * (1.1 if tarz != "kraft" else 2.6))[..., None]
    boya = lambda m, renk, a: img.__setitem__(m, img[m] * (1 - a) + np.array(ManimColor(c[renk]).to_rgb()) * 255 * a)
    for y in range(150, h, 60):                                   # satır çizgileri
        boya(np.s_[y:y + 2, :], "rule", .55 if tarz == "kenar" else .45)
    x = int((KENAR_X + 8) * 100)
    boya(np.s_[:, x:x + 3], "orange", .85)                        # çift kenar çizgisi
    boya(np.s_[:, x + 8:x + 10], "orange", .45)
    yy, xx = np.mgrid[0:h, 0:w]
    for cy in (170, 450, 730):                                    # delikler
        d = np.hypot(xx - 32, yy - cy)
        boya(d < 17, "ink", .55 if tarz != "gece" else .12)
    vin = 1 - .13 * (((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) ** 1.5 / 2.8
    rgb = np.clip(img * vin[..., None], 0, 255).astype(np.uint8)
    m = ImageMobject(np.dstack([rgb, np.full((h, w), 255, np.uint8)]))
    m.height = 9.0
    return m.move_to(P(0, -.5)).set_z_index(-100)


class Marj(kalem.Defter):
    theme = TARZ

    def setup(self):
        tahta.Tahta.setup(self)
        self.zemin = zemin(self.theme)
        self.add(self.zemin)
        self.kalem = kalem.kalem("gece" if self.theme == "gece" else "defter").shift(kalem.UZAK)
        self.kalem_ucu = kalem.UZAK.copy()

    # ---- seslendirme ve büyük altyazı ----
    def say(self, i, *steps, extra=0.3):
        name = self.sahne_adi()
        f = Path(self.modul.__file__).parent / "ses" / f"{name}_{i}.mp3"
        dur = MP3(f).info.length
        if self.caption:
            self.remove(self.caption)
        with tempconfig({"pixel_width": 16000}):
            lines = VGroup(*[Text(t, font=tahta.FONT, color=self.c["ink"], font_size=96).scale(34 / 96)
                             for t in textwrap.wrap(self.modul.TEXT[name][i], 70)]).arrange(DOWN, buff=.12)
        lines.move_to(P(0, -4.27))
        back = BackgroundRectangle(lines, color=self.c["card"], fill_opacity=.95, buff=.14)
        self.caption = VGroup(back, lines).set_z_index(10)
        self.add(self.caption)
        self.add_sound(str(f))
        self._zaman(i, dur)
        used = 0
        steps = [list(a) if isinstance(a, (list, tuple)) else [a] for a in steps]
        if steps:                                   # önce eskiler silinsin, yenisi üstlerine binmesin
            cikan = [a for a in steps[0] if isinstance(a, FadeOut)]
            if cikan:
                self.play(*cikan, run_time=.4)
                used = .4
                steps[0] = [a for a in steps[0] if not isinstance(a, FadeOut)]
                steps = [a for a in steps if a]
        pay = (dur * .92 - used) / max(1, len(steps))
        for anims in steps:
            rt = round(pay * 30) / 30
            for x in anims:
                getattr(x, "adim", lambda r: None)(rt)
            self.play(*anims, run_time=rt)
            used += rt
        self.wait(max(1 / 30, dur + extra - used))

    def sahne_adi(self):
        return type(self).__name__

    # ---- hazır öğeler ----
    def t(self, s, size=40, renk="ink", pos=ORIGIN, **kw):
        return tahta.text(s, self.c[renk], size, **kw).move_to(pos)

    def baslik(self, s):
        m = tahta.text(s, self.c["ink"], 54)
        m.move_to(P(-4.7 + m.width / 2, 3.38))
        serit = Rectangle(width=m.width + .3, height=.3, stroke_width=0).set_fill(self.c["orange"], .25)
        serit.move_to(P(m.get_center()[0], 3.06)).set_z_index(-1)
        return VGroup(serit, m)

    def cizgi(self, a, b, renk="ink", w=6, amp=.012):
        return sketch(Line(a, b, color=self.c[renk], stroke_width=w), amp)

    def halka(self, r, pos, renk="ink", w=6):
        return sketch(Circle(r, color=self.c[renk], stroke_width=w), min(.014, r * .04)).move_to(pos)

    def kart(self, w, h, pos, renk="ink", kalin=4, dolgu="card"):
        k = RoundedRectangle(width=w, height=h, corner_radius=.18, color=self.c[renk], stroke_width=kalin)
        return sketch(k.set_fill(self.c[dolgu], 1), .008).move_to(pos)

    def ok(self, a, b, renk="ink", w=6, uc=.24):
        yon = (b - a) / np.linalg.norm(b - a)
        dik = np.array([-yon[1], yon[0], 0])
        return VGroup(self.cizgi(a, b, renk, w), self.cizgi(b - uc * yon + uc * .7 * dik, b, renk, w, 0),
                      self.cizgi(b - uc * yon - uc * .7 * dik, b, renk, w, 0))

    def adam(self, ayak, s=1.0, renk="ink"):
        """Çöp adam; ayak = iki ayağın orta noktası. Boy yaklaşık 2.1*s."""
        parca = [((0, .75), (0, 1.5)), ((0, .75), (-.35, 0)), ((0, .75), (.35, 0)),
                 ((0, 1.32), (-.48, .92)), ((0, 1.32), (.48, .92))]
        g = VGroup(self.halka(.3, P(0, 1.8), renk), *[self.cizgi(P(*a), P(*b), renk) for a, b in parca])
        return g.scale(s, about_point=ORIGIN).shift(ayak)

    def capa(self, pos, s=1.0, renk="orange", w=7):
        """Çıpa simgesi; pos = ortası, boy yaklaşık 1.2*s."""
        r = self.c[renk]
        kol = [self.halka(.13, P(0, .5), renk, w), self.cizgi(P(0, .37), P(0, -.54), renk, w, 0),
               self.cizgi(P(-.27, .2), P(.27, .2), renk, w, 0),
               ArcBetweenPoints(P(-.46, -.12), P(.46, -.12), angle=PI * .95, color=r, stroke_width=w)]
        uclar = [Polygon(P(k * .47, .04), P(k * .56, -.18), P(k * .37, -.16), color=r, stroke_width=3).set_fill(r, 1) for k in (-1, 1)]
        return VGroup(*kol, *uclar).scale(s, about_point=ORIGIN).shift(pos)

    def igne(self, pos, renk="teal"):
        """Tahmin iğnesi; ucu pos noktasında."""
        return VGroup(Line(pos, pos + P(0, .42), color=self.c[renk], stroke_width=7),
                      Dot(pos + P(0, .52), radius=.16, color=self.c[renk]))

    def halat(self, a, b, renk="orange", sark=.35):
        orta = (a + b) / 2 + P(0, -sark)
        return CubicBezier(a, orta, orta, b, color=self.c[renk], stroke_width=5)

    def cetvel(self, y, x0=-3.9, x1=6.9, ust=100, adim=10, yazilan=(0, 50, 100)):
        def X(v):
            return P(x0 + (x1 - x0) * v / ust, y)
        g = VGroup(self.cizgi(X(0), X(ust), "ink", 5, .006))
        for v in range(0, ust + 1, adim):
            g.add(self.cizgi(X(v) + P(0, -.12), X(v) + P(0, .12), "ink", 4, 0))
        etiket = VGroup(*[self.t(str(v), 28, "gray", X(v) + P(0, -.42)) for v in yazilan])
        return g, etiket, X

    def kenar_notu(self, satirlar, y=.4, renk="ink", acik=-.04):
        """Kenar boşluğundaki yapışkan not (izleyicinin cevabı)."""
        yazi = VGroup(*[tahta.text(s, self.c[renk], 36) for s in satirlar]).arrange(DOWN, buff=.18)
        if yazi.width > 1.95:
            yazi.scale_to_fit_width(1.95)
        kutu = self.kart(2.3, yazi.height + .55, ORIGIN, "orange", 4)
        return VGroup(kutu, yazi).rotate(acik).move_to(P(NOT_X + .05, y))

    def geri_say(self, sn, pos):
        """İzleyiciye düşünme süresi: halka içinde geri sayım."""
        for k in range(sn, 0, -1):
            rakam = self.t(str(k), 64, "orange", pos)
            halka = Circle(.62, color=self.c["orange"], stroke_width=8).move_to(pos)
            self.add(rakam, halka)
            self.play(Uncreate(halka), run_time=1, rate_func=linear)
            self.remove(rakam, halka)
