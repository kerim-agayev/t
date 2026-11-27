"""Video 2: The Farthest Thing Humans Ever Sent (Voyager 1). Kaynaklar ARASTIRMA.md.
(kanal/ içinde) .venv/Scripts/python render.py 002-voyager taslak"""
from manim import *
import numpy as np

from tahta import P, Tahta, sketch

TEXT = {
    "Hook": [
        "Right now, the farthest thing humans have ever made may still be calling home. But the call is empty.",
        "In November twenty twenty-six, days before a historic milestone, Voyager 1 stopped sending its data. A bare radio signal kept arriving.",
        "Then, on November eighteenth, it became the first spacecraft ever to be one full light-day from Earth.",
        "One day, at the speed of light. But how far is that, really? And is it far at all?",
    ],
    "LightRuler": [
        "To feel it, we need a ruler. Ours is light, the fastest thing there is.",
        "Light covers about three hundred thousand kilometers every second.",
        "From Earth to the Moon, it needs about one point three seconds.",
        "From the Sun to Earth, a little over eight minutes.",
        "Now stretch the ruler to one whole day. Everything you just heard is squeezed into this tiny corner.",
        "Voyager 1 is at the other end, about twenty-six billion kilometers away. To get there, it has been flying for forty-nine years.",
    ],
    "Launch": [
        "Rewind to nineteen seventy-seven. NASA had a rare chance.",
        "The outer planets were lining up in a way that happens only about once every one hundred and seventy-five years.",
        "A spacecraft could swing past one planet and use its gravity to hurry on to the next, like a slingshot.",
        "That trick could cut a flight to Neptune from thirty years to twelve.",
        "So two probes set out. Voyager 2 left first. Voyager 1 followed sixteen days later, on September fifth.",
        "But it was on a faster path. By December, it had overtaken its twin.",
    ],
    "Jupiter": [
        "Its first stop was Jupiter, in March nineteen seventy-nine. On our ruler, that is only about forty-three minutes from the Sun.",
        "There, the Voyagers saw something never before seen on another world: active volcanoes.",
        "They were on Io, a moon of Jupiter. Some plumes rose more than three hundred kilometers high.",
        "Voyager 1 also helped reveal a faint ring around Jupiter. Then it used the giant's pull to race on toward Saturn.",
    ],
    "Titan": [
        "Saturn came in November nineteen eighty, about seventy-nine light-minutes from the Sun.",
        "But here came a choice. Voyager 1 could pass close to Saturn's largest moon, Titan, at a price.",
        "The Titan flyby bent its path northward, up and out of the plane where the planets travel.",
        "So it would never visit Uranus or Neptune. Only its twin went on to see them.",
        "Neptune, the farthest planet, is only about four light-hours from the Sun. Voyager 1 was headed far beyond that.",
    ],
    "PaleDot": [
        "In nineteen ninety, about six billion kilometers from the Sun, Voyager 1 turned its camera back toward home.",
        "It took a family portrait of the solar system.",
        "In that picture, Earth is a point of light, about one pixel in size.",
        "Every person alive that day was on that dot.",
        "After that, its cameras were switched off for good.",
        "And all of that was only about five and a half hours up our ruler.",
    ],
    "Bubble": [
        "The Sun blows a constant wind of particles, which inflates a giant bubble around the planets.",
        "For more than two more decades, Voyager 1 flew toward the edge of that bubble.",
        "On August twenty-fifth, twenty twelve, about seventeen light-hours out, it crossed into interstellar space.",
        "Nobody knew for certain that day. Confirmation came almost a year later, from waves in the gas around it.",
        "It had left the Sun's bubble. But, as you will see, it has not left the solar system.",
    ],
    "Repairs": [
        "Keeping it alive is its own adventure. Its computers handle about eight thousand instructions per second. Your phone handles billions.",
        "In late twenty twenty-three, it began sending data that nobody could read.",
        "Engineers traced it to what looked like a failed memory chip, and worked around it. By June twenty twenty-four, the science was flowing again.",
        "In twenty twenty-five, they even revived thrusters that had not worked since two thousand four.",
        "But power is running out. Its nuclear power source loses about four watts every year.",
        "So instruments go dark, one by one. By April twenty twenty-six, only two science instruments were still on.",
    ],
    "Quiet": [
        "And distance makes every fix painfully slow. A command now takes a full day to reach it.",
        "The answer needs another day to come back. Ask on Monday, and you hear the reply on Wednesday.",
        "That is the challenge right now. On November fourteenth, twenty twenty-six, the team found that the data had stopped.",
        "A carrier signal still reached the giant dishes on Earth. So the spacecraft was still transmitting.",
        "As this video was made, engineers did not yet know the cause. They said finding it could take weeks or longer.",
    ],
    "BigScale": [
        "So here is the real question. After forty-nine years, how far has it actually gone?",
        "Let this one square be a light-day: the whole gap between Voyager 1 and us.",
        "This is one light-year. Three hundred and sixty-five of those squares.",
        "At about seventeen kilometers per second, a single light-year takes Voyager nearly eighteen thousand years.",
        "It should reach the inner edge of the Oort cloud, a vast swarm of icy bodies, in about three hundred years. Getting past it may take thirty thousand.",
        "In about forty thousand years, it will pass a star called Gliese 445, still one point seven light-years away. It will not stop there.",
    ],
    "Record": [
        "Long before then, it will have gone silent. But it carries one more message.",
        "On its side is a golden record, thirty centimeters wide.",
        "It holds greetings in fifty-five languages, one hundred and fifteen images, and about ninety minutes of music.",
        "There is surf, wind, thunder, and the songs of whales.",
        "Nobody may ever play it. We sent it anyway.",
    ],
    "End": [
        "So here is the whole ruler. The Moon, the Sun, the planets, the pale blue dot, the edge of the bubble, and now, one light-day.",
        "Nothing we built has ever traveled farther. And on the scale of the stars, it has barely stepped outside.",
        "If you could add one thing to that golden record, what would it be? Tell me in the comments.",
        "Next time, something much closer to home: what would happen if the Moon disappeared?",
    ],
}

