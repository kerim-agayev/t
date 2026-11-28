"""python belge.py <video-klasörü>  -> SENARYO.md, SESLENDIRME.md, altyazi.srt (taslak veya final render sonrası).
Videonun sahneler.py dosyasında TEXT, SAHNE (sahne -> bölüm, tahta, ekranda, bağ), META (başlık, notlar) olmalı.
001-black-holes kendi belge.py dosyasını kullanır."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
H = (HERE / sys.argv[1]).resolve()
sys.path[:0] = [str(HERE), str(H)]
from sahneler import DUYGU, META, SAHNE, TEXT  # noqa: E402


def zaman(t, srt=False):
    ms = round(t * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}" if srt else f"{m}:{s:02}"


t, srt, tablo, metin, bolum, ses = 0.0, [], [], [], [], []
tahmin = H / "media/tahmin.json"                 # stills.py: video yokken tahmini zaman
tahmin = json.loads(tahmin.read_text()) if tahmin.exists() and not list(H.glob("media/videos/sahneler/*/*.mp4")) else None
for ad, satirlar in TEXT.items():
    ad_en, tahta, ekran, bag = SAHNE[ad]
    if tahmin:
        uzun, anlar = tahmin[ad]["uzun"], tahmin[ad]["anlar"]
    else:
        klip = max(H.glob(f"media/videos/sahneler/*/{ad}.mp4"), key=lambda p: p.stat().st_mtime)
        uzun = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(klip)], text=True))
        anlar = json.loads((H / "media/zaman" / f"{ad}.json").read_text())
    bolum.append(f"{zaman(t)} {ad_en}")
    tablo.append(f"| {len(tablo) + 1} | {zaman(t)} | {uzun:.0f} sn | {ad_en} | {tahta} | {ekran} | {bag} |")
    metin.append(f"### {len(metin) + 1}. {ad_en}\n" + " ".join(satirlar))
    ses.append(f"### {ad}\n" + "".join(f"- `{ad}_{i}.mp3` {DUYGU.get(f'{ad}_{i}', '')} {s}\n" for i, s in enumerate(satirlar)))
    for i, s in enumerate(satirlar):
        bas, d = anlar[str(i)]
        srt.append(f"{len(srt) + 1}\n{zaman(t + bas, True)} --> {zaman(t + bas + d, True)}\n{s}\n")
    t += uzun
kelime = sum(len(s.split()) for v in TEXT.values() for s in v)
karakter = sum(len(s) for v in TEXT.values() for s in v)
(H / "altyazi.srt").write_text("\n".join(srt), encoding="utf-8")
(H / "SENARYO.md").write_text(f"""# Senaryo: {META['baslik']}

Üretildi: `belge.py` (metni `sahneler.py` içinde değiştir). Süre {zaman(t)}{' (TAHMİNİ: video henüz üretilmedi)' if tahmin else ''}, {kelime} kelime.

{META['notlar']}

## Sahne tablosu
| # | Başlangıç | Süre | Sahne | Tahta | Ekranda | Soru / bağ |
|---|---|---|---|---|---|---|
{chr(10).join(tablo)}

## Seslendirme metni
{chr(10).join(chr(10) + m for m in metin)}

## Bölümler (açıklamaya)
```
{chr(10).join(bolum)}
```
""", encoding="utf-8")
(H / "SESLENDIRME.md").write_text(f"""# Seslendirme

ElevenLabs `eleven_v4`, ses: `8GmsjNWRZ3Rk8VmRpvBZ` (kullanıcı seçimi). Metin yaklaşık {karakter} karakter; köşeli etiketler yalnız sese gider.
`kanal_2/` içinde (Git Bash). Anahtar yalnız `../.env` dosyasında (git dışı).
```bash
set -a; . ../.env; set +a
.venv/Scripts/python eleven.py {H.name}
.venv/Scripts/python render.py {H.name} final
.venv/Scripts/python belge.py {H.name}
```

{chr(10).join(ses)}""", encoding="utf-8")
print(zaman(t), kelime, "kelime", karakter, "karakter")
