"""3 kapak taslağı. (bu klasörde) PYTHONPATH=.. ../.venv/Scripts/python -m manim -s -r 1280,720 kapak.py A B C"""
from manim import *

from sahneler import Sahne
from tahta import FONT, P


class Kapak(Sahne):
    def setup(self):
        super().setup()
        self.camera.frame_center = ORIGIN
        self.zemin.move_to(ORIGIN)

    def yazi(self, s, renk, h, pos):
        return Text(s, font=FONT, color=self.c[renk], font_size=96).scale_to_fit_height(h).set_stroke(self.c[renk], 5).move_to(pos)


class A(Kapak):                 # 65'te duran çark
    def construct(self):
        o = P(3.2, .35)
        dilim, sayi, orta, ibre = self.cark(o, 3.0)
        VGroup(dilim, sayi, orta).rotate(self.hedef_aci(65), about_point=o)
        dilim[5].set_fill(self.c["orange"], 1)
        self.add(dilim, sayi, orta, ibre, self.yazi("PICK A", "ink", 1.45, P(-4.0, 1.3)), self.yazi("NUMBER", "orange", 1.55, P(-3.7, -.7)))


class B(Kapak):                 # aynı soru, iki cevap
    def construct(self):
        self.add(self.yazi("SAME QUESTION", "ink", 1.25, P(0, 3.0)))
        for x, c0, c1, renk in ((-3.9, "10", "25%", "teal"), (3.9, "65", "45%", "orange")):
            capa = self.capa(P(x, -2.4), 1.9, "orange", 12)
            self.add(capa, self.yazi(c0, "ink", .8, P(x - 1.8, -2.4)), self.yazi(c1, renk, 1.9, P(x, .65)),
                     self.halat(capa[0].get_top(), P(x, -.55), sark=.15))
        self.add(self.yazi("≠", "red", 1.2, P(0, .6)))


class C(Kapak):                 # yargıçlar da
    def construct(self):
        yargic = self.adam(P(3.4, -3.5), 2.5)
        for m in yargic.family_members_with_points():
            m.set_stroke(width=14)
        bas = self.kart(2.1, .95, P(5.85, .35), "ink", 9, "orange").rotate(-PI / 4.5)
        sap = self.cizgi(P(5.75, .2), P(4.55, -1.25), "ink", 18, 0)
        d12 = VGroup(self.kart(2.4, 1.6, P(-5.2, -2.1), "teal", 9), self.yazi("12?", "teal", .85, P(-5.2, -2.1)))
        d34 = VGroup(self.kart(2.4, 1.6, P(-2.1, -2.1), "orange", 9), self.yazi("34?", "orange", .85, P(-2.1, -2.1)))
        self.add(yargic, sap, bas, d12, d34, self.yazi("EVEN", "ink", 1.55, P(-3.9, 2.3)), self.yazi("JUDGES", "orange", 1.75, P(-3.4, .35)))
