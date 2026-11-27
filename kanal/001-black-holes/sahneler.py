"""Video 1: Every Type of Black Hole, From Tiny to Monstrous. Kaynaklar ARASTIRMA.md.
(kanal/ içinde) .venv/Scripts/python render.py 001-black-holes taslak"""
from manim import *
import numpy as np

from tahta import P, Tahta, sketch

TEXT = {
    "Hook": [
        "Here is a black hole. In theory, it could be smaller than an atom.",
        "And here is another one, so wide that Voyager 1, after almost fifty years of flying, has covered only a fraction of the distance across it.",
        "Same name. Same physics. Wildly different sizes.",
        "So how small, and how big, can a black hole actually get? Let's climb the whole ladder.",
    ],
    "What": [
        "First, what is it? Throw a ball up, and gravity pulls it back. Throw it fast enough, and it escapes.",
        "Squeeze enough mass into a small enough space, and the speed you need to escape becomes faster than light.",
        "The boundary where that happens is called the event horizon. Nothing that crosses it comes back out.",
        "But a black hole is not a cosmic vacuum cleaner. From far away, it pulls like any other object with the same mass.",
        "If the Sun were swapped for a black hole of equal mass, Earth would freeze, but it would keep its orbit.",
    ],
    "Rule": [
        "So what decides how big one gets? Mostly its mass. And there is one simple rule.",
        "For a black hole that is not spinning, every Sun's worth of mass adds about three kilometers to the radius of its event horizon.",
        "Double the mass, and the horizon becomes twice as wide.",
        "Now try it with Earth. To become a black hole, our whole planet would have to be squeezed to about the width of a marble.",
    ],
    "Primordial": [
        "So let's start at the bottom. The smallest rung is also the strangest, because nobody has ever found one.",
        "Scientists think black holes might have formed in the first second after the universe began. They are called primordial black holes.",
        "In theory, some could weigh far less than a paperclip. Others could outweigh the Sun a hundred thousand times.",
        "One with the mass of an asteroid would have a horizon about the size of an atom.",
        "Theory also says the very tiniest should slowly evaporate and disappear. So far, all of this is unproven.",
        "To reach black holes we have real evidence for, we need a dying star.",
    ],
    "Stellar": [
        "When a very massive star, around twenty times the Sun's mass or more, runs out of fuel, its core can collapse.",
        "What remains is a stellar-mass black hole. The lightest one NASA lists weighs just three point eight Suns. Its horizon would fit across a city.",
        "But if a black hole gives off no light, how do we find it? Watch its neighbor.",
        "The nearest one we know, Gaia BH1, is about fifteen hundred light-years away. We know it is there because a star keeps circling something unseen.",
        "Its larger cousin, Gaia BH3, holds about thirty-three Suns inside a horizon roughly two hundred kilometers wide.",
        "Our galaxy may hide as many as one hundred million of these.",
    ],
    "Fall": [
        "But what if you got too close? Imagine falling in, feet first.",
        "Near a small black hole, gravity pulls your feet much harder than your head.",
        "You are stretched long and squeezed thin. Scientists really do call it spaghettification.",
        "And it happens before you even reach the horizon.",
        "Here is the twist: near a giant black hole, the difference is gentler. You could cross the horizon in one piece.",
        "You still would not come back. So how do black holes get that big?",
    ],
    "Middle": [
        "Between star-sized black holes and giants, there should be a middle class: from about a hundred to hundreds of thousands of Suns.",
        "For decades, it was the missing link. Candidates kept appearing, but proof was hard.",
        "In twenty twenty-three, detectors felt two black holes collide. They merged into one of more than two hundred and twenty-five Suns.",
        "And inside the star cluster Omega Centauri, Hubble data revealed seven stars moving so fast that something heavy must be holding them.",
        "That hidden object weighs at least eight thousand two hundred Suns. Its horizon would be almost four Earths wide, or more.",
        "It is still called a candidate. The next rung is not.",
    ],
    "Center": [
        "At the center of our own galaxy, about twenty-seven thousand light-years away, sits Sagittarius A star.",
        "It is a supermassive black hole, weighing about four million Suns.",
        "Astronomers tracked stars whipping around an invisible point for years. That work shared the Nobel Prize in twenty twenty.",
        "Its horizon is about seventeen Suns wide. Big, but it would still fit easily inside the orbit of Mercury.",
        "In twenty twenty-two, the Event Horizon Telescope showed us its glowing ring and dark shadow.",
        "Gas and mergers help such monsters grow, but how they first formed is still a mystery. And this one is small, as giants go.",
    ],
    "M87": [
        "Meet M87 star, about fifty-five million light-years away, in another galaxy.",
        "It holds about six and a half billion Suns. In twenty nineteen, it became the first black hole ever imaged.",
        "Now watch the scale change. Here is the Sun, and here is the orbit of Neptune, the farthest planet.",
        "The horizon of M87 star reaches about four times farther than that.",
        "Our entire family of planets would fit inside, with plenty of room to spare.",
    ],
    "Monster": [
        "And still, there are bigger ones. Far away, a blazing quasar called TON 618 is powered by a monster.",
        "Its mass is hard to measure. Estimates run from about forty billion to sixty-six billion Suns.",
        "Take the lower number. The horizon's radius is about eight hundred times the distance from Earth to the Sun.",
        "Remember Voyager 1? In November twenty twenty-six, it reached one light-day from us.",
        "That is about a hundred and seventy-three Earth-Sun distances, after nearly fifty years.",
        "Placed at the center of TON 618, it would be only about a fifth of the way to the edge.",
    ],
    "Ladder": [
        "Now put every rung on one board.",
        "An atom-sized primordial black hole, if it exists.",
        "A city-sized one, born from a dead star.",
        "A candidate wider than several Earths, hiding in a star cluster.",
        "A giant that fits inside Mercury's orbit. One that swallows the planets. And a monster that makes our farthest probe look close to home.",
    ],
    "End": [
        "So how small can a black hole be? In theory, smaller than an atom. In evidence, a few times the mass of the Sun.",
        "And how big? Tens of billions of Suns, as far as we can tell today.",
        "Which one surprised you most: the one nobody has found, or the one we can barely fit on the board? Tell me in the comments.",
        "Next time: that tiny probe. How far has humanity actually reached?",
    ],
}

