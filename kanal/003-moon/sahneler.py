"""Video 3: What If the Moon Disappeared? Kaynaklar ARASTIRMA.md. Defter tarzı + kalem efekti (../kalem.py).
(kanal/ içinde) .venv/Scripts/python render.py 003-moon taslak"""
from manim import *
import numpy as np

from kalem import Defter
from tahta import P, sketch

TEXT = {
    "Hook": [
        "Tonight, the Moon disappears. No explosion, no debris. It is simply gone.",
        "And for about one point three seconds, you would have no idea.",
        "Then the night changes. So do the oceans. Some living things lose an old signal.",
        "And there is a bigger worry. Without the Moon, could Earth itself start to tip over?",
    ],
    "Rules": [
        "First, the rules of our experiment. The Moon vanishes cleanly, and nothing else is touched.",
        "It sits about three hundred and eighty-four thousand kilometers away.",
        "It is a bit more than a quarter as wide as Earth, with about one eightieth of its mass.",
    ],
    "FirstSecond": [
        "Light needs about one point three seconds to cross that gap. Gravity travels at the same speed.",
        "So for that moment, you still see the Moon, and Earth still feels its pull.",
        "Then both stop at once.",
        "Earth does not fly off into space. Its path around the Sun is set by the Sun, and it barely changes.",
    ],
    "FirstNight": [
        "On the first night, the brightest thing in the night sky is missing.",
        "The sky gets darker, and faint stars have less glare to compete with.",
        "For some animals, that is a problem.",
        "One African dung beetle can roll its ball in a straight line by reading a faint pattern in moonlight.",
        "On moonless nights in that study, the beetles wandered. Later work found some can steer by the Milky Way, but one guide would be gone.",
    ],
    "Tides": [
        "Next, the ocean. The Moon pulls hardest on the side of Earth facing it, and weakest on the far side.",
        "That difference stretches the oceans into two bulges. As Earth turns, most coasts pass through two high tides a day.",
        "The Sun does this too. But it is so far away that its tide force is a little less than half of the Moon's.",
        "Take the Moon away, and a typical tide shrinks to less than half its size. Local coastlines would differ.",
        "The extra big spring tides and the gentle neap tides vanish. High water would follow the Sun, at about the same hours each day.",
    ],
    "ShoreLife": [
        "That matters at the edge of the sea. The strip that floods and dries each day would likely become narrower.",
        "And some creatures keep time with the Moon. In the Gulf of Mexico, many corals spawn together, days after August's full moon.",
        "Scientists think the lunar cycle, sunlight and water temperature work together as their signal.",
        "Remove one of those cues, and nobody knows how well that timing would hold.",
    ],
    "EmptySky": [
        "Within a month, you notice something else. There are no phases. No crescent, no full moon.",
        "Eclipses of the Moon are over, of course. So are eclipses of the Sun.",
        "We get those thanks to a coincidence. The Sun is about four hundred times wider than the Moon, and about four hundred times farther away.",
        "So the two look almost the same size in our sky. Without the Moon, that show is over.",
    ],
    "LongDays": [
        "Now zoom out to centuries. The Moon's tides act like a gentle brake on Earth's spin.",
        "Today, each century adds roughly two thousandths of a second to the length of a day.",
        "It sounds like nothing. But one study suggests that one point four billion years ago, a day lasted under nineteen hours.",
        "Without the Moon, only the weaker solar tides would keep braking. Our days would lengthen far more slowly.",
    ],
    "Tilt": [
        "And now, the big question. Earth leans about twenty-three and a half degrees. That lean gives us seasons.",
        "The Moon helps hold it steady. Today the tilt only nods by about one point three degrees either way.",
        "In nineteen ninety-three, Jacques Laskar and colleagues calculated what happens without that help.",
        "The result was dramatic. The tilt could turn chaotic, anywhere from nearly zero to about eighty-five degrees.",
        "Near that extreme, each pole in turn would point almost straight at the Sun.",
    ],
    "Twist": [
        "That became a famous idea: no Moon, no stable climate. But the story did not end there.",
        "In twenty twelve, another team simulated moonless Earths over billions of years.",
        "Their tilt wandered far more than ours. Yet for hundreds of millions of years, it typically stayed in a band about twenty degrees wide.",
        "So a moonless Earth would be less steady, but probably not tumbling wildly any time soon.",
        "What that would mean for climate and life is still being studied.",
    ],
    "Origin": [
        "Which makes you wonder how we got a Moon at all.",
        "The leading idea: about four and a half billion years ago, a body perhaps the size of Mars hit the young Earth. The debris became the Moon.",
        "And it is already leaving, very slowly, by about three point eight centimeters a year.",
        "So slowly that you will never notice. Quite unlike tonight.",
    ],
    "End": [
        "So if the Moon vanished: darker nights at once, weaker tides within hours, and no more eclipses.",
        "Over the ages, days would stretch more slowly, and Earth's tilt would lose its steady hand.",
        "Which change would you miss the most? Tell me in the comments.",
        "Next time: how do you measure the distance to a star you can never reach?",
    ],
}

