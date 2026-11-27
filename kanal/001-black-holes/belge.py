"""sahneler.py metni + ses süreleri -> SENARYO.md, altyazi.srt, bölüm zamanları. (kanal/ içinde) python 001-black-holes/belge.py"""
import subprocess
import sys
from pathlib import Path

H = Path(__file__).parent
sys.path[:0] = [str(H.parent), str(H)]
from mutagen.mp3 import MP3  # noqa: E402
from sahneler import TEXT  # noqa: E402

# sahne: (bölüm adı, tahta, ekranda ne var, açılan/kapanan soru)
SAHNE = {
    "Hook": ("How small? How big?", "siyah", "nokta kadar delik, tahtaya sığmayan delik, Voyager izi", "AÇ: ne kadar küçük/büyük? AÇ: Voyager"),
    "What": ("What is a black hole?", "siyah", "top atışı, olay ufku, Güneş yerine kara delik", "ama süpürge değil"),
    "Rule": ("One rule for size", "beyaz", "1 ve 2 Güneş yarıçapı, Dünya -> bilye", "bu yüzden boyut = kütle"),
    "Primordial": ("Primordial (hypothetical)", "siyah", "hayalet daire, ilk saniye, atom", "ama kanıt yok"),
    "Stellar": ("Stellar mass", "siyah", "yıldız çöküşü, şehir ölçeği, eşlik yıldızı", "ışık yok, nasıl bulunur?"),
    "Fall": ("Falling in", "beyaz", "çöp adam uzar; devde tek parça", "ters köşe; AÇ: nasıl bu kadar büyür?"),
    "Middle": ("Intermediate mass", "siyah", "kayıp halka, 2023 birleşmesi, Omega Centauri", "ama hâlâ aday"),
    "Center": ("Sagittarius A*", "siyah", "yıldız yörüngeleri, Merkür yörüngesi, halka", "büyüme sorusu açık kalır (dürüstçe)"),
    "M87": ("M87*", "siyah", "Neptün yörüngesi içeride", "ama daha büyüğü var"),
    "Monster": ("TON 618", "siyah", "Voyager yarıçapın 1/5'inde", "KAPAT: Voyager"),
    "Ladder": ("The whole ladder", "beyaz", "tüm basamaklar tek tahtada", "görsel zirve"),
    "End": ("So how small, how big?", "siyah", "iki uç yan yana, Voyager köprüsü", "KAPAT: ana soru; izleyiciye soru; video 2"),
}


def zaman(t, srt=False):
    ms = round(t * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}" if srt else f"{m}:{s:02}"


EK = {("Center", 3): .7, ("Center", 4): .4}   # sahneler.py'de cümle öncesi temizleme süreleri
t, srt, tablo, metin, bolum = 0.0, [], [], [], []
for ad, satirlar in TEXT.items():
    ad_en, tahta, ekran, soru = SAHNE[ad]
    klip = max(H.glob(f"media/videos/sahneler/*/{ad}.mp4"), key=lambda p: p.stat().st_mtime)  # son render
    uzun = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(klip)], text=True))
    bolum.append(f"{zaman(t)} {ad_en}")
    tablo.append(f"| {len(tablo) + 1} | {zaman(t)} | {uzun:.0f} sn | {ad_en} | {tahta} | {ekran} | {soru} |")
    metin.append(f"### {len(metin) + 1}. {ad_en}\n" + " ".join(satirlar))
    bas = t
    for i, s in enumerate(satirlar):
        bas += EK.get((ad, i), 0)
        d = MP3(H / "ses" / f"{ad}_{i}.mp3").info.length
        srt.append(f"{len(srt) + 1}\n{zaman(bas, True)} --> {zaman(bas + d, True)}\n{s}\n")
        bas += d + .3
    t += uzun
kelime = sum(len(s.split()) for v in TEXT.values() for s in v)
(H / "altyazi.srt").write_text("\n".join(srt), encoding="utf-8")
(H / "SENARYO.md").write_text(f"""# Senaryo: Every Type of Black Hole, From Tiny to Monstrous

Durum: **onaylandı (2026-11-27), video üretildi.** Bu dosya `belge.py` ile `sahneler.py` metninden üretilir; metni orada değiştir.

- İzleyici: uzayı merak eden, fizik bilmeyen İngilizce izleyici.
- Büyük soru: Bir kara delik ne kadar küçük veya büyük olabilir?
- Akılda kalacak: aynı fizik, atom altı (teori) ile onlarca milyar Güneş arası; boyutu kütle belirler.
- Biçim: küçükten büyüğe tur. Süre {zaman(t)}, {kelime} kelime, video sesi geçici (en-US-AndrewNeural), ElevenLabs ile değişecek: SESLENDIRME.md.
- Kanca: seçilen "nokta ile tahtaya sığmayan daire". Elenen: "yıldızın çöküş anı" (soru geç geliyor), "Güneş yerine kara delik koysak?" (asıl soruyu karşılamıyor).
- Sapma: küçükten büyüğe sıra, arada tek ters köşe (düşme sahnesi) ritim için.

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
print(zaman(t), kelime)

# ElevenLabs veya kendi sesin için metin: dosya adı + cümle
(H / "SESLENDIRME.md").write_text("""# Seslendirme metni ve ses değiştirme

Videodaki ses **geçici** (edge-tts, en-US-AndrewNeural). Yayından önce değiştirilecek.

## ElevenLabs ile (evde)
1. Yeni hesapta API anahtarı ve ses kimliği (Voice ID) al. **Anahtarı dosyaya veya commit'e yazma.**
2. `kanal/` içinde (Git Bash):
   ```bash
   uv venv -p 3.13 && uv pip install -r requirements.txt      # bir kez
   export ELEVENLABS_API_KEY=...  ELEVENLABS_VOICE_ID=...
   .venv/Scripts/python eleven.py 001-black-holes              # ses/ dosyalarının üstüne yazar
   .venv/Scripts/python render.py 001-black-holes final        # görüntü yeni sese göre yeniden kurulur
   .venv/Scripts/python 001-black-holes/belge.py               # altyazi.srt ve bölüm zamanları
   ```
3. SENARYO.md sonundaki yeni bölüm zamanlarını PAKET.md açıklamasına kopyala.

Notlar: ElevenLabs ücretsiz plan aylık 10.000 kredi (bu metin yaklaşık """ + str(sum(len(s) for v in TEXT.values() for s in v)) + """ karakter); **ticari lisans Starter planda**
(2026-11-27 fiyat sayfası; para kazanılacaksa Starter al ve sesi o planda üret). Kendi sesin: aynı adlarla `ses/` içine mp3 koy, 3. satırdaki render'ı çalıştır.

## Metin (satır başı = dosya adı)
""" + "".join(f"\n### {sahne}\n" + "".join(f"- `{sahne}_{i}.mp3` — {s}\n" for i, s in enumerate(v)) for sahne, v in TEXT.items()), encoding="utf-8")
