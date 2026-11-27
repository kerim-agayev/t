"""Şablon: yeni video için bu dosyayı kopyala. TEXT sırası = sahne sırası; sınıf adı = TEXT anahtarı."""
from manim import *

from tahta import P, Tahta, sketch

TEXT = {
    "Space": [
        "This is how we draw the inside of space: on a black board.",
        "One idea at a time, drawn while you hear it.",
    ],
    "Human": [
        "And when we come back to the human scale, the board turns white.",
    ],
}


class Space(Tahta):
    theme = "siyah"

    def construct(self):
        c = self.c
        hole = sketch(Circle(1.1, color=c["ink"], stroke_width=6).set_fill("#000000", 1)).move_to(P(-2.5, 0))
        ring = sketch(Ellipse(width=4.6, height=1.3, color=c["yellow"], stroke_width=9).move_to(P(-2.5, 0)), .03)
        self.say(0, Write(self.title("Inside Space")), [Create(ring), FadeIn(hole)])
        arrow = Arrow(P(2.4, .9), P(-1.3, .5), color=c["blue"], stroke_width=6)
        self.say(1, Create(arrow), Write(self.label("one idea", "blue", P(3.6, 1.2), 40)))
        self.end()


class Human(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        ground = self.ln(P(-6, -2), P(6, -2))
        person = VGroup(sketch(Circle(.35, color=c["ink"], stroke_width=6).move_to(P(-3, -.05))),
                        *[self.ln(P(*a), P(*b)) for a, b in [((-3, -.4), (-3, -1.2)), ((-3, -1.2), (-3.4, -2)), ((-3, -1.2), (-2.6, -2)),
                                                             ((-3, -.6), (-3.6, -1)), ((-3, -.6), (-2.2, -.1))]])
        sun = sketch(Circle(.8, color=c["yellow"], stroke_width=8).move_to(P(3, 1.2)))
        self.say(0, [Write(self.title("Human Scale")), Create(ground)], Create(person), Create(sun))
        self.end()
