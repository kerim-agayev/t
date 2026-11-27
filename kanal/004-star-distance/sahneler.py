"""Video 4: How Do You Measure a Star You Can Never Reach? Kaynaklar ARASTIRMA.md.
Tarz: gözlem defteri + göz merceği: solda geometri, sağda aynı anda hesaplanan görüntü.
(kanal/ içinde) .venv/Scripts/python render.py 004-star-distance taslak"""
from manim import *
import numpy as np

from kalem import Defter
from tahta import P, sketch, text

TEXT = {
    "Hook": [
        "No ship can reach a star. No tape measure is long enough. Yet we know how far away many of them are.",
        "To see how, hold one finger up at arm's length. Close one eye, then switch.",
        "Your finger jumps against the wall behind it.",
        "Now bring it closer. The jump gets bigger.",
        "That small jump is the idea that first measured the distance to a star. But making it work took centuries.",
    ],
    "Trick": [
        "Here is why it works. Your two eyes look from two different places.",
        "A nearby object seems to move against things far behind it. The nearer it is, the more it moves.",
        "So if you know how far apart your two viewpoints are, and you measure the size of the jump, geometry gives you the distance.",
        "No ruler has to touch anything. Astronomers call this shift parallax.",
    ],
    "Orbit": [
        "For a star, your eyes are hopelessly close together. We need a wider pair. Luckily, we are riding on one.",
        "Look at a star today. Then wait six months.",
        "Earth has moved to the other side of its orbit, about three hundred million kilometers away.",
        "A nearby star should now sit in a slightly different spot against the distant ones.",
        "Simple. Except that, for a very long time, nobody saw it move at all.",
    ],
    "Tycho": [
        "In the late fifteen hundreds, Tycho Brahe was the finest observer alive. He had no telescope, but his instruments were superb.",
        "He found no shift. So he faced a choice.",
        "Either Earth does not travel around the Sun, or the stars are unbelievably far away, with an enormous emptiness in between.",
        "That emptiness seemed absurd to him. It was one of his main objections to a moving Earth.",
        "The shift was real. It was just far too small for him. Even his best work was at least twenty times too coarse.",
    ],
    "Hooke": [
        "Telescopes raised hopes. In sixteen sixty-nine, Robert Hooke built one into his rooms at a London college.",
        "It looked straight up, through holes in a floor and the roof. He lay on the floor beneath it and watched a star called Gamma Draconis.",
        "It passes almost directly overhead, where the air bends starlight least.",
        "In sixteen seventy-four, he announced success. But he had only four observations, from a troublesome instrument.",
        "Other astronomers were not convinced. They were right.",
    ],
    "Bradley": [
        "In seventeen twenty-five, Samuel Molyneux and James Bradley set out to repeat Hooke's work. And the star moved!",
        "Back and forth, in a smooth yearly cycle. But the timing was wrong. It was three months off from what parallax predicts.",
        "Bradley found the answer. Imagine walking through falling rain.",
        "You tilt your umbrella forward, because your own motion changes where the rain seems to come from.",
        "Light does the same to a moving Earth. This is called the aberration of starlight, and it is direct evidence that we really are moving.",
        "Parallax was still hiding underneath. Bradley concluded it was probably less than half an arcsecond.",
        "That put his star more than four hundred thousand times farther away than the Sun.",
    ],
    "Suspect": [
        "An arcsecond is one three-thousand-six-hundredth of a degree. To catch something that small, you must pick the right star.",
        "Which ones are close? Brightness can fool you. But there is a better clue.",
        "Watch from a passing train: nearby trees rush by, while far hills barely move.",
        "In the sky, a faint double star called Sixty-one Cygni was drifting unusually fast from year to year. That suggested it was near.",
        "And from his observatory, the German astronomer Friedrich Bessel could follow it all year. He made it his target.",
    ],
    "Heliometer": [
        "Bessel had a special instrument, a heliometer, the last design of the great lens maker Joseph Fraunhofer.",
        "Its main lens was sliced into two halves. Slide one half, and every star splits into two images.",
        "Bessel slid the glass until the image of his target met a faint neighbor.",
        "A fine screw told him how far the lens had moved, and so, the angle between the stars.",
        "Comparing neighbors was the clever part. Bradley's effect shifts them both almost equally, so it cancels out.",
        "A shift that belongs only to the nearer star remains.",
        "He did this again and again, about a hundred times against each of two faint stars, across a whole year.",
    ],
    "Wave": [
        "Then came the arithmetic, all by hand.",
        "He had to separate the star's steady drift across the sky from anything that repeated once a year.",
        "Point by point, a pattern appeared. Forward, then back.",
        "A gentle wave, keeping time with Earth's orbit. There it was.",
        "Astronomers define parallax as half of the full swing, the shift caused by one Earth to Sun distance.",
        "In eighteen thirty-eight, Bessel announced a value of about zero point three one four arcseconds.",
        "For the first time, a star had a convincing distance. And the shift that Tycho had looked for was finally there.",
    ],
    "Distance": [
        "How small is that? Picture a one euro coin about fifteen kilometers away. Its width covers about the angle Bessel measured.",
        "Now draw the triangle. Its short side is the distance from Earth to the Sun, which astronomers had estimated by watching Venus cross the Sun in the seventeen sixties.",
        "Its sharp tip is at the star. The rule is beautifully simple. Half the angle means twice the distance.",
        "Bessel's angle gives about ten light years. Today's value, measured from space, is about eleven point four.",
        "With a split lens and patient eyes, he came within about ten percent.",
        "A later study suggests that temperature changes in the instrument can explain the gap.",
    ],
    "Race": [
        "But Bessel was not alone. In eighteen thirty-seven, Wilhelm Struve had already reported a tentative parallax for the bright star Vega.",
        "It was remarkably close to the modern value. Then he added more data, and his answer roughly doubled, away from the truth.",
        "Meanwhile, Thomas Henderson had observed Alpha Centauri from South Africa years earlier, but he published after Bessel.",
        "Who was first is still discussed. Bessel usually gets the credit for the first convincing measurement.",
        "And Henderson's target belongs to the closest star system of all. Yet even its nearest member, Proxima Centauri, has a parallax of less than one arcsecond.",
        "No wonder it took so long.",
    ],
    "Gaia": [
        "The same idea now flies in space.",
        "From twenty fourteen to early twenty twenty-five, Europe's Gaia spacecraft observed about two billion stars and other objects.",
        "Its finest measurements are like spotting the width of a human hair from about a thousand kilometers.",
        "And those distances help calibrate special pulsing stars, which carry the ruler much farther, to other galaxies.",
        "It all starts with your finger and two eyes.",
        "So, which would have been harder for you: a year of careful measuring, or the math by hand? Tell me in the comments.",
        "Next time: the day in eighteen fifty-nine when the Sun made telegraph wires spark.",
    ],
}

DUYGU = {
    "Hook_0": "[mysterious]", "Hook_1": "[playfully]", "Hook_4": "[suspenseful]",
    "Trick_3": "[warmly]",
    "Orbit_0": "[curious]", "Orbit_4": "[serious]",
    "Tycho_2": "[thoughtful]",
    "Hooke_3": "[excited]", "Hooke_4": "[amused]",
    "Bradley_0": "[surprised]", "Bradley_2": "[curious]", "Bradley_6": "[awe]",
    "Suspect_1": "[curious]",
    "Heliometer_0": "[impressed]", "Heliometer_5": "[excited]",
    "Wave_0": "[serious]", "Wave_3": "[amazed]", "Wave_6": "[awe]",
    "Distance_0": "[playfully]", "Distance_4": "[impressed]",
    "Race_1": "[surprised]", "Race_5": "[thoughtful]",
    "Gaia_2": "[amazed]", "Gaia_4": "[warmly]", "Gaia_6": "[mysterious]",
}