DUYGU = {
    "Hook_0": "[mysterious]", "Hook_1": "[whispers]", "Hook_3": "[suspenseful]",
    "Rules_0": "[playfully]",
    "FirstSecond_2": "[dramatic]", "FirstSecond_3": "[reassuring]",
    "FirstNight_0": "[softly]", "FirstNight_3": "[amazed]",
    "Tides_0": "[curious]", "Tides_3": "[serious]",
    "ShoreLife_1": "[warmly]", "ShoreLife_3": "[thoughtful]",
    "EmptySky_2": "[excited]", "EmptySky_3": "[wistful]",
    "LongDays_2": "[surprised]",
    "Tilt_0": "[serious]", "Tilt_3": "[dramatic]",
    "Twist_0": "[curious]", "Twist_2": "[relieved]",
    "Origin_1": "[excited]", "Origin_3": "[amused]",
    "End_2": "[warmly]", "End_3": "[curious]",
}

META = {
    "baslik": "What If the Moon Disappeared?",
    "notlar": """- İzleyici: uzayı merak eden, fizik bilmeyen İngilizce izleyici.
- Büyük soru: Ay yok olsaydı ne değişirdi; Dünya devrilir miydi?
- Tür: N (ne olurdu). Motif: sağ üstte zaman damgası (1,3 sn -> milyarlarca yıl).
- Omurga: Story Spine ("bir gece... bu yüzden...") + zirvede yanlış inanç testi (1993 sonucu -> 2012 düzeltmesi).
- Kanca: seçilen "1,3 saniye fark etmezsin". Elenen: "denizler durur" (yanlış), "Dünya devrilir" (kesin değil, soru olarak kullanıldı).
- Döngü defteri: "Dünya devrilir mi?" (Hook -> Tilt, Twist).
- Görsel tarz (yeni): kareli defter + gece dokusu, kalem ucuyla çizim ve yazı, taramalı boyama, canlı gelgit ve eksen hareketi.""",
}

