"""Final video denetimi. (kanal_2/ içinde)
kare   : PYTHONUTF8=1 uv run --no-project -p 3.13 --with pillow python -X utf8 -I araclar/final_kontrol.py <klasör> kare
         -> <klasör>/media/kontrol/sayfa_*.png (her cümlenin sonundaki kare)
senkron: PYTHONUTF8=1 uv run --no-project -p 3.13 --with faster-whisper python -X utf8 -I araclar/final_kontrol.py <klasör> senkron
         -> her altyazı aralığında doğru cümle söyleniyor mu"""
import difflib
import re
import subprocess
import sys
from pathlib import Path

H = Path(__file__).resolve().parent.parent / sys.argv[1]
S = H / "media/kontrol"


def sn(x):
    h, m, s = x.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


bloklar = [b.split("\n") for b in (H / "altyazi.srt").read_text(encoding="utf-8").strip().split("\n\n")]
srt = [(sn(b[1].split(" --> ")[0]), sn(b[1].split(" --> ")[1]), " ".join(b[2:])) for b in bloklar]

if sys.argv[2] == "kare":
    from PIL import Image, ImageDraw, ImageFont
    S.mkdir(parents=True, exist_ok=True)
    yazi = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
    kareler = []
    for n, (a, b, _) in enumerate(srt):
        yol = S / f"{n:02d}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{b - .12:.3f}", "-i", str(H / "video.mp4"), "-frames:v", "1",
                        "-vf", "scale=480:270", str(yol)], check=True)
        kareler.append((f"{n + 1}  @{b:.1f}s", yol))
    for k in range(0, len(kareler), 15):
        grup = kareler[k:k + 15]
        sayfa = Image.new("RGB", (3 * 488 + 8, (len(grup) + 2) // 3 * 300 + 8), (60, 60, 60))
        d = ImageDraw.Draw(sayfa)
        for n, (isim, yol) in enumerate(grup):
            x, y = 8 + (n % 3) * 488, 8 + (n // 3) * 300
            sayfa.paste(Image.open(yol), (x, y))
            d.text((x + 4, y + 272), isim, font=yazi, fill=(255, 255, 255))
        sayfa.save(S / f"sayfa_{k // 15 + 1}.png")
    print(len(kareler), "kare ->", S)
else:
    import numpy as np
    from faster_whisper import WhisperModel
    ham = subprocess.run(["ffmpeg", "-v", "error", "-i", str(H / "video.mp4"), "-vn", "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    ses = np.frombuffer(ham, np.float32).copy()
    model = WhisperModel("base.en", device="cpu", compute_type="int8", cpu_threads=4)

    def sade(s):
        return re.findall(r"[a-z0-9]+", s.lower().replace(",", ""))

    sorun = 0
    for n, (a, b, metin) in enumerate(srt):
        parca = ses[max(0, int((a - .05) * 16000)):int((b + .05) * 16000)]
        p = list(model.transcribe(parca, language="en", beam_size=3, word_timestamps=True)[0])
        duyulan = " ".join(x.text.strip() for x in p)
        sozcuk = [w for x in p for w in (x.words or [])]
        bas = sozcuk[0].start - .05 if sozcuk else 9
        oran = difflib.SequenceMatcher(None, sade(metin), sade(duyulan)).ratio()
        if oran < .85 or bas > .8:
            sorun += 1
            print(f"KONTROL {n + 1} @{a:.2f}-{b:.2f} benzerlik {oran:.2f} ilk-soz {bas:.2f}s\n   metin  : {metin}\n   duyulan: {duyulan}", flush=True)
    print(f"{len(srt)} cümle denetlendi, sorunlu {sorun}; son altyazı bitişi {srt[-1][1]:.2f}s, ses uzunluğu {len(ses) / 16000:.2f}s")
