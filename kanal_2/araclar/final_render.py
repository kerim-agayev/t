"""Final render + belge.py; çalıştığı sürece Windows'un uykuya geçmesini engeller (kalıcı ayar değiştirmez).
(kanal_2/ içinde, arka planda) PYTHONUTF8=1 .venv/Scripts/python -u araclar/final_render.py <klasör> > <günlük dosyası> 2>&1"""
import ctypes
import subprocess
import sys
import time
from pathlib import Path

K = Path(__file__).resolve().parent.parent
klasor = sys.argv[1]
ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
bas = time.time()
try:
    r = subprocess.run([sys.executable, "-u", str(K / "render.py"), klasor, "final"], cwd=K)
    if r.returncode == 0:
        r = subprocess.run([sys.executable, str(K / "belge.py"), klasor], cwd=K)
finally:
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
print(f"cikis {r.returncode}, toplam {(time.time() - bas) / 60:.1f} dk")
sys.exit(r.returncode)