SAHNE = {
    "Hook": ("Tonight, the Moon is gone", "gece", "Ay çizilir, silinir; 1,3 sn", "AÇ: Dünya devrilir mi?"),
    "Rules": ("The rules", "defter", "Dünya-Ay ölçüleri", "bu yüzden önce deney"),
    "FirstSecond": ("The first 1.3 seconds", "defter", "ışık ve çekim gelir, kesilir; yörünge", "ama Dünya yerinde"),
    "FirstNight": ("The first night", "gece", "karanlık gök, böcek yolu", "bu yüzden canlılar"),
    "Tides": ("The tides", "gece", "canlı gelgit şişkinliği, Güneş payı", "ana etki"),
    "ShoreLife": ("Life at the shore", "defter", "kıyı şeridi, mercan", "belirsiz"),
    "EmptySky": ("No phases, no eclipses", "gece", "evreler silinir, 400/400", "ay sonra"),
    "LongDays": ("Longer days", "defter", "dönen saat, 19 saatlik gün", "yüzyıllar"),
    "Tilt": ("Would Earth tip over?", "gece", "eksen salınımı, 0-85 derece", "ZİRVE"),
    "Twist": ("The twist", "gece", "dar bant", "KAPAT: devrilme sorusu"),
    "Origin": ("Where the Moon came from", "defter", "Theia çarpışması, uzaklaşma", "ama zaten gidiyor"),
    "End": ("What would you miss?", "gece", "zaman çizgisi", "izleyiciye soru; video 4"),
}


class Hook(Defter):
    def construct(self):
        c = self.c
        sky = self.yildizlar(60, 3)
        self.add(sky)
        ay = self.ay(1.6, P(3.4, .6))
        gone = self.yaz(self.label("tonight...", "ink", P(-3.6, 2.0), 46))
        self.say(0, self.ciz(ay), gone, [FadeOut(ay, scale=.2)])
        iz = DashedVMobject(Circle(1.6, color=c["gray"], stroke_width=4).move_to(P(3.4, .6)), num_dashes=30)
        sn = self.label("1.3 s", "yellow", P(-3.6, .2), 110)
        self.say(1, [FadeIn(iz)], self.yaz(sn))
        kelime = VGroup(self.label("night", "blue", P(-5.0, -1.6), 40), self.label("oceans", "blue", P(-2.8, -1.6), 40),
                        self.label("life", "green", P(-.6, -1.6), 40))
        self.say(2, self.yaz(kelime[0]), self.yaz(kelime[1]), self.yaz(kelime[2]))
        e = self.dunya(1.0, ORIGIN)
        eksen = self.ln(P(0, -1.6), P(0, 1.6), "red", 6)
        g = VGroup(e, eksen).move_to(P(3.4, .6))
        soru = self.label("tip over?", "red", P(3.4, -1.9), 56)
        self.say(3, [FadeOut(iz, sn), FadeIn(g)], [Rotate(g, -70 * DEGREES, about_point=P(3.4, .6))], self.yaz(soru))
        self.end()


class Rules(Defter):
    theme = "defter"

    def construct(self):
        t, _ = self.baslik("The experiment")
        e = self.dunya(1.4, P(-4.4, .2))
        m = self.ay(.38, P(4.9, .2))
        kural = self.label("vanishes cleanly · nothing else touched", "red", P(0, 2.1), 32)
        self.say(0, self.ciz(t, e, m), self.yaz(kural))
        ok = DoubleArrow(P(-2.8, .2), P(4.3, .2), color=self.c["ink"], buff=0, stroke_width=4)
        km = self.label("≈ 384,000 km", "ink", P(.8, .75), 42)
        self.say(1, self.ciz(ok), self.yaz(km))
        w = self.label("width ≈ 27% of Earth", "blue", P(3.4, -1.3), 32)
        mass = self.label("mass ≈ 1/80", "green", P(3.4, -2.2), 32)
        self.say(2, self.yaz(w), self.yaz(mass))
        self.end()


