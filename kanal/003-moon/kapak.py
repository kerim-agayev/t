"""3 kapak taslağı. (bu klasörde) PYTHONPATH=.. ../.venv/Scripts/python -m manim -s -r 1280,720 kapak.py A B C"""
from manim import *

from kalem import Defter
from tahta import FONT, P


class Kapak(Defter):
    def setup(self):
        super().setup()
        self.camera.frame_center = ORIGIN
        self.zemin.move_to(ORIGIN)

    def yazi(self, s, renk, h, pos):
        return Text(s, font=FONT, color=self.c[renk], font_size=96, weight=BOLD).scale_to_fit_height(h).move_to(pos)

    def kalin(self, g, w):
        for m in g.family_members_with_points():
            if m.get_stroke_width():
                m.set_stroke(width=max(m.get_stroke_width() * 2.2, w))
        return g


class A(Kapak):                 # Ay'ın yerinde boşluk
    def construct(self):
        bos = DashedVMobject(Circle(2.3, color=self.c["ink"], stroke_width=14).move_to(P(3.4, .2)), num_dashes=22)
        self.add(self.kalin(self.dunya(1.5, P(-4.2, -1.5)), 10), bos, self.yazi("?", "yellow", 2.2, P(3.4, .2)),
                 self.yazi("NO MOON", "yellow", 1.05, P(-3.4, 2.3)))


class B(Kapak):                 # devrilen Dünya
    def construct(self):
        g = VGroup(self.kalin(self.dunya(2.4, ORIGIN), 12), Arrow(P(0, 2.4), P(0, 3.9), color=self.c["red"], buff=0, stroke_width=22, max_tip_length_to_length_ratio=.4, max_stroke_width_to_length_ratio=100),
                   Line(P(0, -3.5), P(0, -2.4), color=self.c["red"], stroke_width=22))
        self.add(g.rotate(-62 * DEGREES, about_point=ORIGIN).shift(P(3.2, -.3)), self.yazi("TIP", "ink", 1.7, P(-4.3, 1.0)),
                 self.yazi("OVER?", "red", 1.5, P(-4.1, -1.1)))


class C(Kapak):                 # silinen Ay
    theme = "defter"

    def construct(self):
        self.add(self.kalin(self.ay(2.3, P(3.4, -.2)), 10), Line(P(1.0, -2.6), P(5.9, 2.3), color=self.c["red"], stroke_width=30),
                 self.yazi("GONE", "red", 1.9, P(-3.4, .8)), self.yazi("TONIGHT", "ink", 1.1, P(-3.4, -1.3)))
