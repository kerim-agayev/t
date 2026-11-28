"""Video 1: Why Your First Number Traps You. Kaynaklar ARASTIRMA.md. Tarz: ../marj.py (kenar boşluklu defter + çıpa).
(kanal_2/ içinde) .venv/Scripts/python stills.py 001-first-number   -> video üretmeden her cümlenin karesi"""
from manim import *

from marj import NOT_X, Marj
from tahta import P

TEXT = {
    "Hook": [
        "Before we start, I need one number from you. Watch the wheel.",
        "It stopped on 65.",
        "Now think: is the share of United Nations members that are African higher or lower than 65 percent?",
        "Next, pick your own exact percentage. Write it down, so you can't quietly change it later.",
        "In a famous experiment, a spinning wheel moved people's answers. Did this one just move yours?",
    ],
    "Wheel": [
        "In 1974, the psychologists Amos Tversky and Daniel Kahneman described an experiment much like this.",
        "People watched a wheel of fortune spin. It was marked 0 to 100, but rigged to stop only at 10 or 65.",
        "They said whether the true answer was higher or lower, then moved up or down from that number.",
        "Different groups got different starting numbers. The question stayed the same.",
        "Starting from 10, the median answer, the one in the middle, was 25 percent.",
        "Starting from 65, it was 45 percent.",
        "A wheel knows nothing about the United Nations. Yet the two groups' middle answers were 20 points apart.",
    ],
    "Careless": [
        "Were they just being careless? The authors report that paying for accuracy did not reduce the effect.",
        "Later work adds a catch: incentives can help when people know which way to adjust.",
        "So here is a second test from the 1974 paper, and this one you can try yourself.",
    ],
    "Multiply": [
        "You have five seconds. Don't work it all out. Just estimate this.",
        "Got a number? In the study, high school students had five seconds to estimate a product like this.",
        "But one group saw it starting from 8. Another group saw it starting from 1.",
        "The group that saw 8 first gave a median guess of 2,250.",
        "The group that saw 1 first gave 512.",
        "Same numbers, same product. And the real answer is 40,320.",
        "The authors' explanation: people may work out the first few steps, then adjust upward, but not far enough.",
    ],
    "Gandhi": [
        "Fine. But surely a ridiculous number would do nothing. Anyone can see it is nonsense.",
        "In one study, people compared Mahatma Gandhi's age with either 9 or 140.",
        "Both are absurd. Yet after 140 the average guess was about 67 years, and after 9, about 50.",
    ],
    "House": [
        "Still, an expert, you might think, would see straight through it.",
        "In a 1987 study, Gregory Northcraft and Margaret Neale gave estate agents a 10-page booklet on a house.",
        "It held the facts needed to price it, plus a listing price: above the appraisal for some, below for others.",
        "The agents' estimates moved toward that listing price. So did the estimates of non-experts.",
        "To be fair, a listing price can carry real information. So here is a harder case.",
    ],
    "Judges": [
        "Trial judges, with more than 15 years of experience on average, were asked to sentence a hypothetical criminal case.",
        "They considered a sentencing demand that openly came from a computer science student playing prosecutor.",
        "In the researchers' account, judges shown a demand of 34 months gave almost 8 months more than those shown 12.",
        "In later research, junior lawyers threw secretly loaded dice to set the demand. It still pulled their sentences.",
    ],
    "Why": [
        "So why does a number pull, even when you know where it came from?",
        "One leading explanation: to compare, your mind tests the number, and facts that fit it come forward.",
        "In one study, people judged whether the average German car costs more or less than 40,000 marks, or 20,000.",
        "The researchers reported that after the high number, people spotted words like Mercedes and BMW faster.",
        "And after the low one, words like VW. But a 2019 team ran new versions and did not find this word effect.",
        "Anchoring still appeared, and their word test may be too weak to settle why. So treat the explanation as open.",
        "Some starting points you pick yourself. To guess when vodka freezes, you may start at water's 0 degrees Celsius.",
        "Then you move downward. With starting points like these, research suggests we tend to stop too soon.",
    ],
    "Limits": [
        "Now the part that is easy to leave out. Not every number you happen to see will grab you.",
        "In a 2020 paper, David Shanks and colleagues found that incidental numbers had no reliable effect on price estimates.",
        "But the classic setup, compare first and then estimate, has held up well.",
        "Many Labs, a project with 36 samples and 6,344 participants, gave a high or low hint first. Anchoring appeared.",
    ],
    "Defense": [
        "So can you simply watch out for it? A warning may not be enough.",
        "In one study, students were warned, some even told which way the pull would go. The pull did not go away.",
        "Something else did help. Car experts who listed reasons against a suggested price were pulled less.",
        "So here is a habit to try. Treat it as my suggestion, not a proven cure.",
        "Make your own guess before you hear theirs. Then ask: why might their number be wrong?",
    ],
    "Close": [
        "Now, back to your number. Today, 54 of the 193 United Nations members belong to the African Group.",
        "That is about 28 percent. How close were you?",
        "A confession: our wheel was staged, like theirs. I chose 65. And one answer can't show whether it moved you.",
        "To see that, you need to compare groups with different starting numbers, as those researchers did.",
        "So keep this: a number you stop to weigh can quietly become the place where your thinking starts.",
        "What did you write down? Tell me in the comments, even if you saw the trick coming.",
        "Next time: you can only study the planes that came back. So where would you add armor?",
    ],
}

# sese giden duygu etiketleri (altyazıda görünmez)
DUYGU = {
    "Hook_0": "[playfully]", "Hook_3": "[warmly]", "Hook_4": "[mysterious]",
    "Wheel_3": "[curious]", "Wheel_6": "[surprised]",
    "Careless_1": "[thoughtful]", "Careless_2": "[playfully]",
    "Multiply_0": "[excited]", "Multiply_5": "[amazed]",
    "Gandhi_0": "[amused]",
    "House_4": "[thoughtful]",
    "Judges_2": "[serious]", "Judges_3": "[surprised]",
    "Why_0": "[curious]", "Why_4": "[serious]", "Why_6": "[playfully]",
    "Limits_0": "[serious]",
    "Defense_0": "[thoughtful]", "Defense_3": "[warmly]",
    "Close_2": "[amused]", "Close_4": "[thoughtful]", "Close_5": "[warmly]", "Close_6": "[mysterious]",
}

