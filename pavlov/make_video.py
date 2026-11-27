"""ses/*.mp3 -> narration.mp3 + timing.js -> pavlov.mp4

Kendi sesinle: ses/0.mp3 ... ses/5.mp3 dosyalarının üzerine kaydını koy, tekrar çalıştır.
Metni değiştirdiysen ilgili ses/N.mp3 dosyasını sil, yeniden üretilir.
Ses: ELEVENLABS_API_KEY ortam değişkeni varsa ElevenLabs, yoksa ücretsiz edge-tts.
"""
import asyncio, base64, json, os, subprocess, tempfile, time, urllib.request
from pathlib import Path

from websockets.sync.client import connect

HERE = Path(__file__).parent
FPS, PORT, PAUSE = 20, 9333, 0.7
VOICE = "tr-TR-AhmetNeural"  # kadın sesi: tr-TR-EmelNeural
TEXTS = [
    "Telefonun bildirim sesini duyunca elin neden hemen telefona gidiyor? Cevabın ipucu, Pavlov'un köpeklerinde saklı.",
    "Birinci adım. Köpek yemeği görünce salyası akar. Bunu öğrenmesine gerek yoktur. Yemek koşulsuz uyarıcı, salya ise koşulsuz tepkidir.",
    "İkinci adım. Sadece zil çalıyoruz. Köpek için bu sesin henüz bir anlamı yok, salya akmıyor. Buna nötr uyarıcı denir.",
    "Üçüncü adım, eşleştirme. Önce zil çalar, hemen ardından yemek gelir. Bu defalarca tekrarlanır.",
    "Ve sonuç. Artık yemek olmasa bile, zil sesi salyayı akıtmaya yeter. Zil koşullu uyarıcıya, salya da koşullu tepkiye dönüştü.",
    "Hep zil diye anlatılır, ama Pavlov metronom gibi başka sesler de kullandı. Peki seni hangi ses koşullandırdı? Yorumlara yaz!",
]


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def speak_eleven(missing, key):
    voice = os.environ.get("ELEVENLABS_VOICE", "JBFqnCBsd6RMkjVDRZzb")  # George
    for i, path in missing:
        body = {"text": TEXTS[i], "model_id": "eleven_multilingual_v2",
                # komşu metin tonlamayı bölümler arasında tutarlı yapar
                "previous_text": " ".join(TEXTS[:i])[-300:], "next_text": " ".join(TEXTS[i+1:])[:300]}
        request = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
            json.dumps(body).encode(), {"xi-api-key": key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                path.write_bytes(response.read())
        except urllib.error.HTTPError as e:
            raise SystemExit(f"ElevenLabs HTTP {e.code}: {e.read().decode()}")
        print(f"ElevenLabs: bölüm {i} hazır")


async def speak(missing):
    import edge_tts
    for i, path in missing:
        await edge_tts.Communicate(TEXTS[i], VOICE, rate="-4%").save(str(path))


def build_audio():
    files = [HERE / "ses" / f"{i}.mp3" for i in range(len(TEXTS))]
    missing = [(i, f) for i, f in enumerate(files) if not f.exists()]
    if missing:
        if key := os.environ.get("ELEVENLABS_API_KEY"):
            speak_eleven(missing, key)
        else:
            asyncio.run(speak(missing))
    durations = [
        round(float(run("ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(f))) + PAUSE, 2)
        for f in files
    ]
    inputs = [x for f in files for x in ("-i", str(f))]
    graph = "".join(
        f"[{i}:a]aresample=44100,aformat=channel_layouts=mono,apad,atrim=0:{d}[a{i}];"
        for i, d in enumerate(durations)
    ) + "".join(f"[a{i}]" for i in range(len(files))) + f"concat=n={len(files)}:v=0:a=1[out]"
    run("ffmpeg", "-y", *inputs, "-filter_complex", graph, "-map", "[out]", str(HERE / "narration.mp3"))
    add_dings(durations)
    (HERE / "timing.js").write_text(f"const DUR = {json.dumps(durations)};\n", encoding="utf-8")
    return sum(durations)


def add_dings(durations):
    times = [sum(durations[:n]) + .2 + durations[n] * .6 for n in (2, 3, 4)]
    ding = "aevalsrc='0.12*(sin(2*PI*1320*t)+0.5*sin(2*PI*2640*t))*exp(-4*t)':s=44100:d=1.2"
    sources = [x for _ in times for x in ("-f", "lavfi", "-i", ding)]
    graph = "".join(f"[{i+1}:a]adelay={int(t*1000)}[d{i}];" for i, t in enumerate(times))
    graph += "[0:a]" + "".join(f"[d{i}]" for i in range(len(times))) + f"amix=inputs={len(times)+1}:duration=first:normalize=0"
    mixed = HERE / "mixed.mp3"
    run("ffmpeg", "-y", "-i", str(HERE / "narration.mp3"), *sources, "-filter_complex", graph, str(mixed))
    mixed.replace(HERE / "narration.mp3")


def record(total):
    edge = next(p for p in (
        Path(os.environ[v]) / "Microsoft/Edge/Application/msedge.exe"
        for v in ("ProgramFiles(x86)", "ProgramFiles")) if p.exists())
    profile = tempfile.mkdtemp()
    browser = subprocess.Popen([str(edge), "--headless=new", "--disable-gpu", f"--remote-debugging-port={PORT}",
                                f"--user-data-dir={profile}", "about:blank"])
    try:
        for _ in range(50):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
                url = next(t["webSocketDebuggerUrl"] for t in tabs if t["type"] == "page")
                break
            except (OSError, StopIteration):
                time.sleep(0.2)
        else:
            raise RuntimeError("Edge'e bağlanılamadı")
        with connect(url, max_size=None) as ws:
            n = 0

            def cdp(method, **params):
                nonlocal n
                n += 1
                ws.send(json.dumps({"id": n, "method": method, "params": params}))
                while (msg := json.loads(ws.recv(timeout=60))).get("id") != n:
                    pass
                if "error" in msg or "exceptionDetails" in msg.get("result", {}):
                    raise RuntimeError(msg)
                return msg["result"]

            def js(code):
                return cdp("Runtime.evaluate", expression=code, awaitPromise=True,
                           returnByValue=True)["result"].get("value")

            cdp("Emulation.setDeviceMetricsOverride", width=1600, height=900, deviceScaleFactor=1.2, mobile=False)
            cdp("Page.navigate", url=(HERE / "index.html").as_uri() + "?render")
            for _ in range(100):
                if js("document.readyState === 'complete' && typeof render === 'function'"):
                    break
                time.sleep(0.1)
            else:
                raise RuntimeError("sayfa yüklenmedi")
            js("document.fonts.load('700 30px Caveat', 'şİğ').then(() => document.fonts.ready).then(() => 1)")

            out = HERE / "pavlov.mp4"
            ff = subprocess.Popen(
                ["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                 "-i", str(HERE / "narration.mp3"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
                 "-c:a", "aac", "-shortest", str(out)], stdin=subprocess.PIPE)
            previous_key, frame = None, None
            for k in range(int(total * FPS)):
                t = k / FPS
                # çizim durduğunda aynı kareyi yeniden kullan
                key = js(f"render({t})")
                if key != previous_key:
                    frame = base64.b64decode(cdp("Page.captureScreenshot", format="jpeg", quality=92)["data"])
                    previous_key = key
                ff.stdin.write(frame)
            ff.stdin.close()
            if ff.wait():
                raise RuntimeError("ffmpeg hata verdi")
            cdp("Browser.close")
    finally:
        try:
            browser.wait(timeout=10)
        except subprocess.TimeoutExpired:
            browser.kill()
    return out


if __name__ == "__main__":
    total = build_audio()
    video = record(total)
    length = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)))
    assert abs(length - total) < 1, f"video {length}s, ses {total}s"
    print(f"OK {video} ({length:.1f}s)")
