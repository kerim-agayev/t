"""Trigonometri videosu. Önce sesler: .venv/Scripts/python video.py  |  sonra render: .venv/Scripts/python render.py [taslak]
Metni değiştirince ilgili ses/<Sahne>_<n>.mp3 dosyasını sil."""
import asyncio
import textwrap
from pathlib import Path

import numpy as np
from manim import *
from mutagen.mp3 import MP3

from kareler import FONT, THEMES, P, line, sketch, text

HERE = Path(__file__).parent
SES = HERE / "ses"

TEXT = {
    "Giris": [
        "Karşında dev bir dağ var. Tepesine çıkman yasak, elinde dağı ölçecek bir metre de yok.",
        "Yine de boyunu hesaplayabilir misin? Tek ihtiyacın bir açı ve bir uzaklık.",
        "Bunu mümkün kılan fikrin adı trigonometri. Birçok öğrencinin gözünü korkutan o konu.",
        "Bu videoda formül ezberlemeyeceğiz. Formüllerin nereden doğduğunu göreceğiz.",
    ],
    "Ucgen": [
        "Güneşli bir günde bir ağaca ve yanındaki çubuğa bak. İkisi de yere gölge bırakıyor.",
        "Güneş ışınları aynı açıyla geldiği için, ortaya iki benzer üçgen çıkar. Biri küçük, biri büyük.",
        "Küçük üçgende yükseklik bölü gölge neyse, büyük üçgende de tam olarak o.",
        "Demek ki bu oran üçgenin büyüklüğüne değil, yalnızca açıya bağlı. Bu orana tanjant diyoruz.",
        "Açı otuz beş derece ise tanjant yaklaşık sıfır virgül yedi. Yüz metre uzaktaki bir kule, göz hizandan yaklaşık yetmiş metre yukarıdadır.",
    ],
    "BirimCember": [
        "Şimdi dünyayı geride bırakalım. Yarıçapı bir birim olan bir çember çizelim.",
        "Üçgenimizi içine yerleştirelim. Uzun kenar çemberin yarıçapı oldu, yani uzunluğu bir.",
        "Böylece yatay kenarın adı kosinüs, dikey kenarın adı sinüs olur.",
        "Açı değiştikçe nokta döner. Sinüs noktanın yüksekliğini, kosinüs ise yatay konumunu anlatır.",
        "Dik üçgende bu açı doksan dereceye ulaşamazdı. Ama çember durmaz. Yüz altmış iki derecede yükseklik hâlâ pozitif, ve on sekiz derecedekiyle aynı.",
        "Bir de Pisagor'u hatırla. Sinüsün karesi artı kosinüsün karesi, her açıda bire eşittir.",
    ],
    "Radyan": [
        "Peki bir tam tur neden üç yüz altmış derece? Bu sayıyı insanlar seçti.",
        "Matematiğin kendi ölçüsünü bulalım. Yarıçapı bir ip gibi al, ve çemberin üzerine sar.",
        "İpin kapladığı açıya bir radyan denir. Bu yaklaşık elli yedi derecedir.",
        "Sarmaya devam et. İki, üç, dört, beş, altı. Ve küçük bir parça daha.",
        "Tam turda yaklaşık altı virgül yirmi sekiz yarıçap var, yani iki pi radyan. Dikkat: pi radyan yarım turdur, bir radyan değil.",
    ],
    "Dalga": [
        "Şimdi videonun en güzel anı. Noktayı döndürelim, ve yüksekliğini sağa doğru adım adım kaydedelim.",
        "İzle. Dönen hareket, gözünün önünde açılıyor.",
        "Bu dalga, sinüs fonksiyonunun grafiği. Tepede bir, dipte eksi bir. Her iki pi'de kendini tekrar eder.",
        "Aynı şeyi yatay konum için yaparsan kosinüs dalgası çıkar. Aynı şekil, yalnızca çeyrek tur önden gidiyor.",
        "Demek ki dönmek ile dalgalanmak, aslında aynı hareketin iki yüzü.",
    ],
    "Ses": [
        "Bir diyapazonun sesi, neredeyse saf bir sinüs dalgasıdır.",
        "Ona daha hızlı ve daha küçük bir dalga ekleyelim. Şekil değişiyor.",
        "Birkaç tane daha. Dalga giderek köşeli bir şekle yaklaşıyor.",
        "Fransız matematikçi Furye'nin açtığı yol sayesinde biliyoruz ki, tekrar eden karmaşık sesler sinüslere ayrılabilir. Müziği sıkıştıran teknolojiler de bu fikrin yakın akrabalarını kullanır.",
    ],
    "Tarih": [
        "Peki sinüs ne demek? Yaklaşık bin beş yüz yıl önce Hintli matematikçi Aryabhata, yarım kirişe cya diyordu.",
        "Kelime Arapçaya ciba olarak geçti. Sesli harfler yazılmayınca, sonradan ceyb diye okundu. Ceyb; koy, kıvrım demekti.",
        "Latince çevirmenler de ona sinus dedi. Yani her sinüs yazdığında, eski bir yanlış okumanın izini taşıyorsun.",
        "Şimdi dağımıza dönelim. Bin sekiz yüz elli ikide Radhanath Sikdar, uzaktan yapılan açı ölçümlerinden Everest'in yüksekliğini hesapladı.",
        "Büyük bir ekip çalışmasıyla bulunan değer, bugünkü ölçüme yalnızca on metre kadar uzaktaydı. Üstelik zirveye henüz kimse çıkmamıştı.",
    ],
    "Tuzak": [
        "Son bir tuzak soru. Sinüs otuz artı altmış, sinüs otuz artı sinüs altmışa eşit mi?",
        "Videoyu durdur, ve birkaç saniye düşün.",
        "Soldaki sinüs doksan, yani bir. Sağdaki ise sıfır virgül beş artı sıfır virgül seksen yedi, yaklaşık bir virgül otuz yedi.",
        "Eşit değil! Çünkü sinüs bir çarpan değil, bir fonksiyon. Çemberi gözünde canlandır: yükseklikler öyle toplanmaz.",
        "Trigonometri bir ezber listesi değil, dönen bir noktanın hikâyesi. Sırada hangi konu olsun? Yorumlara yaz.",
    ],
}
# seslendirme için yazılışı farklı olan sözcüklerin altyazı karşılığı
CAPTION = {"Furye'nin": "Fourier'nin", "cya": "jya", "ciba": "jiba", "ceyb": "jaib", "Ceyb": "Jaib"}