# sahne -> (bölüm adı, tahta, ekranda, soru / bağ)
SAHNE = {
    "Hook": ("Pick a number", "defter", "çark 65'te durur; soru; kenar notu; geri sayım", "açar: çark seni oynattı mı?"),
    "Wheel": ("The wheel from 1974", "defter", "iki cetvel: çıpa 10 → 25, çıpa 65 → 45", "ama: belki dikkatsizdiler"),
    "Careless": ("Were they careless?", "defter", "para ödülü; etki azalmadı", "bu yüzden: kendin dene"),
    "Multiply": ("Five seconds", "defter", "8×…×1 / 1×…×8; ölçekli çubuklar", "ama: saçma sayı etkilemez, değil mi?"),
    "Gandhi": ("A ridiculous number", "defter", "yaş cetveli, 140'ta çıpa", "ama: uzmanlar fark eder?"),
    "House": ("What about experts?", "defter", "ev, kitapçık, iki liste fiyatı", "ama: fiyat bilgi taşır → daha zor örnek"),
    "Judges": ("Even judges", "defter", "12 / 34 ay talebi, 8 ay fark, zar", "bu yüzden: neden?"),
    "Why": ("Why it pulls", "defter", "araba sözcükleri; votka termometresi", "ama: her sayı etkiler mi?"),
    "Limits": ("Where it breaks", "defter", "arka plan sayısı / karşılaştır-tahmin et", "bu yüzden: korunabilir misin?"),
    "Defense": ("Can you defend yourself?", "defter", "uyarı; karşı nedenler; iki adım", "kapanır: senin cevabın"),
    "Close": ("Your number", "defter", "54/193 nokta; itiraf; soru; uçak", "kapanır: çark; köprü: video 2"),
}

META = {
    "baslik": "Why Your First Number Traps You",
    "notlar": """Omurga: **D (deney) + T (tuzak)**: izleyici oynar → 1974 sonucu → ama dikkatsizlik? → kendin dene → uzmanlar → neden → sınır → korunma → izleyicinin cevabı.

ABT: İlk duyduğumuz sayının ilgisiz olduğunu bilsek de **ve** onu yok sayacağımızı sansak da, **ama** deneylerde tahminler ona doğru kayıyor, **bu yüzden** kendi tahminini önce yapmak ve karşı nedenleri sormak denemeye değer.""",
}

WH = P(-.8, .05)
DILIM = [10, 80, 35, 5, 90, 65, 20, 50, 75, 40]


class Sahne(Marj):
    def cark(self, o, r):
        """Çark gövdesi (döner parçalar) ve sabit ibre."""
        a = TAU / len(DILIM)
        dilim, sayi = VGroup(), VGroup()
        for k, v in enumerate(DILIM):
            renk = ["teal", "card", "orange", "card"][k % 4]
            s = AnnularSector(inner_radius=0, outer_radius=r, angle=a, start_angle=k * a, color=self.c["ink"], stroke_width=4)
            s.set_fill(self.c[renk], 1 if renk == "card" else .45).set_stroke(self.c["ink"], 4).shift(o)
            dilim.add(s)
            m = (k + .5) * a
            sayi.add(self.t(str(v), int(21 * r), "ink").rotate(m - PI / 2).move_to(o + r * .72 * P(np.cos(m), np.sin(m))))
        orta = Dot(o, radius=r * .07, color=self.c["ink"])
        ibre = Polygon(o + P(0, r - .22), o + P(-.28, r + .38), o + P(.28, r + .38), color=self.c["ink"], stroke_width=4)
        ibre.set_fill(self.c["red"], 1).set_z_index(5)
        return dilim, sayi, orta, ibre

    @staticmethod
    def hedef_aci(v):
        """Çarkı v dilimi tepeye gelecek şekilde döndüren açı (negatif, üç tur)."""
        m = (DILIM.index(v) + .5) * TAU / len(DILIM)
        return -3 * TAU + (PI / 2 - m) % TAU


class Hook(Sahne):
    def construct(self):
        dilim, sayi, orta, ibre = self.cark(WH, 2.35)
        govde = VGroup(dilim, sayi, orta)
        self.say(0, [self.ciz(dilim), FadeIn(sayi), FadeIn(orta), FadeIn(ibre)],
                 Rotate(govde, self.hedef_aci(65), about_point=WH, rate_func=rate_functions.ease_out_cubic))
        buyuk = VGroup(self.halka(1.15, P(4.4, .2), "orange", 9), self.t("65", 150, "orange", P(4.4, .2)))
        self.say(1, [self.ciz(buyuk[0]), FadeIn(buyuk[1], scale=1.6)])
        hedef = P(-2.9, -.15)
        tam = VGroup(govde, ibre)
        soru = VGroup(self.t("African countries", 56, "ink", P(3.0, 2.1)), self.t("in the United Nations", 56, "ink", P(3.0, 1.25)),
                      self.t("higher or lower than 65%?", 56, "orange", P(3.0, .1)))
        oklar = VGroup(self.ok(P(1.4, -1.9), P(1.4, -.85), "teal", 10, .35), self.ok(P(4.6, -.85), P(4.6, -1.9), "teal", 10, .35),
                       self.t("higher?", 40, "teal", P(1.4, -2.45)), self.t("lower?", 40, "teal", P(4.6, -2.45)))
        self.say(2, [FadeOut(buyuk), tam.animate.scale(.66, about_point=WH).shift(hedef - WH)], self.yaz(soru), FadeIn(oklar))
        nott = self.kenar_notu(["my guess:", "_____ %"], .2)
        kalemlik = self.t("your exact %", 54, "teal", P(3.0, -1.5))
        self.say(3, [FadeOut(oklar), self.yaz(kalemlik)], FadeIn(nott, shift=LEFT * .4))
        self.geri_say(4, P(3.0, -2.55))
        capa = self.capa(P(2.0, -.1), 2.3)
        etiket = self.t("65", 60, "orange", P(2.0, 2.0))
        ip = self.halat(capa[0].get_left(), nott.get_right() + P(0, -.1), sark=2.9)
        q = self.t("did it move you?", 62, "ink", P(3.4, -2.6))
        self.say(4, [FadeOut(soru), FadeOut(kalemlik), FadeOut(tam)], [FadeIn(capa, shift=DOWN), FadeIn(etiket, shift=DOWN)],
                 Create(ip), self.yaz(q))
        self.end()