# ElevenLabs v4 duygu etiketleri (yalnız ses)
DUYGU = {
    "Hook_0": "[mysterious]", "Hook_2": "[amazed]", "Hook_3": "[curious]",
    "LightRuler_0": "[warmly]", "LightRuler_4": "[amazed]",
    "Launch_0": "[excited]", "Launch_5": "[playfully]",
    "Jupiter_1": "[amazed]",
    "Titan_1": "[serious]", "Titan_3": "[wistful]",
    "PaleDot_2": "[softly]", "PaleDot_3": "[softly]",
    "Bubble_2": "[excited]",
    "Repairs_0": "[amused]", "Repairs_3": "[impressed]", "Repairs_4": "[serious]",
    "Quiet_2": "[serious]", "Quiet_4": "[thoughtful]",
    "BigScale_0": "[curious]", "BigScale_2": "[amazed]", "BigScale_5": "[thoughtful]",
    "Record_0": "[softly]", "Record_3": "[warmly]", "Record_4": "[softly]",
    "End_1": "[thoughtful]", "End_2": "[warmly]", "End_3": "[excited]",
}

META = {
    "baslik": "The Farthest Thing Humans Ever Sent",
    "notlar": """- İzleyici: uzayı merak eden, fizik bilmeyen İngilizce izleyici.
- Büyük soru: Bir ışık günü gerçekte ne kadar uzak, ve bu "uzak" mı?
- Tür: Ö (gerçek ölçek). Tek referans: **ışık cetveli** (0-24 ışık saati, doğrusal); her durakta aynı cetvel.
- Omurga: VE-AMA-BU YÜZDEN. 49 yıldır uçuyor ve bir ışık günü uzakta, ama yıldız ölçeğinde bu çok az; bu yüzden mesajını yanında taşıyor.
- Kanca: seçilen "boş çağrı" (güncel olay). Elenen: "mesaj bir günde gidiyor" (zirveden önce söylenir), "altın plak" (sona saklandı).
- Döngü defteri: boş sinyal (Hook -> Quiet, **açık olduğu dürüstçe söylenir**); "ne kadar uzak?" (Hook -> BigScale).
- Zirve: 1 kare / 365 kare. Bitiş: tüm cetvel, izleyiciye soru, video 3 köprüsü.
- **Yayından önce:** veri kesintisinin son durumunu kontrol et (Quiet ve Hook sahneleri 2026-11-27 durumunu anlatır).""",
}

