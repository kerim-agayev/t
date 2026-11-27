"""Bilim alt nişleri: YouTube Data API v3 ile son 12 ayın videoları.
YOUTUBE_API_KEY ortam değişkeni gerekir. Kota: sorgu başına yaklaşık 100 birim (günlük ücretsiz 10.000).
python altnis.py <çıktı.json>"""
import json
import os
import re
import statistics as st
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

ANAHTAR = os.environ["YOUTUBE_API_KEY"]
NISLER = {
    "Uzay ve astronomi": ["space explained", "what would happen universe explained"],
    "'Ne olurdu' bilim": ["what if science explained", "what would happen if earth"],
    "Mühendislik: nasıl çalışır": ["how does it work engineering animation", "engineering explained 3d animation"],
    "İnsan vücudu": ["how your body works explained", "what happens to your body animation"],
    "Görsel matematik": ["math explained visually", "why does this math work animation"],
    "Olasılık ve paradoks": ["paradox explained", "probability puzzle explained"],
    "Ölçek karşılaştırma": ["size comparison 3d animation", "scale of the universe comparison"],
    "Fizik kavramları": ["physics explained animation", "quantum physics explained simply"],
    "Dünya ve coğrafya bilimi": ["earth science explained", "geography explained why"],
    "Canlılar ve evrim": ["evolution explained animation", "animal biology explained"],
    "Bilgisayar ve internet": ["how computers work explained", "how the internet works animation"],
    "Yapay zekâ anlatımı": ["how ai works explained", "neural networks explained visually"],
    "Psikoloji bilimi": ["psychology explained animation", "why your brain does this"],
    "Bilim tarihi": ["history of science explained", "how scientists discovered"],
    "Ekonomi anlatımı (kıyas)": ["economics explained animation", "how money works explained"],
}


def api(yol, **q):
    url = f"https://www.googleapis.com/youtube/v3/{yol}?{urllib.parse.urlencode(q)}"
    istek = urllib.request.Request(url, headers={"X-goog-api-key": ANAHTAR})
    try:
        with urllib.request.urlopen(istek, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"API hatası {e.code}: {e.read().decode(errors='replace')[:600]}")


def parcala(x):
    return [x[i:i + 50] for i in range(0, len(x), 50)]


simdi = datetime.now(timezone.utc)
once = lambda g: (simdi - timedelta(days=g)).strftime("%Y-%m-%dT%H:%M:%SZ")
bulunan = {}
for nis, sorgular in NISLER.items():
    ids = []
    for s in sorgular:
        r = api("search", part="id", q=s, type="video", maxResults=50, relevanceLanguage="en", regionCode="US",
                videoDuration="medium", publishedAfter=once(365), publishedBefore=once(30))
        ids += [x["id"]["videoId"] for x in r["items"]]
    bulunan[nis] = list(dict.fromkeys(ids))
    print("arandı:", nis, len(bulunan[nis]), flush=True)

videolar, kanallar = {}, {}
for p in parcala(list({i for v in bulunan.values() for i in v})):
    for x in api("videos", part="snippet,statistics", id=",".join(p), maxResults=50)["items"]:
        videolar[x["id"]] = x
for p in parcala(list({v["snippet"]["channelId"] for v in videolar.values()})):
    for x in api("channels", part="statistics", id=",".join(p), maxResults=50)["items"]:
        kanallar[x["id"]] = x["statistics"]


def ingilizce(v):
    s = v["snippet"]
    dil = s.get("defaultAudioLanguage") or s.get("defaultLanguage")
    if dil:
        return dil.startswith("en")
    harf = [c for c in s["title"] if c.isalpha()]
    return bool(harf) and sum(c.isascii() for c in harf) / len(harf) > .95 and bool(re.search(r"\b(the|how|why|what|is|of|if|your)\b", s["title"], re.I))


sonuc = {}
for nis, ids in bulunan.items():
    satir = []
    for i in ids:
        v = videolar.get(i)
        if not v or not ingilizce(v) or "viewCount" not in v["statistics"]:
            continue
        k = kanallar.get(v["snippet"]["channelId"], {})
        satir.append(dict(id=i, baslik=v["snippet"]["title"], kanal=v["snippet"]["channelTitle"], izlenme=int(v["statistics"]["viewCount"]),
                          abone=None if k.get("hiddenSubscriberCount") else int(k.get("subscriberCount", 0))))
    kucuk = [x for x in satir if x["abone"] is not None and x["abone"] < 100_000]
    toplam = sum(x["izlenme"] for x in satir) or 1
    kanal_top = {}
    for x in satir:
        kanal_top[x["kanal"]] = kanal_top.get(x["kanal"], 0) + x["izlenme"]
    sonuc[nis] = dict(
        n=len(satir),
        medyan=st.median([x["izlenme"] for x in satir]) if satir else 0,
        kucuk_n=len(kucuk),
        kucuk_medyan=st.median([x["izlenme"] for x in kucuk]) if kucuk else 0,
        kucuk_100bin=sum(x["izlenme"] >= 100_000 for x in kucuk) / len(kucuk) if kucuk else 0,
        ilk5_pay=sum(sorted(kanal_top.values(), reverse=True)[:5]) / toplam,
        ornek=sorted(kucuk, key=lambda x: -x["izlenme"])[:4],
        videolar=satir)

json.dump(dict(tarih=simdi.isoformat(), nisler=sonuc), open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False)
print(f"\n{'niş':30} {'n':>3} {'medyan':>9} {'küçük n':>7} {'küçük medyan':>12} {'küçük>100b':>10} {'ilk5 payı':>9}")
for nis, r in sorted(sonuc.items(), key=lambda x: -x[1]["kucuk_medyan"]):
    print(f"{nis:30} {r['n']:>3} {r['medyan']:>9.0f} {r['kucuk_n']:>7} {r['kucuk_medyan']:>12.0f} {r['kucuk_100bin']:>10.0%} {r['ilk5_pay']:>9.0%}")
for nis, r in sorted(sonuc.items(), key=lambda x: -x[1]["kucuk_medyan"])[:6]:
    print(f"\n## {nis}")
    for x in r["ornek"]:
        print(f"  {x['izlenme']:>9} | abone {x['abone']:>6} | {x['kanal'][:24]} | {x['baslik'][:80]}")