async def voices():
    import edge_tts
    SES.mkdir(exist_ok=True)
    for scene, lines in TEXT.items():
        for i, s in enumerate(lines):
            f = SES / f"{scene}_{i}.mp3"
            if not f.exists():
                await edge_tts.Communicate(s, "tr-TR-AhmetNeural", rate="+10%").save(str(f))
    print(sum(len(s) for v in TEXT.values() for s in v), "karakter")


config.frame_height, config.frame_width = 9.0, 16.0


class Base(Scene):
    theme = "siyah"

    def setup(self):
        self.c = THEMES[self.theme]
        self.camera.background_color = self.c["bg"]
        self.camera.frame_center = P(0, -.5)      # alttaki ek alan altyazı bandı
        self.caption = None

    def say(self, i, *steps, extra=0.3):
        """i. cümleyi seslendirir; adımlar cümle süresine eşit paylaştırılır."""
        name = type(self).__name__
        f = SES / f"{name}_{i}.mp3"
        dur = MP3(f).info.length
        s = TEXT[name][i]
        for a, b in CAPTION.items():
            s = s.replace(a, b)
        if self.caption:
            self.remove(self.caption)
        # 48+ punto Pango satır kaydırması yapıyor; altyazı küçük punto ile
        lines = VGroup(*[Text(t, font=FONT, color=self.c["ink"], font_size=32).scale(22 / 32) for t in textwrap.wrap(s, 96)]).arrange(DOWN, buff=.1)
        lines.move_to(P(0, -4.35))
        back = BackgroundRectangle(lines, color=self.c["bg"], fill_opacity=.88, buff=.12)
        self.caption = VGroup(back, lines).set_z_index(10)
        self.add(self.caption)
        self.add_sound(str(f))
        used = 0
        for step in steps:
            anims = step if isinstance(step, (list, tuple)) else [step]
            rt = round(dur * .92 / len(steps) * 30) / 30
            self.play(*anims, run_time=rt)
            used += rt
        self.wait(max(1 / 30, dur + extra - used))

    def title(self, s):
        t = text(s, self.c["ink"], 38).move_to(P(0, 3.4))
        u = line(t.get_corner(DL) + DOWN * .1, t.get_corner(DR) + DOWN * .1, self.c["yellow"], 7)
        return VGroup(t, u)

    def label(self, s, color, pos, size=32):
        return text(s, self.c[color], size).move_to(pos)

    def ln(self, a, b, color="ink", w=6):
        return line(a, b, self.c[color], w)

    def end(self):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=.6)