class FirstSecond(Defter):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("The first moment", "T + 1.3 s")
        e = self.dunya(1.0, P(-4.8, .2))
        m = self.ay(.5, P(4.8, .2))
        isik = DashedLine(P(4.2, .6), P(-3.6, .6), color=c["yellow"], stroke_width=7, dash_length=.25)
        cekim = DashedLine(P(4.2, -.2), P(-3.6, -.2), color=c["blue"], stroke_width=7, dash_length=.25)
        l = VGroup(self.label("light", "yellow", P(.2, 1.1), 34), self.label("gravity", "blue", P(.2, -.75), 34))
        self.say(0, self.ciz(t, d, e, m), [Create(isik), Create(cekim), FadeIn(l)])
        hala = self.label("you still see it · Earth still feels it", "ink", P(0, -2.0), 36)
        self.say(1, self.yaz(hala))
        bos = DashedVMobject(Circle(.5, color=c["gray"]).move_to(P(4.8, .2)), num_dashes=16)
        self.say(2, [FadeOut(m, isik, cekim, l, hala, scale=.3), FadeIn(bos)])
        self.play(FadeOut(e, bos), run_time=.4)
        gunes = VGroup(self.tara(.8, P(0, .1), "yellow", .14), self.daire(.8, P(0, .1), "yellow", 6))
        yol = sketch(Ellipse(width=8.6, height=3.9, color=c["gray"], stroke_width=4).move_to(P(0, .1)), .01)
        nokta = Dot(yol.point_from_proportion(0), radius=.24, color=c["blue"])
        az = self.label("orbit: barely changes", "green", P(0, -2.6), 36)
        self.say(3, self.ciz(gunes, yol), [FadeIn(nokta)], [MoveAlongPath(nokta, yol), FadeIn(az)])
        self.end()


class FirstNight(Defter):
    def construct(self):
        c = self.c
        t, d = self.baslik("The first night", "T + 12 h")
        ay = self.ay(1.0, P(4.6, 1.0))
        ufuk = sketch(ArcBetweenPoints(P(-7.5, -2.4), P(7.5, -2.4), angle=-PI * .16, color=c["green"], stroke_width=7))
        self.say(0, self.ciz(t, d, ufuk, ay), [FadeOut(ay, scale=.2)])
        sky = self.yildizlar(130, 11, y=(-1.2, 2.5))
        self.say(1, [LaggedStartMap(FadeIn, sky, lag_ratio=.01)])
        self.play(sky.animate.set_opacity(.25), run_time=.4)
        govde = VGroup(self.daire(.5, P(-4.6, -.6), "ink", 6), *[self.ln(P(-4.6 + dx, -.6 + dy), P(-4.6 + 1.7 * dx, -.6 + 1.5 * dy), "ink", 5)
                                                                for dx, dy in [(-.45, .3), (-.5, 0), (-.45, -.3), (.45, .3), (.5, 0), (.45, -.3)]])
        top = VGroup(self.tara(.55, P(-3.35, -.9), "yellow", .12), self.daire(.55, P(-3.35, -.9), "yellow", 5))
        self.say(2, self.ciz(govde, top))
        ay2 = self.ay(.55, P(5.4, 1.5))
        duz = DashedLine(P(-2.6, -.9), P(5.6, -.9), color=c["blue"], stroke_width=7, dash_length=.3)
        s1 = self.label("moonlight: straight", "blue", P(-4.5, .55), 30)
        self.say(3, self.ciz(ay2), [Create(duz), FadeIn(s1)])
        egri = VMobject(color=c["red"], stroke_width=7).set_points_smoothly(
            [P(-2.6, -.9), P(-1.2, .3), P(.2, -1.5), P(.9, .5), P(-.6, 1.0), P(1.9, 1.5), P(2.6, -.2), P(4.2, .6)])
        s2 = self.label("no moon: wandering", "red", P(-4.5, 1.35), 30)
        self.say(4, [FadeOut(ay2)], self.ciz(egri), self.yaz(s2))
        self.end()