SAHNE = {
    "Hook": ("The empty call", "siyah", "Voyager, boş sinyal dalgaları, 1 ışık günü", "AÇ: sinyal; AÇ: ne kadar uzak?"),
    "LightRuler": ("A ruler made of light", "beyaz", "Ay, Güneş, 24 saatlik cetvel", "bu yüzden cetvel; Voyager öbür uçta"),
    "Launch": ("A rare chance, 1977", "beyaz", "gezegen dizilişi, sapan yolu, iki araç", "oraya nasıl gitti?"),
    "Jupiter": ("Volcanoes at Jupiter", "siyah", "Jüpiter, Io püskürmesi, halka", "bu yüzden Satürn'e"),
    "Titan": ("The Titan choice", "siyah", "yol yukarı kıvrılır, Uranüs/Neptün geride", "ama bedeli vardı"),
    "PaleDot": ("The pale blue dot", "siyah", "geri bakan araç, tek piksel", "ve bu yalnız 5,5 saat"),
    "Bubble": ("Leaving the bubble", "siyah", "güneş rüzgârı balonu, sınır geçişi", "ama sistemden çıkmadı"),
    "Repairs": ("Keeping it alive", "beyaz", "çip, iticiler, güç çubuğu", "ama güç bitiyor"),
    "Quiet": ("A two-day conversation", "siyah", "giden-gelen sinyal, takvim, çanak", "KAPAT: boş sinyal (henüz çözülmedi)"),
    "BigScale": ("How far is it, really?", "siyah", "1 kare ve 365 kare, Oort, Gliese 445", "ZİRVE, KAPAT: ne kadar uzak?"),
    "Record": ("The golden record", "beyaz", "altın plak ve içindekiler", "ama yanında mesaj var"),
    "End": ("The whole ruler", "siyah", "tüm duraklar tek cetvelde", "izleyiciye soru; video 3"),
}

K = "#000000"
Y = -2.4                                   # cetvel yüksekliği


def x_of(saat):
    return -6 + 12 * saat / 24


def voyager(pos, color, s=1.0):
    parts = [sketch(Arc(radius=.62, start_angle=PI * .5, angle=PI, color=color, stroke_width=6)),
             sketch(Line(P(0, .62), P(0, -.62), color=color, stroke_width=6)),
             sketch(Square(.42, color=color, stroke_width=5).move_to(P(.28, 0))),
             sketch(Line(P(.45, .15), P(1.6, .8), color=color, stroke_width=4)),
             sketch(Line(P(.45, -.15), P(1.3, -.75), color=color, stroke_width=4)),
             sketch(Line(P(-.62, 0), P(-.95, 0), color=color, stroke_width=4))]
    parts += [Square(.17, color=color, stroke_width=4).move_to(P(*q)).rotate(a) for q, a in [((1.6, .8), .45), ((.9, -.5), -.65), ((1.3, -.75), -.65)]]
    return VGroup(*parts).scale(s, about_point=ORIGIN).shift(pos)


def waves(pos, color, n=3, left=True):
    a0 = PI * .75 if left else -PI * .25
    return VGroup(*[Arc(radius=.5 + .45 * i, start_angle=a0, angle=PI * .5, arc_center=pos, color=color, stroke_width=5) for i in range(n)])


def disc(r, pos, color, fill=.35, w=5):
    return sketch(Circle(r, color=color, stroke_width=w).set_fill(color, fill), min(.018, r * .04)).move_to(pos)


def stars(n, seed, color, x=(-6.8, 6.8), y=(-3.0, 2.7)):
    rng = np.random.default_rng(seed)
    return VGroup(*[Dot(P(rng.uniform(*x), rng.uniform(*y)), radius=rng.uniform(.012, .035), color=color) for _ in range(n)])


class Cetvel(Tahta):
    """Her durakta aynı doğrusal ışık cetveli: 0-24 saat."""

    def axis(self):
        c = self.c
        g = VGroup(self.ln(P(-6, Y), P(6, Y), "ink", 5))
        for h in (0, 6, 12, 18, 24):
            g.add(Line(P(x_of(h), Y - .12), P(x_of(h), Y + .12), color=c["ink"], stroke_width=4),
                  self.label(f"{h} h", "gray", P(x_of(h), Y - .45), 22))
        return g

    def mark(self, saat, text, color="yellow", up=.75, size=28):
        x = x_of(saat)
        lab = self.label(text, color, P(float(np.clip(x, -4.9, 4.9)), Y + up), size)
        return VGroup(Dot(P(x, Y), radius=.11, color=self.c[color]),
                      Line(P(x, Y + .1), P(x, max(Y + .12, lab.get_bottom()[1] - .08)), color=self.c[color], stroke_width=3), lab)