META = {
    "baslik": "How Do You Measure a Star You Can Never Reach?",
    "notlar": """- İzleyici: uzayı merak eden, geometri hatırlamayan İngilizce izleyici.
- Büyük soru: gidemediğimiz bir yıldızın uzaklığını nasıl biliyoruz?
- Tür: B (dedektif). Omurga: imkânsız soru → yetmeyen fikirler → zekice çözüm → sınama.
- ABT: Yıldıza gidemeyiz ve cetvelimiz yoktur, ama Dünya yer değiştirdikçe yakın yıldız çok az kayar, bu yüzden o kaymayı ölçen uzaklığı bulur.
- Yayın günü Gaia DR4 durumunu kontrol et (2 Aralık 2026 planlanıyor).
- Döngü defteri: "yıldız da kayar mı?" (Hook -> Wave); "niye görünmüyor?" (Orbit -> Race); Bradley'nin kayması (Bradley -> Heliometer).
- Görsel tarz (yeni): göz merceği (geometriyle aynı anda hesaplanan görüntü), dedektif damgaları, çalışan ikiye kesik mercek, nokta nokta beliren dalga.""",
}

SAHNE = {
    "Hook": ("A finger and a star", "gece", "parmak iki gözle atlar", "AÇ: yıldız da atlar mı?"),
    "Trick": ("The trick", "defter", "iki bakış noktası, yakın ve uzak", "açı = uzaklık"),
    "Orbit": ("A bigger pair of eyes", "gece", "yörünge + göz merceği", "ama kayma görünmüyor"),
    "Tycho": ("The star that would not move", "defter", "iki seçenek, damga", "çok uzak mı?"),
    "Hooke": ("Through the floors", "defter", "dik teleskop, dört nokta", "ama ikna etmedi"),
    "Bradley": ("The wrong season", "gece", "iki dalga, yağmurda şemsiye", "başka şey buldu"),
    "Suspect": ("Choose your suspect", "gece", "tren, hızlı gezen çift yıldız", "hangi yıldız yakın?"),
    "Heliometer": ("A lens cut in half", "defter", "kayan yarım mercek, çift görüntü", "Bradley etkisi silinir"),
    "Wave": ("The wave", "gece", "noktalar, dalga, 0.314", "ZİRVE"),
    "Distance": ("From angle to distance", "defter", "avro, ince üçgen", "10 ve 11,4 ışık yılı"),
    "Race": ("The race", "defter", "üç gözlemci", "kim ilk?"),
    "Gaia": ("A billion wobbles", "gece", "uzay aracı, saç teli, basamaklar", "izleyiciye soru; video 5"),
}

KOYU, KAGIT = "#2b2a28", "#efe6cf"
IY = ORIGIN


class Sahne(Defter):
    # ---- bu videonun ortak parçaları ----
    def bitir(self):
        for m in list(self.mobjects):
            if m is not self.zemin:
                m.clear_updaters(recursive=True)
        self.end()

    def damga(self, s, renk, pos, aci=12, size=44):
        y = text(s, self.c[renk], size)
        kutu = sketch(RoundedRectangle(width=y.width + .6, height=y.height + .45, corner_radius=.15, color=self.c[renk], stroke_width=7))
        return VGroup(kutu, y.move_to(kutu)).rotate(aci * DEGREES).move_to(pos).set_z_index(8)

    def vur(self, d):
        return FadeIn(d, scale=2.4)

    def kart(self, w, h, pos, aci=0):
        golge = RoundedRectangle(width=w, height=h, corner_radius=.12, stroke_width=0).set_fill("#000000", .22).shift(P(.12, -.12))
        yuz = RoundedRectangle(width=w, height=h, corner_radius=.12, stroke_color="#8b8678", stroke_width=3).set_fill(KAGIT, 1)
        return VGroup(golge, yuz).rotate(aci * DEGREES).move_to(pos)

    def yildiz(self, pos, r=.14, renk="#ffd166"):
        return VGroup(Circle(r * 2.6, stroke_width=0).set_fill(renk, .16), Star(5, outer_radius=r * 1.5, stroke_width=0).set_fill(renk, 1)).move_to(pos)

    def mercek(self, r, pos, seed=4):
        """Göz merceği: koyu daire, sabit uzak yıldızlar, artı işareti. Yakın yıldız ayrıca eklenir."""
        rng = np.random.default_rng(seed)
        uzak = VGroup()
        while len(uzak) < 26:
            q = rng.uniform(-r, r, 2)
            if np.linalg.norm(q) < r * .9:
                uzak.add(Dot(pos + P(*q), radius=rng.uniform(.025, .06), color="#cfd6e6"))
        cerceve = VGroup(Circle(r + .16, color="#c9a25a", stroke_width=14).move_to(pos), Circle(r + .3, color="#8a6f3c", stroke_width=4).move_to(pos))
        cam = Circle(r, stroke_width=0).set_fill("#050a14", 1).move_to(pos)
        nisan = VGroup(Line(pos + LEFT * r, pos + RIGHT * r), Line(pos + DOWN * r, pos + UP * r)).set_stroke("#6f7c99", 2, .6)
        return VGroup(cam, nisan, uzak, cerceve)

    def goz(self, pos, acik=True):
        ak = sketch(Ellipse(width=1.3, height=.8, color=self.c["ink"], stroke_width=5).move_to(pos), .008)
        if acik:
            return VGroup(ak, Dot(pos, radius=.2, color=self.c["blue"]))
        return VGroup(self.ln(pos + P(-.65, 0), pos + P(.65, 0), "ink", 6))

    def parmak(self, h=2.6):
        deri = "#e8b58a"
        govde = RoundedRectangle(width=.7, height=h, corner_radius=.34, stroke_color=self.c["ink"], stroke_width=5).set_fill(deri, 1)
        tirnak = RoundedRectangle(width=.42, height=.55, corner_radius=.2, stroke_color="#b9805c", stroke_width=3).set_fill("#f3d3bd", 1)
        tirnak.move_to(govde.get_top() + DOWN * .45)
        bogum = Arc(radius=.5, start_angle=PI * .3, angle=PI * .4, color="#b9805c", stroke_width=4).move_to(govde.get_center() + DOWN * .1)
        return VGroup(govde, tirnak, bogum)


