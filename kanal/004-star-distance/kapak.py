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
        return Text(s, font=FONT, color=self.c[renk], font_size=96, weight=BOLD).scale_to_fit_height(h).move_to(pos)


class A(Kapak):                 # parmak, arkasında iki yere atlayan yıldız
    def construct(self):
        self.add(self.yildizlar(90, 4, y=(-4.2, 4.2)))
        a, b = P(1.2, 1.5), P(5.8, 1.5)
        golge = self.yildiz(a, .62).set_opacity(.28)
        ok = CurvedArrow(a + P(.1, 1.2), b + P(-.1, 1.2), color=self.c["red"], stroke_width=20, angle=-PI / 2.6, tip_length=.55)
        el = self.parmak(5.0).scale(1.75).move_to(P(3.5, -3.0))
        for m in el.family_members_with_points():
            if m.get_stroke_width():
                m.set_stroke(width=10)
        self.add(golge, self.yildiz(b, .62), ok, el, self.yazi("HOW", "ink", 1.7, P(-3.9, 1.2)), self.yazi("FAR?", "yellow", 2.1, P(-3.8, -1.2)))


class B(Kapak):                 # yörünge üçgeni
    def construct(self):
        self.add(self.yildizlar(70, 9, y=(-4.2, 4.2)))
        s, uc = P(-1.5, -2.4), P(3.6, 2.6)
        sol, sag = s + P(-3.0, 0), s + P(3.0, 0)
        self.add(Ellipse(width=6, height=1.5, color=self.c["gray"], stroke_width=8).move_to(s),
                 Line(sol, uc, color=self.c["yellow"], stroke_width=14), Line(sag, uc, color=self.c["yellow"], stroke_width=14),
                 Dot(s, radius=.55, color=self.c["yellow"]), Dot(sol, radius=.42, color=self.c["blue"]), Dot(sag, radius=.42, color=self.c["blue"]),
                 self.yildiz(uc, .6), self.yazi("NO RULER", "ink", 1.1, P(-3.2, 2.6)), self.yazi("?", "red", 2.0, P(5.9, .4)))


class C(Kapak):                 # ikiye kesik mercek
    theme = "defter"

    def construct(self):
        o, r = P(3.3, -.1), 2.7

        def yarim(a, kay):
            yay = Arc(radius=r, start_angle=a, angle=PI, arc_center=o, color=self.c["blue"], stroke_width=16)
            g = VMobject(color=self.c["blue"], stroke_width=16).set_points(yay.points).add_points_as_corners([yay.get_start()])
            return g.set_fill(self.c["blue"], .3).shift(kay)
        self.add(yarim(PI / 2, DOWN * .65), yarim(-PI / 2, UP * .65), self.yildiz(o + UP * .85, .5, "#d99a00"), self.yildiz(o + DOWN * .85, .5, "#d99a00"),
                 self.yazi("SPLIT", "red", 1.6, P(-3.6, 1.0)), self.yazi("THE LENS", "ink", 1.05, P(-3.5, -1.1)))