class Hook(Tahta):
    def construct(self):
        c = self.c
        sky = stars(80, 2, c["gray"])
        v = voyager(P(3.6, .7), c["blue"], 1.3)
        w = waves(P(2.2, .7), c["blue"])
        self.add(sky)
        self.say(0, [FadeIn(v)], Create(w))
        empty = self.label("data: [          ]", "ink", P(-3.4, 1.7), 40)
        carrier = FunctionGraph(lambda x: .22 * np.sin(8 * x), x_range=[-5.8, -1], color=c["blue"], stroke_width=4).shift(UP * .4)
        self.say(1, Write(empty), Create(carrier))
        day = self.label("18 NOV 2026\n1 LIGHT-DAY", "yellow", P(-3.4, -1.5), 46)
        line = DashedLine(P(-6.5, -2.9), P(6.5, -2.9), color=c["yellow"], stroke_width=5)
        self.say(2, Write(day), Create(line))
        q = self.label("how far is that?", "red", P(2.8, -1.8), 46)
        self.say(3, [FadeOut(empty, carrier, w)], Write(q))
        self.end()


class LightRuler(Cetvel):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("A ruler made of light")
        beam = Arrow(P(-5.5, 1.3), P(5.5, 1.3), color=c["yellow"], stroke_width=9, buff=0)
        self.say(0, Write(t), GrowArrow(beam))
        speed = self.label("≈ 300,000 km every second", "ink", P(0, 2.1), 34)
        self.say(1, Write(speed))
        earth, moon = disc(.5, P(-4.4, -.3), c["blue"]), disc(.18, P(-1.6, -.3), c["gray"], .6)
        m = self.label("Moon: 1.3 s", "ink", P(-3.0, -1.35), 30)
        self.say(2, [FadeIn(earth, moon)], [Create(DashedLine(P(-3.85, -.3), P(-1.8, -.3), color=c["yellow"])), Write(m)])
        sun = disc(.9, P(4.6, -.3), c["yellow"], .8)
        s = self.label("Sun → Earth: 8 min", "ink", P(1.8, -1.35), 30)
        self.say(3, FadeIn(sun), Write(s))
        axis = self.axis()
        corner = self.mark(.14, "Moon + Sun-Earth: here", "red", 1.5)
        self.say(4, [FadeOut(*[x for x in self.mobjects if x not in (t, self.caption)])], Create(axis), FadeIn(corner))
        now = self.mark(24, "Voyager 1\n≈ 26 billion km", "blue", 1.7, 30)
        v = voyager(P(3.6, 1.2), c["blue"], .9)
        years = self.label("≈ 49 years of flight", "blue", P(-1.2, 1.2), 34)
        self.say(5, [FadeIn(now), FadeIn(v)], Write(years))
        self.end()


