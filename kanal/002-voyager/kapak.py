"""3 kapak taslağı. (bu klasörde) PYTHONPATH=.. ../.venv/Scripts/python -m manim -s -r 1280,720 kapak.py A B C"""
from manim import *

from sahneler import voyager
from tahta import FONT, P, THEMES

R = THEMES["siyah"]


def yazi(s, color, h, pos):
    return Text(s, font=FONT, color=R[color], font_size=96, weight=BOLD).scale_to_fit_height(h).move_to(pos)


def arac(pos, s):
    v = voyager(P(0, 0), R["blue"], s)
    for m in v.family_members_with_points():
        m.set_stroke(width=14)
    return v.move_to(pos)


class Kapak(Scene):
    def setup(self):
        self.camera.background_color = R["bg"]


class A(Kapak):                 # tek odak: araç ve süre
    def construct(self):
        self.add(arac(P(3.0, .2), 2.6), yazi("1 DAY", "yellow", 1.6, P(-3.5, 1.2)), yazi("AWAY", "ink", 1.2, P(-3.5, -.7)))


class B(Kapak):                 # cetvel: biz burada, o orada
    def construct(self):
        self.add(Line(P(-6.5, -1.2), P(6.5, -1.2), color=R["ink"], stroke_width=12),
                 Dot(P(-6.2, -1.2), radius=.28, color=R["blue"]), yazi("US", "blue", .8, P(-5.9, -2.5)),
                 arac(P(4.9, .45), 1.4), Dot(P(6.2, -1.2), radius=.28, color=R["yellow"]),
                 yazi("HOW FAR?", "yellow", 1.4, P(-1.8, 1.9)))


class C(Kapak):                 # sessizlik
    def construct(self):
        self.add(arac(P(2.9, -.4), 2.3), yazi("SILENT?", "red", 1.5, P(-3.4, 2.2)),
                 *[Arc(radius=r, start_angle=PI * .8, angle=PI * .4, arc_center=P(.7, -.4), color=R["blue"], stroke_width=14) for r in (1.0, 1.8, 2.6)])