class Tides(Defter):
    def construct(self):
        c = self.c
        t, d = self.baslik("The tides", "T + 1 day")
        merkez = P(-2.4, -.1)
        aci, ger = ValueTracker(.0), ValueTracker(1.0)
        su = always_redraw(lambda: Ellipse(width=2 * (1.35 + .62 * ger.get_value() - .12), height=2 * 1.38, color=c["blue"], stroke_width=6)
                           .set_fill(c["blue"], .28).rotate(aci.get_value()).move_to(merkez))
        ay = self.ay(.5, ORIGIN)
        ay.add_updater(lambda m: m.move_to(merkez + 3.3 * P(np.cos(aci.get_value()), np.sin(aci.get_value()))))
        e = self.dunya(1.15, merkez)
        ay.update()
        self.say(0, self.ciz(t, d, e), [FadeIn(su, ay)])
        iki = self.label("two bulges\n≈ two high tides a day", "blue", P(3.9, 1.4), 32)
        self.say(1, [Rotate(e, TAU * .5, about_point=merkez), FadeIn(iki)], aci.animate.set_value(.55))
        gunes = VGroup(self.tara(.7, P(5.4, -1.5), "yellow", .13), self.daire(.7, P(5.4, -1.5), "yellow", 6))
        oran = self.label("Sun's tide force:\na bit under half", "yellow", P(2.6, -1.9), 30)
        self.say(2, self.ciz(gunes), self.yaz(oran))
        az = self.label("typical tide:\nless than half", "red", P(3.9, 1.4), 40)
        self.play(FadeOut(iki, scale=.8), run_time=.4)
        self.say(3, [FadeOut(ay), ger.animate.set_value(.38), aci.animate.set_value(-.35)], self.yaz(az))
        saat = self.label("high water: same hours daily", "green", P(2.9, .0), 32)
        self.say(4, [Rotate(e, TAU, about_point=merkez)], self.yaz(saat))
        su.clear_updaters()
        self.end()


class ShoreLife(Defter):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("Life at the shore", "T + 1 week")
        kum = self.ln(P(-6.6, .9), P(.2, -2.4), "yellow", 9)
        yuksek = self.ln(P(-4.7, 0), P(.2, 0), "blue", 6)
        alcak = self.ln(P(-1.6, -1.55), P(.2, -1.55), "blue", 6)
        serit = DoubleArrow(P(-.3, -1.5), P(-.3, -.05), color=c["red"], buff=0, stroke_width=6)
        self.say(0, self.ciz(t, d, kum, yuksek, alcak), [FadeIn(serit), serit.animate.scale(.45)])

        def dal(p, aci, boy, n):
            q = p + boy * P(np.cos(aci), np.sin(aci))
            g = [self.ln(p, q, "red", 4 + 2 * n)]
            if n:
                g += dal(q, aci + .5, boy * .74, n - 1) + dal(q, aci - .45, boy * .74, n - 1)
            return g
        mercan = VGroup(*dal(P(3.6, -2.6), PI / 2, 1.2, 3))
        ay = self.ay(.55, P(1.6, 2.0))
        ag = self.label("Gulf of Mexico:\ndays after the\nAugust full moon", "ink", P(5.4, 1.9), 26)
        self.say(1, self.ciz(mercan, ay), self.yaz(ag))
        yumurta = VGroup(*[Dot(P(x, y), radius=.07, color=c["yellow"]) for x, y in
                           zip(np.random.default_rng(5).uniform(2.2, 5.2, 45), np.random.default_rng(6).uniform(-1.2, .9, 45))])
        isaret = self.label("moon + sun + water temperature", "blue", P(-3.0, 2.3), 30)
        self.say(2, [LaggedStart(*[FadeIn(y, shift=UP * .8) for y in yumurta], lag_ratio=.04)], self.yaz(isaret))
        soru = self.label("timing without it: unknown", "red", P(-3.0, 1.55), 32)
        self.say(3, [FadeOut(ay, scale=.2)], self.yaz(soru))
        self.end()


