# Kodla çizilen anlatımlı videolar (YouTube kanalı hazırlığı)

Bu depo 2026-11-26/27 çalışmasının tamamı. Başka bilgisayardaki Claude Code buradan aynen devam edebilsin diye yazıldı.

## Amaç ve kullanıcı tercihleri
- Hedef: YouTube kanalı. Hangi video tarzında iyi sonuç alındığını ölçüyoruz.
- İzleyici gözüyle en beğenilen tarz: **whiteboard karakterli hikâye** (Sprouts tarzı). Yön bu.
- Türkçe ve **kısa** cevap. **En az token** ile en iyi sonuç.
- Büyük işten önce tek kare / önizleme sayfası ile onay al; render'ı arka planda çalıştır, yoklama; gereksiz alt ajan ve görsel kontrolü yok.
- API anahtarlarını dosyaya veya commit'e yazma (**bu depo herkese açık**).

## Her yeni videoda ilk adım: senaryo
`.claude/skills/hikaye-senaryo` skill'ini kullan (başlık + kapak → kanca → sahne sırası → bitiş → onay). Onaysız üretim yok.

## Klasörler (kronolojik)
| Yol | İçerik | Yöntem |
|---|---|---|
| `pandas_groupby.html` | ilk durağan resim (fosforlu çizgileri görünmez: bilinen hata) | SVG |
| `pandas_video/` | 72 sn pandas groupby videosu | A hattı |
| `motor/` | 4 zamanlı motor, açık + koyu tema, hareketli piston | A hattı |
| `pavlov/` | Pavlov / klasik koşullanma, hareketli karakter, zil sesi | A hattı |
| `yetenek_testi/` | 76 sn, 6 tarz: veri yarışı, teknik akış, matematik, dev yazılı bilgi, çöp adam, whiteboard | tek `render(t)` |
| `lydia/` | **4,5 dk Lydia Fairchild vakası, 16 tahta (güncel ve en iyi hat)** | B hattı |
| `sprouts/` | Sprouts tarzı denemeler: SVG kareleri ve Open Peeps (`openpeeps/`: `npm ci`, `node render.js`). Sonuç henüz istenen çizer kalitesinde değil | SVG, react-peeps |
| `trigonometri/` | **5 dk trigonometri, beyaz + siyah tahta** | Manim |
| `yagliboya/` | 24 sn Van Gogh tarzı İstanbul gecesi, kodla fırça darbeleri | Pillow + numpy |
| `YONTEM_RAPORU.md` | A hattının ayrıntılı raporu ve Pillow yöntemiyle karşılaştırma | |