class Wheel(Sahne):
    def construct(self):
        bas = self.baslik("A wheel and a question")
        yil = self.t("1974", 130, "orange", P(1.1, 1.5))
        kisi = VGroup(self.adam(P(-1.4, -2.3), 1.05), self.t("Amos Tversky", 40, "ink", P(-1.4, -2.75)),
                      self.adam(P(3.6, -2.3), 1.05, "teal"), self.t("Daniel Kahneman", 40, "teal", P(3.6, -2.75)))
        self.say(0, self.yaz(bas), FadeIn(yil, scale=1.4), FadeIn(kisi))
        o = P(-1.6, -.25)
        dilim, sayi, orta, ibre = self.cark(o, 1.9)
        izleyen = self.adam(P(3.7, -1.9), 1.25)
        aralik = self.t("rigged: only 10 or 65", 46, "teal", P(2.4, 2.05))
        self.say(1, [FadeOut(yil), FadeOut(kisi), self.ciz(dilim), FadeIn(sayi), FadeIn(orta), FadeIn(ibre), FadeIn(izleyen)],
                 [Rotate(VGroup(dilim, sayi, orta), self.hedef_aci(65), about_point=o, rate_func=rate_functions.ease_out_cubic),
                  FadeIn(aralik)])
        orta_kart = VGroup(self.kart(2.1, 1.3, P(-1.5, 0)), self.t("65", 80, "orange", P(-1.5, 0)))
        yukari = VGroup(self.ok(P(-1.5, .85), P(-1.5, 2.0), "teal", 9, .32), self.t("higher", 44, "teal", P(-.1, 1.55)))
        asagi = VGroup(self.ok(P(-1.5, -.85), P(-1.5, -2.0), "teal", 9, .32), self.t("lower", 44, "teal", P(-.1, -1.55)))
        adimlar = VGroup(self.t("1.  higher or lower?", 52, "ink", P(3.9, .8)), self.t("2.  your estimate", 52, "ink", P(3.9, -.5)))
        self.say(2, [FadeOut(VGroup(dilim, sayi, orta, ibre)), FadeOut(izleyen), FadeOut(aralik), FadeIn(orta_kart)],
                 [FadeIn(yukari), FadeIn(asagi), self.yaz(adimlar[0])], self.yaz(adimlar[1]))
        yA, yB = .95, -1.75
        ca, ea, XA = self.cetvel(yA)
        cb, eb, XB = self.cetvel(yB)
        ga = self.t("group A: wheel gives 10", 42, "ink", P(4.8, yA + .95))
        gb = self.t("group B: wheel gives 65", 42, "ink", P(4.8, yB + .95))
        self.say(3, [FadeOut(orta_kart), FadeOut(yukari), FadeOut(asagi), FadeOut(adimlar)],
                 [self.ciz(ca), FadeIn(ea), FadeIn(ga)], [Create(cb), FadeIn(eb), FadeIn(gb)])

        def cek(X, y, a, b, no):
            capa = self.capa(X(a) + P(0, -.62), .72)
            av = self.t(str(a), 38, "orange", X(a) + P(-.65 if no == 0 else .65, -.55))
            pin = self.igne(X(a))
            ip = always_redraw(lambda: self.halat(capa[0].get_center(), pin[0].get_start() + P(0, .15), sark=.3))
            return capa, av, pin, ip

        ac, aav, apin, aip = cek(XA, yA, 10, 25, 0)
        self.add(aip)
        s25 = self.t("25%", 62, "teal", XA(25) + P(0, 1.02))
        self.say(4, [FadeIn(ac, shift=DOWN * .4), FadeIn(aav), FadeIn(apin)],
                 apin.animate.shift(XA(25) - XA(10)), FadeIn(s25, scale=1.4))
        bc, bav, bpin, bip = cek(XB, yB, 65, 45, 1)
        self.add(bip)
        s45 = self.t("45%", 62, "teal", XB(45) + P(0, 1.02))
        self.say(5, [FadeIn(bc, shift=DOWN * .4), FadeIn(bav), FadeIn(bpin)],
                 bpin.animate.shift(XB(45) - XB(65)), FadeIn(s45, scale=1.4))
        ym = -.1
        fark = VGroup(DashedLine(XA(25) + P(0, -.1), P(XA(25)[0], ym), color=self.c["gray"], stroke_width=4),
                      DashedLine(XB(45) + P(0, 1.45), P(XA(45)[0], ym), color=self.c["gray"], stroke_width=4),
                      self.ok(P(XA(35)[0], ym), P(XA(25)[0], ym), "red", 7), self.ok(P(XA(35)[0], ym), P(XA(45)[0], ym), "red", 7))
        puan = self.t("20 points", 52, "red", P(XA(63)[0], ym - .02))
        bos = self.t("an irrelevant number", 40, "gray", P(4.8, 2.65))
        self.say(6, FadeIn(bos), Create(fark), self.yaz(puan))
        self.end()


class Careless(Sahne):
    def construct(self):
        bas = self.baslik("Were they just careless?")
        para = VGroup(*[VGroup(Ellipse(width=1.7, height=.5, color=self.c["ink"], stroke_width=5).set_fill(self.c["orange"], .75)
                               .move_to(P(-2.4 + dx, -1.35 + .3 * k))) for dx, n in ((-1.0, 3), (1.0, 6)) for k in range(n)])
        odul = self.t("pay for accuracy", 56, "ink", P(-2.3, 1.6))
        kart = self.kart(5.0, 2.8, P(3.7, .1))
        soru = self.t("smaller effect?", 54, "ink", P(3.7, .85))
        hayir = self.t("NO", 110, "red", P(3.7, -.45))
        rapor = self.t("the 1974 report", 36, "gray", P(3.7, 1.95))
        self.say(0, [self.yaz(bas), FadeIn(para, lag_ratio=.15)], FadeIn(odul), [FadeIn(kart), FadeIn(soru), FadeIn(rapor)],
                 FadeIn(hayir, scale=1.8))
        sonra = VGroup(self.kart(10.2, 3.6, P(1.1, .1), "teal", 6), self.t("later work, 2010", 40, "gray", P(1.1, 1.3)),
                       self.t("incentives can help", 72, "teal", P(1.1, .2)),
                       self.t("when people know which way to adjust", 46, "ink", P(1.1, -.95)))
        self.say(1, [FadeOut(VGroup(para, odul, kart, soru, hayir, rapor)), FadeIn(sonra[:2])], self.yaz(sonra[2]), FadeIn(sonra[3]))
        sira = VGroup(self.t("your turn", 130, "teal", P(1.1, .55)), self.t("get ready: five seconds", 50, "ink", P(1.1, -1.2)))
        self.say(2, FadeOut(sonra), self.yaz(sira[0]), FadeIn(sira[1]))
        self.end()