def mountain(c):
    base, top, eye = P(3.2, -2.1), P(3.2, 1.6), P(-3.9, -2.1)
    m = sketch(Polygon(P(.4, -2.1), P(2.1, .1), P(2.5, -.2), top, P(4.0, .35), P(4.5, .55), P(6.4, -2.1),
                       color=c["ink"], stroke_width=6).set_fill("#cfd8e3", .55), .03)
    snow = sketch(Polygon(P(2.72, .45), top, P(3.68, .72), P(3.35, .52), P(3.1, .85), color=c["ink"], stroke_width=4).set_fill(WHITE, 1))
    ground = line(P(-6.6, -2.1), P(6.6, -2.1), c["ink"])
    sight = sketch(DashedLine(eye, top, color=c["red"], stroke_width=6, dash_length=.18))
    height = line(base, top, c["blue"], 8)
    dist = DoubleArrow(eye + DOWN * .35, base + DOWN * .35, buff=0, color=c["green"], stroke_width=6, tip_length=.22)
    angle = sketch(Arc(radius=1.2, start_angle=0, angle=np.arctan2(3.7, 7.1), arc_center=eye, color=c["red"], stroke_width=7))
    h = eye + LEFT * .45
    person = VGroup(sketch(Circle(.27, color=c["ink"], stroke_width=6).move_to(h + UP * 1.2)),
                    *[line(h + P(*a), h + P(*b), c["ink"]) for a, b in
                      [((0, .93), (0, .38)), ((0, .38), (-.28, 0)), ((0, .38), (.28, 0)), ((0, .8), (.55, .95)), ((0, .8), (-.35, .45))]])
    return ground, VGroup(m, snow), person, sight, angle, height, dist, eye


class Giris(Base):
    theme = "beyaz"

    def construct(self):
        c = self.c
        ground, m, person, sight, angle, height, dist, eye = mountain(c)
        t = self.title("Tırmanmadan bir dağın boyu ölçülür mü?")
        self.say(0, [Create(ground), Create(m)], Create(person))
        no = Cross(stroke_color=c["red"], stroke_width=9).scale(.35).move_to(P(3.2, 2.2))
        self.say(1, [Write(t), Create(no)], [FadeOut(no), Create(sight), Create(angle)], [Create(dist)], Create(height))
        a = self.label("açı", "red", eye + P(1.9, .35))
        d = self.label("uzaklık", "green", P(-.4, -2.78), 28)
        q = self.label("boy = ?", "blue", P(5.5, 1.3), 38)
        big = self.label("TRİGONOMETRİ", "ink", P(-2.7, 1.2), 58)
        self.say(2, [Write(a), Write(d), Write(q)], Write(big), Indicate(big, color=c["yellow"]))
        cross = self.ln(P(-5.6, .45), P(-1.6, .45), "red", 7)
        a2 = self.label("ezber listesi", "gray", P(-3.6, .45), 34)
        why = self.label("nereden doğdu?", "green", P(-3.4, -.35), 40)
        self.say(3, Write(a2), Create(cross), Write(why))
        self.end()


