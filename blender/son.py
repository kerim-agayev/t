"""Ses, yazı ve birleştirme: ../trigonometri/.venv/Scripts/python son.py -> domino.mp4"""
import json
import subprocess
import wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
SR, DUR = 48000, 30.0
o = json.loads((HERE / "olaylar.json").read_text())
rng = np.random.default_rng(3)
iz = np.zeros(int(SR * DUR))


def ekle(t, ses):
    a = int(t * SR)
    iz[a:a + len(ses)] += ses[: len(iz) - a]


def vurus(frekans, sure, guc, gurultu):
    t = np.arange(int(SR * sure)) / SR
    zarf = np.exp(-t * 6 / sure) * np.minimum(1, t * 2000)
    govde = np.sin(2 * np.pi * frekans * t) + 0.5 * np.sin(2 * np.pi * frekans * 2.37 * t)
    gur = np.convolve(rng.normal(0, 1, len(t)), np.ones(12) / 12, "same")
    return guc * zarf * (govde + gurultu * gur * np.exp(-t * 18 / sure))


# taş büyüdükçe ses kalınlaşır, uzar ve güçlenir
for i, t in enumerate(o["carpma"]):
    k = i / (len(o["carpma"]) - 1)
    ekle(t, vurus(2600 * (70 / 2600) ** k, 0.07 + 0.9 * k ** 2, 0.10 + 0.5 * k, 1.5))
ekle(o["son"], vurus(42, 3.2, 1.0, 4.0))
ekle(o["son"], vurus(95, 1.4, 0.6, 6.0))
ruzgar = np.convolve(rng.normal(0, 1, len(iz)), np.ones(400) / 400, "same")
iz += ruzgar * 0.08
iz = np.tanh(iz * 1.1)
with wave.open(str(HERE / "ses.wav"), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((iz * 30000).astype(np.int16).tobytes())


def zaman(t):
    return f"0:{int(t // 60):02d}:{t % 60:05.2f}"


def boy(m):
    return f"{m * 100:.1f} cm".replace(".", ",") if m < 1 else f"{m:.1f} m".replace(".", ",")


satir = lambda a, b, stil, metin: f"Dialogue: 0,{zaman(a)},{zaman(b)},{stil},,0,0,0,,{{\fad(180,180)}}{metin}"
olaylar = [satir(0.2, 3.5, "Buyuk", "1 santimlik bir taş,\\Napartman boyunda bir taşı devirebilir mi?")]
for i, t in enumerate(o["carpma"]):
    son = o["carpma"][i + 1] if i + 1 < len(o["carpma"]) else o["son"]
    olaylar.append(f"Dialogue: 0,{zaman(t)},{zaman(son)},Sayac,,0,0,0,,{i + 1}. taş  ·  {boy(o['boy'][i])}")
olaylar.append(satir(o["son"] + 1.6, DUR, "Buyuk", f"20 taş: 1 cm'den {boy(o['boy'][-1])}'ye\\NHer biri öncekinin yalnız 1,5 katı"))
stil = "Style: {},Segoe UI,{},&H00FFFFFF,&H000000FF,&H00201408,&H80000000,-1,0,0,0,100,100,0,0,1,{},2,{},60,60,{},1"
(HERE / "yazi.ass").write_text("\n".join([
    "[Script Info]", "ScriptType: v4.00+", "PlayResX: 1920", "PlayResY: 1080", "", "[V4+ Styles]",
    "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
    stil.format("Buyuk", 76, 5, 8, 70), stil.format("Sayac", 62, 4, 1, 55), "", "[Events]",
    "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text", *olaylar]), encoding="utf-8")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", "kare/%04d.jpg", "-i", "ses.wav", "-vf", "ass=yazi.ass",
                "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-15",
                "-ar", "48000", "-shortest", "domino.mp4"], cwd=HERE, check=True)
print("OK domino.mp4")