class Multiply(Sahne):
    def construct(self):
        bas = self.baslik("Five seconds")
        buyuk = self.t("8 × 7 × 6 × 5 × 4 × 3 × 2 × 1", 62, "ink", P(1.2, .7))
        cerceve = self.kart(10.4, 2.0, P(1.2, .7))
        self.say(0, [self.yaz(bas), FadeIn(cerceve)], self.yaz(buyuk), extra=.2)
        self.geri_say(5, P(1.1, -1.7))
        tahta_yazi = self.t("high school students · five seconds", 46, "teal", P(1.1, 2.15))
        self.say(1, FadeIn(tahta_yazi))
        ust = VGroup(cerceve, buyuk)
        k2 = self.kart(8.2, 1.45, P(-.5, -1.5))
        ikinci = self.t("1 × 2 × 3 × 4 × 5 × 6 × 7 × 8", 52, "ink", P(-.5, -1.5))
        k1 = self.kart(8.2, 1.45, P(-.5, .85))
        birinci = self.t("8 × 7 × 6 × 5 × 4 × 3 × 2 × 1", 52, "ink", P(-.5, .85))
        g1 = self.t("one group saw:", 36, "gray", P(-3.0, 1.92))
        g2 = self.t("another group saw:", 36, "gray", P(-2.75, -.43))
        self.say(2, [FadeOut(tahta_yazi), ReplacementTransform(ust, VGroup(k1, birinci)), FadeIn(g1)],
                 [FadeIn(k2), FadeIn(g2)], self.yaz(ikinci))
        baslik_m = self.t("median guess", 34, "gray", P(5.45, 1.92))
        s1 = self.t("2,250", 82, "teal", P(5.45, .85))
        s2 = self.t("512", 82, "teal", P(5.45, -1.5))
        self.say(3, [FadeIn(baslik_m), FadeIn(s1, scale=1.5)])
        self.say(4, FadeIn(s2, scale=1.5))
        x0, tam = -1.2, 6.6
        satir = VGroup()
        for ad, deger, yazi, renk, y in (("8 first", 2250, "2,250", "teal", 1.35), ("1 first", 512, "512", "teal", 0),
                                         ("real answer", 40320, "40,320", "orange", -1.35)):
            w = tam * deger / 40320
            cubuk = Rectangle(width=w, height=.62, stroke_width=0).set_fill(self.c[renk], 1).move_to(P(x0 + w / 2, y))
            etiket = self.t(ad, 48, "ink", P(-3.0, y))
            sayi = self.t(yazi, 52, renk)
            sayi.move_to(P(x0 + w + .25 + sayi.width / 2, y)) if deger < 40000 else sayi.move_to(P(x0 + w - 1.2, y - .75))
            satir.add(VGroup(etiket, cubuk, sayi))
        olcek = self.t("bars drawn to scale", 30, "gray", P(5.6, 2.25))
        self.say(5, [FadeOut(VGroup(k1, birinci, k2, ikinci, g1, g2, baslik_m, s1, s2)), FadeIn(satir[0]), FadeIn(satir[1])],
                 [GrowFromEdge(satir[2][1], LEFT), FadeIn(satir[2][0]), FadeIn(olcek)], FadeIn(satir[2][2], scale=1.5))
        sol = VGroup(self.kart(5.0, 3.0, P(-1.8, .25)), self.t("8 × 7 × 6", 66, "ink", P(-1.8, 1.0)),
                     self.t("= 336 so far", 62, "teal", P(-1.8, -.4)))
        sag = VGroup(self.kart(5.0, 3.0, P(4.1, .25)), self.t("1 × 2 × 3", 66, "ink", P(4.1, 1.0)),
                     self.t("= 6 so far", 62, "teal", P(4.1, -.4)))
        alt = self.t("then adjust upward... and stop too soon", 52, "orange", P(1.1, -2.35))
        ornek = self.t("example: the first three steps", 36, "gray", P(1.1, 2.3))
        self.say(6, [FadeOut(satir), FadeOut(olcek), FadeIn(sol), FadeIn(ornek)], FadeIn(sag), self.yaz(alt))
        self.end()


class Gandhi(Sahne):
    def construct(self):
        bas = self.baslik("A ridiculous number")
        sayi = self.t("140", 220, "orange", P(1.1, .35))
        sacma = self.t("nonsense, right?", 60, "ink", P(1.1, -2.1))
        self.say(0, self.yaz(bas), FadeIn(sayi, scale=1.5), self.yaz(sacma))
        c, e, X = self.cetvel(-1.0, -3.9, 6.6, 150, 10, (0, 50, 100, 150))
        soru = self.t("Mahatma Gandhi: how old?", 60, "ink", P(1.1, 2.2))
        c9 = VGroup(self.capa(X(9) + P(0, .95), 1.15, "teal"), self.t("9", 54, "teal", X(9) + P(0, 2.05)))
        c140 = VGroup(self.capa(X(140) + P(0, .95), 1.15), self.t("140", 54, "orange", X(140) + P(0, 2.05)))
        self.say(1, [FadeOut(sacma), FadeOut(sayi), self.yaz(soru)], [Create(c), FadeIn(e)],
                 [FadeIn(c9, shift=DOWN), FadeIn(c140, shift=DOWN)])
        p50, p67 = self.igne(X(50), "teal"), self.igne(X(67), "orange")
        y50 = self.t("after 9: about 50", 44, "teal", P(-.75, .75))
        y67 = self.t("after 140: about 67", 44, "orange", P(3.0, -.05))
        bag = VGroup(self.cizgi(X(50) + P(-.05, .75), P(-.65, .45), "teal", 3, 0),
                     self.cizgi(X(67) + P(.2, .55), P(1.25, -.1), "orange", 3, 0))
        not2 = self.t("average estimates, Strack & Mussweiler", 32, "gray", P(1.1, -2.45))
        self.say(2, [FadeIn(p67, shift=RIGHT), FadeIn(y67), Create(bag[1])], [FadeIn(p50, shift=LEFT), FadeIn(y50), Create(bag[0])],
                 FadeIn(not2))
        self.end()