class Ucgen(Base):
    theme = "beyaz"

    def construct(self):
        c, y0 = self.c, -1.9
        t = self.title("Aynı açı, aynı oran")
        ground = self.ln(P(-6.6, y0), P(6.6, y0))
        trunk = self.ln(P(.4, y0), P(.4, .3), "ink", 14)
        leaves = VGroup(*[sketch(Circle(r, color=c["ink"], stroke_width=4).set_fill(c["green"], .55).move_to(P(x, y)), .03)
                          for x, y, r in [(.4, 1.0, .75), (-.2, .55, .5), (1.0, .55, .5)]])
        stick = self.ln(P(-4.2, y0), P(-4.2, -.85), "ink", 10)
        sun = VGroup(sketch(Circle(.45, color=c["yellow"], stroke_width=7).set_fill(c["yellow"], .8)),
                     *[Line(.62 * P(np.cos(a), np.sin(a)), .9 * P(np.cos(a), np.sin(a)), color=c["yellow"], stroke_width=6)
                       for a in np.arange(0, TAU, TAU / 8)]).move_to(P(-5.8, 1.9))
        k = 1.35                                  # gölge / yükseklik
        s_small, s_big = P(-4.2 + 1.05 * k, y0), P(.4 + 3.65 * k, y0)
        sh1, sh2 = self.ln(P(-4.2, y0 - .03), s_small, "gray", 11), self.ln(P(.4, y0 - .03), s_big, "gray", 11)
        self.say(0, [Write(t), Create(ground)], [Create(trunk), Create(leaves), Create(stick), FadeIn(sun)], [Create(sh1), Create(sh2)])
        t1 = Polygon(P(-4.2, y0), P(-4.2, -.85), s_small, color=c["red"], stroke_width=5).set_fill(c["red"], .15)
        t2 = Polygon(P(.4, y0), P(.4, y0 + 3.65), s_big, color=c["red"], stroke_width=5).set_fill(c["red"], .12)
        self.say(1, Create(t1), Create(t2))
        h1 = self.label("h", "blue", P(-4.55, -1.35))
        g1 = self.label("g", "green", P(-3.5, -2.35))
        h2 = self.label("H", "blue", P(.02, -.8))
        g2 = self.label("G", "green", P(2.8, -2.35))
        eq = self.label("h / g  =  H / G", "ink", P(3.6, 1.9), 40)
        self.say(2, [Write(h1), Write(g1)], [Write(h2), Write(g2)], Write(eq))
        a1 = Arc(radius=.5, start_angle=PI, angle=-np.arctan2(1, k), arc_center=s_small, color=c["red"], stroke_width=7)
        a2 = Arc(radius=1.0, start_angle=PI, angle=-np.arctan2(1, k), arc_center=s_big, color=c["red"], stroke_width=7)
        tan = self.label("tan θ  =  karşı / komşu", "red", P(3.6, .95), 36)
        self.say(3, [Create(a1), Create(a2)], Write(tan), Circumscribe(tan, color=c["yellow"]))
        self.play(*[FadeOut(m) for m in self.mobjects if m not in (t, self.caption)], run_time=.5)
        base, top, eye = P(2.6, -1.6), P(2.6, 1.2), P(-1.4, -1.6)
        tower = VGroup(sketch(Rectangle(width=.7, height=2.8, color=c["ink"], stroke_width=6).set_fill("#d9d3c7", 1).move_to((base + top) / 2)))
        tri = VGroup(self.ln(eye, base, "green"), self.ln(base, top, "blue", 9), self.ln(eye, top, "red"))
        arc = Arc(radius=.9, start_angle=0, angle=35 * DEGREES, arc_center=eye, color=c["red"], stroke_width=7)
        l = VGroup(self.label("35°", "red", eye + P(1.4, .4)), self.label("100 m", "green", P(.6, -2.05)),
                   self.label("tan 35° ≈ 0,70", "red", P(-3.9, .9), 38),
                   self.label("100 × 0,70 ≈ 70 m", "blue", P(-3.6, -.1), 40))
        self.say(4, [Create(tower), Create(tri), Create(arc)], [Write(l[0]), Write(l[1])], Write(l[2]), Write(l[3]))
        self.end()


