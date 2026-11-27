"""python render.py <video-klasörü> [ses|taslak|final]   (kanal/ içinde, .venv python'u ile)
ses: eksik sesler. taslak: 640x360, her sahneden bir kare (onizleme.png) + taslak.mp4. final: 1440p video.mp4."""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
klasor = (HERE / sys.argv[1]).resolve()
kip = sys.argv[2] if len(sys.argv) > 2 else "taslak"
env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONWARNINGS": "ignore", "PYTHONPATH": str(HERE)}
sys.path[:0] = [str(HERE), str(klasor)]
import sahneler                      # noqa: E402  TEXT (sahne -> cümleler, sırayla) ve sahne sınıfları
from tahta import sesler             # noqa: E402

sesler(sahneler.TEXT, klasor)
if kip == "ses":
    sys.exit()
res, fps, dizin, cikti = ("640,360", "10", "360p10", "taslak.mp4") if kip == "taslak" else ("2560,1440", "30", "1440p30", "video.mp4")
dosyalar = []
for ad in sahneler.TEXT:
    r = subprocess.run([sys.executable, "-m", "manim", "--resolution", res, "--frame_rate", fps, "sahneler.py", ad], cwd=klasor,
                       env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(f"{ad} HATA:\n{(r.stderr or r.stdout)[-2500:]}")
    dosyalar.append(klasor / "media/videos/sahneler" / dizin / f"{ad}.mp4")
    print("sahne", ad, flush=True)
liste = klasor / "media/liste.txt"
liste.write_text("".join(f"file '{f.as_posix()}'\n" for f in dosyalar), encoding="utf-8")
ff = ["ffmpeg", "-y", "-loglevel", "error"]
subprocess.run(ff + ["-f", "concat", "-safe", "0", "-i", str(liste), "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                     "-af", "aresample=async=1:first_pts=0,loudnorm=I=-16:TP=-1.5", "-ar", "48000", str(klasor / cikti)], check=True)
if kip == "taslak":                                    # her sahnenin sonuna yakın bir kare, tek sayfada
    kareler = klasor / "media/kare"
    kareler.mkdir(exist_ok=True)
    for i, f in enumerate(dosyalar):
        subprocess.run(ff + ["-sseof", "-0.9", "-i", str(f), "-frames:v", "1", str(kareler / f"{i:02d}.png")], check=True)
    sutun = 2
    satir = (len(dosyalar) + 1) // sutun
    subprocess.run(ff + ["-i", str(kareler / "%02d.png"), "-vf", f"tile={sutun}x{satir}:padding=8:color=red", "-frames:v", "1",
                         str(klasor / "onizleme.png")], check=True)
sure = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(klasor / cikti)], text=True)
print(f"OK {cikti} {float(sure):.1f} sn")
