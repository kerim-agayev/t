"""Figma vektörü ve Open Peeps sahnesini anlatımlı videoya çevirir. Çalıştır: python make.py [figma|openpeeps]
Gerekli: Edge, ffmpeg, pip install websockets edge-tts. Sesler ses/ klasöründe saklanır (metin değişirse ilgili dosyayı sil)."""
import asyncio, base64, json, os, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path

from websockets.sync.client import connect

HERE = Path(__file__).parent
FPS, PORT, PAUSE = 24, 9335, 0.6

# her satır: cümle, o sırada çizilen gruplar, kamera [x, y, genişlik, yükseklik]
SCENES = {
    "figma": [
        ("Sokakta yürürken biri size büyük bir hediye uzatsa, ne yapardınız?", ["parchment", "city-buildings", "streetlamp"], [0, 0, 1600, 900]),
        ("Gülümseyen satıcı kutuyu uzatıyor ve bedava olduğunu söylüyor.", ["ground-shadows", "salesman", "gift"], [110, 90, 800, 450]),
        ("Genç kadın düşünüyor: Bunu alırsam neyden vazgeçmiş olurum?", ["woman"], [520, 90, 720, 405]),
        ("Arkadaşı ise şüpheli. Çünkü her seçimin görünmeyen bir bedeli vardır. Buna fırsat maliyeti denir.", ["young-man"], [0, 0, 1600, 900]),
    ],
    "openpeeps": [
        ("Üç arkadaş, sıkıcı bir filmin ortasında tartışıyor.", ["title", "ground"], [0, 0, 1600, 900]),
        ("Birincisi ısrarlı: İki yüz elli lira verdim, sonuna kadar izleyeceğim!", ["peep0", "bubble0"], [0, 150, 1000, 562]),
        ("İkincisi kararsız. Üçüncüsü ise kollarını kavuşturmuş, soruyor: Eee, sonra?", ["peep1", "peep2", "bubble1"], [560, 150, 1040, 585]),
        ("Harcanan para geri gelmez. Karar verirken yalnızca bundan sonrasına bakın.", [], [0, 0, 1600, 900]),
    ],
}

# sayfada çalışır: çizilerek belirme, hafif hareket, kamera, altyazı
ANIM = r"""
<style>#cap{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);max-width:90vw;background:#17110dd9;color:#fff;
font:34px "Segoe UI",sans-serif;padding:10px 26px;border-radius:14px;text-align:center;width:max-content}
body{margin:0}body>svg{width:100vw;height:100vh;display:block}</style><div id="cap"></div>
<script>
const svg = document.querySelector('body > svg'), cap = document.getElementById('cap');
const $ = id => document.getElementById(id);
function setup() {   // Open Peeps sahnesindeki adsız parçalara ad ver
  document.querySelectorAll('.peep').forEach((e, i) => e.id = 'peep' + i);
  [...svg.children].filter(e => e.tagName === 'g' && e.querySelector(':scope > rect')).forEach((e, i) => e.id = 'bubble' + i);
  const t = svg.querySelector(':scope > text'); if (t) t.id = 'title';
  const g = svg.querySelector(':scope > path'); if (g) g.id = 'ground';
}
function wrap(e) { const g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); e.replaceWith(g); g.append(e); return g; }
let groups, movers = [];
function init() {
  setup();
  groups = SCENE.flatMap(([, ids], i) => ids.map((id, k) => {
    const e = $(id); if (!e) throw new Error('grup yok: ' + id);
    const parts = e.matches('path,text,rect') ? [e] : [...e.querySelectorAll('path,text,rect,circle,ellipse')];
    const span = DUR[i]*.7/ids.length;
    return {id, e, parts: parts.map(p => ({p, len: p.getTotalLength ? p.getTotalLength() : 0, stroke: p.getAttribute('stroke')})),
            at: START[i] + .15 + k*span, dur: span};
  }));
  for (const [id, fn] of [
    ['salesman', (s, b) => `translate(${6*Math.sin(s*2.2)} ${3*Math.sin(s*4.4)})`],
    ['gift', (s, b) => `translate(${6*Math.sin(s*2.2)} ${7*Math.sin(s*4.4)}) rotate(${2.5*Math.sin(s*3)} ${b.x+b.width/2} ${b.y+b.height/2})`],
    ['salesman-head', (s, b) => `rotate(${3*Math.sin(s*2.6)} ${b.x+b.width/2} ${b.y+b.height})`],
    ['woman', (s, b) => `rotate(${.9*Math.sin(s*1.5)} ${b.x+b.width/2} ${b.y+b.height})`],
    ['man-head', (s, b) => `rotate(${4*Math.sin(s*1.9)} ${b.x+b.width/2} ${b.y+b.height})`],
    ...[0,1,2].map(i => ['peep'+i, (s, b) => `translate(${b.x+b.width/2} ${b.y+b.height}) skewX(${1.2*Math.sin(s*1.8+i*2)}) scale(1 ${1+.008*Math.sin(s*3+i)}) translate(${-b.x-b.width/2} ${-b.y-b.height})`]),
  ]) { const e = $(id); if (e) { const g = wrap(e); movers.push({g, fn, b: g.getBBox(), owner: id}); } }
}
const clamp = v => Math.max(0, Math.min(1, v)), ease = v => v*v*(3-2*v);
function render(t) {
  for (const g of groups) {
    const n = g.parts.length;
    g.parts.forEach(({p, len, stroke}, i) => {
      // grubun parçaları kısa üst üste binmeyle sırayla çizilir
      const q = clamp((t - g.at - i/n*g.dur*.7) / (g.dur*.3)), s = p.style;
      s.visibility = q ? 'visible' : 'hidden';
      const drawing = q > 0 && q < 1;
      s.fillOpacity = drawing ? clamp(q*2 - 1) : '';
      s.stroke = drawing && !stroke && len ? '#1d1916' : '';
      s.strokeWidth = drawing && !stroke && len ? '3px' : '';
      s.strokeDasharray = drawing && len ? `${len} ${len}` : '';
      s.strokeDashoffset = drawing && len ? len*(1-q) : '';
      if (!len) s.opacity = q < 1 ? q : '';
    });
  }
  for (const m of movers) {
    const g = groups.find(g => m.owner === g.id || $(g.id).contains(m.g));
    const s = g ? t - g.at - g.dur : -1;      // çizimi bitince hareket başlar
    m.g.setAttribute('transform', s > 0 ? m.fn(s*Math.min(1, s*2) , m.b) : '');
  }
  let i = START.findLastIndex(s => t >= s); i = Math.max(0, i);
  const a = SCENE[Math.max(0, i-1)][2], b = SCENE[i][2], k = ease(clamp((t - START[i]) / 1.4));
  svg.setAttribute('viewBox', a.map((v, j) => v + (b[j]-v)*k).join(' '));
  cap.textContent = SCENE[i][0];
}
</script>
"""


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