class BirimCember(Base):
    def construct(self):
        c = self.c
        O, R = P(-3.1, -.35), 2.35
        ang = ValueTracker(50 * DEGREES)
        pt = lambda: O + R * P(np.cos(ang.get_value()), np.sin(ang.get_value()))
        foot = lambda: P(pt()[0], O[1])
        t = self.title("Üçgen, çemberin içinde yaşıyor")
        axes = VGroup(self.ln(O + LEFT * 3, O + RIGHT * 3, "gray", 3), self.ln(O + DOWN * 2.65, O + UP * 2.65, "gray", 3))
        circle = sketch(Circle(R, color=c["ink"], stroke_width=5).move_to(O), .018)
        self.say(0, Write(t), [Create(axes), Create(circle)])
        hyp = always_redraw(lambda: Line(O, pt(), color=c["yellow"], stroke_width=8))
        cos = always_redraw(lambda: Line(O, foot(), color=c["blue"], stroke_width=10))
        sin = always_redraw(lambda: Line(foot(), pt(), color=c["red"], stroke_width=10))
        dot = always_redraw(lambda: Dot(pt(), radius=.13, color=c["yellow"]))
        one = self.label("1", "yellow", O, 36).add_updater(
            lambda m: m.move_to((O + pt()) / 2 + .35 * P(-np.sin(ang.get_value()), np.cos(ang.get_value()))))
        self.say(1, Create(hyp), [Create(cos), Create(sin), FadeIn(dot)], Write(one))
        r1 = self.label("yatay  =  cos θ", "blue", P(3.4, 1.4), 38)
        r2 = self.label("dikey  =  sin θ", "red", P(3.4, .5), 38)
        self.say(2, [Write(r1), Indicate(cos, color=c["blue"])], [Write(r2), Indicate(sin, color=c["red"])])
        deg = always_redraw(lambda: text(f"θ = {round(ang.get_value() / DEGREES)}°", c["ink"], 38).move_to(P(3.4, -.7)))
        self.add(deg)
        self.say(3, ang.animate.set_value(80 * DEGREES), ang.animate.set_value(20 * DEGREES), ang.animate.set_value(60 * DEGREES))
        ghost_pt = O + R * P(np.cos(18 * DEGREES), np.sin(18 * DEGREES))
        ghost = VGroup(DashedLine(P(ghost_pt[0], O[1]), ghost_pt, color=c["green"], stroke_width=7),
                       DashedLine(O, ghost_pt, color=c["green"], stroke_width=4), Dot(ghost_pt, radius=.1, color=c["green"]))
        same = self.label("sin 162° = sin 18° ≈ 0,31", "green", P(3.4, -1.7), 34)
        level = DashedLine(ghost_pt, O + R * P(np.cos(162 * DEGREES), np.sin(162 * DEGREES)), color=c["gray"], stroke_width=4)
        self.say(4, ang.animate.set_value(90 * DEGREES), ang.animate.set_value(162 * DEGREES), [Create(ghost), Create(level)], Write(same))
        py = self.label("sin² θ + cos² θ = 1", "yellow", P(3.4, -1.7), 40)
        box = sketch(SurroundingRectangle(py, color=c["yellow"], buff=.22, stroke_width=4))
        self.say(5, [FadeOut(ghost), FadeOut(same), FadeOut(level), ang.animate.set_value(50 * DEGREES)],
                 [Write(py), Create(box)], ang.animate.set_value(130 * DEGREES), ang.animate.set_value(40 * DEGREES))
        self.end()