K = "#000000"


def hole(r, pos, ring, w=7):
    """Kara delik: siyah disk + renkli kenar."""
    return sketch(Circle(r, color=ring, stroke_width=w).set_fill(K, 1), min(.018, r * .05)).move_to(pos)


def dot(pos, color, r=.09):
    return Dot(pos, radius=r, color=color)


def circ(r, pos, color, w=5, fill=0):
    return sketch(Circle(r, color=color, stroke_width=w).set_fill(color, fill), min(.018, r * .04)).move_to(pos)


def person(base, color, s=1.0):
    parts = [((0, 1.15), (0, .5)), ((0, .5), (-.28, 0)), ((0, .5), (.28, 0)), ((0, .95), (-.4, .6)), ((0, .95), (.4, .6))]
    g = VGroup(sketch(Circle(.24, color=color, stroke_width=5)).move_to(P(0, 1.42)),
               *[sketch(Line(P(*a), P(*b), color=color, stroke_width=5)) for a, b in parts])
    return g.scale(s, about_point=ORIGIN).shift(base)


def stars(n, seed, color, x=(-6.8, 6.8), y=(-3.0, 2.7)):
    rng = np.random.default_rng(seed)
    return VGroup(*[Dot(P(rng.uniform(*x), rng.uniform(*y)), radius=rng.uniform(.012, .035), color=color) for _ in range(n)])


