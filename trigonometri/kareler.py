"""Örnek kareler. Çalıştır: .venv/Scripts/manim -qh -s kareler.py Beyaz Siyah"""
from manim import *
import numpy as np

FONT = "Segoe Print"
THEMES = {
    "beyaz": dict(bg="#fbfaf5", ink="#1f2328", red="#d6453b", blue="#2f6fd6", yellow="#e0a106", green="#2f9a58", gray="#8a8f98"),
    "siyah": dict(bg="#14171c", ink="#f2f2ee", red="#ff6b5e", blue="#58c4dd", yellow="#ffd95a", green="#83c167", gray="#6c727c"),
}


def text(s, color, size=34, **kw):
    # büyük çizip küçültmek harf aralığını düzgün tutar
    return Text(s, font=FONT, color=color, font_size=96, **kw).scale(size / 96)


def sketch(m, amp=0.018, seed=0):
    """Elle çizilmiş hissi: noktaları hafifçe dalgalandırır."""
    for sub in m.family_members_with_points():
        sub.insert_n_curves(24)
        sub.apply_function(lambda p: p + amp * np.array(
            [np.sin(3.1 * p[1] + 2.3 * p[0] + seed), np.sin(2.7 * p[0] - 1.9 * p[1] + seed * 2), 0]))
    return m


def line(a, b, color, width=6, **kw):
    return sketch(Line(a, b, color=color, stroke_width=width, **kw))


def P(x, y):
    return np.array([x, y, 0.0])


class Beyaz(Scene):
    def construct(self):
        c = THEMES["beyaz"]
        self.camera.background_color = c["bg"]
        title = text("Tırmanmadan bir dağın boyunu ölçebilir misin?", c["ink"], 40).to_edge(UP, buff=.45)
        under = line(title.get_corner(DL) + DOWN * .12, title.get_corner(DR) + DOWN * .12, c["yellow"], 9)
        ground = line(P(-6.6, -2.4), P(6.6, -2.4), c["ink"])
        base, top, eye = P(3.2, -2.4), P(3.2, 1.8), P(-3.9, -2.4)
        mountain = sketch(Polygon(P(.4, -2.4), P(2.1, .2), P(2.5, -.1), top, P(4.0, .5), P(4.5, .7), P(6.4, -2.4),
                                  color=c["ink"], stroke_width=6).set_fill("#cfd8e3", .55), .03)
        snow = sketch(Polygon(P(2.72, .55), top, P(3.68, .85), P(3.35, .65), P(3.1, .95), color=c["ink"], stroke_width=4).set_fill(WHITE, 1))
        sight = sketch(DashedLine(eye + UP * .02, top, color=c["red"], stroke_width=6, dash_length=.18))
        height = line(base, top + DOWN * .02, c["blue"], 8)
        dist = DoubleArrow(eye + DOWN * .4, base + DOWN * .4, buff=0, color=c["green"], stroke_width=6, tip_length=.22)
        angle = sketch(Arc(radius=1.2, start_angle=0, angle=np.arctan2(4.2, 7.1), arc_center=eye, color=c["red"], stroke_width=7))
        # çöp adam gözlemci
        h = eye + LEFT * .45
        person = VGroup(sketch(Circle(.27, color=c["ink"], stroke_width=6).move_to(h + UP * 1.2)),
                        line(h + UP * .93, h + UP * .38, c["ink"]), line(h + UP * .38, h + P(-.28, 0), c["ink"]),
                        line(h + UP * .38, h + P(.28, 0), c["ink"]), line(h + UP * .8, h + P(.55, .95), c["ink"]),
                        line(h + UP * .8, h + P(-.35, .45), c["ink"]))
        labels = VGroup(text("açı = 35°", c["red"], 30).move_to(eye + P(2.2, .4)),
                        text("uzaklık: biliniyor", c["green"], 30).move_to(P(-.4, -3.35)),
                        text("boy = ?", c["blue"], 38).move_to(P(5.7, 1.2)))
        pointer = CurvedArrow(P(5.4, .85), P(3.4, -.2), angle=-PI / 3, color=c["blue"], stroke_width=4, tip_length=.2)
        self.add(title, under, mountain, snow, ground, sight, height, dist, angle, person, labels, pointer)


class Siyah(Scene):
    def construct(self):
        c = THEMES["siyah"]
        self.camera.background_color = c["bg"]
        title = text("Üçgen, çemberin içinde yaşıyor", c["ink"], 40).to_edge(UP, buff=.45)
        under = line(title.get_corner(DL) + DOWN * .12, title.get_corner(DR) + DOWN * .12, c["yellow"], 8)
        O, R, a = P(-2.9, -.55), 2.7, 50 * DEGREES
        tip = O + R * P(np.cos(a), np.sin(a))
        foot = P(tip[0], O[1])
        axes = VGroup(line(O + LEFT * 3.4, O + RIGHT * 3.4, c["gray"], 3), line(O + DOWN * 3.1, O + UP * 3.1, c["gray"], 3))
        circle = sketch(Circle(R, color=c["ink"], stroke_width=5).move_to(O), .02)
        fill = Polygon(O, foot, tip, stroke_width=0).set_fill(c["yellow"], .12)
        sides = VGroup(line(O, foot, c["blue"], 10), line(foot, tip, c["red"], 10), line(O, tip, c["yellow"], 8))
        corner = VGroup(line(foot + P(-.25, 0), foot + P(-.25, .25), c["gray"], 3), line(foot + P(-.25, .25), foot + P(0, .25), c["gray"], 3))
        arc = sketch(Arc(radius=.65, start_angle=0, angle=a, arc_center=O, color=c["ink"], stroke_width=4))
        marks = VGroup(Dot(tip, radius=.13, color=c["yellow"]),
                       text("θ", c["ink"], 34).move_to(O + .98 * P(np.cos(a / 2), np.sin(a / 2))),
                       text("1", c["yellow"], 38).move_to((O + tip) / 2 + P(-.3, .25)),
                       text("cos θ", c["blue"], 32).next_to((O + foot) / 2, DOWN, buff=.2),
                       text("sin θ", c["red"], 32).next_to((foot + tip) / 2, RIGHT, buff=.2))
        side = VGroup(text("yatay  =  cos θ", c["blue"], 38), text("dikey  =  sin θ", c["red"], 38),
                      text("sin² θ + cos² θ = 1", c["yellow"], 40),
                      text("(Pisagor, kılık değiştirmiş)", c["gray"], 28)).arrange(DOWN, buff=.55).move_to(P(3.6, -.5))
        box = sketch(SurroundingRectangle(side[2], color=c["yellow"], buff=.25, stroke_width=4))
        self.add(title, under, axes, fill, circle, sides, corner, arc, marks, side, box)