class Radyan(Base):
    def construct(self):
        c = self.c
        O, R = P(-2.6, -.4), 2.2
        at = lambda a, r=R: O + r * P(np.cos(a), np.sin(a))
        t = self.title("Radyan: çemberin kendi cetveli")
        circle = sketch(Circle(R, color=c["ink"], stroke_width=4).move_to(O), .015)
        q = self.label("360° ?", "yellow", P(3.4, 1.4), 54)
        self.say(0, [Write(t), Create(circle)], Write(q))
        radius = Line(O, at(0), color=c["yellow"], stroke_width=10)
        r_lab = self.label("yarıçap = 1", "yellow", O + P(.9, -.3), 22)
        rope = radius.copy()
        first = Arc(R, 0, 1, arc_center=O, color=c["yellow"], stroke_width=12)
        self.say(1, [FadeOut(q), Create(radius), Write(r_lab)], rope.animate.shift(UP * .02), Transform(rope, first))
        spoke = Line(O, at(1), color=c["yellow"], stroke_width=5)
        mark = Arc(.6, 0, 1, arc_center=O, color=c["ink"], stroke_width=5)
        eq = self.label("1 radyan ≈ 57,3°", "yellow", P(3.4, 1.4), 44)
        n1 = self.label("1", "yellow", at(.5, R + .4))
        self.say(2, [Create(spoke), Create(mark)], [Write(eq), Write(n1)])
        colors = ["green", "blue", "red", "green", "blue"]
        steps = [[Create(Arc(R, k, 1, arc_center=O, color=c[colors[k - 1]], stroke_width=12)),
                  FadeIn(self.label(str(k + 1), colors[k - 1], at(k + .5, R + .4)))] for k in range(1, 6)]
        last = Arc(R, 6, TAU - 6, arc_center=O, color=c["ink"], stroke_width=14)
        rest = self.label("+0,28", "ink", at(6.1, R + .65), 24)
        self.say(3, *steps, [Create(last), Write(rest)])
        full = self.label("tam tur = 2π ≈ 6,28 radyan", "ink", P(3.4, .3), 28)
        half = self.label("π radyan = 180°", "green", P(3.5, -.7), 40)
        warn = self.label("π radyan ≠ 1 radyan", "red", P(3.5, -1.7), 40)
        self.say(4, Write(full), Write(half), [Write(warn), Indicate(warn, color=c["red"])])
        self.end()


class Dalga(Base):
    def construct(self):
        c = self.c
        O, R, x0, w = P(-4.8, -.2), 1.5, -2.5, 9.0
        a = ValueTracker(0)
        pt = lambda: O + R * P(np.cos(a.get_value()), np.sin(a.get_value()))
        tip = lambda: P(x0 + a.get_value() * w / (2 * TAU), pt()[1])
        t = self.title("Dönen nokta bir dalga çizer")
        axes = VGroup(self.ln(O + LEFT * 1.8, O + RIGHT * 1.8, "gray", 3), self.ln(O + DOWN * 1.9, O + UP * 1.9, "gray", 3),
                      self.ln(P(x0, O[1]), P(x0 + w + .2, O[1]), "gray", 3), self.ln(P(x0, -2.1), P(x0, 1.7), "gray", 3))
        circle = sketch(Circle(R, color=c["ink"], stroke_width=5).move_to(O), .012)
        moving = VGroup(always_redraw(lambda: Line(O, pt(), color=c["yellow"], stroke_width=6)),
                        always_redraw(lambda: Line(P(pt()[0], O[1]), pt(), color=c["red"], stroke_width=8)),
                        always_redraw(lambda: DashedLine(pt(), tip() + RIGHT * .001, color=c["gray"], stroke_width=3)),
                        always_redraw(lambda: Dot(pt(), radius=.11, color=c["yellow"])),
                        always_redraw(lambda: Dot(tip(), radius=.09, color=c["red"])))
        trace = always_redraw(lambda: ParametricFunction(
            lambda u: P(x0 + u * w / (2 * TAU), O[1] + R * np.sin(u)),
            t_range=[0, max(a.get_value(), .001), .05], color=c["red"], stroke_width=7))
        self.say(0, [Write(t), Create(axes), Create(circle)], [FadeIn(moving), FadeIn(trace)], a.animate.set_value(PI / 2))
        self.say(1, a.animate(rate_func=linear).set_value(TAU))
        marks = VGroup(self.label("1", "ink", P(x0 - .3, O[1] + R), 28), self.label("−1", "ink", P(x0 - .4, O[1] - R), 28),
                       self.label("2π", "ink", P(x0 + w / 2, O[1] - 1.85), 28), self.label("4π", "ink", P(x0 + w, O[1] - 1.85), 28))
        name = self.label("sin", "red", P(5.6, 1.9), 40)
        self.say(2, a.animate(rate_func=linear).set_value(2 * TAU), [Write(marks), Write(name)])
        wave = ParametricFunction(lambda u: P(x0 + u * w / (2 * TAU), O[1] + R * np.cos(u)),
                                  t_range=[0, 2 * TAU, .05], color=c["blue"], stroke_width=6)
        cname = self.label("cos", "blue", P(4.2, 1.9), 40)
        self.say(3, FadeOut(moving), [Create(wave), Write(cname)])
        end = self.label("dönmek  =  dalgalanmak", "yellow", P(2.0, -2.75), 38)
        self.say(4, Write(end), Circumscribe(end, color=c["yellow"]))
        self.end()


