"""Manim denemesi: dönen nokta sinüs dalgası çizer. LaTeX gerekmez.
Çalıştır: .venv/Scripts/manim -qm test_cember.py Cember"""
from manim import *
import numpy as np


class Cember(Scene):
    def construct(self):
        self.camera.background_color = "#14171c"   # siyah tahta
        font = "Segoe Print"
        title = Text("Dönen nokta dalga çizer", font=font, font_size=34).to_edge(UP)
        O, R = np.array([-4.2, -0.3, 0]), 1.7
        start = np.array([-1.6, -0.3, 0])
        circle = Circle(radius=R, color=WHITE).move_to(O)
        axes = VGroup(Line(O + LEFT*2, O + RIGHT*2), Line(O + DOWN*2, O + UP*2),
                      Line(start, start + RIGHT*8)).set_stroke(GREY, 2)
        t = ValueTracker(0)

        def P():
            a = t.get_value()
            return O + R*np.array([np.cos(a), np.sin(a), 0])

        def tip():
            return np.array([start[0] + t.get_value()*8/(2*TAU), P()[1], 0])

        moving = VGroup(
            always_redraw(lambda: Line(O, P(), color=YELLOW, stroke_width=5)),
            always_redraw(lambda: Line([P()[0], O[1], 0], P(), color=RED, stroke_width=7)),
            always_redraw(lambda: Line(O, [P()[0], O[1], 0], color=BLUE, stroke_width=7)),
            always_redraw(lambda: DashedLine(P(), tip(), color=GREY, stroke_width=2)),
            always_redraw(lambda: Dot(P(), color=YELLOW, radius=0.1)),
        )
        wave = TracedPath(tip, stroke_color=RED, stroke_width=5)
        labels = VGroup(Text("sin θ  (yükseklik)", font=font, font_size=26, color=RED),
                        Text("cos θ  (yatay)", font=font, font_size=26, color=BLUE)
                        ).arrange(RIGHT, buff=1).to_edge(DOWN)
        self.play(Write(title), Create(axes), Create(circle), run_time=2)
        t.set_value(0.001)
        self.add(wave, moving)
        self.play(FadeIn(labels), run_time=0.5)
        self.play(t.animate.set_value(2*TAU), run_time=8, rate_func=linear)
        self.wait()
