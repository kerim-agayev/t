# Yöntem raporu: kodla çizilen anlatımlı videolar

Rapor tarihi: 2026-11-27. Kaynaklar: bu klasördeki dosyalar, `ffprobe`, sürüm komutları. Yalnızca oturum geçmişinden bilinen şeyler **(oturum)** ile işaretlidir.

## 1. Yöntem

### 1.1 Teknoloji

| Bileşen | Sürüm | Görevi |
|---|---|---|
| HTML + satır içi SVG + CSS + düz JavaScript | harici JS kütüphanesi yok | çizim, animasyon, oynatıcı |
| Python | 3.14.4 | ses, zamanlama, video üretimi |
| websockets (Python) | 16.0 | headless Edge'i DevTools protokolüyle (CDP) sürmek |
| Microsoft Edge (headless, `--disable-gpu`) | 158.0.4370.33 | sayfayı işlemek, kare yakalamak |
| ffmpeg / ffprobe | 9.1 (gyan.dev full build) | ses birleştirme, süre ölçme, H.264 kodlama |
| Caveat fontu (Google Fonts, ağdan) | 500, 700 | el yazısı görünümü; yedek: Segoe Print |
| ElevenLabs API, `eleven_multilingual_v2` | REST (`urllib`) | final videoların seslendirmesi |
| edge-tts | 7.3.1 | anahtar yoksa ücretsiz yedek ses |

Node.js 26.13.0 kurulu, ama bu üretim hattında kullanılmıyor.

### 1.2 Skill, MCP, plugin, yapay zekâ modelleri

- Kodu ve anlatım metinlerini Claude Code (Claude Sonnet 5.5) yazdı. Claude kullanım maliyeti: bilmiyorum.
- Çizim ve video üretiminde skill veya MCP aracı çağrılmadı **(oturum)**. Oturumda bazı pluginler (ör. ponytail, superpowers) yönlendirme metni yüklüyordu; çizim/video aracı sağlamadılar.
- Yapay zekâ görsel veya video modeli kullanılmadı.
- Tek üretken ses modeli ElevenLabs. Seslendirilen metin: pandas 983, motor 849, Pavlov 703 karakter (toplam 2535) **(oturum)**. Harcanan kredi, plan türü ve ücret: bilmiyorum (anahtarın hesap bilgisi okuma izni yoktu).
- Varsayılan ses kimliği kodda `JBFqnCBsd6RMkjVDRZzb` ("George"); `ELEVENLABS_VOICE` ile değişir. Oturumda bu değişken ayarlanmadı **(oturum)**.

### 1.3 Resim nasıl çizildi

- Tamamı kodla üretilen vektör: `path`, `text`, `circle`. Hazır görsel, üretilen görsel ve ikon seti yok. Tek hazır varlık font.
- Küçük yardımcı fonksiyonlar (`box`, `rect`, `oval`, `arrow`, `marker`, `table`, `person`, `dog`, `bell`, `engine`) elle verilmiş koordinatlarla 1600×900 tuvale çizer.
- Titrek çizgi: SVG filtresi `feTurbulence` (fractalNoise, baseFrequency 0.022–0.025, 2 oktav, sabit seed) + `feDisplacementMap` (scale 5–6). Motor ve Pavlov videolarında filtre tüm şekilleri içeren tek gruba uygulanır; metinler filtre dışında kalır. pandas videosunda filtre her `path` öğesine ayrı uygulanır.
- Fosforlu kalem: yarı saydam kalın eğri. Gölge: kaydırılmış yarı saydam çizgi (pandas).

### 1.4 El çiziyor hissi veren animasyon