class Ses(Base):
    def construct(self):
        c = self.c

        def wave(n, color):
            f = lambda x: sum(np.sin((2 * k + 1) * x) / (2 * k + 1) for k in range(n)) * 1.7
            return ParametricFunction(lambda x: P(-6 + x * 12 / (2 * TAU), -.3 + f(x)), t_range=[0, 2 * TAU, .015],
                                      color=c[color], stroke_width=6)

        def part(n):
            return self.label(" + ".join(["sin x", "sin 3x / 3", "sin 5x / 5"][:n]) + (" + …" if n > 3 else ""), "ink", P(0, 2.2), 34)

        t = self.title("Sesin içindeki sinüsler")
        axis = self.ln(P(-6.2, -.3), P(6.2, -.3), "gray", 3)
        w, lab = wave(1, "blue"), part(1)
        self.say(0, [Write(t), Create(axis)], Create(w), Write(lab))
        small = ParametricFunction(lambda x: P(-6 + x * 12 / (2 * TAU), -.3 + np.sin(3 * x) / 3 * 1.7),
                                   t_range=[0, 2 * TAU, .02], color=c["green"], stroke_width=4)
        self.say(1, Create(small), [Transform(w, wave(2, "yellow")), FadeOut(small), Transform(lab, part(2))])
        self.say(2, [Transform(w, wave(3, "yellow")), Transform(lab, part(3))],
                 [Transform(w, wave(6, "red")), Transform(lab, part(4))], Transform(w, wave(20, "red")))
        f = self.label("karmaşık dalga  →  sinüslerin toplamı", "yellow", P(0, -2.5), 36)
        self.say(3, Write(f), Transform(w, wave(3, "yellow")), Transform(w, wave(20, "red")))
        self.end()


