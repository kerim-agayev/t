"""Her cümlenin sesini yazıya döker (faster-whisper), senaryoyla karşılaştırır; süre ve konuşma hızını ölçer.
(kanal_2/ içinde) PYTHONUTF8=1 uv run --no-project -p 3.13 --with faster-whisper python -X utf8 -I araclar/ses_kontrol.py <klasör> [model] [Sahne_n ...]
model: base.en (varsayılan) | small.en (şüpheli cümleleri ikinci kez dinlemek için)."""
import ast
import difflib
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

H = Path(__file__).resolve().parent.parent / sys.argv[1]
model_adi = sys.argv[2] if len(sys.argv) > 2 else "base.en"
secili = set(sys.argv[3:])
agac = ast.parse((H / "sahneler.py").read_text(encoding="utf-8"))
TEXT = next(ast.literal_eval(n.value) for n in agac.body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "TEXT")
model = WhisperModel(model_adi, device="cpu", compute_type="int8", cpu_threads=4)
SAYI = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "eight": "8", "nine": "9", "ten": "10"}


def sade(s):
    s = s.lower().replace("%", " percent").replace(",", "").replace("-", " ")
    return [SAYI.get(w, w) for w in re.findall(r"[a-z0-9]+", s)]


toplam = 0.0
for sahne, satirlar in TEXT.items():
    for i, metin in enumerate(satirlar):
        if secili and f"{sahne}_{i}" not in secili:
            continue
        ham = subprocess.run(["ffmpeg", "-v", "error", "-i", str(H / "ses" / f"{sahne}_{i}.mp3"), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                             capture_output=True, check=True).stdout          # av sürümünden bağımsız çözme
        parcalar, bilgi = model.transcribe(np.frombuffer(ham, np.float32).copy(), language="en", beam_size=3)
        parcalar = list(parcalar)
        duyulan = " ".join(p.text.strip() for p in parcalar)
        sure = bilgi.duration
        toplam += sure
        a, b = sade(metin), sade(duyulan)
        es = difflib.SequenceMatcher(None, a, b)
        fark = [(op, " ".join(a[i1:i2]), " ".join(b[j1:j2])) for op, i1, i2, j1, j2 in es.get_opcodes() if op != "equal"]
        hiz = len(metin) / sure
        bayrak = "KONTROL" if es.ratio() < .995 or hiz < 8.5 or hiz > 20 else "ok"
        print(f"{bayrak:7} {sahne}_{i} {sure:5.1f}s {hiz:4.1f}k/s benzerlik {es.ratio():.2f}", flush=True)
        if fark:
            print("        fark:", fark, flush=True)
print(f"toplam ses {toplam:.1f} s")