class EmptySky(Defter):
    def construct(self):
        c = self.c
        t, d = self.baslik("An empty sky", "T + 1 month")
        evre = VGroup()
        for i, k in enumerate([.0, .28, .55, 1.0, .55, .28]):
            pos = P(-5.2 + 2.08 * i, .9)
            g = VGroup(self.daire(.6, pos, "gray", 3))
            if k:
                g.add(Circle(.58, stroke_width=0).set_fill(c["ink"], .9).stretch(k, 0).move_to(pos))
            evre.add(g)
        self.say(0, self.ciz(t, d, evre), [LaggedStart(*[FadeOut(g, scale=.2) for g in evre], lag_ratio=.15)])
        gun = VGroup(self.tara(1.2, P(0, .3), "yellow", .15), self.daire(1.2, P(0, .3), "yellow", 6))
        golge = Circle(1.2, color=c["ink"], stroke_width=4).set_fill(c["bg"], 1).move_to(P(-3.2, .3))
        yok = self.label("no more eclipses", "red", P(4.4, .3), 36)
        self.say(1, self.ciz(gun), [FadeIn(golge), golge.animate.move_to(P(0, .3))], self.yaz(yok))
        self.play(FadeOut(gun, golge, yok), run_time=.4)
        goz = VGroup(self.daire(.12, P(-6.2, -.5), "ink", 5))
        s = VGroup(self.tara(1.7, P(4.6, -.5), "yellow", .18), self.daire(1.7, P(4.6, -.5), "yellow", 6))
        m = self.ay(.42, P(-3.5, -.5))
        isin = VGroup(self.ln(P(-6.2, -.5), P(4.5, 1.2), "gray", 3), self.ln(P(-6.2, -.5), P(4.5, -2.2), "gray", 3))
        a = self.label("400 × wider", "yellow", P(4.6, 2.0), 34)
        b = self.label("400 × farther", "blue", P(.4, -2.4), 34)
        self.say(2, self.ciz(goz, m, s, isin), self.yaz(a), self.yaz(b))
        self.say(3, [FadeOut(m, scale=.2)])
        self.end()


class LongDays(Defter):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("Longer days", "T + 100 years")
        merkez = P(-3.8, -.2)
        kadran = VGroup(self.daire(2.0, merkez, "ink", 7), *[self.ln(merkez + 1.7 * P(np.cos(a), np.sin(a)), merkez + 1.92 * P(np.cos(a), np.sin(a)), "ink", 4)
                                                             for a in np.linspace(0, TAU, 24, endpoint=False)])
        ibre = Line(merkez, merkez + UP * 1.55, color=c["red"], stroke_width=9)
        fren = self.label("Moon tides = a gentle brake", "blue", P(2.8, 1.7), 32)
        self.say(0, self.ciz(t, d, kadran, ibre), [Rotate(ibre, -TAU * 1.3, about_point=merkez, rate_func=rush_from)], self.yaz(fren))
        ms = self.label("+ ≈ 0.002 s\nper century", "red", P(2.8, .2), 52)
        self.say(1, [Rotate(ibre, -TAU * .6, about_point=merkez), FadeIn(ms)])
        eski = self.label("1.4 billion years ago:\n≈ 18.7 hours (one study)", "ink", P(2.8, -1.7), 34)
        self.say(2, [Rotate(ibre, TAU * 2.2, about_point=merkez)], self.yaz(eski))
        yavas = self.label("no Moon: far slower lengthening", "green", P(2.8, .2), 32)
        self.play(FadeOut(ms, fren), run_time=.4)
        self.say(3, [Rotate(ibre, -TAU * .4, about_point=merkez, rate_func=linear)], self.yaz(yavas))
        self.end()


