# Kodla çizilen anlatımlı videolar (YouTube kanalı hazırlığı)

Bu depo 2026-11-26/27 çalışmasının tamamı. Başka bilgisayardaki Claude Code buradan aynen devam edebilsin diye yazıldı.

## Amaç ve kullanıcı tercihleri
- Hedef: YouTube kanalı. **Tarz ve niş seçildi (2026-11-27), aşağıdaki "Kanal" bölümü.** Önceki klasörler deneme çalışmaları.
- Kullanıcıyla Türkçe ve **kısa** cevap. **En az token** ile en iyi sonuç. Video dili İngilizce.
- Büyük işten önce tek kare / önizleme sayfası ile onay al; render'ı arka planda çalıştır, yoklama; gereksiz alt ajan ve görsel kontrolü yok.
- API anahtarlarını dosyaya veya commit'e yazma (**bu depo herkese açık**).

## Evde sıfırdan başlama (git clone sonrası)
Gerekenler (PATH'te): [uv](https://docs.astral.sh/uv/), ffmpeg, internet; Windows (Segoe Print yazı tipi). Blender yalnız 3D sahne gerekirse.
```bash
git clone https://github.com/kerim-agayev/t.git && cd t/kanal
uv venv -p 3.13 && uv pip install -r requirements.txt                  # bir kez
.venv/Scripts/python render.py ornek taslak                            # kurulum denemesi -> ornek/onizleme.png
```
Sonra Claude Code'u `t/` klasöründe aç ve yaz: **"001 videosunun sesini ElevenLabs ile değiştir"**. Claude `kanal/001-black-holes/SESLENDIRME.md` dosyasını izler. Yeni video için sıra: bu dosya → `hikaye-senaryo` skill'i → `STIL_REHBERI.md`.

## Kanal
- **Marka:** ad "Chalk Orbit" (öneri; müsaitliği kontrol edilmedi). `kanal/marka/profil_800.png` ve `banner_2560x1440.png` yüklemeye hazır (kaynak görseller ChatGPT üretimi, aynı klasörde).
- **Niş:** İngilizce "uzay ve ölçek, tahtada": evrenle ilgili merak sorularını çizerek anlatmak. Veri ve sınırları: `NIS_ARASTIRMASI.md`.
- **Tarz:** varsayılan beyaz + siyah tahta animasyonu. Sahne için başka tarz açıkça daha iyiyse kullan: seçim kuralı ve tarz anlatımı **`STIL_REHBERI.md`**.
- **Üretim:** `kanal/` (ortak `tahta.py`, `render.py`; her video `kanal/NNN-ad/` içinde `BRIF.md`, `ARASTIRMA.md`, `SENARYO.md`, `sahneler.py`). Video sesi şimdilik geçici (edge-tts); kullanıcı ElevenLabs ile değiştirecek (`kanal/eleven.py`).
- **Video 1 durumu (2026-11-27):** üretildi (kapak C). **Bekleyen: ses değişimi** → `kanal/001-black-holes/SESLENDIRME.md` adımları, sonra izle ve yayınla (`PAKET.md`).
- **Yayın:** haftada 1 uzun video (5-10 dk) + her birinden 2-3 dikey Shorts (30-45 sn, tek soru tek cevap; dikey ayrıca render edilir, kırpılmaz; dikey şablon henüz yok).
- **Kurallar:** her sayı ve iddia kaynaklı, yazmadan önce doğrulanır; kapakta videoda olmayan vaat yok; art arda aynı başlık kalıbı yok.
- İlk 8 videodan sonra YouTube Studio verisine göre sıra ve türler güncellenir.

### YouTube'a API ile yükleme (kurulmadı; kullanıcı isteyince)
2026-11-27'de soruldu. Aşağıdakiler genel bilgiye dayanıyor: **kurmadan önce güncel resmi dokümandan doğrula.**
- MCP gerekmez: YouTube Data API v3 ile küçük bir betik (topluluk MCP'lerine kanal yazma yetkisi verme).
- API ile: video, başlık, açıklama, etiket, bölümler, kapak (telefonla doğrulanmış kanal), altyazı, oynatma listesi, yayın zamanlama, yorum yazma.
- Elle (Studio): bitiş ekranı, kartlar, kapak A/B testi, para kazanma, yorum sabitleme.
- Gerekli: Google Cloud'da OAuth istemcisi (API anahtarı yetmez) ve tarayıcıda kullanıcının bir kez onayı. İstemci sırrı ve yetki dosyası repoya girmez (önce `.gitignore`).
- Sınır: denetimden geçmemiş yeni API projelerinden yüklenen videolar gizli kalıyor. Denetim yoksa Studio'dan elle yükle, metinleri videonun `PAKET.md` dosyasından al.
- Yükleme ve yayınlama her seferinde kullanıcı onayıyla.

### Türler ve hikâye omurgaları
| Kod | Tür | Süre | Omurga |
|---|---|---|---|
| Tur | Küçükten büyüğe tur | 8-10 dk | tek ana soru; her durak "ama daha tuhafı var" ile bağlanır |
| Ö | Gerçek ölçek | 6-8 dk | tek tanıdık referans; her adımda sezgi kırılır; zirvede hepsi tek karede |
| N | Ne olurdu? | 6-8 dk | "bu yüzden... ama..." zinciri; saniyeden milyon yıla |
| B | Nasıl biliyoruz? | 6-8 dk | dedektif: imkânsız görünen soru → yetmeyen fikir → zekice çözüm → sınama |
| O | Olay ve nadirlikler | 8-10 dk | olayın ortasından sahne → ne gördüler → açıklama → bugün ne demek |

### İlk 50 video (yayın sırası)
Başlıklar taslak. 2, 5, 16, 25, 30, 35, 40, 41, 50 numaralardaki temel iddialar 2026-11-27'de arama özetlerinden kontrol edildi; 17'deki toplam, bilinen ortalama çaplardan hesaplandı. Diğerleri doğrulanmadı; her videodan önce birincil kaynaktan kontrol et. Talep tek tek ölçülmedi.

| # | Tür | Başlık | Kanca / görsel fikir |
|---|---|---|---|
| 1 | Tur | Every Type of Black Hole, From Tiny to Monstrous | bir kara delik ne kadar küçük veya büyük olabilir? |
| 2 | Ö | The Farthest Thing Humans Ever Sent | Voyager 1: 18 Kasım 2026'da bir ışık günü uzakta (güncel) |
| 3 | N | What If the Moon Disappeared? | gelgit, gece, eksen: adım adım kayıplar |
| 4 | B | How Do You Measure a Star You Can Never Reach? | parmak denemesiyle paralaks |
| 5 | O | In 1859, a Solar Storm Made Telegraphs Spark | olayın ortasından: kıvılcım saçan telgraf |
| 6 | Tur | Every Type of Star, and What Makes Them Different | renk ve sıcaklık merdiveni |
| 7 | Ö | How Big Is the Solar System, Really? | Güneş küçülünce gezegenler nerede kalır? |
| 8 | N | What If the Sun Vanished Right Now? | ilk 8 dakika hiçbir şey fark edilmez |
| 9 | B | How Did Someone Measure Earth With a Stick? | Eratosthenes'in gölgesi |
| 10 | O | Sky Events You May Only See Once | nadirlik merdiveni |
| 11 | O | The Last Seconds of a Dying Star | saniye saniye çöküş |
| 12 | B | Why Is the Night Sky Dark? | "sonsuz yıldız varsa neden karanlık?" |
| 13 | N | What If You Fell Into a Black Hole? | iki gözlemci, iki farklı hikâye |
| 14 | B | What Is a Star Made Of? We Never Touched One | ışığın barkodu |
| 15 | O | The Explosion That Flattened a Forest | Tunguska 1908 |
| 16 | N | Will We Really Crash Into Andromeda? | yazı tura: 10 milyar yılda yaklaşık yarı yarıya (2025 çalışması) |
| 17 | Ö | Can All the Planets Fit Between Earth and the Moon? | ortalama çaplarla sığar (~380.000 km); ekvator çapıyla sığmaz, söyle |
| 18 | N | What If Earth Stopped Spinning? | atmosfer dönmeye devam eder |
| 19 | B | The Universe Has an Age. How Did We Find It? | filmi geriye sarmak |
| 20 | O | The Signal That Made an Astronomer Write "Wow!" | tek satırlık kâğıt çıktısı |
| 21 | B | Why Did Pluto Stop Being a Planet? | üç şart, biri eksik |
| 22 | Ö | One Light-Year: A Trip Nobody Could Finish | video 2'ye geri bağ: bir ışık günü bile yaklaşık 49 yıl sürdü |
| 23 | N | What Would Your Sky Look Like If Earth Had Rings? | farklı şehirlerden gökyüzü |
| 24 | B | How Do You Weigh a Planet? | Cavendish'in burulma düzeneği |
| 25 | O | Three Visitors From Another Star | 1I, 2I, 3I (yayın öncesi sayıyı yeniden kontrol et) |
| 26 | N | How Would We Stop an Asteroid? | bir çarpışma denemesi: DART |
| 27 | Ö | Space Is Full of Stars. So Why Is It So Empty? | yıldızlar arası ölçek |
| 28 | N | Does Jupiter Really Protect Earth? | kalkan mı, sapan mı? |
| 29 | B | How Do We Know What's Inside Earth? | deprem dalgalarıyla röntgen |
| 30 | O | Billions of Planets May Be Drifting Without a Sun | tahminler trilyonlara çıkıyor, belirsizliği söyle |
| 31 | N | What If a Star Exploded Near Earth? | uzaklığa göre sonuç halkaları |
| 32 | Ö | If the Universe Were One Year Old, When Did You Appear? | takvim yaprakları |
| 33 | N | Could Life Survive Under Two Suns? | kararlı yörünge şartı |
| 34 | B | Galaxies Are Rushing Away. How Do We Know? | kızıla kayma |
| 35 | O | Betelgeuse Will Explode. Will We See It? | NASA: büyük olasılıkla ~100.000 yıl içinde |
| 36 | Tur | The Strangest Planets We've Found | giderek tuhaflaşan sıra |
| 37 | Ö | What Would a Teaspoon of Neutron Star Weigh? | terazide dağlar |
| 38 | N | Could You Stand Up on an Earth Twice as Big? | yerçekimi ve beden |
| 39 | B | How Do You Find a Planet You Can't See? | yıldız ışığındaki minik düşüş |
| 40 | O | The Explosion So Bright It Overwhelmed Our Detectors | GRB 221009A |
| 41 | B | Where Did the Gold in Your Ring Come From? | çarpışan nötron yıldızları; magnetar payı tartışmalı |
| 42 | Ö | How Big Can a Star Get? | tahtaya sığmayan çember |
| 43 | N | What If You Dug a Tunnel Through Earth? | düşüp geri gelen yolcu |
| 44 | B | Why Do Scientists Fire Lasers at the Moon? | Ay'daki aynalar |
| 45 | O | In 2015, We Heard Two Black Holes Collide | "duyduk" benzetmesini açıkla |
| 46 | B | Why Don't We Get an Eclipse Every Month? | eğik yörünge |
| 47 | Ö | Does the Universe Have an Edge? | gözlenebilir sınır ile gerçek kenar farkı |
| 48 | N | What Would You See Near Light Speed? | ışık hızına neden ulaşılamaz |
| 49 | B | How Did We Photograph a Black Hole? | Dünya boyunda teleskop |
| 50 | O | One Day, Total Solar Eclipses Will End | NASA: yaklaşık 600 milyon yıl sonra (tahminler değişiyor) |

Kontrol kaynakları: [Carrington](https://www.history.com/articles/a-perfect-solar-superstorm-the-1859-carrington-event), [Voyager 1 ışık günü](https://svs.gsfc.nasa.gov/15120), [Andromeda 2025](https://esahubble.org/news/heic2508/), [yıldızlararası cisimler](https://arxiv.org/abs/2602.08956), [başıboş gezegenler](https://universetoday.com/162522/there-could-be-trillions-of-rogue-planets-wandering-the-milky-way), [Betelgeuse](https://science.nasa.gov/universe/what-is-betelgeuse-inside-the-strange-volatile-star), [GRB 221009A](https://www.nasa.gov/universe/nasa-missions-study-what-may-be-a-1-in-10000-year-gamma-ray-burst), [altın ve magnetarlar](https://www.simonsfoundation.org/2025/04/29/flares-from-magnetized-stars-can-forge-planets-worth-of-gold-other-heavy-elements/), [son tam tutulma](https://www.space.com/37627-total-solar-eclipse-earth-moon-alignment-future.html).

## Her yeni videonun iş sırası (önce `.claude/skills/hikaye-senaryo` skill'i)
1. **Konu** seç: niş, izleyici, konsept, görsel tarz.
2. **Akış:** yaklaşık süre, başlık + kapak, kanca, konu sırası, bitiş.
3. **Senaryo:** sahne sahne ne olacağı.
4. **Seslendirme metni:** süreyle uyumlu.
5. **Resimler:** videodan önce stil örneği ve sahne kareleri.
6. **Video:** ses → taslak → final.

- Adımlar onayla ilerler; senaryo ve resimler onaylanmadan video üretme.
- Storytelling teknikleri her adımda uygulanır. **Tek kalıba sıkıştırma:** anlatı biçimi konuya, konsepte (matematik, Sprouts tarzı, yağlı boya...) ve kanal nişine göre değişir.
- Genel teknikler hep aynı: güçlü ve dürüst kanca, merak boşluğu, "ama / bu yüzden" bağları, somut anlatım, görsel zirve, net bitiş, uydurma bilgi yok.

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
| `vroid/erteleme/` | **3 dk 3D anime karakterli psikoloji hikâyesi** (hazır CC0 VRM modeli) | three.js + three-vrm |
| `vroid/mino/` | Tamamen kodla kurulan özgün chibi karakter (video onay bekliyor) | three.js |
| `blender/` | **30 sn 3D domino zinciri (1 cm → 22 m)**, sesli ve yazılı | Blender 5.1 + Python |
| `NIS_ARASTIRMASI.md` | Dünya geneli niş, gelir ve alt niş araştırması | |
| `kanal/` | **Kanal videoları: ortak tahta şablonu, örnek, 001 brifi** | Manim |
| `STIL_REHBERI.md` | Tahta tarzı kuralları ve hangi sahnede hangi tarz | |
| `analiz/` | Alt niş istatistik betiği (`YOUTUBE_API_KEY` ortam değişkeni) | YouTube Data API |
| `YONTEM_RAPORU.md` | A hattının ayrıntılı raporu ve Pillow yöntemiyle karşılaştırma | |

## B hattı (elle çizim hikâyeleri; kanal videolarında `kanal/` kullanılır)
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

## 3D karakter hattı
Ayrıntı, kurulum, model indirme ve MCP araştırması: `vroid/NASIL_YAPILDI.md`.
```bash
cd vroid && npm ci                 # bir kez; modelleri NASIL_YAPILDI.md'deki komutla indir
node render.js erteleme taslak     # örnek kareler
node render.js erteleme            # final (önce erteleme/ses.py)
node render.js mino kare           # özgün karakter önizlemesi
```
Video için MCP kullanılmadı; VRoid MCP kurulmadı. Figma kullanılmaz.

## Blender hattı
```bash
cd blender
B="/c/Program Files/Blender Foundation/Blender 5.1/blender.exe"
"$B" -b --factory-startup -P domino.py -- kare 2.9 13 29.5   # örnek kareler (kare/)
"$B" -b --factory-startup -P domino.py -- video              # 900 kare, bu PC'de yaklaşık 9 dk (Eevee)
../trigonometri/.venv/Scripts/python son.py                  # ses + yazı + domino.mp4
```
- Eklenti veya MCP yok; her şey `domino.py` içinde kodla kuruluyor (`olaylar.json` zamanları `son.py`'ye taşır).
- Ölçek 1 cm-22 m olduğu için Blender fiziği yerine basit sarkaç + temas hesabı; kamera ve odak ölçekle büyür.
- `son.py` içinde ASS satır sonu Python metninde `\\N` (çift ters bölü) yazılmalı.

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
