"""python eleven.py <video-klasörü>  -> sahneler.TEXT'i ElevenLabs ile ses/<Sahne>_<n>.mp3 olarak yazar (üstüne).
Ortam: ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID. Model eleven_v4; duygu etiketleri sahneler.DUYGU
(yalnız sese gider, altyazıda görünmez). Üretilen satırlar ses/eleven.json'a işlenir; tekrar çalıştırınca kredi harcamaz."""
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

klasor = (Path(__file__).parent / sys.argv[1]).resolve()
sys.path[:0] = [str(Path(__file__).parent), str(klasor)]
import sahneler  # noqa: E402

TEXT, DUYGU = sahneler.TEXT, getattr(sahneler, "DUYGU", {})

key, ses = os.environ.get("ELEVENLABS_API_KEY"), os.environ.get("ELEVENLABS_VOICE_ID")
if not key or not ses:
    sys.exit("ELEVENLABS_API_KEY ve ELEVENLABS_VOICE_ID ortam degiskenlerini ayarla.")
hedef = klasor / "ses"
hedef.mkdir(exist_ok=True)
kayit = hedef / "eleven.json"
yapilan = json.loads(kayit.read_text()) if kayit.exists() else {}
satir = [(f"{ad}_{i}.mp3", s, DUYGU.get(f"{ad}_{i}", "")) for ad, v in TEXT.items() for i, s in enumerate(v)]
for n, (dosya, s, duygu) in enumerate(satir):
    soylenen = f"{duygu} {s}".strip()
    iz = hashlib.sha1(f"{ses}|eleven_v4|{soylenen}".encode()).hexdigest()
    if yapilan.get(dosya) == iz and (hedef / dosya).exists():
        continue
    govde = {"text": soylenen, "model_id": "eleven_v4",            # önceki/sonraki cümle tonlamayı tutarlı yapar
             "previous_text": satir[n - 1][1] if n else "", "next_text": satir[n + 1][1] if n + 1 < len(satir) else ""}
    istek = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{ses}?output_format=mp3_44100_128",
                                   data=json.dumps(govde).encode(), headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        veri = urllib.request.urlopen(istek, timeout=120).read()
    except urllib.error.HTTPError as e:
        sys.exit(f"{dosya}: HTTP {e.code} {e.read()[:300]!r}")
    (hedef / dosya).write_bytes(veri)
    yapilan[dosya] = iz
    kayit.write_text(json.dumps(yapilan, indent=1))
    print(n + 1, "/", len(satir), dosya, flush=True)
print("bitti")