class Tilt(Defter):
    def construct(self):
        c = self.c
        t, d = self.baslik("Would Earth tip over?", "T + millions of years")
        m = P(-2.6, -.2)
        egim, gorun = ValueTracker(0), ValueTracker(0)          # eksen ve sayı Dünya çizildikten sonra belirir
        dik = DashedLine(m + DOWN * 2.4, m + UP * 2.4, color=c["gray"], stroke_width=4)
        e = self.dunya(1.35, m)

        def eksen():
            a = egim.get_value() * DEGREES
            u = P(np.sin(a), np.cos(a))
            return VGroup(Line(m - 2.35 * u, m - 1.4 * u, color=c["red"], stroke_width=8),
                          Arrow(m + 1.4 * u, m + 2.45 * u, color=c["red"], buff=0, stroke_width=8)).set_opacity(gorun.get_value())
        ax = always_redraw(eksen)
        say_ = always_redraw(lambda: self.label(f"{egim.get_value():.1f}°", "yellow", P(2.4, .2), 100).set_opacity(gorun.get_value()))
        mevsim = self.label("tilt → seasons", "ink", P(2.4, -1.4), 38)
        self.add(ax, say_)
        self.say(0, self.ciz(t, d, e, dik), [gorun.animate.set_value(1), egim.animate.set_value(23.4)], self.yaz(mevsim))
        mn = self.ay(.45, P(5.7, 1.6))
        oy = self.label("with the Moon: ± 1.3°", "green", P(2.4, -2.3), 34)
        self.say(1, self.ciz(mn), [egim.animate(rate_func=there_and_back).set_value(24.7), FadeIn(oy)], [egim.animate(rate_func=there_and_back).set_value(22.1)])
        yil = self.label("1993 · Laskar and colleagues", "blue", P(2.4, 1.9), 32)
        self.say(2, [FadeOut(mn, mevsim, oy, scale=.4)], self.yaz(yil))
        genis = self.label("moonless: 0° to ≈ 85°", "red", P(2.4, -1.5), 40)
        self.say(3, [egim.animate.set_value(2), FadeIn(genis)], egim.animate.set_value(70), egim.animate.set_value(15), egim.animate.set_value(85))
        gun = VGroup(self.tara(.65, P(6.0, -.2), "yellow", .13), self.daire(.65, P(6.0, -.2), "yellow", 6))
        self.play(FadeOut(say_), run_time=.3)
        say_.clear_updaters()
        self.say(4, self.ciz(gun))
        ax.clear_updaters()
        self.end()


class Twist(Defter):
    def construct(self):
        c = self.c
        t, d = self.baslik("But then came 2012", "T + billions of years")
        sol, alt = -5.8, -2.3

        def y(deg):
            return alt + 4.5 * deg / 90
        eks = VGroup(self.ln(P(sol, alt), P(sol, y(90)), "ink", 5), self.ln(P(sol, alt), P(5.8, alt), "ink", 5))
        etiket = VGroup(*[self.label(f"{k}°", "gray", P(sol - .55, y(k)), 24) for k in (0, 30, 60, 90)],
                        self.label("time →", "gray", P(5.2, alt - .4), 24))
        rng = np.random.default_rng(3)
        xs = np.linspace(sol + .1, 5.6, 90)

        def egri(v, renk, w=5):
            return VMobject(color=c[renk], stroke_width=w).set_points_smoothly([P(a, y(b)) for a, b in zip(xs, v)])
        vahsi = np.clip(42 + 40 * np.sin(np.linspace(0, 11, 90)) + rng.normal(0, 6, 90), 1, 85)
        v1 = egri(vahsi, "red")
        fikir = self.label("1993 idea (sketch)", "red", P(3.7, 2.55), 28)
        self.say(0, self.ciz(t, d, eks, etiket), self.ciz(v1), self.yaz(fikir))
        yeni = self.label("2012: new simulations", "blue", P(-1.4, 2.55), 30)
        self.say(1, [v1.animate.set_stroke(opacity=.18), fikir.animate.set_opacity(.25)], self.yaz(yeni))
        bant = Rectangle(width=11.5, height=y(34) - y(13), stroke_width=0).set_fill(c["green"], .22).move_to(P(-.05, (y(34) + y(13)) / 2))
        sakin = np.clip(23.5 + 8 * np.sin(np.linspace(0, 9, 90)) + 2 * np.sin(np.linspace(0, 41, 90)), 14, 33)
        v2 = egri(sakin, "green", 6)
        b = self.label("band ≈ 20° wide (illustration)", "green", P(1.2, y(48)), 32)
        self.say(2, [FadeIn(bant)], self.ciz(v2), self.yaz(b))
        sonuc = self.label("less steady, not wild (for ages)", "yellow", P(1.2, y(62)), 34)
        self.say(3, [FadeOut(v1, fikir)], self.yaz(sonuc))
        soru = self.label("climate and life: still studied", "ink", P(1.2, y(76)), 30)
        self.say(4, self.yaz(soru))
        self.end()