class Launch(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("1977: a rare chance")
        sun = disc(.35, P(-6, -1.6), c["yellow"], .9)
        self.say(0, Write(t), FadeIn(sun))
        pts = [(-3.6, -.9, .45, "red", "Jupiter"), (-.6, .2, .4, "yellow", "Saturn"), (2.4, 1.0, .28, "green", "Uranus"), (5.3, 1.5, .28, "blue", "Neptune")]
        planets = VGroup(*[VGroup(disc(r, P(x, y), c[col]), self.label(n, "ink", P(x, y - r - .35), 26)) for x, y, r, col, n in pts])
        rare = self.label("once every ≈ 175 years", "red", P(-3.3, 2.2), 32)
        self.say(1, LaggedStartMap(FadeIn, planets), Write(rare))
        path = VMobject(color=c["ink"], stroke_width=5).set_points_smoothly(
            [P(-6, -1.6), P(-3.7, -.15), P(-.7, 1.0), P(2.3, 1.75), P(5.6, 2.35)])
        probe = Dot(P(-6, -1.6), radius=.14, color=c["ink"])
        self.say(2, [Create(path)], MoveAlongPath(probe, path))
        trick = self.label("to Neptune: 30 years → 12", "green", P(2.6, -1.4), 34)
        self.say(3, Write(trick))
        a, b = voyager(P(-1.7, -2.2), c["gray"], .7), voyager(P(1.4, -2.2), c["blue"], .7)
        la = self.label("V2 · 20 Aug", "gray", P(-1.5, -3.2), 26)
        lb = self.label("V1 · 5 Sep", "blue", P(1.6, -3.2), 26)
        self.say(4, [FadeOut(trick), FadeIn(a), Write(la)], [FadeIn(b), Write(lb)])
        self.say(5, [VGroup(a, la).animate.shift(RIGHT * .6), VGroup(b, lb).animate.shift(RIGHT * 3.9)])
        self.end()


class Jupiter(Cetvel):
    def construct(self):
        c = self.c
        t = self.title("March 1979: Jupiter")
        axis = self.axis()
        jup = disc(1.5, P(-3.6, .8), c["red"], .35)
        bands = VGroup(*[self.ln(P(-3.6 - w, .8 + dy), P(-3.6 + w, .8 + dy), "yellow", 4) for dy, w in [(-.6, 1.3), (0, 1.45), (.6, 1.3)]])
        m = self.mark(.72, "43 light-minutes", "yellow", .75)
        self.say(0, [Write(t), FadeIn(jup, bands), Create(axis)], FadeIn(m))
        io = disc(.75, P(2.6, .3), c["yellow"], .55)
        name = self.label("Io", "ink", P(2.6, -.8), 36)
        plume = VGroup(*[ArcBetweenPoints(P(2.6, 1.05), P(2.6 + dx, .9), angle=-np.sign(dx) * PI * .75, color=c["ink"], stroke_width=4) for dx in (-1.2, -.7, .7, 1.2)])
        self.say(1, [FadeIn(io), Write(name)], Create(plume))
        high = DoubleArrow(P(4.4, 1.05), P(4.4, 2.1), color=c["red"], buff=0, stroke_width=5)
        h = self.label("> 300 km", "red", P(5.6, 1.6), 32)
        self.say(2, Create(high), Write(h))
        ring = Ellipse(width=4.6, height=.9, color=c["blue"], stroke_width=4).move_to(P(-3.6, .8)).rotate(.18)
        go = Arrow(P(-1.2, -.9), P(5.8, -.9), color=c["blue"], buff=0, stroke_width=6)
        s = self.label("to Saturn", "blue", P(5.0, -1.35), 28)
        self.say(3, [FadeOut(io, name, plume, high, h), Create(ring)], [GrowArrow(go), Write(s)])
        self.end()


class Titan(Cetvel):
    def construct(self):
        c = self.c
        t = self.title("November 1980: Saturn and Titan")
        axis = self.axis()
        sat = VGroup(disc(.9, P(-3.8, .1), c["yellow"], .4), Ellipse(width=3.3, height=.75, color=c["yellow"], stroke_width=5).rotate(.25).move_to(P(-3.8, .1)))
        m = self.mark(1.32, "79 light-minutes", "yellow", .75)
        self.say(0, [Write(t), FadeIn(sat), Create(axis)], FadeIn(m))
        titan = disc(.3, P(-.9, -.2), c["red"], .7)
        tl = self.label("Titan", "red", P(-.9, -.85), 28)
        self.say(1, FadeIn(titan), Write(tl))
        plane = DashedLine(P(-6.6, -.2), P(6.6, -.2), color=c["gray"], stroke_width=3)
        pl = self.label("plane of the planets", "gray", P(4.8, -.95), 24)
        path = VMobject(color=c["blue"], stroke_width=6).set_points_smoothly([P(-6.4, -.4), P(-3.4, -1.0), P(-1.0, -.55), P(.4, .5), P(2.0, 2.4)])
        self.say(2, [Create(plane), Write(pl)], Create(path))
        u, n = disc(.28, P(2.6, -.2), c["green"]), disc(.28, P(5.2, -.2), c["blue"])
        ul = self.label("Uranus   Neptune\nonly Voyager 2", "ink", P(3.9, .75), 28)
        self.say(3, [FadeIn(u, n)], Write(ul))
        m2 = self.mark(4.2, "Neptune: 4 light-hours", "blue", .7, 26)
        self.say(4, [FadeOut(m), FadeIn(m2)])
        self.end()


class PaleDot(Cetvel):
    def construct(self):
        c = self.c
        t = self.title("14 February 1990")
        sky = stars(60, 8, c["gray"], y=(-.8, 2.6))
        v = voyager(P(4.6, .6), c["blue"], 1.0)
        d = self.label("≈ 6 billion km from the Sun", "ink", P(1.0, 2.4), 30)
        self.say(0, [Write(t), FadeIn(sky, v)], Write(d))
        frame = Rectangle(width=5.6, height=3.4, color=c["ink"], stroke_width=5).move_to(P(-3.4, .5))
        look = DashedLine(P(3.6, .6), P(-.6, .5), color=c["blue"])
        self.say(1, [FadeOut(sky, d), Create(look)], Create(frame))
        bands = VGroup(*[Line(P(-5.8 + dx, -1.1), P(-4.2 + dx, 2.1), color=col, stroke_width=26, stroke_opacity=.14)
                         for dx, col in [(.4, c["yellow"]), (1.8, c["red"]), (3.0, c["gray"])]])
        dot = Square(.12, color=c["blue"], stroke_width=0).set_fill(c["blue"], 1).move_to(P(-3.15, .55))
        circ = Circle(.45, color=c["yellow"], stroke_width=4).move_to(dot)
        px = self.label("Earth ≈ 1 pixel", "yellow", P(2.0, 1.8), 36)
        self.say(2, [FadeIn(bands, dot)], [Create(circ), Write(px)])
        us = self.label("all of us", "blue", P(1.6, -.1), 36)
        self.say(3, [Write(us), Indicate(dot, scale_factor=3)])
        off = self.label("camera: OFF", "red", P(4.6, -.7), 34)
        self.say(4, Write(off))
        axis = self.axis()
        m = self.mark(5.56, "only 5.5 light-hours", "yellow", .75)
        self.say(5, [Create(axis)], FadeIn(m))
        self.end()


class Bubble(Cetvel):
    def construct(self):
        c = self.c
        t = self.title("The Sun's bubble")
        centre = P(-3.2, .4)
        sun = disc(.45, centre, c["yellow"], .9)
        wind = VGroup(*[Arrow(centre + .65 * P(np.cos(a), np.sin(a)), centre + 1.7 * P(np.cos(a), np.sin(a)), color=c["yellow"], buff=0, stroke_width=4)
                        for a in np.linspace(0, TAU, 10, endpoint=False)])
        bubble = sketch(Circle(2.25, color=c["blue"], stroke_width=6)).move_to(centre)
        self.say(0, [Write(t), FadeIn(sun)], LaggedStartMap(GrowArrow, wind), Create(bubble))
        probe = Dot(centre + P(.8, 0), radius=.16, color=c["ink"])
        self.say(1, probe.animate.move_to(centre + P(2.25, 0)))
        out = self.label("25 August 2012\ninterstellar space", "ink", P(3.4, 1.8), 36)
        axis = self.axis()
        m = self.mark(16.9, "17 light-hours", "blue", .75)
        self.say(2, [probe.animate.move_to(centre + P(4.6, 0)), Write(out)], [Create(axis), FadeIn(m)])
        wav = FunctionGraph(lambda x: .2 * np.sin(11 * x), x_range=[.2, 3.6], color=c["green"], stroke_width=4).shift(DOWN * .55)
        conf = self.label("confirmed ≈ 1 year later", "green", P(4.2, -1.1), 28)
        self.say(3, Create(wav), Write(conf))
        still = self.label("out of the bubble, not out of the solar system", "red", P(3.0, 1.8), 26)
        self.play(FadeOut(out), run_time=.4)
        self.say(4, Write(still))
        self.end()


class Repairs(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("Keeping it alive")
        a = self.label("Voyager: ≈ 8,000\ninstructions / second", "blue", P(-3.6, 1.6), 34)
        b = self.label("your phone:\nbillions", "ink", P(3.6, 1.6), 34)
        self.say(0, [Write(t), Write(a)], Write(b))
        chip = VGroup(sketch(Square(1.7, color=c["ink"], stroke_width=6)),
                      *[Line(P(x, s * .85), P(x, s * 1.2), color=c["ink"], stroke_width=5) for x in (-.5, 0, .5) for s in (-1, 1)]).move_to(P(-3.6, -.9))
        junk = self.label("#?@ 0x%$ ??", "red", P(1.4, -.4), 44)
        self.say(1, [FadeOut(a, b), FadeIn(chip)], Write(junk))
        cross = Cross(chip[0], stroke_color=c["red"], stroke_width=8).scale(.6)
        ok = self.label("June 2024: science is back", "green", P(1.9, -1.6), 36)
        self.say(2, Create(cross), [FadeOut(junk), Write(ok)])
        v = voyager(P(-3.2, .1), c["blue"], 1.5)
        puff = VGroup(*[Line(P(-4.8, y), P(-5.9, y + dy), color=c["red"], stroke_width=7) for y, dy in [(.1, 0), (.35, .35), (-.15, -.35)]])
        th = self.label("thrusters: idle since 2004\nrevived 2025", "ink", P(2.8, .3), 34)
        self.say(3, [FadeOut(chip, cross, ok), FadeIn(v)], [Create(puff), Write(th)])
        bar = Rectangle(width=8, height=.7, color=c["ink"], stroke_width=5).move_to(P(0, -1.9))
        fill = Rectangle(width=7.8, height=.5, stroke_width=0).set_fill(c["green"], .9).move_to(P(0, -1.9))
        watt = self.label("power: − ≈ 4 W every year", "red", P(0, -2.75), 34)
        self.say(4, [FadeOut(puff, th), Create(bar), FadeIn(fill)], [fill.animate.stretch(.35, 0, about_edge=LEFT).set_fill(c["red"], .9), Write(watt)])
        names = ["cameras", "particles", "plasma", "magnetometer", "plasma waves"]
        lamps = VGroup(*[VGroup(disc(.28, P(-5.4 + 2.7 * i, 1.8), c["green"], .9), self.label(n, "ink", P(-5.4 + 2.7 * i, 1.15), 24)) for i, n in enumerate(names)])
        two = self.label("2 science instruments still on (April 2026)", "ink", P(0, -.2), 34)
        self.play(FadeOut(v), run_time=.4)
        self.say(5, [FadeIn(lamps)], [*[lamps[i][0].animate.set_color(c["gray"]) for i in range(3)], Write(two)])
        self.end()


class Quiet(Tahta):
    def construct(self):
        c = self.c
        t = self.title("A two-day conversation")
        dish = VGroup(sketch(Arc(radius=1.4, start_angle=PI * .72, angle=PI * .56, color=c["ink"], stroke_width=8, arc_center=P(-4.1, .6))),
                      self.ln(P(-5.5, .6), P(-4.7, .6), "ink", 4), self.ln(P(-5.45, .45), P(-5.45, -1.0), "ink", 6),
                      self.ln(P(-6.0, -1.0), P(-4.9, -1.0), "ink", 6))
        v = voyager(P(4.8, .6), c["blue"], 1.0)
        cmd = Dot(P(-4.3, 1.0), radius=.18, color=c["yellow"])
        l1 = self.label("command: 1 day →", "yellow", P(-.2, 1.8), 36)
        self.say(0, [Write(t), FadeIn(dish, v)], [cmd.animate.move_to(P(3.4, 1.0)), Write(l1)])
        ans = Dot(P(3.4, .2), radius=.18, color=c["blue"])
        l2 = self.label("← reply: 1 day", "blue", P(-.2, -.35), 36)
        week = self.label("Mon: ask      Wed: answer", "ink", P(-.2, -1.7), 40)
        self.say(1, [ans.animate.move_to(P(-4.3, .2)), Write(l2)], Write(week))
        d = self.label("14 November 2026: data stopped", "red", P(0, -2.75), 34)
        self.say(2, [FadeOut(cmd, ans, l1, l2, week), Write(d)])
        carrier = FunctionGraph(lambda x: .25 * np.sin(9 * x), x_range=[-4.3, 3.3], color=c["blue"], stroke_width=4).shift(UP * .6)
        cl = self.label("carrier signal: still there", "blue", P(-.4, 1.6), 32)
        self.say(3, Create(carrier), Write(cl))
        q = self.label("cause: ?   (late November 2026)", "yellow", P(-.2, -1.3), 40)
        self.say(4, Write(q))
        self.end()


class BigScale(Tahta):
    def construct(self):
        c = self.c
        t = self.title("How far is it, really?")
        yrs = self.label("49 years", "blue", P(0, .2), 70)
        self.say(0, Write(t), Write(yrs))
        cells = VGroup(*[Square(.2, color=c["gray"], stroke_width=2).move_to(P(-6.2 + .27 * (i % 25), 2.3 - .27 * (i // 25))) for i in range(365)])
        one = Square(2.4, color=c["yellow"], stroke_width=6).set_fill(c["yellow"], .9).move_to(P(0, .1))
        l1 = self.label("1 light-day\n= Voyager's distance", "yellow", P(4.2, 1.5), 32)
        self.say(1, [FadeOut(yrs), FadeIn(one)], Write(l1))
        target = cells[0].copy().set_stroke(c["yellow"]).set_fill(c["yellow"], 1)
        l2 = self.label("1 light-year\n= 365 squares", "ink", P(4.2, -.2), 32)
        self.say(2, Transform(one, target), [LaggedStartMap(FadeIn, cells[1:]), Write(l2)])
        l3 = self.label("≈ 18,000 years\nper light-year", "red", P(4.2, -1.9), 36)
        self.say(3, Write(l3), Indicate(one, scale_factor=3))
        centre = P(-3.0, -.2)
        sun = disc(.14, centre, c["yellow"], 1)
        rng = np.random.default_rng(4)
        oort = VGroup(*[Dot(centre + r * P(np.cos(a), np.sin(a)), radius=.025, color=c["blue"])
                        for r, a in zip(rng.uniform(1.4, 2.6, 420), rng.uniform(0, TAU, 420))])
        o1 = self.label("inner edge: ≈ 300 years", "ink", P(3.4, 1.4), 32)
        o2 = self.label("beyond it: ≈ 30,000 years", "blue", P(3.4, .5), 32)
        self.play(FadeOut(cells, one, l1, l2, l3), run_time=.5)
        self.say(4, FadeIn(sun, oort), Write(o1), Write(o2))
        star = Star(5, outer_radius=.35, color=c["yellow"]).set_fill(c["yellow"], 1).move_to(P(5.6, -1.2))
        path = DashedLine(centre, P(5.0, -2.5), color=c["ink"])
        gap = DashedLine(P(5.0, -2.5), star.get_center(), color=c["red"])
        g = self.label("Gliese 445\n≈ 40,000 years: still 1.7 light-years off", "red", P(2.7, -3.0), 26)
        self.say(5, [FadeOut(o1, o2), Create(path), FadeIn(star)], [Create(gap), Write(g)])
        self.end()


class Record(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("The golden record")
        centre = P(-3.4, 0)
        v = voyager(P(0, 0), c["gray"], 1.8)
        self.say(0, Write(t), FadeIn(v))
        disk = VGroup(disc(2.2, centre, c["yellow"], .85, 7),
                      *[Circle(r, color=c["ink"], stroke_width=1.5, stroke_opacity=.45).move_to(centre) for r in (1.75, 1.35, .95)],
                      disc(.55, centre, c["red"], .8), Dot(centre, radius=.08, color=c["ink"]))
        w = self.label("30 cm", "ink", P(-3.4, -2.75), 32)
        self.say(1, [FadeOut(v), FadeIn(disk)], Write(w))
        items = VGroup(*[self.label(s, "ink", P(2.8, y), 36) for s, y in
                         [("greetings: 55 languages", 1.9), ("115 images", 1.0), ("≈ 90 minutes of music", .1)]])
        self.say(2, Write(items[0]), Write(items[1]), Write(items[2]))
        sounds = self.label("surf · wind · thunder · whales", "blue", P(2.8, -1.2), 34)
        self.say(3, [Write(sounds), Rotate(disk, PI, about_point=centre)])
        last = self.label("sent anyway", "red", P(2.8, -2.4), 48)
        self.say(4, Write(last))
        self.end()


class End(Cetvel):
    def construct(self):
        c = self.c
        sky = stars(70, 31, c["gray"], y=(-1.2, 2.8))
        self.add(sky)
        t = self.title("One light-day")
        axis = self.axis()
        marks = VGroup(self.mark(.2, "Moon, Sun,\nJupiter, Saturn", "gray", 1.9, 24), self.mark(4.2, "Neptune", "blue", .75, 24),
                       self.mark(5.56, "pale blue dot", "yellow", 1.35, 24), self.mark(16.9, "edge of the bubble", "green", .75, 24),
                       self.mark(24, "now", "red", 1.5, 34))
        self.say(0, [Write(t), Create(axis)], LaggedStartMap(FadeIn, marks))
        far = self.label("far for us · tiny for the stars", "ink", P(1.0, 1.2), 40)
        self.say(1, Write(far))
        disk = VGroup(disc(.8, P(-4.2, 1.2), c["yellow"], .85), disc(.2, P(-4.2, 1.2), c["red"], .8))
        q = self.label("what would YOU add?", "yellow", P(1.0, 1.2), 46)
        self.say(2, [FadeOut(far), FadeIn(disk)], Write(q))
        moon = disc(.8, P(-4.2, 1.2), c["gray"], .7)
        n = self.label("next: what if the Moon disappeared?", "blue", P(1.4, 1.2), 34)
        self.say(3, [FadeOut(q), ReplacementTransform(disk, moon), Write(n)], FadeOut(moon))
        self.wait(.5)