class Hook(Sahne):
    def construct(self):
        c = self.c
        sky = self.yildizlar(70, 4)
        self.add(sky)
        y = self.yildiz(P(0, 1.0), .3)
        a = self.label("how far?", "yellow", P(0, -.7), 72)
        metre = VGroup(self.ln(P(-7, -2.2), P(-2.2, -2.2), "ink", 6), *[self.ln(P(x, -2.2), P(x, -1.95), "ink", 4) for x in np.arange(-6.8, -2.3, .4)])
        self.say(0, [FadeIn(y)], self.ciz(metre), self.yaz(a))
        self.play(FadeOut(y, a, metre, sky), run_time=.4)

        duvar = VGroup(*[self.ln(P(x, -.4), P(x, 2.5), "gray", 4) for x in np.arange(-6, 6.1, 1.2)])
        el = self.parmak().move_to(P(0, -.6)).set_z_index(3)
        sol, sag = P(-2.2, -2.75), P(2.2, -2.75)
        gozler = VGroup(self.goz(sol), self.goz(sag, False))
        self.say(1, self.ciz(duvar), [FadeIn(el, shift=UP)], [FadeIn(gozler)])
        golge = self.parmak().move_to(P(-1.8, -.6)).set_opacity(.22)
        diger = VGroup(self.goz(sol, False), self.goz(sag))
        ok = CurvedArrow(P(1.4, 2.1), P(-1.4, 2.1), color=c["yellow"], stroke_width=8, angle=PI / 3)
        atla = self.label("jump!", "yellow", P(0, 3.2), 56)
        # sol gözle parmak duvarda sağda, sağ gözle solda görünür
        self.play(el.animate.shift(RIGHT * 1.8), run_time=.01)
        self.say(2, [Transform(gozler, diger), el.animate(rate_func=rush_from).shift(LEFT * 3.6)],
                 [FadeIn(golge.move_to(P(1.8, -.6))), Create(ok)], self.yaz(atla))
        yakin = self.label("closer → bigger jump", "red", P(0, 3.2), 50)
        self.play(FadeOut(ok, atla, golge), run_time=.3)
        iri = self.parmak().scale(1.4)

        def git(x, sol_acik):
            return [Transform(el, iri.copy().move_to(P(x, -.45))), Transform(gozler, VGroup(self.goz(sol, sol_acik), self.goz(sag, not sol_acik)))]
        self.say(3, git(-3.9, True), git(3.9, False), [*git(-3.9, True), FadeIn(yakin)])
        self.play(FadeOut(duvar, el, gozler, yakin), run_time=.4)
        y = self.yildiz(P(0, .9), .26)
        asir = self.label("one idea · centuries of failure", "ink", P(0, -1.7), 44)
        self.say(4, [FadeIn(y)], [y.animate.shift(LEFT * .9)], [y.animate.shift(RIGHT * 1.8)], self.yaz(asir))
        self.bitir()