class Hook(Tahta):
    def construct(self):
        c = self.c
        self.add(stars(70, 1, c["gray"]))
        tiny = dot(P(-5, 0), c["yellow"], .05)
        glass = circ(.75, P(-5, 0), c["gray"], 3)
        t = self.label("smaller than an atom?", "yellow", P(-4.4, -1.35), 28)
        self.say(0, [FadeIn(tiny), Create(glass)], Write(t))
        big = hole(4.6, P(4.6, -.2), c["red"], 9)
        probe = dot(P(1.0, -.2), c["blue"])
        path = self.ln(P(.1, -.2), P(1.0, -.2), "blue", 6)
        lab = self.label("Voyager 1", "blue", P(1.5, .35), 26)
        self.say(1, GrowFromCenter(big), [FadeIn(probe), Create(path), Write(lab)])
        same = self.label("same name · same physics", "ink", P(-3.2, 1.9), 30)
        self.say(2, Write(same))
        q = self.label("HOW SMALL?  HOW BIG?", "yellow", P(-3.5, -2.5), 40)
        self.say(3, Write(q), Indicate(q, color=c["red"]))
        self.end()


class What(Tahta):
    def construct(self):
        c = self.c
        t = self.title("What is a black hole?")
        ground = sketch(Arc(radius=5, start_angle=PI * .62, angle=-PI * .24, arc_center=P(-3.8, -7.4), color=c["green"], stroke_width=7))
        up = CurvedArrow(P(-4.4, -2.3), P(-3.1, -2.45), angle=-PI * .9, color=c["ink"], stroke_width=5)
        out = Arrow(P(-3.6, -2.35), P(-1.9, 1.3), color=c["yellow"], stroke_width=6, buff=0)
        self.say(0, [Write(t), Create(ground)], Create(up), Create(out))
        h = hole(.9, P(-3.4, .2), c["red"])
        light = Arrow(P(-3.4, .2), P(-1.9, 1.5), color=c["yellow"], stroke_width=6, buff=0)
        back = CurvedArrow(P(-1.9, 1.5), P(-2.9, .9), angle=-PI * .8, color=c["yellow"], stroke_width=5)
        need = self.label("escape speed > light speed", "yellow", P(-3.4, -2.6), 28)
        self.say(1, [FadeOut(ground, up, out), GrowFromCenter(h)], Create(light), [Create(back), Write(need)])
        ring = DashedVMobject(Circle(1.25, color=c["blue"], stroke_width=5).move_to(P(-3.4, .2)), num_dashes=28)
        eh = self.label("event horizon", "blue", P(-3.4, 2.05), 32)
        self.say(2, [FadeOut(light, back), Create(ring)], Write(eh))
        sun_orbit = DashedVMobject(Circle(2.0, color=c["gray"], stroke_width=3).move_to(P(3.2, -.2)), num_dashes=40)
        sun = circ(.55, P(3.2, -.2), c["yellow"], 6, .85)
        earth = dot(P(5.2, -.2), c["blue"], .16)
        no = self.label("not a vacuum cleaner", "ink", P(3.2, 2.45), 30)
        self.say(3, [FadeIn(sun), Create(sun_orbit), FadeIn(earth)], Write(no))
        swap = hole(.14, P(3.2, -.2), c["red"], 5)
        cold = self.label("colder · same orbit", "blue", P(3.2, -2.7), 30)
        self.say(4, Transform(sun, swap), [Rotate(earth, TAU * .75, about_point=P(3.2, -.2)), Write(cold)])
        self.end()


