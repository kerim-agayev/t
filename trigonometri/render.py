"""Sahneleri render edip birleştirir. python render.py [taslak] [Sahne ...]"""
import subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).parent
ORDER = ["Giris", "Ucgen", "BirimCember", "Radyan", "Dalga", "Ses", "Tarih", "Tuzak"]
draft = "taslak" in sys.argv
only = [a for a in sys.argv[1:] if a in ORDER]
res, fps, folder, out = ("640,360", "10", "360p10", "taslak.mp4") if draft else ("1920,1080", "30", "1080p30", "trigonometri.mp4")
start = time.time()
manim = HERE / ".venv/Scripts/manim.exe"
for name in only or ORDER:
    r = subprocess.run([str(manim), "--resolution", res, "--frame_rate", fps, "video.py", name], cwd=HERE,
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8", "PYTHONWARNINGS": "ignore"})
    if r.returncode:
        sys.exit(f"{name} HATA:\n{(r.stderr or r.stdout)[-2500:]}")
    print(name, f"{time.time() - start:.0f}s", flush=True)
files = [HERE / "media/videos/video" / folder / f"{n}.mp4" for n in ORDER]
if all(f.exists() for f in files):
    lst = HERE / "media/liste.txt"
    lst.write_text("".join(f"file '{f.as_posix()}'\n" for f in files), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "160k", "-af", "loudnorm=I=-16", "-ar", "48000", str(HERE / out)], check=True)
    d = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(HERE / out)], text=True)
    print(f"OK {out} {float(d):.1f}s, toplam {time.time() - start:.0f}s")