class Trick(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, _ = self.baslik("Why it works")
        sol, sag = P(-1.5, -2.7), P(1.5, -2.7)
        gozler = VGroup(self.goz(sol), self.goz(sag))
        uzak = self.ln(P(-6.6, 2.3), P(6.6, 2.3), "gray", 5)
        agac = VGroup(*[Triangle(color=c["green"], stroke_width=3).set_fill(c["green"], .5).scale(.22).move_to(P(x, 2.55)) for x in np.arange(-6.2, 6.3, .8)])
        self.say(0, self.ciz(t, gozler), self.ciz(uzak, agac))
        d = ValueTracker(1.6)                                      # cismin yüksekliği (gözlere yakınlık)

        def isinlar():
            h = d.get_value()
            cisim = P(0, -2.7 + h)
            g = VGroup()
            for goz, renk in ((sol, "red"), (sag, "blue")):
                u = (2.3 - goz[1]) / (cisim[1] - goz[1])
                uc = goz + u * (cisim - goz)
                g.add(DashedLine(goz, uc, color=c[renk], stroke_width=5, dash_length=.2), Dot(uc, radius=.17, color=c[renk]))
            a, b = g[1].get_center(), g[3].get_center()
            g.add(Line(P(b[0], 1.8), P(a[0], 1.8), color=c["yellow"], stroke_width=10))
            g.add(Dot(cisim, radius=.3, color=c["ink"]).set_z_index(5))
            return g
        r = always_redraw(isinlar)
        yazi = self.label("jump", "yellow", P(5.3, 1.1), 44)
        self.add(r)
        self.say(1, [d.animate.set_value(3.8)], [d.animate.set_value(1.5), FadeIn(yazi)])
        taban = DoubleArrow(P(-1.5, -3.25), P(1.5, -3.25), color=c["ink"], buff=0, stroke_width=4)
        form = VGroup(self.label("known gap", "ink", P(-4.8, -1.1), 36), self.label("+ measured jump", "yellow", P(-4.8, -1.9), 36),
                      self.label("= distance", "red", P(-4.8, -2.7), 44))
        self.say(2, [FadeIn(taban)], self.yaz(form[0]), self.yaz(form[1]), self.yaz(form[2]))
        ad = self.label("parallax", "blue", P(4.7, -1.9), 70)
        self.say(3, [d.animate.set_value(2.4)], self.yaz(ad))
        self.bitir()


class Orbit(Sahne):
    def construct(self):
        c = self.c
        t, _ = self.baslik("A bigger pair of eyes")
        gunes = P(-3.5, -2.0)
        R, D = 2.2, 3.0                                            # yörünge yarıçapı, yıldız yüksekliği (ölçeksiz)
        faz = ValueTracker(PI)                                     # PI: Dünya solda
        yor = DashedVMobject(Ellipse(width=2 * R, height=1.1, color=c["gray"], stroke_width=4).move_to(gunes), num_dashes=44)
        sun = VGroup(self.tara(.38, gunes, "yellow", .09), self.daire(.38, gunes, "yellow", 5))
        yakin = gunes + P(0, D)

        def dunya_yeri():
            a = faz.get_value()
            return gunes + P(R * np.cos(a), .55 * np.sin(a))
        yer = always_redraw(lambda: Dot(dunya_yeri(), radius=.24, color=c["blue"]).set_z_index(6))
        yy = self.yildiz(yakin, .16)
        olcek = self.label("not to scale", "gray", P(-6.0, 2.3), 24)
        self.say(0, self.ciz(t, sun, yor), [FadeIn(yer, olcek)], [FadeIn(yy)])

        merkez = P(3.9, .1)
        m = self.mercek(2.3, merkez)

        def gorunen():
            e = dunya_yeri()
            x = e[0] + (yakin[0] - e[0]) * 2.2                     # görüş çizgisinin uzak gökteki yeri
            return merkez + P((x - gunes[0]) * .45, .35)
        cizgi = always_redraw(lambda: DashedLine(dunya_yeri(), dunya_yeri() + 1.45 * (yakin - dunya_yeri()), color=c["yellow"], stroke_width=4, dash_length=.18))
        gy = always_redraw(lambda: self.yildiz(gorunen(), .17).set_z_index(4))
        ad = self.label("what you see", "ink", P(3.9, -2.9), 34)
        self.play(FadeIn(m), run_time=.4)
        self.add(cizgi, gy)
        bugun = self.label("today", "blue", P(-6.3, -2.75), 32)
        self.say(1, [FadeIn(ad)], self.yaz(bugun))
        iz = self.yildiz(gorunen(), .17).set_opacity(.25)
        self.add(iz)
        sonra = self.label("+ 6 months", "blue", P(-.25, -2.75), 32)
        km = self.label("≈ 300 million km", "ink", P(-3.5, -3.15), 30)
        self.say(2, [faz.animate.set_value(TAU)], self.yaz(sonra), self.yaz(km))
        kay = DoubleArrow(iz.get_center() + DOWN * .6, gorunen() + DOWN * .6, color=c["red"], buff=0, stroke_width=6, tip_length=.2)
        self.say(3, [Create(kay)], [faz.animate.set_value(TAU + PI)], [faz.animate.set_value(2 * TAU)])
        yok = self.damga("NOT SEEN", "red", P(3.9, 1.7))
        sabit = self.yildiz(merkez + P(0, .35), .17)
        self.remove(gy)
        self.add(sabit)
        self.say(4, [FadeOut(kay, iz), faz.animate.set_value(2 * TAU + PI)], [faz.animate.set_value(3 * TAU), self.vur(yok)])
        self.bitir()


class Tycho(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("Tycho Brahe", "1580s")
        o = P(-4.6, -2.2)
        kadran = VGroup(Arc(radius=2.9, start_angle=0, angle=PI / 2, arc_center=o, color=c["ink"], stroke_width=8),
                        self.ln(o, o + P(2.9, 0), "ink", 7), self.ln(o, o + P(0, 2.9), "ink", 7),
                        *[self.ln(o + 2.65 * P(np.cos(a), np.sin(a)), o + 2.9 * P(np.cos(a), np.sin(a)), "ink", 3) for a in np.linspace(.08, PI / 2 - .08, 14)])
        kol = Line(o, o + 3.2 * P(np.cos(.75), np.sin(.75)), color=c["red"], stroke_width=8)
        yok = self.label("no telescope", "blue", P(.8, .9), 40)
        self.say(0, self.ciz(t, d, kadran), [FadeIn(kol), Rotate(kol, .35, about_point=o, rate_func=there_and_back)], self.yaz(yok))
        sifir = self.label("shift measured: none", "red", P(2.6, -.4), 46)
        self.say(1, [Rotate(kol, -.45, about_point=o, rate_func=there_and_back), FadeOut(yok)], self.yaz(sifir))
        self.play(FadeOut(kadran, kol, sifir), run_time=.4)
        k1 = self.kart(5.6, 3.6, P(-3.4, -.2), 2)
        k2 = self.kart(5.6, 3.6, P(3.4, -.2), -2)
        a = VGroup(text("A", c["blue"], 54), text("Earth stands still", KOYU, 34)).arrange(DOWN, buff=.4).move_to(k1)
        b = VGroup(text("B", c["blue"], 54), text("stars are absurdly\nfar away", KOYU, 34)).arrange(DOWN, buff=.4).move_to(k2)
        self.say(2, [FadeIn(k1, shift=UP)], self.yaz(a), [FadeIn(k2, shift=UP)], self.yaz(b))
        bos = self.damga("ABSURD?", "red", P(3.4, -2.35), 8, 40)
        sec = SurroundingRectangle(k1, color=c["red"], stroke_width=9, buff=.14)
        self.say(3, [self.vur(bos)], self.ciz(sec))
        self.play(FadeOut(k1, k2, a, b, bos, sec), run_time=.4)

        def cubuk(y, w, renk, ad):
            k = Rectangle(width=w, height=.7, stroke_color=c[renk], stroke_width=5).set_fill(c[renk], .45).move_to(P(-2.6 + w / 2, y))
            return VGroup(k, self.label(ad, "ink", P(-4.7, y), 34))
        goz = cubuk(.9, 8.0, "red", "Tycho can see")
        shift = cubuk(-.5, .32, "green", "real shift")
        kat = self.label("≥ 20 × too small to catch", "red", P(.4, -2.0), 46)
        cb = self.damga("TOO SMALL", "red", P(4.6, -.55), -10)
        self.say(4, [FadeIn(goz, shift=RIGHT)], [FadeIn(shift, shift=RIGHT)], self.yaz(kat), [self.vur(cb)])
        self.bitir()


class Hooke(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, d = self.baslik("Straight up", "1669")
        ev = VGroup(self.ln(P(-6.3, -3.0), P(-1.3, -3.0), "ink", 8), self.ln(P(-6.0, -3.0), P(-6.0, 1.2), "ink", 6), self.ln(P(-1.6, -3.0), P(-1.6, 1.2), "ink", 6),
                    self.ln(P(-6.0, -1.0), P(-4.2, -1.0), "ink", 6), self.ln(P(-3.4, -1.0), P(-1.6, -1.0), "ink", 6),
                    self.ln(P(-6.4, 1.2), P(-4.2, 1.8), "red", 7), self.ln(P(-3.4, 1.8), P(-1.2, 1.2), "red", 7))
        ev.shift(RIGHT * 1.4)
        self.say(0, self.ciz(t, d), self.ciz(ev))
        tup = VGroup(self.ln(P(-4.05, -2.1), P(-4.05, 2.5), "blue", 6), self.ln(P(-3.55, -2.1), P(-3.55, 2.5), "blue", 6),
                     Ellipse(width=.75, height=.22, color=c["blue"], stroke_width=7).move_to(P(-3.8, 2.55)),
                     Ellipse(width=.55, height=.18, color=c["blue"], stroke_width=7).move_to(P(-3.8, -2.15)))
        adam = VGroup(self.daire(.28, P(-3.8, -2.6), "ink", 6), self.ln(P(-3.52, -2.7), P(-2.0, -2.75), "ink", 8))
        yy = self.yildiz(P(-3.8, 3.1), .14, "#d99a00")
        ad = self.label("Gamma Draconis", "ink", P(-1.0, 2.6), 30)
        isin = DashedLine(P(-3.8, 2.95), P(-3.8, -2.35), color=c["yellow"], stroke_width=6, dash_length=.2)
        VGroup(tup, adam, yy, isin).shift(RIGHT * 1.4)
        ad.move_to(P(.1, 2.75))
        self.say(1, self.ciz(tup, adam), [FadeIn(yy, ad)], [Create(isin)])
        dik = VGroup(self.label("overhead", "blue", P(3.8, 1.3), 46), self.label("least bending by air", "ink", P(3.8, .4), 34))
        self.say(2, self.yaz(dik[0]), self.yaz(dik[1]))
        self.play(FadeOut(dik), run_time=.3)
        k = self.kart(5.8, 4.2, P(3.8, -.7), -1)
        eks = VGroup(Line(P(1.4, -2.1), P(6.3, -2.1), color=KOYU, stroke_width=4), Line(P(1.4, -2.1), P(1.4, .5), color=KOYU, stroke_width=4))
        bas = text("1674: \"found it!\"", c["blue"], 36).move_to(P(3.8, .9))
        nok = VGroup(*[Dot(P(x, y), radius=.16, color=c["red"]) for x, y in [(2.1, -1.5), (3.1, -.8), (4.5, -.2), (5.7, -1.2)]])
        dort = text("4 observations", KOYU, 28).move_to(P(3.8, -2.5))
        self.say(3, [FadeIn(k, shift=UP), FadeIn(eks)], self.yaz(bas), [LaggedStart(*[FadeIn(n, scale=3) for n in nok], lag_ratio=.5)], [FadeIn(dort)])
        st = self.damga("NOT CONVINCING", "red", P(3.8, -.9), 14, 40)
        self.say(4, [self.vur(st)])
        self.bitir()


class Bradley(Sahne):
    def construct(self):
        c = self.c
        t, d = self.baslik("Same star, again", "1725")
        y0, x0, w = -.2, -5.6, 11.2
        eks = VGroup(self.ln(P(x0, y0), P(x0 + w, y0), "gray", 4),
                     *[self.ln(P(x0 + w * k / 4, y0 - .15), P(x0 + w * k / 4, y0 + .15), "gray", 4) for k in range(5)],
                     *[self.label(s, "gray", P(x0 + w * k / 4, -2.35), 26) for k, s in enumerate(["0", "3 mo", "6 mo", "9 mo", "12 mo"])])
        bek = FunctionGraph(lambda x: y0 + 1.5 * np.cos(TAU * (x - x0) / w), x_range=[x0, x0 + w], color=c["gray"], stroke_width=6)
        gor = FunctionGraph(lambda x: y0 + 1.5 * np.sin(TAU * (x - x0) / w), x_range=[x0, x0 + w], color=c["yellow"], stroke_width=8)
        hareket = self.label("it moves!", "yellow", P(3.6, 2.3), 48)
        self.say(0, self.ciz(t, d, eks), self.ciz(gor), self.yaz(hareket))
        b = DashedVMobject(bek, num_dashes=50)
        b_ad = self.label("parallax predicts", "gray", P(-3.6, 2.2), 32)
        ok = DoubleArrow(P(x0, 1.75), P(x0 + w / 4, 1.75), color=c["red"], buff=0, stroke_width=7, tip_length=.22)
        uc = self.label("3 months off", "red", P(x0 + w / 4 + 2.1, 1.75), 40)
        nd = self.label("(sketch)", "gray", P(6.0, -3.0), 24)
        self.say(1, [FadeOut(hareket), FadeIn(nd)], [Create(b), FadeIn(b_ad)], [Create(ok)], self.yaz(uc))
        self.play(*[FadeOut(m) for m in (eks, gor, b, b_ad, ok, uc, nd)], run_time=.4)

        yer = self.ln(P(-7, -3.0), P(7, -3.0), "green", 7)
        rng = np.random.default_rng(2)
        yagmur = VGroup()
        for x, y, f in zip(rng.uniform(-7, 7, 70), rng.uniform(-2.4, 2.4, 70), rng.uniform(0, 1, 70)):
            damla = Line(P(x, y), P(x, y - .35), color=c["blue"], stroke_width=4)

            def dus(m, dt):
                m.shift(DOWN * 4 * dt)
                if m.get_y() < -2.7:
                    m.shift(UP * 5.2)
            damla.add_updater(dus)
            yagmur.add(damla)

        def insan(egim):
            bas = P(0, -.9)
            govde = VGroup(self.daire(.32, bas, "ink", 6), self.ln(P(0, -1.2), P(0, -2.2), "ink", 7),
                           self.ln(P(0, -2.2), P(-.45, -3.0), "ink", 7), self.ln(P(0, -2.2), P(.45, -3.0), "ink", 7))
            sem = VGroup(Arc(radius=1.1, start_angle=0, angle=PI, arc_center=P(0, .2), color=c["red"], stroke_width=9),
                         self.ln(P(-1.1, .2), P(1.1, .2), "red", 6), self.ln(P(0, .2), P(0, -1.3), "ink", 5)).rotate(egim, about_point=P(0, -1.3))
            return VGroup(govde, sem).set_z_index(4)
        kisi = insan(0).shift(LEFT * 2.5)
        self.say(2, [FadeIn(yer, yagmur, kisi)])
        egik = insan(-35 * DEGREES).shift(RIGHT * 2.5)
        yon = self.label("walking →", "ink", P(-4.6, 2.2), 36)
        self.say(3, [Transform(kisi, egik), FadeIn(yon)])
        self.play(*[FadeOut(m) for m in (yer, yagmur, kisi, yon)], run_time=.4)
        for m in yagmur:
            m.clear_updaters()

        iz = DashedLine(P(-6.4, -2.4), P(-1.2, -2.4), color=c["gray"], stroke_width=4)
        yer2 = Dot(P(-4.2, -2.4), radius=.34, color=c["blue"]).set_z_index(4)
        hiz = Arrow(P(-3.8, -2.4), P(-2.0, -2.4), color=c["red"], buff=0, stroke_width=8)
        isik = Arrow(P(-4.2, 1.8), P(-4.2, -2.0), color=c["yellow"], buff=0, stroke_width=7)
        gorunen = DashedLine(P(-4.2, -2.4), P(-2.7, 1.8), color=c["ink"], stroke_width=5, dash_length=.2)
        et = VGroup(self.label("real\nlight", "yellow", P(-5.3, .6), 30), self.label("seems to\ncome from", "ink", P(-1.7, .6), 30),
                    self.label("our motion", "red", P(-2.5, -3.0), 30))
        isim = VGroup(self.label("aberration", "yellow", P(3.2, 1.4), 64), self.label("starlight seems tilted\nbecause we move", "ink", P(3.2, -.2), 36),
                      self.damga("EARTH MOVES", "green", P(3.2, -2.0), 6, 42))
        self.say(4, self.ciz(iz, isik), [FadeIn(yer2, hiz, et[0], et[2])], [Create(gorunen), FadeIn(et[1])], self.yaz(isim[0]), [FadeIn(isim[1])], [self.vur(isim[2])])
        self.play(*[FadeOut(m) for m in (iz, yer2, hiz, isik, gorunen, *et, *isim)], run_time=.4)
        sinir = self.label("parallax < 0.5″  (probably)", "red", P(0, 1.3), 54)
        self.say(5, self.yaz(sinir))
        a = self.yildiz(P(-5.6, -1.2), .2)
        yol = DashedLine(P(-5.0, -1.2), P(5.3, -1.2), color=c["gray"], stroke_width=5, dash_length=.25)
        y2 = self.yildiz(P(5.9, -1.2), .2)
        kat = VGroup(self.label("Sun", "yellow", P(-5.6, -2.1), 30), self.label("γ Draconis", "ink", P(5.5, -2.1), 30),
                     self.label("> 400,000 × the Earth–Sun distance", "yellow", P(0, -.45), 38))
        self.say(6, [FadeIn(a, y2, kat[0], kat[1])], [Create(yol)], self.yaz(kat[2]))
        self.bitir()


class Suspect(Sahne):
    def construct(self):
        c = self.c
        t, _ = self.baslik("Which star is close?")
        bir = self.label("1″ = 1 / 3600 of a degree", "yellow", P(0, 1.2), 56)
        sky = self.yildizlar(60, 8, y=(-3.0, .2))
        self.say(0, self.ciz(t), self.yaz(bir), [FadeIn(sky)])
        parlak = self.yildiz(P(-3.5, -1.3), .45)
        sonuk = self.yildiz(P(3.5, -1.3), .12)
        q = VGroup(self.label("bright ≠ close", "red", P(0, -2.9), 44))
        self.say(1, [FadeOut(bir), FadeIn(parlak, sonuk)], self.yaz(q[0]))
        self.play(FadeOut(parlak, sonuk, q, sky), run_time=.4)

        daglar = VMobject(color=c["gray"], stroke_width=6).set_points_as_corners(
            [P(x, y) for x, y in zip(np.linspace(-14, 14, 15), [.2, 1.6, .5, 1.9, .3, 1.4, .7, 1.8, .4, 1.5, .2, 1.7, .6, 1.3, .3])])

        def agac(x):
            return VGroup(Line(P(x, -2.9), P(x, -1.9), color=c["yellow"], stroke_width=10),
                          Triangle(color=c["green"], stroke_width=5).set_fill(c["green"], .8).scale(.8).move_to(P(x, -1.35)))
        agaclar = VGroup(*[agac(x) for x in (-5, -.5, 4, 8.5, 13, 17.5)])
        pencere = VGroup(self.ln(P(-6.9, -3.1), P(6.9, -3.1), "ink", 8), self.ln(P(-6.9, 2.4), P(6.9, 2.4), "ink", 8))
        self.say(2, [FadeIn(daglar, agaclar, pencere), agaclar.animate(rate_func=linear).shift(LEFT * 14), daglar.animate(rate_func=linear).shift(LEFT * 1.2)])
        self.play(FadeOut(daglar, agaclar, pencere), run_time=.4)

        sky = self.yildizlar(90, 14)
        self.add(sky)
        ikili = VGroup(self.yildiz(P(-4.0, -1.0), .13, "#ffb067"), self.yildiz(P(-3.6, -1.25), .1, "#ff9a67"))
        ad = self.label("61 Cygni", "yellow", P(-3.8, -2.75), 44)
        self.play(FadeIn(ikili, ad), run_time=.3)
        iz = TracedPath(ikili[0].get_center, stroke_color=c["yellow"], stroke_width=5)
        self.add(iz)
        hiz = self.label("drifting fast → probably near", "green", P(2.4, 1.7), 40)
        notu = self.label("drift exaggerated", "gray", P(5.6, -3.0), 24)
        g = VGroup(ikili, ad)
        c0 = g.get_center()
        self.say(3, [g.animate(rate_func=linear).move_to(c0 + P(3.1, 1.1)), FadeIn(notu)], [g.animate(rate_func=linear).move_to(c0 + P(5.4, 1.95)), FadeIn(hiz)])
        hedef = VGroup(Circle(.85, color=c["red"], stroke_width=7), Line(LEFT * 1.15, LEFT * .6, color=c["red"], stroke_width=7),
                       Line(RIGHT * .6, RIGHT * 1.15, color=c["red"], stroke_width=7), Line(UP * .6, UP * 1.15, color=c["red"], stroke_width=7),
                       Line(DOWN * .6, DOWN * 1.15, color=c["red"], stroke_width=7)).move_to(ikili)
        bessel = self.label("Friedrich Bessel · Königsberg", "ink", P(-2.6, 2.25), 38)
        iz.clear_updaters()
        self.say(4, [FadeOut(hiz)], self.yaz(bessel), self.ciz(hedef))
        self.bitir()


class Heliometer(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, _ = self.baslik("The heliometer")
        L, r = P(-4.0, -.3), 1.8
        kay = ValueTracker(0)

        def yarim(sag):  # yarım disk
            a = -PI / 2 if sag else PI / 2
            yay = Arc(radius=r, start_angle=a, angle=PI, arc_center=L, color=c["blue"], stroke_width=7)
            g = VMobject(color=c["blue"], stroke_width=7).set_points(yay.points).add_points_as_corners([yay.get_start()])
            return g.set_fill(c["blue"], .22)
        sol = yarim(False)
        sag0 = yarim(True)
        sag = always_redraw(lambda: sag0.copy().shift(UP * kay.get_value()))
        kim = self.label("designed by Joseph Fraunhofer", "ink", P(2.8, 1.6), 34)
        self.say(0, self.ciz(t, sol, sag0), self.yaz(kim))
        self.remove(sag0)
        self.add(sag)
        self.play(FadeOut(kim), run_time=.3)

        merkez = P(3.2, -.1)
        m = self.mercek(2.2, merkez, 12)
        m[2].set_opacity(.35)
        hedef = merkez + P(-.35, -.55)
        komsu = merkez + P(-.35, 1.0)
        fark = komsu[1] - hedef[1]
        sabit = VGroup(self.yildiz(hedef, .17), self.yildiz(komsu, .09, "#cfd6e6")).set_z_index(3)
        kopya = always_redraw(lambda: VGroup(self.yildiz(hedef + UP * kay.get_value() * fark, .17),
                                             self.yildiz(komsu + UP * kay.get_value() * fark, .09, "#cfd6e6")).set_opacity_by_gradient(.9).set_z_index(3)
                              if kay.get_value() > .02 else VGroup(Dot(hedef, radius=.001)))
        self.play(FadeIn(m, sabit), run_time=.4)
        self.add(kopya)
        ikiz = self.label("one star → two images", "blue", P(-4.0, -3.0), 34)
        self.say(1, [kay.animate.set_value(.45)], self.yaz(ikiz))
        ad = VGroup(self.label("target", "yellow", merkez + P(.95, -.55), 24).set_color("#ffd166"),
                    self.label("neighbor", "ink", merkez + P(.95, 1.35), 24).set_color("#eef0e6")).set_z_index(5)
        halka = Circle(.4, color="#ff7a66", stroke_width=7).move_to(komsu).set_z_index(6)
        self.say(2, [FadeIn(ad), FadeOut(ikiz)], [kay.animate.set_value(1.0)], [Create(halka)])

        vida = always_redraw(lambda: text(f"screw: {kay.get_value() * 42.7:05.1f}", c["red"], 44).move_to(P(-4.0, -3.0)))
        self.add(vida)
        aci = self.label("→ angle between the stars", "red", P(2.9, -3.25), 32)
        self.say(3, [kay.animate.set_value(.3)], [kay.animate.set_value(1.0)], self.yaz(aci))
        self.play(FadeOut(halka, ad, aci), run_time=.3)
        ayni = VGroup(sabit, ad)
        k1 = Arrow(hedef + P(.25, 0), hedef + P(1.15, 0), color="#6ec6ff", buff=0, stroke_width=7)
        k2 = Arrow(komsu + P(.25, 0), komsu + P(1.15, 0), color="#6ec6ff", buff=0, stroke_width=7)
        VGroup(k1, k2).set_z_index(6)
        iptal = self.label("same push on both → cancels", "blue", P(3.2, -3.25), 32)
        vida.clear_updaters()
        kopya.clear_updaters()
        self.say(4, [FadeOut(kopya), FadeIn(k1, k2)], [sabit.animate.shift(RIGHT * .5), k1.animate.shift(RIGHT * .5), k2.animate.shift(RIGHT * .5)], self.yaz(iptal))
        self.play(FadeOut(k1, k2, iptal), sabit.animate.shift(LEFT * .5), run_time=.4)
        kalan = Arrow(hedef + P(.28, 0), hedef + P(1.0, 0), color="#ff7a66", buff=0, stroke_width=8).set_z_index(6)
        yalniz = self.label("only the near star's own shift", "red", P(3.2, -3.25), 32)
        self.say(5, [FadeIn(kalan), FadeIn(yalniz)], [sabit[0].animate.shift(RIGHT * .6), kalan.animate.shift(RIGHT * .6)])
        self.play(*[FadeOut(x) for x in (sol, sag, vida, m, sabit, kalan, yalniz)], run_time=.4)
        sag.clear_updaters()
        cet = VGroup(*[VGroup(*[Line(UP * .28, DOWN * .28, color=c["ink" if k < 100 else "blue"], stroke_width=4).move_to(P(-6.3 + (i % 25) * .38, y - (i // 25) * .6))
                                for i in range(100)]) for k, y in ((0, 1.9), (100, -.9))])
        n = VGroup(self.label("≈ 100 vs star a", "ink", P(5.2, 1.0), 30), self.label("≈ 100 vs star b", "blue", P(5.2, -1.8), 30),
                   self.label("one full year", "red", P(5.2, -3.1), 38))
        self.say(6, [LaggedStart(*[FadeIn(s) for s in cet[0]], lag_ratio=.03), FadeIn(n[0])], [LaggedStart(*[FadeIn(s) for s in cet[1]], lag_ratio=.03), FadeIn(n[1])], self.yaz(n[2]))
        self.bitir()


class Wave(Sahne):
    def construct(self):
        c = self.c
        t, d = self.baslik("The wave", "1837 – 1838")
        x0, w, y0 = -6.0, 12.0, -.7
        rng = np.random.default_rng(61)
        xs = np.sort(rng.uniform(x0, x0 + w, 100))

        def dalga(x):
            return 1.35 * np.sin(TAU * 1.15 * (x - x0) / w)
        gurultu = rng.normal(0, .3, 100)
        kayma = .17 * (xs - x0) - 1.0                              # yıldızın düzenli sürüklenmesi
        eks = VGroup(self.ln(P(x0, -2.9), P(x0 + w, -2.9), "gray", 4), self.label("one year +", "gray", P(5.2, -3.3), 26))
        notu = self.label("illustration, not Bessel's data", "gray", P(-3.8, -3.3), 24)
        nok = VGroup(*[Dot(P(x, y0 + dalga(x) + g + k), radius=.065, color=c["ink"]) for x, g, k in zip(xs, gurultu, kayma)])
        el = self.label("by hand", "blue", P(3.8, 2.4), 46)
        self.say(0, self.ciz(t, d, eks), self.yaz(el), [FadeIn(notu)])
        dogru = DashedLine(P(x0, y0 - 1.0), P(x0 + w, y0 - 1.0 + .17 * w), color=c["red"], stroke_width=6, dash_length=.25)
        s = self.label("steady drift", "red", P(-3.6, 1.5), 36)
        self.say(1, [LaggedStart(*[FadeIn(p, scale=3) for p in nok], lag_ratio=.02)], [Create(dogru), FadeIn(s)])
        self.say(2, [FadeOut(el), FadeOut(s)], [*[p.animate.shift(DOWN * k) for p, k in zip(nok, kayma)], Transform(dogru, DashedLine(P(x0, y0), P(x0 + w, y0), color=c["gray"], stroke_width=4, dash_length=.25))])
        egri = FunctionGraph(lambda x: y0 + dalga(x), x_range=[x0, x0 + w], color=c["yellow"], stroke_width=11)
        var = self.damga("THERE IT IS", "green", P(3.6, 1.9), -6, 48)
        self.say(3, self.ciz(egri), [self.vur(var)])
        self.play(FadeOut(var), run_time=.3)
        ust, alt = y0 + 1.35, y0 - 1.35
        tam = DoubleArrow(P(6.45, alt), P(6.45, ust), color=c["gray"], buff=0, stroke_width=6, tip_length=.2)
        yarim = DoubleArrow(P(-6.45, y0), P(-6.45, ust), color=c["red"], buff=0, stroke_width=9, tip_length=.2)
        cz = VGroup(DashedLine(P(x0, ust), P(x0 + w, ust), color=c["gray"], stroke_width=3), DashedLine(P(x0, alt), P(x0 + w, alt), color=c["gray"], stroke_width=3))
        pl = self.label("parallax = half the swing", "red", P(-2.6, 1.7), 38)
        self.say(4, [Create(cz), Create(tam)], [Create(yarim)], self.yaz(pl))
        deger = self.label("0.314″", "yellow", P(2.8, 2.2), 96)
        self.say(5, [FadeOut(pl)], [nok.animate.set_opacity(.35)], self.yaz(deger))
        son = self.label("Tycho's missing shift: found", "green", P(-3.1, 2.2), 34)
        self.say(6, [egri.animate.set_stroke(width=16)], [egri.animate.set_stroke(width=11)], self.yaz(son))
        self.bitir()


class Distance(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, _ = self.baslik("How small is 0.314″?")
        para = VGroup(Circle(.95, stroke_color="#8a6f3c", stroke_width=6).set_fill("#d9b45a", 1), Circle(.62, stroke_color="#8a8f98", stroke_width=5).set_fill("#cfd3da", 1))
        para = VGroup(para, text("1 €", KOYU, 40)).move_to(P(4.9, -.3))
        goz = self.goz(P(-5.6, -.3))
        isin = VGroup(self.ln(P(-4.9, -.3), P(4.9, .65), "gray", 3), self.ln(P(-4.9, -.3), P(4.9, -1.25), "gray", 3))
        km = self.label("≈ 15 km", "red", P(-.3, 1.4), 60)
        self.say(0, self.ciz(t, goz), [FadeIn(para, scale=2)], self.ciz(isin), self.yaz(km))
        self.play(FadeOut(para, goz, isin, km, t), run_time=.4)
        t, _ = self.baslik("The skinny triangle")
        uzun = ValueTracker(5.2)
        S, E = P(-5.8, -1.7), P(-5.8, .5)                          # Güneş, Dünya; ucu yıldızda
        gun = VGroup(self.tara(.33, S, "yellow", .08), self.daire(.33, S, "yellow", 5))
        yer = Dot(E, radius=.2, color=c["blue"]).set_z_index(4)
        kisa = Line(S, E, color=c["blue"], stroke_width=9)
        ad = self.label("1 Earth–Sun\ndistance", "blue", P(-4.2, -2.7), 28)
        venus = self.label("estimated from Venus transits, 1760s", "ink", P(1.7, -.6), 30)

        def ucgen():
            q = S + RIGHT * uzun.get_value()
            u = (E - q) / np.linalg.norm(E - q)
            a0 = np.arctan2(u[1], u[0])
            return VGroup(Line(S, q, color=c["ink"], stroke_width=6), Line(E, q, color=c["ink"], stroke_width=6),
                          Arc(radius=2.6, start_angle=a0, angle=PI - a0, arc_center=q, color=c["red"], stroke_width=9),
                          self.yildiz(q + RIGHT * .25, .16, "#d99a00"))
        u = always_redraw(ucgen)
        self.say(1, self.ciz(gun, kisa), [FadeIn(yer)], [FadeIn(ad)], self.yaz(venus))
        self.add(u)
        kural1 = self.label("angle", "red", P(-.7, 1.4), 48)
        kural2 = self.label("angle ÷ 2  →  distance × 2", "red", P(0, 1.8), 52)
        self.say(2, [FadeOut(venus), FadeIn(kural1)], [FadeOut(kural1), uzun.animate.set_value(10.4)], self.yaz(kural2))
        u.clear_updaters()
        self.play(*[FadeOut(x) for x in (u, gun, yer, kisa, ad, kural2)], run_time=.4)

        def cubuk(y, v, renk, ad_):
            k = Rectangle(width=v * .74, height=.85, stroke_color=c[renk], stroke_width=6).set_fill(c[renk], .4).move_to(P(-3.0 + v * .37, y))
            return VGroup(k, self.label(ad_, "ink", P(-5.0, y), 34), self.label(f"{v:.1f}", renk, P(-1.95 + v * .74, y), 44))
        a = cubuk(.9, 10.4, "blue", "Bessel")
        b = cubuk(-.5, 11.4, "green", "today")
        ly = self.label("light years", "ink", P(.4, 2.1), 36)
        self.say(3, [FadeIn(a, shift=RIGHT), FadeIn(ly)], [FadeIn(b, shift=RIGHT)])
        yuz = self.label("within ≈ 10%", "red", P(.4, -1.8), 60)
        self.say(4, self.yaz(yuz))
        isi = self.label("likely culprit: temperature (later study)", "ink", P(.4, -2.9), 32)
        self.say(5, self.yaz(isi))
        self.bitir()


class Race(Sahne):
    theme = "defter"

    def construct(self):
        c = self.c
        t, _ = self.baslik("Three observers")

        def sutun(x, isim, yildiz_adi):
            k = self.kart(4.2, 5.0, P(x, -.55))
            g = VGroup(text(isim, c["blue"], 38), text(yildiz_adi, KOYU, 30)).arrange(DOWN, buff=.15).move_to(P(x, 1.15))
            return k, g

        def satir(s, renk, x, y, size=32):
            return text(s, renk, size).move_to(P(x, y))
        k1, g1 = sutun(-4.6, "Struve", "Vega")
        a = satir("1837:  0.125″", c["green"], -4.6, -.1, 38)
        self.say(0, self.ciz(t), [FadeIn(k1, shift=UP)], self.yaz(g1), self.yaz(a))
        dogru = satir("modern: 0.130″", KOYU, -4.6, -.85, 28)
        b = satir("later: 0.261″", c["red"], -4.6, -1.8, 38)
        self.say(1, self.yaz(dogru), self.yaz(b))
        k2, g2 = sutun(0, "Henderson", "Alpha Centauri")
        h = VGroup(satir("observed\n1832 – 33", KOYU, 0, -.3, 32), satir("published\n1839", c["red"], 0, -1.9, 32))
        self.say(2, [FadeIn(k2, shift=UP)], self.yaz(g2), self.yaz(h[0]), self.yaz(h[1]))
        k3, g3 = sutun(4.6, "Bessel", "61 Cygni")
        e = VGroup(satir("1838:  0.314″", c["green"], 4.6, -.1, 38), satir("≈ 100 points\nper reference", KOYU, 4.6, -1.2, 28))
        st = self.damga("CONVINCING", "green", P(4.6, -2.35), 10, 34)
        self.say(3, [FadeIn(k3, shift=UP), FadeIn(g3, e)], [self.vur(st)])
        self.play(*[FadeOut(x) for x in (k1, g1, a, dogru, b, k2, g2, h, k3, g3, e, st)], run_time=.4)
        x0, birim = -5.6, 9.6

        def cubuk(y, v, renk, ad):
            k = Rectangle(width=v * birim, height=.7, stroke_color=c[renk], stroke_width=5).set_fill(c[renk], .4).move_to(P(x0 + v * birim / 2, y))
            return VGroup(k, self.label(ad, "ink", P(x0 + 2.0, y + .75), 32))
        bir = DashedLine(P(x0 + birim, -2.8), P(x0 + birim, 2.2), color=c["red"], stroke_width=6, dash_length=.25)
        bir_ad = self.label("1″", "red", P(x0 + birim, 2.6), 44)
        p = cubuk(.5, .768, "blue", "Proxima: 0.77″")
        z = cubuk(-1.6, .314, "green", "61 Cygni: 0.31″")
        self.say(4, [Create(bir), FadeIn(bir_ad)], [FadeIn(p, shift=RIGHT)], [FadeIn(z, shift=RIGHT)])
        son = self.label("every star: under 1″", "red", P(2.2, -2.7), 40)
        self.say(5, self.yaz(son))
        self.bitir()


class Gaia(Sahne):
    def construct(self):
        c = self.c
        sky = self.yildizlar(120, 30)
        self.add(sky)
        t, _ = self.baslik("Parallax, in space")
        o = P(-3.6, 0)
        kalkan = RegularPolygon(10, color=c["yellow"], stroke_width=6).set_fill(c["yellow"], .18).scale(2.0).stretch(.34, 1).move_to(o + DOWN * .5)
        govde = VGroup(RegularPolygon(6, color=c["ink"], stroke_width=6).set_fill("#34435f", 1).scale(.8).stretch(.8, 1).move_to(o + UP * .25),
                       self.daire(.2, o + P(-.28, .3), "blue", 5), self.daire(.2, o + P(.28, .3), "blue", 5))
        arac = VGroup(kalkan, govde)
        self.say(0, self.ciz(t, arac))
        yil = VGroup(self.label("2014 – 2025", "blue", P(2.8, 1.2), 56), self.label("≈ 2 billion\nstars and objects", "yellow", P(2.8, -.6), 46))
        self.say(1, [arac.animate.shift(UP * .35)], self.yaz(yil[0]), [FadeIn(yil[1], scale=.6)])
        self.play(FadeOut(yil), run_time=.3)
        sac = sketch(Line(P(5.2, -2.0), P(5.2, 1.4), color="#c98d5a", stroke_width=5), .05)
        yol = DoubleArrow(P(-1.4, -1.9), P(4.9, -1.9), color=c["ink"], buff=0, stroke_width=5, tip_length=.22)
        km = self.label("≈ 1000 km", "yellow", P(1.7, -2.6), 46)
        s = self.label("one human hair", "ink", P(4.9, 1.95), 32)
        kon = VGroup(self.ln(o + P(1.0, .3), P(5.2, .1), "blue", 2), self.ln(o + P(1.0, .3), P(5.2, -.15), "blue", 2))
        self.say(2, self.ciz(sac, kon), [FadeIn(s), Create(yol)], self.yaz(km))
        self.play(*[FadeOut(x) for x in (arac, sac, yol, km, s, kon)], run_time=.4)
        basamak = VGroup()
        for i, (ust, renk) in enumerate([("parallax\nnearby stars", "blue"), ("pulsing stars\n(Cepheids)", "yellow"), ("other\ngalaxies", "green")]):
            x, y = -4.4 + 4.4 * i, -2.0 + 1.15 * i
            basamak.add(VGroup(self.ln(P(x - 1.9, y), P(x + 1.9, y), renk, 9), self.label(ust, renk, P(x, y + .75), 32)))
        nabiz = self.yildiz(P(0, 1.3), .22)
        self.say(3, [FadeIn(basamak[0], shift=UP * .4)], [FadeIn(basamak[1], nabiz, shift=UP * .4)], [nabiz.animate(rate_func=there_and_back).scale(1.8)],
                 [FadeIn(basamak[2], shift=UP * .4)])
        self.play(FadeOut(basamak, nabiz), run_time=.4)
        el = self.parmak(2.4).move_to(P(1.6, -.8))
        gozler = VGroup(self.goz(P(-1.8, -2.85)), self.goz(P(1.8, -2.85), False))
        self.say(4, [FadeIn(el, gozler)], [el.animate.shift(LEFT * 3.2), Transform(gozler, VGroup(self.goz(P(-1.8, -2.85), False), self.goz(P(1.8, -2.85))))])
        self.play(FadeOut(el, gozler), run_time=.4)
        q = VGroup(self.label("a year of measuring", "blue", P(-3.5, .6), 42), self.label("or", "ink", P(0, .6), 42),
                   self.label("math by hand?", "yellow", P(3.7, .6), 42))
        self.say(5, self.yaz(q[0]), [FadeIn(q[1])], self.yaz(q[2]))
        tel = VGroup(self.ln(P(-5.5, -2.9), P(-5.5, -1.4), "ink", 7), self.ln(P(5.5, -2.9), P(5.5, -1.4), "ink", 7),
                     sketch(ArcBetweenPoints(P(-5.5, -1.45), P(5.5, -1.45), angle=PI / 9, color=c["ink"], stroke_width=4)))
        kiv = VGroup(*[Star(6, outer_radius=.3, inner_radius=.08, stroke_width=0).set_fill(c["yellow"], 1).move_to(P(x, -2.0)) for x in (-2.4, .3, 2.8)])
        n = self.label("next: 1859, when telegraph wires sparked", "red", P(0, 1.8), 40)
        self.say(6, [FadeOut(q), FadeIn(tel)], self.yaz(n), [LaggedStart(*[FadeIn(k, scale=3) for k in kiv], lag_ratio=.3)])
        self.wait(.5)
        self.bitir()
