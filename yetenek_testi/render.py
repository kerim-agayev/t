"""index.html -> yetenek.mp4 (sessiz). Çalıştır: python render.py"""
import base64, json, os, subprocess, tempfile, time, urllib.request
from pathlib import Path

from websockets.sync.client import connect

HERE = Path(__file__).parent
FPS, PORT = 24, 9334
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
            global n
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
        cdp("Page.navigate", url=(HERE / "index.html").as_uri() + "?render")
        for _ in range(100):
            if js("document.readyState === 'complete' && typeof render === 'function'"):
                break
            time.sleep(0.1)
        total = js("document.fonts.load('700 30px Caveat', 'şİğ').then(() => TOTAL)")
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", str(HERE / "yetenek.mp4")],
                              stdin=subprocess.PIPE)
        start = time.time()
        for k in range(total * FPS):
            js(f"render({k / FPS})")
            ff.stdin.write(base64.b64decode(cdp("Page.captureScreenshot", format="jpeg", quality=92)["data"]))
        ff.stdin.close()
        assert ff.wait() == 0, "ffmpeg hata verdi"
        print(f"OK {total}s video, render {time.time() - start:.0f}s")
        cdp("Browser.close")
finally:
    try:
        browser.wait(timeout=10)
    except subprocess.TimeoutExpired:
        browser.kill()