- Her SVG öğesi oluşturulduğu bölüm numarasıyla bir listeye yazılır; liste sırası çizim sırasıdır.
- Her öğeye ağırlık verilir (yol uzunluğu veya karakter sayısı); bölümün süresi ağırlıklara göre paylaştırılır.
- Düz çizgiler: `getTotalLength()` + `stroke-dasharray` / `stroke-dashoffset`; dolgu çizimin ikinci yarısında belirir.
- Metin ve kesikli çizgiler: soldan sağa `clip-path: inset(...)` açılması (harf harf yazma değil).
- Kalem simgesi `getPointAtLength()` ile çizilen noktayı, metinde sınır kutusunu takip eder.
- `render(t)` yalnızca `t`'ye bağlıdır; bu yüzden ileri geri sarma ve kare üretimi aynı kodu kullanır.
- Hareket: motorda krank-biyel kinematiği (`d` özniteliği her karede yeniden hesaplanır); Pavlov'da zil, kuyruk, kulak, salya için `transform` ve saydamlık (`move()` listesi).

### 1.5 Video çıktısı

1. `ses/N.mp3` eksikse üretilir.
2. `ffprobe` ile süre ölçülür, her bölüme 0.7 sn eklenir; ffmpeg `apad` + `concat` → `narration.mp3`; süreler `timing.js`'e yazılır.
3. Pavlov'da ayrıca ffmpeg `aevalsrc` ile sentezlenen zil sesi 3 noktaya `adelay` + `amix` ile eklenir.
4. Headless Edge `index.html?render` açar (1600×900, `deviceScaleFactor` 1.2 → 1920×1080).
5. Her kare için `render(t)` çağrılır, `Page.captureScreenshot` (JPEG, kalite 92) alınır. Sayfa durumu değişmediyse önceki kare yeniden kullanılır.
6. Kareler `image2pipe` ile ffmpeg'e gider: libx264, CRF 20, yuv420p, ses AAC.
7. Betik video süresinin ses süresinden 1 sn'den az saptığını `assert` ile denetler.

Ekran kaydı, Remotion veya Manim kullanılmadı.

### 1.6 Kamera

Perspektif, kamera hareketi, yakınlaştırma yok. Sabit 2B tuval.

### 1.7 Ses, altyazı, senkron

- Türkçe seslendirme var (mono, 44.1 kHz). Ayrı altyazı yok; ekrandaki yazılar çizimin parçası.
- Senkron **bölüm düzeyinde**: metin bölümlere ayrılır, her bölümün çizimi o bölümün süresinin ilk kısmına sığdırılır (pandas %80; motor anlatım panellerinde %55, Pavlov panellerinde %60, diğerlerinde %80). Kalan sürede hareket oynar. Kelime düzeyinde zaman damgası kullanılmıyor.
- Kullanıcı kendi kaydını `ses/N.mp3` olarak koyarsa zamanlama buna göre yeniden hesaplanır (bu yol denenmedi).

### 1.8 Çıktılar

Tümü 1920×1080, 20 FPS, H.264 + AAC.

| Dosya | Süre | Boyut (bayt) | Ses üretiminden MP4'ün bitişine (dosya zaman damgaları) |
|---|---|---|---|
| `pandas_video/pandas_groupby.mp4` | 71.6 sn | 2 302 090 | yaklaşık 108 sn |
| `motor/motor.mp4` | 62.5 sn | 3 865 091 | bilmiyorum (`narration.mp3` sonradan yeniden yazıldı) |
| `motor/motor_dark.mp4` | 62.5 sn | 3 643 529 | yaklaşık 3 dk (ses hazırdı) |
| `pavlov/pavlov.mp4` | 54.75 sn | 3 533 530 | yaklaşık 93 sn |

Kod yazma dahil toplam süre ölçülmedi. Dosya zaman damgalarına göre motorda `motor.png` 18:06, son açık video 18:18; Pavlov'da `index.html` 18:51, video 18:52. Bunlar arada kullanıcı beklemesi de içerebilir. Donanım: Intel i5-12400F, 32 GB RAM.

### 1.9 Dosyalar

