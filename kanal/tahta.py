"""Kanalın tahta tarzı: renkler, el çizimi yardımcıları, sesle senkron sahne.
Her video klasöründeki sahneler.py bunu kullanır (örnek: ornek/sahneler.py)."""
import asyncio
import sys
import textwrap
from pathlib import Path

import numpy as np
from manim import *
from mutagen.mp3 import MP3

FONT = "Segoe Print"
SES_ADI, SES_HIZI = "en-US-AndrewNeural", "+0%"      # taslak seçim; ilk videoda örnek dinletip onaylat
THEMES = {
    "beyaz": dict(bg="#fbfaf5", ink="#1f2328", red="#d6453b", blue="#2f6fd6", yellow="#e0a106", green="#2f9a58", gray="#8a8f98"),
    "siyah": dict(bg="#14171c", ink="#f2f2ee", red="#ff6b5e", blue="#58c4dd", yellow="#ffd95a", green="#83c167", gray="#6c727c"),
}
config.frame_height, config.frame_width = 9.0, 16.0


def P(x, y):
    return np.array([x, y, 0.0])


def text(s, color, size=34, **kw):
    # büyük çizip küçültmek harf aralığını düzgün tutar (uzun satırı kaydırır: satır başına ~40 karakter)
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


class Tahta(Scene):
    """Kullanım: class Kanca(Tahta): theme = "siyah"; construct içinde self.say(i, adım, ...)."""
    theme = "siyah"

    def setup(self):
        self.c = THEMES[self.theme]
        self.camera.background_color = self.c["bg"]
        self.camera.frame_center = P(0, -.5)      # alttaki ek alan altyazı bandı
        self.caption = None
        self.modul = sys.modules[type(self).__module__]

    def say(self, i, *steps, extra=0.3):
        """i. cümleyi seslendirir; adımlar cümle süresine eşit paylaştırılır."""
        name = type(self).__name__
        f = Path(self.modul.__file__).parent / "ses" / f"{name}_{i}.mp3"
        dur = MP3(f).info.length
        if self.caption:
            self.remove(self.caption)
        # 48+ punto Pango satır kaydırması yapıyor; altyazı küçük puntoyla
        lines = VGroup(*[Text(t, font=FONT, color=self.c["ink"], font_size=32).scale(22 / 32)
                         for t in textwrap.wrap(self.modul.TEXT[name][i], 96)]).arrange(DOWN, buff=.1)
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
        return VGroup(t, line(t.get_corner(DL) + DOWN * .1, t.get_corner(DR) + DOWN * .1, self.c["yellow"], 7))

    def label(self, s, color, pos, size=32):
        return text(s, self.c[color], size).move_to(pos)

    def ln(self, a, b, color="ink", w=6):
        return line(a, b, self.c[color], w)

    def end(self):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=.6)


def sesler(text_dict, klasor):
    """Eksik cümleleri seslendirir. Metin değişince ilgili ses/<Sahne>_<n>.mp3 dosyasını sil."""
    async def calis():
        import edge_tts
        hedef = Path(klasor) / "ses"
        hedef.mkdir(exist_ok=True)
        for sahne, satirlar in text_dict.items():
            for i, s in enumerate(satirlar):
                f = hedef / f"{sahne}_{i}.mp3"
                for deneme in range(6):
                    if f.exists() and f.stat().st_size:
                        break
                    try:                                       # ücretsiz servis ara sıra boş dönüyor
                        await edge_tts.Communicate(s, SES_ADI, rate=SES_HIZI).save(str(f))
                    except Exception:
                        f.unlink(missing_ok=True)
                        if deneme == 5:
                            raise
                        await asyncio.sleep(2 + 2 * deneme)
    asyncio.run(calis())
    n = sum(len(s) for v in text_dict.values() for s in v)
    print(f"{n} karakter")
