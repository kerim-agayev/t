# Stil rehberi: hangi sahne hangi tarzla

Varsayılan **tahta animasyonu** (kanal kimliği). Başka bir tarz bir sahneyi açıkça daha iyi gösteriyorsa kullanılabilir. Evde alışılan tarz da buradaki seçeneklerden biridir: önyargısız, sahneye göre seç.

## Seçim kuralı
1. Sahne neyi göstermeli: fikir, ölçek, hareket, duygu, atmosfer?
2. Tabloda en uygun tarzı seç.
3. Emin değilsen aynı sahneden **iki tarzda birer kare** üretip kullanıcıya seçtir.
4. Bir videoda en fazla 2 tarz; sürenin çoğu tahta kalsın; ses, altyazı ve renk anlamları aynı kalsın.

| Sahnede ihtiyaç | Tarz | Depodaki örnek | Güçlü | Zayıf |
|---|---|---|---|---|
| Fikir, ölçek şeması, grafik, formül, yörünge | **Tahta, Manim (varsayılan)** | `kanal/`, `trigonometri/` | hassas hareket, sesle senkron | gerçekçi görüntü, karakter |
| Elle çizilen hikâye, insanlar, olay anlatımı | Tahta, çizim motoru | `lydia/` | karakter ve kalem hissi | sürekli hareket, kamera |
| 3D ölçek, fizik, "ne olurdu" zirvesi | Blender | `blender/` | derinlik, ışık, etki | render süresi |
| Atmosfer, kanca veya kapak resmi, yağlı boya | Pillow + numpy fırça darbeleri | `yagliboya/` | sinematik görünüm | yavaş render, diyagrama uygun değil |
| Evdeki Pillow çizim motoru (yağlı boya, 3B düzlemler, kamera) | evdeki kod | **bu depoda yok** | doku, derinlik, kamera (tanıma göre) | burada görülmedi |
| 3D anime karakterli hikâye | three.js + VRM | `vroid/` | ifade, karakter | doğal hareket zor |

## Tahta tarzının kuralları (`kanal/tahta.py`)
- **İki tahta:** siyah = uzayın ve fikrin içi; beyaz = insan ölçeği, Dünya, tarih, "nasıl ölçüldü?". Geçiş anlam taşır, süs değil.
- **Renk anlamı video boyunca sabit** (ör. mavi = mesafe, kırmızı = dikkat, sarı = ana fikir, yeşil = sonuç). Renkler `THEMES` içinden.
- **Yazı:** Segoe Print; başlık üstte, sarı alt çizgili (`title`); ekrandaki yazı kısa, anlatımı tekrar etmez.
- **El çizimi hissi:** şekilleri `sketch()` veya `ln()` ile çiz.
- **Ses ve çizim birlikte:** her cümle `say(i, adım1, adım2...)`; söylenen şey o anda belirir.
- **Ekranda tek fikir**; sahne sonunda `end()` ile temizle.
- **Altyazı bandı:** altta, en çok 2 satır; içerik y = -3.4 üstünde, x = -7..7 içinde kalsın.
- **Hareket:** bir şey anlatmıyorsa oynatma. Ölçekte tek tanıdık referans kullan ve onu değiştirme.

## Manim tuzakları
- LaTeX kurulu değil: `MathTex` ve `DecimalNumber` kullanma, `Text` kullan.
- `Text` 48+ puntoda uzun satırı kendiliğinden kaydırıyor; altyazı 32 punto çizilip küçültülüyor.
- Segoe Print alt simgeleri çizemiyor (h₁ bozuk çıkar).
- Yazı çakışması ancak karede görülür: her taslakta `onizleme.png` dosyasına bak (sahne başına tek kare; ara anlar için sahne videosunu aç).

## Her tarzda ortak
Önce örnek kare, onay, sonra render; uzun render arka planda; sesi dinlemediysen ve kareleri görmediysen bunu söyle.