class Tarih(Base):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("“Sinüs” nereden geliyor?")
        O, R = P(-4.3, -.4), 1.6
        a = 55 * DEGREES
        up, down = O + R * P(np.cos(a), np.sin(a)), O + R * P(np.cos(a), -np.sin(a))
        circle = sketch(Circle(R, color=c["ink"], stroke_width=5).move_to(O))
        chord = self.ln(down, up, "gray", 7)
        half = self.ln(P(up[0], O[1]), up, "red", 11)
        bow = VGroup(self.ln(O, up, "ink", 4), self.ln(O, P(up[0], O[1]), "ink", 4))
        w1 = self.label("jya  (yarım kiriş)", "red", P(1.9, 1.5), 38)
        who = self.label("Aryabhata, yaklaşık 500", "gray", P(1.9, .85), 26)
        self.say(0, [Write(t), Create(circle)], [Create(chord), Create(bow)], Create(half), [Write(w1), Write(who)])
        ar = lambda y: Arrow(P(1.9, y), P(1.9, y - .55), buff=0, color=c["gray"], stroke_width=5)
        a1, a2, a3 = ar(.5), ar(-.55), ar(-1.6)
        w2 = self.label("jiba", "blue", P(1.9, -.3), 38)
        w3 = self.label("jaib  (koy, kıvrım)", "green", P(1.9, -1.35), 38)
        self.say(1, [Create(a1), Write(w2)], [Create(a2), Write(w3)])
        w4 = self.label("sinus  →  sinüs", "red", P(1.9, -2.4), 42)
        self.say(2, [Create(a3), Write(w4)], Circumscribe(w4, color=c["yellow"]))
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.caption], run_time=.5)
        ground, m, person, sight, angle, height, dist, eye = mountain(c)
        t2 = self.title("Everest, 1852")
        who2 = self.label("Radhanath Sikdar", "ink", P(-4.3, 1.9), 34)
        tool = self.label("ölçülen açılar + uzaklıklar", "red", P(-4.3, 1.25), 26)
        self.say(3, [Write(t2), Create(ground), Create(m), Create(person)], [Create(sight), Create(angle), Create(dist)],
                 [Write(who2), Write(tool)], Create(height))
        v1 = self.label("1856 duyurusu: 8.840 m", "blue", P(-3.9, .5), 30)
        v2 = self.label("bugün: 8.849 m", "green", P(-4.5, -.15), 30)
        v3 = self.label("zirveye ilk çıkış: 1953", "gray", P(-.8, -2.8), 24)
        self.say(4, Write(v1), Write(v2), [FadeOut(dist), Write(v3)])
        self.end()


class Tuzak(Base):
    def construct(self):
        c = self.c
        t = self.title("Tuzak soru")
        q = self.label("sin(30° + 60°)  =  sin 30° + sin 60°  ?", "ink", P(0, 1.7), 44)
        self.say(0, Write(t), Write(q))
        mark = self.label("?", "yellow", P(0, -.4), 160)
        self.say(1, FadeIn(mark, scale=.4), Wiggle(mark), extra=3.0)
        left = self.label("sin 90° = 1", "blue", P(-3.6, .3), 46)
        right = self.label("0,50 + 0,87 ≈ 1,37", "red", P(3.1, .3), 46)
        self.say(2, [FadeOut(mark), Write(left)], Write(right))
        ne = self.label("1  ≠  1,37", "yellow", P(0, -.95), 72)
        fn = self.label("sin bir çarpan değil, bir fonksiyon", "ink", P(0, -2.25), 34)
        self.say(3, [Write(ne)], Circumscribe(ne, color=c["red"]), Write(fn))
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.caption], run_time=.5)
        O, R = P(0, .45), 1.9
        a = ValueTracker(0)
        pt = lambda: O + R * P(np.cos(a.get_value()), np.sin(a.get_value()))
        circle = sketch(Circle(R, color=c["ink"], stroke_width=5).move_to(O))
        moving = VGroup(always_redraw(lambda: Line(O, pt(), color=c["yellow"], stroke_width=7)),
                        always_redraw(lambda: Line(P(pt()[0], O[1]), pt(), color=c["red"], stroke_width=9)),
                        always_redraw(lambda: Line(O, P(pt()[0], O[1]), color=c["blue"], stroke_width=9)),
                        always_redraw(lambda: Dot(pt(), radius=.12, color=c["yellow"])))
        story = self.label("dönen bir noktanın hikâyesi", "yellow", P(0, -2.0), 40)
        self.add(circle, moving)
        self.say(4, a.animate(rate_func=linear).set_value(TAU), [Write(story), a.animate(rate_func=linear).set_value(2 * TAU)], extra=2.0)
        self.end()


if __name__ == "__main__":
    asyncio.run(voices())