class House(Sahne):
    def ev(self, o):
        r = self.c
        govde = self.kart(2.6, 1.9, o + P(0, -.35))
        cati = Polygon(o + P(-1.65, .6), o + P(0, 1.85), o + P(1.65, .6), color=r["ink"], stroke_width=6).set_fill(r["orange"], .6)
        kapi = self.kart(.6, 1.0, o + P(-.55, -.8), dolgu="bg")
        cam = VGroup(self.kart(.75, .7, o + P(.55, -.1), dolgu="bg"), self.cizgi(o + P(.55, -.45), o + P(.55, .25), "ink", 3, 0),
                     self.cizgi(o + P(.18, -.1), o + P(.92, -.1), "ink", 3, 0))
        return VGroup(govde, cati, kapi, cam)

    def construct(self):
        bas = self.baslik("What about experts?")
        uzman = self.adam(P(1.1, -2.0), 1.5)
        canta = self.kart(1.1, .75, P(2.25, -1.0), "ink", 5, "teal")
        balon = self.t("\"I'd see through it\"", 56, "teal", P(1.1, 1.9))
        self.say(0, [self.yaz(bas), FadeIn(uzman), FadeIn(canta)], FadeIn(balon))
        ev = self.ev(P(-2.6, -.1))
        sayfa = VGroup(*[self.kart(2.2, 2.8, P(2.3 + .09 * k, -.2 + .09 * k)) for k in range(4, -1, -1)])
        satirlar = VGroup(*[self.cizgi(P(1.55, y), P(3.05, y), "gray", 4) for y in (.7, .25, -.2, -.65, -1.1)])
        on = self.t("10 pages", 52, "ink", P(2.4, -2.2))
        kim = self.t("Northcraft & Neale, 1987", 46, "teal", P(-1.8, 2.25))
        self.say(1, [FadeOut(uzman), FadeOut(canta), FadeOut(balon), FadeIn(kim)], self.ciz(ev), [FadeIn(sayfa), FadeIn(satirlar), FadeIn(on)])
        orta = DashedLine(P(.3, -.15), P(6.9, -.15), color=self.c["gray"], stroke_width=6)
        deger = self.t("appraisal value", 40, "gray", P(5.4, .22))
        yuksek = VGroup(self.kart(3.5, 1.0, P(5.0, 1.35), "orange", 6), self.t("listed: $83,900", 46, "orange", P(5.0, 1.35)))
        alcak = VGroup(self.kart(3.5, 1.0, P(5.0, -1.65), "teal", 6), self.t("listed: $65,900", 46, "teal", P(5.0, -1.65)))
        ornek = self.t("two of the study's prices", 30, "gray", P(5.0, -2.5))
        self.say(2, [FadeOut(sayfa), FadeOut(satirlar), FadeOut(on), Create(orta), FadeIn(deger)], FadeIn(yuksek, shift=DOWN * .3),
                 [FadeIn(alcak, shift=UP * .3), FadeIn(ornek)])
        yukari = VGroup(*[Dot(P(x, -.15), radius=.16, color=self.c["orange"]) for x in (.85, 1.4, 1.95)])
        asagi = VGroup(*[Dot(P(x, -.15), radius=.16, color=self.c["teal"]) for x in (.85, 1.4, 1.95)])
        kime = VGroup(self.t("agents", 44, "ink", P(-3.5, -2.35)), self.t("+ non-experts", 44, "ink", P(-.9, -2.35)))
        self.say(3, [FadeIn(yukari), FadeIn(asagi), FadeIn(kime[0])],
                 [yukari.animate.shift(P(1.25, .82)), asagi.animate.shift(P(1.25, -.82))], FadeIn(kime[1]))
        adil = VGroup(self.kart(9.6, 2.5, P(1.1, -.2), "ink", 5), self.t("a listing price can be real information", 42, "ink", P(1.1, .35)),
                      self.t("next: a harder case", 54, "orange", P(1.1, -.8)))
        self.say(4, FadeOut(VGroup(ev, orta, deger, yuksek, alcak, ornek, yukari, asagi, kime, kim)), FadeIn(adil[:2]), self.yaz(adil[2]))
        self.end()