class Origin(Defter):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("Where it came from", "T − 4.5 billion years")
        e = self.dunya(1.4, P(-3.2, -.1))
        self.say(0, self.ciz(t, d, e))
        theia = VGroup(self.tara(.72, P(5.4, 1.4), "red", .13), self.daire(.72, P(5.4, 1.4), "red", 6))
        ad = self.label("Theia\n(≈ Mars-sized?)", "red", P(4.6, -.2), 30)
        rng = np.random.default_rng(9)
        parca = VGroup(*[Dot(P(-1.9, .5), radius=rng.uniform(.05, .13), color=c["red" if i % 2 else "gray"]) for i in range(46)])
        hedef = [P(-3.2, -.1) + rng.uniform(2.2, 3.1) * P(np.cos(a), .55 * np.sin(a)) for a in np.linspace(0, TAU, 46)]
        ay = self.ay(.5, P(.4, .3))
        self.say(1, self.ciz(theia), [FadeIn(ad), theia.animate.move_to(P(-1.9, .5))],
                 [FadeOut(theia, ad, scale=1.6), *[p.animate.move_to(q) for p, q in zip(parca, hedef)]],
                 [*[p.animate.move_to(ay.get_center()) for p in parca]], [FadeOut(parca), FadeIn(ay)])
        git = Arrow(P(1.2, .3), P(4.6, .3), color=c["blue"], buff=0, stroke_width=7)
        cm = self.label("≈ 3.8 cm per year", "blue", P(3.0, 1.1), 40)
        self.say(2, [ay.animate.shift(RIGHT * 1.0), git.animate.shift(RIGHT * 1.0)], self.yaz(cm))
        self.say(3, [ay.animate.shift(RIGHT * .25)])
        self.end()


class End(Defter):
    def construct(self):
        c = self.c
        sky = self.yildizlar(50, 21)
        self.add(sky)
        t, _ = self.baslik("Without the Moon")
        yol = self.ln(P(-6.3, -.4), P(6.3, -.4), "ink", 6)

        def durak(x, ust, alt, renk, h=.45):
            return VGroup(Dot(P(x, -.4), radius=.16, color=c[renk]), self.ln(P(x, -.25), P(x, h - .35), renk, 3),
                          self.label(ust, renk, P(x, h), 28), self.label(alt, "gray", P(x, -1.15), 24))
        a = [durak(-5.1, "dark nights", "at once", "blue"), durak(-2.4, "weaker tides", "hours", "blue", 1.35), durak(.5, "no eclipses", "for good", "red")]
        self.say(0, self.ciz(t, yol), self.yaz(a[0]), self.yaz(a[1]), self.yaz(a[2]))
        b = [durak(2.7, "slower braking", "centuries+", "green", 1.35), durak(5.2, "less steady tilt", "ages", "yellow")]
        self.say(1, self.yaz(b[0]), self.yaz(b[1]))
        q = self.label("which would you miss?", "yellow", P(0, -2.3), 48)
        self.say(2, self.yaz(q))
        yildiz = Star(5, outer_radius=.35, color=c["yellow"]).set_fill(c["yellow"], 1).move_to(P(5.2, 1.9))
        n = self.label("next: how far is a star?", "blue", P(0, -2.3), 42)
        self.say(3, [FadeOut(q), FadeIn(yildiz)], self.yaz(n))
        self.wait(.5)