| Yol | Görev |
|---|---|
| `pandas_groupby.html` | ilk durağan resim (kök dizin) |
| `pandas_video/index.html` | pandas: çizim, zaman çizelgesi, oynatıcı |
| `motor/motor.html`, `motor/motor.png` | motor durağan resmi |
| `motor/index.html` | motor animasyonu; `?dark` koyu tema, `?render` video modu |
| `pavlov/pavlov.html`, `pavlov/pavlov.png` | Pavlov durağan resmi |
| `pavlov/index.html` | Pavlov animasyonu |
| `*/make_video.py` | ses + zamanlama + kare yakalama + kodlama; anlatım metni `TEXTS` içinde |
| `*/ses/N.mp3` | bölüm sesleri (44.1 kHz, ~128 kbps) |
| `pandas_video/ses_edge/` | eski edge-tts sesleri; final videoda kullanılmıyor |
| `*/narration.mp3`, `*/timing.js` | üretilen birleşik ses ve süreler |

`motor/make_video.py` ve `pavlov/make_video.py`, pandas betiğinden geçici dönüştürme betikleriyle türetildi; o geçici betikler projede yok **(oturum)**. Yeniden üretim için gerekmiyorlar. Klasörde git deposu yok.

### 1.10 Yeniden üretim

Gereksinim: Windows, Edge (varsayılan kurulum yolu), PATH'te `ffmpeg`/`ffprobe`, internet (font; ses üretilecekse servis).

```bash
python -m pip install websockets==16.0 edge-tts==7.3.1

# var olan ses/*.mp3 kullanılır
cd pandas_video && python make_video.py
cd ../motor     && python make_video.py
python make_video.py --dark          # motor_dark.mp4
cd ../pavlov    && python make_video.py
```

Sesleri de sıfırdan üretmek için ilgili `ses/*.mp3` dosyalarını silin (veya yedekleyin) ve `ELEVENLABS_API_KEY` ortam değişkenini ayarlayın; değişken yoksa edge-tts kullanılır. Yeni sesin süresi farklı olacağından video birebir aynı çıkmaz. Komutlar mevcut çıktıların üzerine yazar.

Durağan PNG **(oturum)**:

```bash
msedge --headless=new --disable-gpu --user-data-dir=<geçici> --window-size=1600,900 \
  --force-device-scale-factor=1.2 --virtual-time-budget=5000 \
  --screenshot=<tam yol>/motor.png file:///<tam yol>/motor.html
```

Bu rapor hazırlanırken komutlar yeniden çalıştırılmadı.

### 1.11 Sorunlar ve zayıf yanlar

Karşılaşılan sorunlar **(oturum)**:
- Eni veya boyu sıfır olan düz çizgiler, sınır kutusuna bağlı SVG filtresinde kayboldu. Video sürümlerinde hafif eğri veya tüm tuvali kapsayan grup filtresiyle çözüldü. Kökteki `pandas_groupby.html` hâlâ eski filtreyi kullanıyor.
- Üst üste binen ve taşan yazılar ancak ekran görüntüsüne bakınca bulundu, koordinatlar elle düzeltildi.
- Motor finalinde iki silindir aynı zamandaydı; faz farkı 180° yapıldı.
- Koyu temada renk tersine çevirme sarıları kahverengiye döndürdü; renk haritasıyla çözüldü.

Zayıf yanlar:
- Koordinatlar elle veriliyor; otomatik yerleşim veya çakışma denetimi yok.
- Karakterler ve nesneler geometrik; serbest elle çizim zenginliği yok.
- Çizgi titremesi sabit; metin harf harf yazılmıyor.
- 20 FPS; tek kare ekran görüntüsü darboğaz.
- Windows + Edge'e bağlı, CDP portu sabit (9333), font ağdan geliyor.
- Oynatıcı ve betik kodu üç klasörde kopya; ortak modül yok.
- Metin değişince eski `ses/N.mp3` elle silinmeli.
- Sesler dinlenerek kontrol edilmedi; etkileşimli oynatıcı gerçek tarayıcıda denenmedi; görsel kontrol yalnızca örnek karelerle yapıldı.