class Judges(Sahne):
    def tokmak(self, o):
        bas = self.kart(1.0, .5, o, "ink", 5, "orange").rotate(-PI / 4.5, about_point=o)
        sap = self.cizgi(o + P(-.12, -.18), o + P(-.75, -.95), "ink", 9, 0)
        return VGroup(sap, bas)

    def zar(self, o, n):
        yer = {1: [(0, 0)], 2: [(-1, 1), (1, -1)], 3: [(-1, 1), (0, 0), (1, -1)], 4: [(-1, 1), (1, 1), (-1, -1), (1, -1)],
               5: [(-1, 1), (1, 1), (0, 0), (-1, -1), (1, -1)], 6: [(-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, -1)]}
        return VGroup(self.kart(1.35, 1.35, o, "ink", 5),
                      *[Dot(o + .36 * P(x, y), radius=.11, color=self.c["ink"]) for x, y in yer[n]])

    def construct(self):
        bas = self.baslik("Even judges")
        yargic = self.adam(P(-2.6, -2.15), 1.4)
        tok = self.tokmak(P(-1.2, .1))
        kim = VGroup(self.t("trial judges", 52, "ink", P(-2.4, 2.15)), self.t("15+ years, on average", 42, "teal", P(-2.4, 1.4)))
        dosya = VGroup(self.kart(3.0, 2.2, P(2.3, -.5), "ink", 5), self.t("criminal", 50, "ink", P(2.3, -.2)),
                       self.t("case", 50, "ink", P(2.3, -.95)))
        varsayim = self.t("(hypothetical)", 34, "gray", P(2.3, -1.95))
        self.say(0, [self.yaz(bas), FadeIn(yargic), FadeIn(tok)], FadeIn(kim), [FadeIn(dosya, shift=UP * .3), FadeIn(varsayim)])
        ogr = self.adam(P(5.6, -2.15), 1.2, "teal")
        ograd = VGroup(self.t("computer science", 40, "teal", P(2.9, -1.35)), self.t("student", 40, "teal", P(2.9, -1.95)))
        balon = VGroup(self.kart(3.7, 1.5, P(4.3, 1.55), "teal", 6), self.t("\"I demand", 44, "teal", P(4.3, 1.88)),
                       self.t("___ months\"", 44, "teal", P(4.3, 1.25)))
        self.say(1, [FadeOut(dosya), FadeOut(varsayim), FadeIn(ogr), FadeIn(ograd)], FadeIn(balon))
        d12 = VGroup(self.kart(3.8, 1.5, P(-1.7, 1.35), "teal", 6), self.t("demand: 12", 62, "teal", P(-1.7, 1.35)))
        d34 = VGroup(self.kart(3.8, 1.5, P(3.9, 1.35), "orange", 6), self.t("demand: 34", 62, "orange", P(3.9, 1.35)))
        aylar = VGroup(*[self.kart(.92, .92, P(-2.45 + 1.02 * k, -.95), "orange", 5, "card") for k in range(8)])
        for k, kutu in enumerate(aylar):
            kutu.set_fill(self.c["orange"], .55 if k < 7 else .2)
        fark = self.t("almost 8 months longer", 62, "orange", P(1.1, -2.35))
        sonra = self.t("sentences after 34, compared with after 12:", 38, "gray", P(1.1, .05))
        kaynak = self.t("as reported by the researchers", 30, "gray", P(1.1, -3.05))
        self.say(2, [FadeOut(VGroup(yargic, tok, kim, ogr, ograd, balon)), FadeIn(d12), FadeIn(d34)],
                 [FadeIn(sonra), FadeIn(aylar, lag_ratio=.2)], [self.yaz(fark), FadeIn(kaynak)])
        zarlar = VGroup(self.zar(P(-2.6, .35), 3), self.zar(P(-1.05, -.15), 6))
        o1 = self.ok(P(.05, .1), P(1.5, .1), "ink", 8, .3)
        talep = VGroup(self.kart(2.0, 1.2, P(2.7, .1), "orange", 6), self.t("demand", 44, "orange", P(2.7, .1)))
        o2 = self.ok(P(3.9, .1), P(5.2, .1), "ink", 8, .3)
        son = VGroup(self.tokmak(P(6.3, .55)), self.t("sentence", 44, "ink", P(6.0, -1.1)))
        alt = self.t("looked random, secretly loaded", 52, "red", P(1.1, -2.35))
        genc = self.t("junior lawyers", 44, "ink", P(-1.8, 1.7))
        self.say(3, [FadeOut(VGroup(d12, d34, aylar, fark, sonra, kaynak)), FadeIn(zarlar, shift=DOWN), FadeIn(genc)],
                 [Create(o1), FadeIn(talep)], [Create(o2), FadeIn(son), self.yaz(alt)])
        self.end()


class Why(Sahne):
    def sozcuk(self, s, pos, renk="gray", w=2.6):
        return VGroup(self.kart(w, .95, pos, renk, 6 if renk != "gray" else 3), self.t(s, 48, renk, pos))

    def construct(self):
        bas = self.baslik("Why does it pull?")
        capa = self.capa(P(-.6, -.2), 2.6)
        q = self.t("?", 220, "ink", P(3.1, -.1))
        self.say(0, [self.yaz(bas), FadeIn(capa, shift=DOWN)], self.yaz(q))
        kisi = self.adam(P(-2.9, -2.4), 1.35)
        balon = VGroup(self.kart(4.4, 1.3, P(-1.6, 1.55), "orange", 6), self.t("\"more than 65?\"", 50, "orange", P(-1.6, 1.55)))
        gercek = VGroup(*[self.sozcuk(s, P(3.6 + .35 * k, .55 - 1.2 * k), "teal", 5.3)
                          for k, s in enumerate(("so many countries...", "a huge continent...", "I can name lots..."))])
        gel = self.t("example thoughts that fit \"more\"", 40, "gray", P(2.8, -2.85))
        self.say(1, [FadeOut(capa), FadeOut(q), FadeIn(kisi), FadeIn(balon)],
                 LaggedStart(*[FadeIn(g, shift=LEFT * 1.2, scale=.6) for g in gercek], lag_ratio=.4), FadeIn(gel))
        soru = self.t("average price of a German car?", 52, "ink", P(1.1, 2.25))
        sol = VGroup(self.kart(4.2, 1.1, P(-1.8, .95), "orange", 6), self.t("vs 40,000 marks", 48, "orange", P(-1.8, .95)))
        sag = VGroup(self.kart(4.2, 1.1, P(4.1, .95), "teal", 6), self.t("vs 20,000 marks", 48, "teal", P(4.1, .95)))
        self.say(2, [FadeOut(VGroup(kisi, balon, gercek, gel)), self.yaz(soru)], FadeIn(sol), FadeIn(sag))
        merc = self.sozcuk("Mercedes", P(-1.8, -.65), "orange", 3.0)
        bmw = self.sozcuk("BMW", P(-1.8, -1.85), "orange", 3.0)
        hizli = self.t("reported: faster", 36, "gray", P(-1.8, -2.75))
        self.say(3, [FadeIn(merc, scale=1.4), FadeIn(hizli)], FadeIn(bmw, scale=1.4))
        vw = self.sozcuk("VW", P(4.1, -.65), "teal", 3.0)
        hizli2 = self.t("reported: faster", 36, "gray", P(4.1, -1.65))
        yeniden = VGroup(self.kart(5.2, .95, P(4.1, -2.6), "red", 6), self.t("2019 retest: not found", 42, "red", P(4.1, -2.6)))
        self.say(4, [FadeIn(vw, scale=1.4), FadeIn(hizli2)], FadeIn(yeniden, scale=1.3))
        acik = VGroup(self.t("anchoring still appeared", 70, "teal", P(1.1, .9)), self.t("why it happens: still open", 70, "orange", P(1.1, -.6)),
                      self.t("the retest's word task may be too weak to decide", 36, "gray", P(1.1, -2.1)))
        self.say(5, [FadeOut(VGroup(soru, sol, sag, merc, bmw, hizli, vw, hizli2, yeniden)), FadeIn(acik[0])], self.yaz(acik[1]), FadeIn(acik[2]))
        x = -2.2
        tup = VGroup(self.kart(.75, 4.3, P(x, .0), "ink", 5), Dot(P(x, -2.35), radius=.55, color=self.c["teal"]),
                     Line(P(x, -2.2), P(x, 1.0), color=self.c["teal"], stroke_width=26))
        sifir = VGroup(self.cizgi(P(x - .65, 1.0), P(x + .9, 1.0), "orange", 7, 0),
                       self.t("water freezes: 0 °C", 52, "orange", P(2.4, 1.0)))
        votka = self.t("vodka freezes: ?", 56, "ink", P(2.4, 2.25))
        self.say(6, [FadeOut(acik), FadeIn(tup), self.yaz(votka)], FadeIn(sifir))
        asagi = self.ok(P(-1.0, .8), P(-1.0, -.75), "teal", 10, .34)
        dur = VGroup(DashedLine(P(-1.7, -.9), P(.4, -.9), color=self.c["teal"], stroke_width=6),
                     self.t("your guess stops here", 46, "teal", P(3.4, -.9)))
        otesi = VGroup(DashedLine(P(-1.7, -2.15), P(.4, -2.15), color=self.c["red"], stroke_width=6),
                       self.t("often not far enough", 46, "red", P(3.4, -2.15)))
        self.say(7, Create(asagi), FadeIn(dur), FadeIn(otesi))
        self.end()