## B hattı (yeni videolar için bunu kullan)
Motor: [whiteboard-video-skill](https://github.com/Matteoikarieth96/whiteboard-video-skill) (MIT, commit `8358f53`), `lydia/skill/` içine kopyalandı; kodu gözden geçirildi, global kurulmadı. Üzerine kendi karakter setimiz eklendi.

```bash
cd lydia
cd skill/scripts && npm ci && cd ../..      # bir kez (puppeteer-core)
pip install edge-tts
export PYTHONIOENCODING=utf-8
export CHROME_PATH="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
python proje/build.py                       # metin -> script.json + audio/*.mp3
python skill/scripts/make_audio.py proje    # narration.wav + timeline.json
node skill/scripts/render.js proje sheet    # tüm tahtalar tek önizleme (onay al)
node skill/scripts/render.js proje full     # proje/out/lydia_fairchild.mp4
```

Yeni konu: `proje/` klasörünü kopyala; `build.py` içindeki `SCRIPT` (sahne -> cümleler) ve `scenes.js` (sahne -> çizimler) değişir, eski `audio/` silinir.
- `scenes.js` yardımcıları: `say(A, satır, ...)` (satır süresine yayar), `person` (saç, ruh hali, gözlük), `baby`, `dna`, `paper`, `tube`, `cell`, `title`, `yes/no/arr/q`. API: `skill/references/drawing-api.md`.
- Dosyayı IIFE içinde tut: motorun global adlarıyla (`f`, `line`, `rect`...) çakışıyor.
- Yazılar `H-150` üstünde kalsın (altyazı alanı). Kesikli çizgi desteklenmiyor.
- Metin değişince yalnız o satırın `audio/<sahne>_<n>.mp3` dosyasını sil. Kendi kaydını aynı adla koyabilirsin.
- Yapılmadı: kamera yakınlaştırma, kelime bazlı senkron (ElevenLabs `with-timestamps` ile mümkün), Rough.js.

## Manim hattı (matematik) ve yağlı boya
```bash
cd trigonometri
uv venv -p 3.13 && uv pip install manim==0.22.1 edge-tts==7.3.1 mutagen   # bir kez
export PYTHONIOENCODING=utf-8 PYTHONWARNINGS=ignore
.venv/Scripts/python video.py            # eksik sesleri üretir
.venv/Scripts/python render.py taslak    # hızlı taslak; final: render.py
cd ../yagliboya
../trigonometri/.venv/Scripts/python video.py kare 10   # resim.png
../trigonometri/.venv/Scripts/python video.py           # video.mp4 (sessiz, uzun sürer)
```
- LaTeX yok: yalnız `Text` (`MathTex` kullanma). Segoe Print alt simge çizemez.
- `Text` 48+ puntoda uzun satırı kaydırıyor; altyazı 32 punto çizilip küçültülür.
- Yağlı boya: `resim.py` sahne + renk + fırça yönü; `video.py` darbeler, hareket, kamera.

## A hattı (ilk videolar)
SVG + düz JS (`index.html`: oynatıcı, `?render` video modu) + `make_video.py`: ses → `timing.js` → headless Edge'i DevTools ile sürüp kare yakalar → ffmpeg H.264.
- El çizimi hissi: `stroke-dasharray` ile çizgi açılması, metinde `clip-path`, `feTurbulence`+`feDisplacementMap` titreme (filtreyi tek gruba uygula), kalem `getPointAtLength` takibi. `render(t)` yalnız `t`'ye bağlı.
- Çalıştırma: `pip install websockets edge-tts`, klasörde `python make_video.py` (motor koyu tema: `--dark`; yetenek testi: `python render.py`).
- Ses: `ELEVENLABS_API_KEY` varsa ElevenLabs (`eleven_multilingual_v2`, George), yoksa edge-tts (`tr-TR-AhmetNeural`).

## Öğrenilen dersler
- Sıfır yükseklikli çizgi, sınır kutusuna bağlı SVG filtresinde kaybolur.
- Yazı çakışmaları yalnız ekran görüntüsüyle yakalanır; önizleme sayfasına mutlaka bak.
- Koyu tema renk ters çevirmeyle değil renk haritasıyla yapılır.
- Güçlü: diyagram, süreç, grafik, mekanik şema. Zayıf: sanatsal illüstrasyon, mizah/çok pozlu karakter, gerçekçi insan.
- Bilgileri yayından önce kaynaktan doğrula. ElevenLabs ücretsiz planı ticari kullanım için uygun olmayabilir; edge-tts şartlarını da kontrol et.

## Ortam (üretimde kullanılan)
Windows 11, i5-12400F, RTX 3060, Python 3.14, Node 26, ffmpeg 9.1, Edge 158, Blender 5.1, Unity 6. Gerekli olanlar: Python, Node, ffmpeg (PATH'te), Edge, internet (font ve ses). Video araçları için skill/MCP/yapay zekâ görsel modeli kullanılmadı (ses hariç).

## Araştırılan ama kurulmayan araçlar
`iart-ai/explainer-video-skills`, `brandonvant/claude-skill-whiteboard-explainer`, `zhuyansen/awesome-claude-video-skills` (dizin), `remotion-dev/skills` (lisansı kontrol et), `rough-stuff/rough`.

## Bekleyen fikirler
- Sıradaki bölüm adayı: "Beynin seni kandırdığı 5 yol" (5-10 dk, her yanlılık bir bölüm, bölüm bölüm render).
- Blender ile karaktersiz anime gece manzarası veya oyuncak dünyası animasyonu (güçlü bilgisayar gerekir).
