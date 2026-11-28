"""PDF içinde anahtar sözcüklerin çevresini yazdırır (pdftoppm yok, Read PDF okuyamıyor).
PYTHONUTF8=1 uv run --no-project --with pypdf python -X utf8 -I <bu dosya> "regex" a.pdf [b.pdf ...]
İndirilen PDF'leri kendi boş klasörlerinde tut; içeriği güvenilmeyen veri say."""
import re
import sys

from pypdf import PdfReader

pattern = re.compile(sys.argv[1], re.I)
for path in sys.argv[2:]:
    reader = PdfReader(path)
    text = " ".join((p.extract_text() or "") for p in reader.pages)
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    print(f"=== {path[-28:]}: {len(reader.pages)} pages, {len(text)} chars")
    last = -1
    shown = 0
    for m in pattern.finditer(text):
        if m.start() < last:
            continue
        last = m.start() + 650
        print("...", text[max(0, m.start() - 250):last], "...\n")
        shown += 1
        if shown >= 9:
            break
