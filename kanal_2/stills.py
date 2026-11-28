"""python stills.py <video-klasörü> [Sahne ...]   Video ÜRETMEDEN her cümlenin son karesi + yerleşim denetimi.
Çıktı: media/kare/<tarz>/<Sahne>_<n>.png; tüm sahneler çalışınca onizleme/sayfa_<k>.png,
SENARYO.md, SESLENDIRME.md, altyazi.srt (tahmini zaman)."""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
klasor = (HERE / sys.argv[1]).resolve()
secili = sys.argv[2:]
sys.path[:0] = [str(HERE), str(klasor)]
from manim import RoundedRectangle, Text, tempconfig  # noqa: E402

import sahneler  # noqa: E402
from marj import KENAR_X, TARZ  # noqa: E402
from tahta import sesler  # noqa: E402

sesler(sahneler.TEXT, klasor)                      # zaman tahmini için ücretsiz taslak sesi
kare_dir = klasor / "media/kare" / TARZ
kare_dir.mkdir(parents=True, exist_ok=True)
sorunlar, kareler, anlar, tahmin = [], [], {}, {}


def metinler(m):
    if isinstance(m, Text):
        if max((s.get_fill_opacity() for s in m.family_members_with_points()), default=0) > .3:
            yield m
        return
    for alt in m.submobjects:
        yield from metinler(alt)


def kartlar(m):
    if isinstance(m, RoundedRectangle):
        yield m
    for alt in m.submobjects:
        yield from kartlar(alt)


def denetle(sahne, ad):
    alt = list(metinler(sahne.caption))
    if len(alt) > 2 or any(a.width > 15.4 for a in alt):
        sorunlar.append(f"{ad}: altyazı {len(alt)} satır")
    govde = [t for m in sahne.mobjects if m is not sahne.caption for t in metinler(m)]
    kutular = [k for m in sahne.mobjects if m is not sahne.caption for k in kartlar(m)]
    for i, a in enumerate(govde):
        x0, x1, y0, y1 = a.get_left()[0], a.get_right()[0], a.get_bottom()[1], a.get_top()[1]
        isim = repr(a.original_text)
        for k in kutular:                           # merkezi bir kartın içinde olan yazı karttan taşmamalı
            ic = k.get_left()[0] < (x0 + x1) / 2 < k.get_right()[0] and k.get_bottom()[1] < (y0 + y1) / 2 < k.get_top()[1]
            if ic and (x0 < k.get_left()[0] + .04 or x1 > k.get_right()[0] - .04):
                sorunlar.append(f"{ad}: karttan taşıyor {isim} yazı {x1 - x0:.2f}, kart {k.width:.2f}")
        if x0 < -7.9 or x1 > 7.9 or y1 > 3.95 or y0 < -3.45:
            sorunlar.append(f"{ad}: taşma {isim} x={x0:.2f}..{x1:.2f} y={y0:.2f}..{y1:.2f}")
        if x0 < KENAR_X + .1 and x1 > KENAR_X - .05:
            sorunlar.append(f"{ad}: kenar çizgisini kesiyor {isim} x={x0:.2f}..{x1:.2f}")
        for b in govde[i + 1:]:
            gx = min(x1, b.get_right()[0]) - max(x0, b.get_left()[0])
            gy = min(y1, b.get_top()[1]) - max(y0, b.get_bottom()[1])
            if gx > .06 and gy > .06:
                sorunlar.append(f"{ad}: yazılar çakışıyor {isim} / {b.original_text!r} ({gx:.2f}x{gy:.2f})")


for ad in sahneler.TEXT:
    if secili and ad not in secili:
        continue

    class Kare(getattr(sahneler, ad)):
        def setup(self):
            super().setup()
            self.renderer._original_skipping_status = True
            self.renderer.skip_animations = True

        def sahne_adi(self):
            return type(self).__mro__[1].__name__

        def _zaman(self, i, dur):
            anlar[str(i)] = [self.renderer.time, dur]

        def say(self, i, *a, **k):
            super().say(i, *a, **k)
            self.renderer.update_frame(self, ignore_skipping=True)
            isim = f"{self.sahne_adi()}_{i}"
            yol = kare_dir / f"{isim}.png"
            Image.fromarray(self.renderer.get_frame()).convert("RGB").save(yol)
            kareler.append((isim, yol))
            denetle(self, isim)

    Kare.__module__ = "sahneler"
    with tempconfig({"dry_run": True, "pixel_width": 1280, "pixel_height": 720, "frame_rate": 10, "disable_caching": True,
                     "media_dir": str(klasor / "media"), "verbosity": "ERROR", "progress_bar": "none"}):
        anlar = {}
        s = Kare()
        s.render()
        tahmin[ad] = {"uzun": s.renderer.time, "anlar": anlar}
    print("sahne", ad, flush=True)

if not secili:
    (klasor / "media/tahmin.json").write_text(json.dumps(tahmin))
    subprocess.run([sys.executable, str(HERE / "belge.py"), klasor.name], check=True)   # SENARYO, SESLENDIRME, altyazi.srt
    sayfa_dir = klasor / "onizleme"
    sayfa_dir.mkdir(exist_ok=True)
    for eski in sayfa_dir.glob("sayfa_*.png"):
        eski.unlink()
    yazi = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
    W, H = 480, 270
    for k in range(0, len(kareler), 12):
        grup = kareler[k:k + 12]
        satir = (len(grup) + 2) // 3
        sayfa = Image.new("RGB", (3 * (W + 8) + 8, satir * (H + 30) + 8), (60, 60, 60))
        d = ImageDraw.Draw(sayfa)
        for n, (isim, yol) in enumerate(grup):
            x, y = 8 + (n % 3) * (W + 8), 8 + (n // 3) * (H + 30)
            sayfa.paste(Image.open(yol).resize((W, H), Image.LANCZOS), (x, y))
            d.text((x + 4, y + H + 2), isim, font=yazi, fill=(255, 255, 255))
        sayfa.save(sayfa_dir / f"sayfa_{k // 12 + 1}.png")
    print(f"tahmini süre {sum(v['uzun'] for v in tahmin.values()):.0f} sn, {len(kareler)} kare")
print("\n".join(sorunlar) if sorunlar else "yerleşim denetimi: sorun yok")