class Rule(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("One rule for size")
        self.say(0, Write(t))
        h1 = hole(.55, P(-5.3, .1), c["red"])
        r1 = self.ln(P(-5.3, .1), P(-4.75, .1), "yellow", 7)
        a = self.label("1 Sun\nradius ≈ 3 km", "ink", P(-5.3, -1.6), 28)
        self.say(1, GrowFromCenter(h1), [Create(r1), Write(a)])
        h2 = hole(1.1, P(-1.2, .1), c["red"])
        r2 = self.ln(P(-1.2, .1), P(-.1, .1), "yellow", 7)
        b = self.label("2 Suns\nradius ≈ 6 km", "ink", P(-1.2, -1.8), 28)
        self.say(2, GrowFromCenter(h2), [Create(r2), Write(b)])
        earth = circ(1.35, P(3.6, .45), c["blue"], 6, .3)
        marble = hole(.17, P(3.6, -1.9), c["red"], 5)
        arrow = Arrow(P(3.6, -.95), P(3.6, -1.65), color=c["ink"], stroke_width=5, buff=0)
        m = self.label("≈ 1.8 cm", "red", P(5.2, -1.9), 36)
        e = self.label("Earth", "blue", P(3.6, 2.2), 34)
        self.say(3, [FadeIn(earth), Write(e)], Create(arrow), [GrowFromCenter(marble), Write(m)])
        self.end()


class Primordial(Tahta):
    def construct(self):
        c = self.c
        t = self.title("1. Primordial black holes (hypothetical)")
        ghost = DashedVMobject(Circle(1.3, color=c["gray"], stroke_width=6).move_to(P(-3.8, .1)), num_dashes=24)
        q = self.label("?", "gray", P(-3.8, .1), 90)
        self.say(0, [Write(t), Create(ghost)], Write(q))
        bang = VGroup(*[self.ln(P(2.8, 1.0) + .25 * P(np.cos(a), np.sin(a)), P(2.8, 1.0) + .95 * P(np.cos(a), np.sin(a)), "yellow", 5)
                        for a in np.linspace(0, TAU, 12, endpoint=False)])
        first = self.label("first second of the universe", "yellow", P(2.8, -.45), 28)
        seeds = VGroup(*[hole(.07, P(2.8, 1.0) + r * P(np.cos(a), np.sin(a)), c["red"], 3) for r, a in [(1.3, .3), (1.5, 2.2), (1.2, 4.0), (1.7, 5.4)]])
        self.say(1, Create(bang), [Write(first), FadeIn(seeds)])
        axis = Arrow(P(-6, -2.6), P(6, -2.6), color=c["ink"], stroke_width=5, buff=0)
        lo = self.label("< a paperclip", "blue", P(-4.6, -2.05), 28)
        hi = self.label("100,000 Suns", "red", P(4.6, -2.05), 28)
        self.say(2, Create(axis), Write(lo), Write(hi))
        atom = VGroup(*[Ellipse(width=2.3, height=.8, color=c["blue"], stroke_width=3).rotate(a).move_to(P(2.8, .4)) for a in (0, PI / 3, -PI / 3)])
        nucleus = hole(.13, P(2.8, .4), c["red"], 4)
        al = self.label("asteroid mass → atom-sized horizon", "ink", P(2.8, 2.25), 28)
        self.say(3, [FadeOut(bang, first, seeds), Create(atom)], [GrowFromCenter(nucleus), Write(al)])
        puff = VGroup(*[dot(P(2.8, .4) + .3 * P(np.cos(a), np.sin(a)), c["yellow"], .05) for a in np.linspace(0, TAU, 10, endpoint=False)])
        un = self.label("UNPROVEN", "red", P(-3.8, 2.1), 44)
        self.say(4, [FadeOut(nucleus), FadeIn(puff)], [puff.animate.scale(4).set_opacity(0), Write(un)])
        star = circ(.7, P(0, .3), c["yellow"], 7, .8)
        self.say(5, [FadeOut(ghost, q, atom, al, axis, lo, hi, un, puff), GrowFromCenter(star)])
        self.end()


class Stellar(Tahta):
    def construct(self):
        c = self.c
        t = self.title("2. Stellar-mass black holes")
        star = circ(1.5, P(-4.2, .2), c["yellow"], 8, .75)
        m = self.label("≈ 20+ Suns", "yellow", P(-4.2, -1.9), 32)
        self.say(0, [Write(t), GrowFromCenter(star)], Write(m), star.animate.scale(1.12))
        h = hole(.55, P(-4.2, .2), c["red"])
        burst = VGroup(*[self.ln(P(-4.2, .2) + 1.0 * P(np.cos(a), np.sin(a)), P(-4.2, .2) + 1.9 * P(np.cos(a), np.sin(a)), "yellow", 4)
                         for a in np.linspace(0, TAU, 14, endpoint=False)])
        city = VGroup(*[Rectangle(width=.34, height=hh, color=c["blue"], stroke_width=4).move_to(P(1.4 + i * .45, -1.9 + hh / 2))
                        for i, hh in enumerate([.6, 1.1, .8, 1.5, .9, 1.25, .5, 1.0])])
        cap = DoubleArrow(P(1.15, -2.3), P(4.85, -2.3), color=c["red"], stroke_width=5, buff=0)
        small = self.label("3.8 Suns ≈ 22 km across", "red", P(3.0, -2.85), 28)
        self.say(1, [Transform(star, h), FadeIn(burst), FadeOut(m)], [FadeOut(burst), Create(city)], [Create(cap), Write(small)])
        how = self.label("no light... so how?", "ink", P(3.2, 1.9), 36)
        self.say(2, [FadeOut(city, cap, small), Write(how)])
        orbit = Circle(1.5, color=c["gray"], stroke_width=3).move_to(P(-4.2, .2))
        friend = dot(P(-2.7, .2), c["yellow"], .25)
        bh1 = self.label("Gaia BH1 · ≈ 1,500 light-years", "yellow", P(2.6, .7), 32)
        self.say(3, [Create(orbit), FadeIn(friend), Write(bh1)], Rotate(friend, TAU * 1.5, about_point=P(-4.2, .2)))
        big = hole(.95, P(2.6, -1.35), c["red"])
        bh3 = self.label("Gaia BH3\n33 Suns\n≈ 200 km", "ink", P(5.2, -1.35), 30)
        self.say(4, GrowFromCenter(big), Write(bh3))
        many = VGroup(*[hole(.06, d.get_center(), c["red"], 3) for d in stars(60, 5, c["red"], x=(-6.5, 6.5), y=(-2.3, 2.4))])
        n = self.label("up to 100,000,000 in the Milky Way", "yellow", P(0, -2.95), 36)
        self.say(5, [FadeOut(how, bh1, orbit, friend, star, big, bh3), LaggedStartMap(FadeIn, many)], Write(n))
        self.end()


class Fall(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("Falling in, feet first")
        h = hole(.8, P(-3.6, -2.0), c["red"])
        p = person(P(-3.6, .6), c["ink"])
        self.say(0, [Write(t), GrowFromCenter(h), Create(p)])
        feet = Arrow(P(-2.6, .75), P(-2.6, -.55), color=c["red"], stroke_width=9, buff=0)
        head = Arrow(P(-2.6, 2.3), P(-2.6, 1.8), color=c["blue"], stroke_width=6, buff=0)
        self.say(1, p.animate.shift(DOWN * .35), [Create(feet), Create(head)])
        name = self.label("spaghettification", "red", P(.1, 1.9), 40)
        self.say(2, p.animate.stretch(2.0, 1, about_edge=UP).stretch(.35, 0), Write(name))
        ring = DashedVMobject(Circle(1.15, color=c["blue"], stroke_width=5).move_to(P(-3.6, -2.0)), num_dashes=24)
        self.say(3, Create(ring))
        giant = hole(3.6, P(4.4, -3.2), c["red"])
        calm = person(P(3.2, .5), c["ink"])
        label = self.label("giant: cross it in one piece", "green", P(3.4, 2.4), 28)
        self.say(4, [FadeOut(name), GrowFromCenter(giant), Create(calm)], [calm.animate.shift(DOWN * 1.9).set_color(c["bg"]), Write(label)])
        q = self.label("how do they get that big?", "ink", P(-3.2, .2), 36)
        self.say(5, [FadeOut(feet, head, ring, h, p), Write(q)])
        self.end()


class Middle(Tahta):
    def construct(self):
        c = self.c
        t = self.title("3. Intermediate-mass black holes")
        small = hole(.3, P(-5, .6), c["red"], 5)
        giant = hole(1.5, P(4.8, .6), c["red"])
        gap = DashedVMobject(Circle(.85, color=c["yellow"], stroke_width=6).move_to(P(-.4, .6)), num_dashes=20)
        lab = self.label("≈ 100 → hundreds of thousands of Suns", "yellow", P(-.4, -1.1), 28)
        self.say(0, [Write(t), FadeIn(small, giant)], [Create(gap), Write(lab)])
        link = self.label("the missing link?", "ink", P(-.4, 2.2), 34)
        self.say(1, Write(link), Indicate(gap, color=c["red"]))
        a, b = hole(.35, P(-2.4, .6), c["blue"], 5), hole(.45, P(1.6, .6), c["blue"], 5)
        res = hole(.75, P(-.4, .6), c["red"])
        waves = VGroup(*[Circle(r, color=c["blue"], stroke_width=3, stroke_opacity=1 - r / 4).move_to(P(-.4, .6)) for r in (1.2, 1.9, 2.6)])
        v = self.label("2023: merger → more than 225 Suns", "blue", P(-.4, -1.9), 30)
        self.say(2, [FadeOut(gap, lab, link, small, giant), FadeIn(a, b)],
                 [a.animate.move_to(P(-.4, .6)), b.animate.move_to(P(-.4, .6))], [FadeOut(a, b), FadeIn(res), Create(waves), Write(v)])
        cluster = stars(220, 9, c["ink"], x=(-3.2, 2.4), y=(-1.5, 2.6))
        name = self.label("Omega Centauri", "ink", P(4.8, 2.2), 32)
        core = P(-.4, .6)
        fast = VGroup(*[Arrow(core + .55 * P(np.cos(k), np.sin(k)), core + 1.7 * P(np.cos(k + .5), np.sin(k + .5)), color=c["yellow"], stroke_width=5, buff=0)
                        for k in np.linspace(0, TAU, 7, endpoint=False)])
        self.say(3, [FadeOut(res, waves, v), FadeIn(cluster), Write(name)], LaggedStartMap(Create, fast))
        h = hole(.5, core, c["red"])
        e = VGroup(*[circ(.13, P(3.5 + i * .3, -1.9), c["blue"], 4, .5) for i in range(4)])
        el = self.label("at least 8,200 Suns\n≈ 3.8+ Earths wide", "ink", P(4.7, -.7), 28)
        self.say(4, GrowFromCenter(h), [Write(el), LaggedStartMap(FadeIn, e)])
        cand = self.label("CANDIDATE", "yellow", P(-4.9, -2.5), 40)
        self.say(5, Write(cand))
        self.end()


class Center(Tahta):
    def construct(self):
        c = self.c
        t = self.title("4. Supermassive: Sagittarius A*")
        sky = stars(120, 12, c["gray"], x=(-6.8, -.2))
        mid = P(-3.6, .1)
        h = hole(.28, mid, c["red"], 5)
        d = self.label("center of the Milky Way\n≈ 27,000 light-years", "ink", P(3.2, 1.7), 28)
        self.say(0, [Write(t), FadeIn(sky)], [GrowFromCenter(h), Write(d)])
        m = self.label("≈ 4,000,000 Suns", "yellow", P(3.2, .5), 40)
        self.say(1, Write(m))
        o1 = Ellipse(width=4.2, height=1.7, color=c["blue"], stroke_width=3).rotate(.5).shift(mid + P(1.1, .55))
        o2 = Ellipse(width=2.6, height=1.5, color=c["green"], stroke_width=3).rotate(-.9).shift(mid + P(-.45, .6))
        s1, s2 = dot(o1.get_start(), c["blue"], .13), dot(o2.get_start(), c["green"], .13)
        nobel = self.label("Nobel Prize 2020", "blue", P(3.2, -.5), 32)
        self.say(2, [Create(o1), Create(o2), FadeIn(s1, s2)], [MoveAlongPath(s1, o1), MoveAlongPath(s2, o2), Write(nobel)])
        centre = P(0, -.25)
        merc = DashedVMobject(Circle(2.75, color=c["gray"], stroke_width=4).move_to(centre), num_dashes=50)
        sgr = hole(.58, centre, c["red"])                       # ölçekli: 24,5 / 115,8 = 0,21
        ml = self.label("Mercury's orbit", "gray", P(4.2, 1.7), 28)
        sl = self.label("horizon\n≈ 17 Suns wide", "red", P(-4.6, -1.7), 28)
        self.play(FadeOut(sky, o1, o2, s1, s2, d, m, nobel), Transform(h, sgr), run_time=.7)      # eski çizim hızlı temizlensin
        self.say(3, [Create(merc), Write(ml)], Write(sl))
        ring = VGroup(*[Circle(r, color=c["yellow"], stroke_width=16, stroke_opacity=o).move_to(centre) for r, o in [(1.2, .9), (1.38, .45), (1.55, .18)]])
        yr = self.label("imaged 2022 (ring drawn, not to scale)", "yellow", P(0, -3.05), 24)
        self.play(FadeOut(merc, ml, sl), run_time=.4)
        self.say(4, FadeIn(ring), Write(yr))
        q = self.label("and as giants go, this one is small", "ink", P(0, 2.3), 32)
        self.say(5, [VGroup(h, ring).animate.scale(.45), Write(q)])
        self.end()


class M87(Tahta):
    def construct(self):
        c = self.c
        t = self.title("Supermassive: M87*")
        mid = P(-.6, -.3)
        ring = VGroup(*[Circle(r, color=col, stroke_width=22, stroke_opacity=o).move_to(mid)
                        for r, col, o in [(1.15, c["yellow"], .95), (1.4, c["red"], .5), (1.65, c["red"], .18)]])
        h = hole(.95, mid, c["yellow"], 4)
        d = self.label("≈ 55 million\nlight-years", "ink", P(4.8, 1.6), 30)
        self.say(0, [Write(t), FadeIn(ring), GrowFromCenter(h)], Write(d))
        m = self.label("≈ 6.5 billion Suns\nfirst image: 2019", "yellow", P(4.8, -.4), 30)
        self.say(1, Write(m))
        sun = dot(mid, c["yellow"], .045)
        nep = Circle(.7, color=c["blue"], stroke_width=5).move_to(mid)       # yarıçap oranı 128/30 = 4,3
        nl = self.label("Neptune's orbit", "blue", P(-5.4, .5), 28)
        point = Arrow(P(-4.6, .15), mid + P(-.72, 0), color=c["blue"], stroke_width=4, buff=.05)
        big = hole(3.0, mid, c["red"], 6)
        self.say(2, [FadeOut(ring, h), FadeIn(sun)], [Create(nep), Write(nl), Create(point)])
        four = self.label("horizon radius\n≈ 4 × farther", "red", P(-5.4, -1.7), 28)
        self.say(3, FadeIn(big), [FadeIn(nep, sun), Write(four)])
        planets = VGroup(*[dot(mid + r * P(np.cos(a), np.sin(a)), c["ink"], .05) for r, a in [(.08, 1), (.13, 3), (.18, 5), (.25, 2), (.36, 4), (.5, 0), (.6, 2.6), (.7, 5.6)]])
        self.add(nep, sun)
        self.say(4, LaggedStartMap(FadeIn, planets))
        self.end()


class Monster(Tahta):
    def construct(self):
        c = self.c
        t = self.title("The monster: TON 618")
        mid = P(0, -.3)
        glow = VGroup(*[Circle(r, color=c["yellow"], stroke_width=26, stroke_opacity=o).move_to(mid) for r, o in [(.5, 1), (.8, .5), (1.15, .2)]])
        jet = VGroup(self.ln(mid + UP * .5, mid + UP * 2.6, "blue", 9), self.ln(mid + DOWN * .5, mid + DOWN * 2.6, "blue", 9))
        self.say(0, [Write(t), FadeIn(glow)], Create(jet))
        est = self.label("≈ 40 to 66\nbillion Suns\n(estimates differ)", "yellow", P(5.3, 1.5), 28)
        self.say(1, Write(est))
        R = 3.0
        big = hole(R, mid, c["red"])
        radius = self.ln(mid, mid + R * P(np.cos(-.55), np.sin(-.55)), "yellow", 7)
        au = self.label("radius ≈ 800 ×\nEarth–Sun distance", "ink", P(5.1, -1.9), 28)
        self.say(2, [FadeOut(glow, jet), GrowFromCenter(big)], [Create(radius), Write(au)])
        reach = mid + R * 173 / 803 * LEFT                       # ölçekli: 173 / 803
        path = self.ln(mid, reach, "blue", 9)
        v = dot(reach, c["blue"], .12)
        vl = self.label("Voyager 1\n1 light-day", "blue", P(-5.2, .7), 30)
        pointer = Arrow(P(-4.4, .25), reach, color=c["blue"], stroke_width=4, buff=.15)
        self.say(3, [FadeOut(radius), Write(vl), Create(pointer)], [Create(path), FadeIn(v)])
        n = self.label("≈ 173 distances\nin ≈ 49 years", "blue", P(-5.1, -1.7), 28)
        self.say(4, Write(n))
        full = DashedLine(mid, mid + R * LEFT, color=c["yellow"], stroke_width=5)
        five = self.label("≈ 1/5 of the way", "yellow", mid + P(-.25, .55), 28)
        self.add(path, v)
        self.say(5, Create(full), [Write(five), Indicate(v, scale_factor=2)])
        self.end()


class Ladder(Tahta):
    theme = "beyaz"

    def construct(self):
        c = self.c
        t = self.title("The whole ladder (not to scale)")
        axis = Arrow(P(-6.7, -1.9), P(6.7, -1.9), color=c["ink"], stroke_width=5, buff=0)
        self.say(0, Write(t), Create(axis))
        data = [(-5.8, .08, "atom-sized\n(hypothetical)"), (-3.7, .22, "city-sized\nstellar"), (-1.5, .42, "candidate:\nwider than Earth"),
                (.9, .68, "inside Mercury's\norbit"), (3.1, .95, "swallows the\nplanets"), (5.45, 1.35, "TON 618")]
        items = [VGroup(hole(r, P(x, -1.9 + r + .15), c["red"], 5),
                        self.label(s, "ink", P(x, -2.45 if i % 2 == 0 else -3.1), 22)) for i, (x, r, s) in enumerate(data)]
        for i in range(3):
            self.say(i + 1, [GrowFromCenter(items[i][0]), Write(items[i][1])])
        self.say(4, *[[GrowFromCenter(m[0]), Write(m[1])] for m in items[3:]])
        self.end()


class End(Tahta):
    def construct(self):
        c = self.c
        self.add(stars(70, 21, c["gray"]))
        small = VGroup(self.label("SMALLEST", "blue", P(-3.6, 2.4), 38),
                       self.label("theory: below atom size\nevidence: a few Suns", "ink", P(-3.6, .9), 30))
        self.say(0, Write(small[0]), Write(small[1]))
        big = VGroup(self.label("BIGGEST", "red", P(3.6, 2.4), 38), self.label("tens of billions of Suns\n(as far as we know)", "ink", P(3.6, .9), 30))
        self.say(1, Write(big[0]), Write(big[1]))
        a = DashedVMobject(Circle(.55, color=c["gray"], stroke_width=5).move_to(P(-3.6, -.9)), num_dashes=16)
        b = hole(1.0, P(3.6, -.9), c["red"])
        q = self.label("which one?", "yellow", P(0, -.9), 40)
        self.say(2, [Create(a), GrowFromCenter(b)], Write(q))
        probe = dot(P(-6.5, -2.9), c["blue"], .12)
        trail = DashedLine(P(-6.5, -2.9), P(6.5, -2.9), color=c["blue"], stroke_width=4)
        nxt = self.label("next: how far have we reached?", "blue", P(0, -2.45), 30)
        self.say(3, [FadeOut(q), Create(trail), probe.animate.move_to(P(6.5, -2.9)), Write(nxt)])
        self.wait(.5)