class Limits(Sahne):
    def construct(self):
        bas = self.baslik("Where it breaks")
        kisi = self.adam(P(1.1, -2.2), 1.4)
        sayilar = VGroup(*[self.t(s, 56, "gray", P(x, y)) for s, x, y in
                           (("47", -3.2, 1.4), ("9", -1.6, -.6), ("213", 4.1, 1.6), ("68", 5.8, -.3), ("5", 3.4, -1.7), ("31", -3.4, -2.0),
                            ("84", .2, 2.1))])
        self.say(0, [self.yaz(bas), FadeIn(kisi)], FadeIn(sayilar, lag_ratio=.2))
        sol = self.kart(5.3, 4.9, P(-1.8, -.35))
        sag = self.kart(5.3, 4.9, P(4.2, -.35))
        a = VGroup(self.t("a number just", 48, "ink", P(-1.8, 1.5)), self.t("in the background", 48, "ink", P(-1.8, .75)),
                   self.t("47", 72, "gray", P(-1.8, -.35)), self.t("no reliable effect", 50, "red", P(-1.8, -1.55)),
                   self.t("3 studies · Shanks et al., 2020", 34, "gray", P(-1.8, -2.4)))
        self.say(1, [FadeOut(kisi), FadeOut(sayilar), FadeIn(sol)], FadeIn(a[:3]), FadeIn(a[3:]))
        b = VGroup(self.t("compare first,", 48, "ink", P(4.2, 1.5)), self.t("then estimate", 48, "ink", P(4.2, .75)))
        tik = VGroup(self.cizgi(P(3.5, -.3), P(4.0, -.85), "teal", 14, 0), self.cizgi(P(4.0, -.85), P(5.1, .15), "teal", 14, 0))
        saglam = VGroup(self.t("robust", 50, "teal", P(4.2, -1.55)), self.t("same 2020 paper", 34, "gray", P(4.2, -2.4)))
        self.say(2, [FadeIn(sag), FadeIn(b)], [Create(tik), FadeIn(saglam)])
        genis = self.kart(9.6, 5.1, P(1.1, -.35))
        ust = self.t("Many Labs: hint first, then estimate", 50, "ink", P(1.1, 1.45))
        orneklem = self.t("36 samples", 44, "ink", P(1.1, .55))
        noktalar = VGroup(*[Dot(P(-.55 + .3 * (k % 12), -.15 - .3 * (k // 12)), radius=.09, color=self.c["teal"]) for k in range(36)])
        kisi_s = self.t("6,344 participants", 44, "ink", P(1.1, -1.45))
        sonuc = self.t("anchoring appeared", 60, "teal", P(1.1, -2.35))
        self.say(3, [FadeOut(VGroup(sol, a, sag, b, tik, saglam)), FadeIn(genis), FadeIn(ust)],
                 [FadeIn(orneklem), FadeIn(noktalar, lag_ratio=.05), FadeIn(kisi_s)], FadeIn(sonuc))
        self.end()


class Defense(Sahne):
    def construct(self):
        bas = self.baslik("Can you defend yourself?")
        ucgen = Polygon(P(-.9, -1.4), P(1.1, 1.9), P(3.1, -1.4), color=self.c["orange"], stroke_width=12).set_fill(self.c["orange"], .2)
        unlem = self.t("!", 150, "orange", P(1.1, -.25))
        yazi = self.t("\"just watch out for it\"", 58, "ink", P(1.1, -2.35))
        self.say(0, [self.yaz(bas), self.ciz(ucgen)], [FadeIn(unlem), FadeIn(yazi)])
        uyari = VGroup(self.kart(8.4, 1.25, P(1.1, 1.45), "orange", 6), self.t("warned + told which way it pulls", 52, "ink", P(1.1, 1.45)))
        c1, e1, X = self.cetvel(-1.35, -3.0, 5.2, 100, 10, ())
        ip = VGroup(self.capa(X(80) + P(0, -.75), .8), self.igne(X(58)), self.halat(X(80) + P(0, -.35), X(58) + P(0, .1)))
        ayni = self.t("the pull did not go away", 54, "red", P(1.1, .0))
        self.say(1, [FadeOut(ucgen), FadeOut(unlem), FadeOut(yazi), FadeIn(uyari)], [Create(c1), FadeIn(ip)], self.yaz(ayni))
        araba = VGroup(
            Polygon(P(-3.7, -1.1), P(-3.7, -.45), P(-3.0, -.35), P(-2.4, .35), P(-1.0, .35), P(-.35, -.35), P(.3, -.5), P(.3, -1.1),
                    color=self.c["ink"], stroke_width=6).set_fill(self.c["teal"], .45),
            *[Circle(.38, color=self.c["ink"], stroke_width=8).set_fill(self.c["card"], 1).move_to(P(x, -1.15)) for x in (-2.85, -.55)])
        kim = self.t("car experts", 52, "ink", P(-1.7, 1.35))
        liste = VGroup(self.kart(5.0, 3.6, P(4.1, .05)), self.t("why this price", 48, "ink", P(4.1, 1.25)),
                       self.t("could be wrong:", 48, "ink", P(4.1, .55)),
                       *[self.cizgi(P(2.3, y), P(5.9, y), "gray", 5, .05) for y in (-.35, -.9, -1.45)])
        az = self.t("pulled less", 70, "teal", P(1.1, -2.45))
        self.say(2, [FadeOut(VGroup(uyari, c1, ip, ayni)), FadeIn(araba), FadeIn(kim)], FadeIn(liste), self.yaz(az))
        aliskanlik = VGroup(self.t("a habit to try", 100, "teal", P(1.1, .7)),
                            self.t("my suggestion, not a proven cure", 50, "gray", P(1.1, -.9)))
        self.say(3, [FadeOut(VGroup(araba, kim, liste, az))], self.yaz(aliskanlik[0]), FadeIn(aliskanlik[1]))
        bir = VGroup(self.kart(10.4, 1.6, P(1.1, .85), "teal", 6), self.t("1.  guess first, before you hear theirs", 46, "ink", P(1.1, .85)))
        iki = VGroup(self.kart(10.4, 1.6, P(1.1, -1.25), "orange", 6), self.t("2.  why might their number be wrong?", 46, "ink", P(1.1, -1.25)))
        self.say(4, [FadeOut(aliskanlik), FadeIn(bir, shift=RIGHT * .5)], FadeIn(iki, shift=RIGHT * .5))
        self.end()


class Close(Sahne):
    def ucak(self, o):
        pts = [(0, 2.0), (.28, 1.6), (.32, .65), (2.9, -.25), (2.9, -.7), (.32, -.3), (.24, -1.35), (1.05, -1.85), (1.05, -2.15),
               (0, -1.95), (-1.05, -2.15), (-1.05, -1.85), (-.24, -1.35), (-.32, -.3), (-2.9, -.7), (-2.9, -.25), (-.32, .65), (-.28, 1.6)]
        g = Polygon(*[o + P(*q) for q in pts], color=self.c["ink"], stroke_width=6).set_fill(self.c["card"], 1)
        return g

    def construct(self):
        bas = self.baslik("Your number")
        noktalar = VGroup(*[Dot(P(-3.6 + .4 * (k % 20), 1.75 - .38 * (k // 20)), radius=.12,
                                color=self.c["orange"] if k < 54 else self.c["gray"]) for k in range(193)])
        aciklama = self.t("54 of 193 members: African Group", 52, "orange", P(.2, -2.45))
        self.say(0, [self.yaz(bas), FadeIn(noktalar[54:])], FadeIn(noktalar[:54], lag_ratio=.1), self.yaz(aciklama))
        nott = self.kenar_notu(["my guess:", "_____ %"], .2)
        kutu = VGroup(self.kart(4.6, 2.5, P(4.8, -.0), "teal", 7), self.t("≈ 28%", 120, "teal", P(4.8, .0)))
        self.say(1, [noktalar.animate.scale(.72, about_point=P(-3.6, 1.75)), FadeIn(nott)], FadeIn(kutu, scale=1.4))
        o = P(-1.7, -.25)
        dilim, sayi, orta, ibre = self.cark(o, 1.9)
        VGroup(dilim, sayi, orta).rotate(self.hedef_aci(65), about_point=o)
        damga = VGroup(self.kart(2.9, 1.1, P(3.6, .7), "red", 8), self.t("STAGED", 70, "red", P(3.6, .7))).rotate(.1)
        tek = self.t("one answer can't show it", 46, "ink", P(3.8, -1.15))
        self.say(2, [FadeOut(VGroup(noktalar, aciklama, kutu)), FadeIn(VGroup(dilim, sayi, orta, ibre))],
                 FadeIn(damga, scale=2.0), FadeIn(tek))

        def grup(x, v, renk):
            kisiler = VGroup(*[self.adam(P(x + dx, -1.75), .75, renk) for dx in (-1.1, 0, 1.1)])
            return VGroup(kisiler, self.capa(P(x, .95), 1.1), self.t(f"start: {v}", 54, "orange", P(x, 2.15)))

        a, b = grup(-1.8, 10, "teal"), grup(4.1, 65, "ink")
        karsi = self.t("compare the groups", 58, "ink", P(1.1, -2.55))
        self.say(3, [FadeOut(VGroup(dilim, sayi, orta, ibre, damga, tek, nott)), FadeIn(a)], FadeIn(b), self.yaz(karsi))
        c, e, X = self.cetvel(-1.7, -3.9, 6.6, 100, 10, ())
        capa = self.capa(X(15) + P(0, .85), 1.2)
        pin = self.igne(X(32))
        ip = self.halat(capa[0].get_center(), pin[0].get_start() + P(0, .15))
        soz = VGroup(self.t("a number you weigh", 76, "orange", P(1.1, 2.0)),
                     self.t("can become your starting point", 62, "ink", P(1.1, .8)))
        self.say(4, [FadeOut(VGroup(a, b, karsi)), self.yaz(soz[0])], [Create(c), FadeIn(capa, shift=DOWN)], [FadeIn(pin), Create(ip), FadeIn(soz[1])])
        yorum = VGroup(self.kart(8.2, 3.0, P(1.1, .15), "teal", 7), self.t("what did you write down?", 66, "ink", P(1.1, .65)),
                       self.t("tell me in the comments", 52, "teal", P(1.1, -.55)))
        kuyruk = Polygon(P(-1.4, -1.34), P(-2.3, -2.35), P(-.4, -1.34), color=self.c["teal"], stroke_width=7).set_fill(self.c["card"], 1)
        self.say(5, [FadeOut(VGroup(c, capa, pin, ip, soz)), FadeIn(yorum[0]), FadeIn(kuyruk)], self.yaz(yorum[1]), FadeIn(yorum[2]))
        ucak = self.ucak(P(-1.2, -.35))
        delik = VGroup(*[Dot(P(-1.2 + x, -.35 + y), radius=.1, color=self.c["red"]) for x, y in
                         ((-2.2, -.38), (-1.7, -.2), (-1.35, -.35), (1.5, -.05), (2.0, -.4), (2.45, -.45), (.05, -.8), (-.08, -.6),
                          (-.6, -1.75), (.55, -1.8), (.1, .25), (-1.0, .05))])
        soru = VGroup(self.t("next time", 50, "gray", P(4.8, 1.25)), self.t("where would you", 56, "ink", P(4.8, .25)),
                      self.t("add armor?", 66, "orange", P(4.8, -.75)))
        eskiz = self.t("sketch", 30, "gray", P(-1.2, -2.95))
        self.say(6, [FadeOut(yorum), FadeOut(kuyruk), self.ciz(ucak), FadeIn(eskiz)], FadeIn(delik, lag_ratio=.2), FadeIn(soru))
        self.wait(1.5)
