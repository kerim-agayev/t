"""3 kapak taslağı (1280x720). (bu klasörde) PYTHONPATH=.. ../.venv/Scripts/python -m manim -s -r 1280,720 kapak.py A B C"""
from manim import *

from tahta import FONT, P, THEMES, sketch

R = THEMES["siyah"]


def yazi(s, color, h, pos):
    return Text(s, font=FONT, color=color, font_size=96, weight=BOLD).scale_to_fit_height(h).move_to(pos)


def hole(r, pos, w=14):
    return sketch(Circle(r, color=R["red"], stroke_width=w).set_fill("#000000", 1)).move_to(pos)


class Kapak(Scene):
    def setup(self):
        self.camera.background_color = R["bg"]


class A(Kapak):                       # nokta ile dev
    def construct(self):
        dot = Dot(P(-4.9, -.6), radius=.09, color=R["yellow"])
        self.add(hole(5.2, P(4.6, -.4), 18), dot, Circle(.8, color=R["ink"], stroke_width=6).move_to(dot),
                 yazi("HOW BIG?", R["yellow"], 1.05, P(-3.5, 2.4)))


class B(Kapak):                       # kara delik ve minik Güneş sistemi
    def construct(self):
        mid = P(2.6, 0)
        self.add(hole(3.4, mid, 20), Circle(.8, color=R["blue"], stroke_width=7).move_to(mid), Dot(mid, radius=.07, color=R["yellow"]),
                 Arrow(P(-2.2, -1.5), mid + P(-.75, -.3), color=R["ink"], stroke_width=9, buff=0),
                 yazi("OUR", R["ink"], .85, P(-4.3, -1.1)), yazi("PLANETS", R["ink"], .85, P(-4.3, -2.3)),
                 yazi("TOO BIG?", R["yellow"], .9, P(-3.9, 2.4)))


class C(Kapak):                       # merdiven
    def construct(self):
        x = -6.3
        for r in (.07, .25, .6, 1.2, 2.5):
            x += r
            self.add(hole(r, P(x, -2.4 + r), 6 + r * 4))
            x += r + .55
        self.add(yazi("EVERY SIZE", R["yellow"], .95, P(-3.5, 3.05)))