async def speak(lines, folder):
    import edge_tts
    for i, text in enumerate(lines):
        f = folder / f"{i}.mp3"
        if not f.exists():
            await edge_tts.Communicate(text, "tr-TR-AhmetNeural", rate="-5%").save(str(f))


def build(name):
    scene = SCENES[name]
    folder = HERE / "ses" / name
    folder.mkdir(parents=True, exist_ok=True)
    asyncio.run(speak([s[0] for s in scene], folder))
    files = [folder / f"{i}.mp3" for i in range(len(scene))]
    dur = [float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f))) + PAUSE for f in files]
    dur[-1] += 2
    graph = "".join(f"[{i}:a]apad,atrim=0:{d:.3f}[a{i}];" for i, d in enumerate(dur))
    graph += "".join(f"[a{i}]" for i in range(len(dur))) + f"concat=n={len(dur)}:v=0:a=1[out]"
    audio = folder / "tum.wav"
    run("ffmpeg", "-y", *[x for f in files for x in ("-i", str(f))], "-filter_complex", graph, "-map", "[out]", str(audio))

    data = (f"<script>const SCENE={json.dumps(scene, ensure_ascii=False)}, DUR={json.dumps(dur)}, "
            f"START=DUR.map((_,i)=>DUR.slice(0,i).reduce((a,b)=>a+b,0));</script>")
    if name == "figma":
        body = (HERE / "figma.svg").read_text(encoding="utf-8")
        page = f'<!doctype html><meta charset="utf-8">{body}{ANIM}{data}'
    else:
        base = (HERE.parent / "openpeeps" / "sahne.html").read_text(encoding="utf-8")
        page = base + ANIM + data
    html = HERE / f"{name}.html"
    html.write_text(page, encoding="utf-8")
    record(html, HERE / f"{name}.mp4", audio, sum(dur))


def record(html, out, audio, total):
    edge = Path(os.environ["ProgramFiles(x86)"]) / "Microsoft/Edge/Application/msedge.exe"
    browser = subprocess.Popen([str(edge), "--headless=new", f"--remote-debugging-port={PORT}",
                                f"--user-data-dir={tempfile.mkdtemp()}", "about:blank"])
    try:
        for _ in range(50):
            try:
                url = next(t["webSocketDebuggerUrl"] for t in
                           json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")) if t["type"] == "page")
                break
            except (OSError, StopIteration):
                time.sleep(0.2)
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
                return cdp("Runtime.evaluate", expression=code, awaitPromise=True, returnByValue=True)["result"].get("value")

            cdp("Emulation.setDeviceMetricsOverride", width=1600, height=900, deviceScaleFactor=1.2, mobile=False)
            cdp("Page.navigate", url=html.as_uri())
            for _ in range(100):
                if js("document.readyState === 'complete' && typeof init === 'function'"):
                    break
                time.sleep(0.1)
            js("document.fonts.ready.then(() => { init(); return 1 })")
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                                   "-i", str(audio), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-c:a", "aac",
                                   "-shortest", str(out)], stdin=subprocess.PIPE)
            for k in range(int(total * FPS)):
                js(f"render({k / FPS})")
                ff.stdin.write(base64.b64decode(cdp("Page.captureScreenshot", format="jpeg", quality=92)["data"]))
            ff.stdin.close()
            assert ff.wait() == 0, "ffmpeg hata verdi"
            print(f"OK {out.name} {total:.1f}s")
            cdp("Browser.close")
    finally:
        try:
            browser.wait(timeout=10)
        except subprocess.TimeoutExpired:
            browser.kill()


if __name__ == "__main__":
    for name in sys.argv[1:] or SCENES:
        build(name)