## 2. Karşılaştırma

A = bu yöntem (SVG + headless Edge). B = diğer yöntem (Python/Pillow çizim motoru). **B'nin çıktısı ve kodu görülmedi**; B sütunu yalnızca verilen tanıma dayanan beklentidir.

| Ölçüt | A: SVG + Edge | B: Pillow motoru |
|---|---|---|
| Görsel kalite | Net vektör çizgi ve metin; diyagramlarda iyi, serbest illüstrasyonda sınırlı | Bilmiyorum (görülmedi). Piksel düzeyi kontrol doku ve boya efektlerine izin verir; sonuç motorun kalitesine bağlı |
| El çizimi hissi | Çizgi açılması + titreme filtresi + kalem simgesi; metin silme efektiyle açılıyor | Bilmiyorum. Adımların kaydedilip oynatılması darbe sırasını doğrudan verebilir |
| Düzeltme kolaylığı | HTML'i tarayıcıda yenileyip hemen görmek mümkün, sarma çubuğu var; koordinatlar elle | Bilmiyorum. Önizleme için ayrıca araç yoksa görüntü/video üretmek gerekir |
| Üretim süresi (render) | 55–72 sn'lik video yaklaşık 1.5–2 dk; motorda yaklaşık 3 dk | Bilmiyorum (ölçüm verilmedi). Tarayıcı olmaması hız avantajı sağlayabilir; ölçülmeli |
| Maliyet | Araçlar ücretsiz; ElevenLabs kredisi (edge-tts yedeği ücret istemiyor); Claude kullanımı | Anlatılan araçlar ücretsiz; videolar sessiz olduğu için ses maliyeti yok; Claude kullanımı bilinmiyor |
| Ses | Var, bölüm düzeyinde senkron, çalışır durumda | Kod yazılmış, test edilmemiş |
| Yeni konuya uyarlama | Yeni sahne kodu, metin ve koordinat gerekir; yardımcılar kopyalanıyor | Yeni sahne kodu gerekir; ortak motorun yeniden kullanım derecesi bilinmiyor |
| Kamera / perspektif | Yok | Var (yağlı boya sahnesi, 3B düzlemler) |
| Etkileşim | Oynatıcı, bölüm düğmeleri | Tanımda yok |
| Taşınabilirlik | Windows + Edge varsayımı | Python + ffmpeg; muhtemelen daha taşınabilir, doğrulanmadı |

### Hangi tarz için hangisi

- **Diyagram, süreç, tablo, kod, mekanik şema:** A uygun; metin, ok, vektör şekil ve parametrik hareket doğrudan destekleniyor.
- **Yağlı boya, dokulu resim, derinlik ve kamera hareketi:** B uygun; A'da bunların hiçbiri yok.
- **Etkileşimli ders sayfası:** A.
- **Elle çizim sırasının önemli olduğu illüstrasyon:** B aday; çıktıları yan yana izlemeden karar verilmemeli.

### Adil karşılaştırma için öneri

İki makinede aynı konu ve aynı metinle 30 sn'lik bir sahne üretin; 1920×1080, 30 FPS (A'da `FPS = 30` yapılabilir, denenmedi). Kod yazma süresini, render süresini, düzeltme turu sayısını kaydedin ve videoları yan yana izleyin.

A'dan B'ye aktarılabilecek fikirler: bölüm sesinin süresinden çizim zamanlaması üretmek, değişmeyen kareleri yeniden kullanmak, süre denetimi için `assert`. B'den A'ya bakılmaya değer fikirler: gerçek darbe sıralı çizim, kamera hareketi (A'da `viewBox` animasyonuyla denenebilir), 30 FPS.
