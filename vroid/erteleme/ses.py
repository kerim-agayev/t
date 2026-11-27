"""SENARYO.md metni -> ses/*.mp3, ses.wav, zaman.json.
Çalıştır (vroid/erteleme içinde): ../../trigonometri/.venv/Scripts/python ses.py"""
import asyncio
import json
import re
import subprocess
import wave
from pathlib import Path

import edge_tts
import numpy as np

HERE = Path(__file__).parent
FPS, SR = 30, 48000
SESLER = {"A": dict(rate="-3%", pitch="+0Hz"),       # anlatıcı
          "E": dict(rate="+6%", pitch="+28Hz"),       # Elif
          "Y": dict(rate="-6%", pitch="-18Hz")}       # yarınki Elif
ELIF = {"Sadece beş dakika.", "Sen kimsin?"}
YARIN = {"Ben yarınki senim.", "Her beş dakikada o sıkıntıyı bana yolladın.", "Yok olmadı.", "Birikti.",
         "Üstüne bir de suçluluk eklendi."}


def sahneler():
    s = (HERE / "SENARYO.md").read_text(encoding="utf-8")
    s = s.split("## 4. Seslendirme metni")[1].split("Toplam ")[0]
    for blok in re.split(r"### \d\. .*\n", s)[1:]:
        m = blok.strip().replace("Elif soruyor: ", "Elif soruyor. ").replace("Cevap geliyor: ", "Cevap geliyor. ")
        yield [(("E" if c in ELIF else "Y" if c in YARIN else "A"), c) for c in re.split(r"(?<=[.?!]) ", m)]


async def main():
    (HERE / "ses").mkdir(exist_ok=True)
    zaman, parcalar = [], []
    for n, satirlar in enumerate(sahneler(), 1):
        t, sesler, cizelge = .35, [], []
        for i, (kim, metin) in enumerate(satirlar):
            f = HERE / "ses" / f"{n}_{i}.mp3"
            if not f.exists():
                for deneme in range(6):                          # ücretsiz servis ara sıra boş dönüyor
                    try:
                        await edge_tts.Communicate(metin, "tr-TR-EmelNeural", **SESLER[kim]).save(str(f))
                        break
                    except Exception as e:
                        f.unlink(missing_ok=True)
                        if deneme == 5:
                            raise RuntimeError(f"{f.name} [{kim}] {metin}") from e
                        await asyncio.sleep(2 + 2 * deneme)
            pcm = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(f), "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"])
            a = np.frombuffer(pcm, np.int16)
            ses_var = np.nonzero(np.abs(a) > 250)[0]                # edge-tts sondaki sessizliği kırp
            a = a[max(ses_var[0] - 1200, 0): ses_var[-1] + 3600]
            dur = len(a) / SR
            cizelge.append(dict(t0=round(t, 3), t1=round(t + dur, 3), kim=kim, metin=metin))
            sesler.append((int(t * SR), a))
            t += dur + (.45 if metin.endswith("?") else .34)
        kare = int(np.ceil((t + .55) * FPS))
        iz = np.zeros(kare * SR // FPS, np.int16)
        for bas, a in sesler:
            iz[bas: bas + len(a)] = a[: len(iz) - bas]
        adim = SR // FPS
        rms = np.sqrt((iz.astype(np.float64).reshape(kare, adim) ** 2).mean(1))
        agiz = np.clip(rms / 5000, 0, 1)
        zaman.append(dict(kare=kare, satirlar=cizelge, agiz=[round(float(v), 2) for v in agiz]))
        parcalar.append(iz)
    with wave.open(str(HERE / "ses.wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(np.concatenate(parcalar).tobytes())
    (HERE / "zaman.json").write_text(json.dumps(zaman, ensure_ascii=False), encoding="utf-8")
    kareler = sum(z["kare"] for z in zaman)
    print(f"OK {kareler / FPS:.1f} sn, {kareler} kare")


asyncio.run(main())
