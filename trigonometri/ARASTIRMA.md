# Trigonometri videosu: araştırma ve sahne planı (2026-11-27)

Kaynaklar arama özetlerinden okundu; tam metinler incelenmedi.

## 1. Öğrenciler nerede takılıyor?
| Güçlük | Kaynak | Videoda çözümü |
|---|---|---|
| Radyanı açı birimi olarak görmemek; "tüm çember 1 radyan" veya π radyan ile 1 radyanı karıştırmak | [Williams (zayıf kanıt, küçük çalışma)](https://www.gcsu.edu/sites/files/page-assets/node-808/attachments/williams.pdf), [radyan: öğretmenler](https://dergipark.org.tr/en/download/article-file/1079757) | Yarıçapı ip gibi çemberin üstüne sar |
| Üçgen tanımı ile birim çemberi bağlayamamak (ör. sin 162°) | [APOS çalışması](https://sciencedirect.com/science/article/abs/pii/S0732312316300311?via=ihub%3D) | Üçgeni çemberin içine koyup döndür |
| Birim çember, eksen eşlemesi, denklem ve özdeşlikler (10. sınıf) | [Türkiye çalışmaları](https://dergipark.org.tr/en/download/article-file/67833), [YÖK tezi](https://acikbilim.yok.gov.tr/handle/20.500.12812/50335) | cos = yatay, sin = dikey; tek renk kodu |
| sin(a+b) = sin a + sin b sanmak (doğrusallık hatası) | [Erzurum, n=205 çalışması](https://dergipark.org.tr/en/download/article-file/508917) | Sayıyla çürüt: sin 90° = 1, ama sin 30° + sin 60° ≈ 1,37 |

Not: bulguların hangi Türk makalesine ait olduğu arama özetinde net değildi; bağlantıyı atıf vermeden önce kontrol et.

## 2. Nasıl anlatılmalı?
- Üçgen mi çember mi önce: kanıt karışık. Küçük, eski bir [kontrollü çalışma](https://merga.net.au/wp-content/uploads/DOCS/common/Uploaded%20files/Annual%20Conference%20Proceedings/1996%20Annual%20Conference%20Proceedings/RP_Kendal_Stacey_1996.pdf) oran yöntemini üstün bulmuş; başka araştırmacılar çemberi savunuyor. **Karar: üçgenle başla, hemen çembere bağla.**
- [Guo, Kim, Rubin 2014](https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf): kısa (6 dakikanın altı) videolar ve tablette çizerek anlatım daha çok izleniyor. Ölçülen izlenme, öğrenme değil.
- Genel bilgi (bu aramada doğrulanmadı): Mayer ilkeleri; vurgulama, bölümlere ayırma, gereksiz yazıdan kaçınma.

## 3. Hikâye malzemesi
- **"Sinüs" adı:** Aryabhata (yaklaşık 500) yarım kirişe *jya* dedi; Arapçaya *jiba* diye geçti; sesli harfsiz yazım *jaib* (koy, kıvrım) okundu; Latinceye *sinus* diye çevrildi. [St Andrews](https://mathshistory.st-andrews.ac.uk/HistTopics/Trigonometric_functions/), [Britannica](https://www.britannica.com/science/trigonometry/India-and-the-Islamic-world)
- **Everest:** Radhanath Sikdar 1852'de ölçüm verilerinden yüksekliği hesapladı; 29.002 fit değeri 1856'da duyuruldu; bugünkü kabul 8.849 m. Katkı payı tartışmalı, ekip işi. [GPS World](https://www.gpsworld.com/peak-xv-the-framework-that-measured-mount-everest/), [Wikipedia](https://en.wikipedia.org/wiki/Radhanath_Sikdar)
- **Ses ve dalgalar:** sinüslerin toplamıyla karmaşık dalga (genel bilgi; `yetenek_testi` sahne 3'te kodu hazır).
- Kullanma: Hipparkhos iddiaları (doğrulanmadı), "GPS trigonometriyle çalışır" sadeleştirmesi.

## 4. Matematik kontrolü
- tan 35° ≈ 0,700; 100 m uzaklıktan 35° bakış açısı yaklaşık 70 m (göz yüksekliği ihmal). Gerçek dağ ölçümü eğrilik ve ışık kırılması düzeltmesi ister.
- 1 radyan ≈ 57,3°; tam tur 2π ≈ 6,28 radyan.
- Birim çemberde nokta (cos θ, sin θ); sin² θ + cos² θ = 1 (Pisagor).
- sin 162° = sin 18° ≈ 0,309.

## 5. Sahne planı (5:00)
**Beyaz tahta = gerçek dünya, siyah tahta = matematiğin içi.**

| Süre | Tahta | Sahne | "Aha" anı |
|---|---|---|---|
| 0:00-0:30 | Beyaz | Dağa tırmanmadan boyunu ölçebilir misin? | Merak sorusu |
| 0:30-1:20 | Beyaz | Benzer üçgenler, tan, ağaç örneği | Açı aynıysa oran aynı |
| 1:20-2:10 | Siyah | Üçgen birim çemberin içine girer ve döner | sin = yükseklik, cos = yatay |
| 2:10-2:50 | Siyah | Yarıçap çembere sarılır: radyan | 6 tam parça ve biraz fazlası |
| 2:50-3:45 | Siyah | Dönen nokta açılıp sinüs dalgası çizer | Çember = dalga (zirve) |
| 3:45-4:10 | Siyah | Dalgalar toplanır: ses | Her ses sinüslerden |
| 4:10-4:40 | Beyaz | Jya'dan sinüse; Sikdar ve Everest | İnsan hikâyesi, girişteki soru çözülür |
| 4:40-5:00 | Siyah | Tuzak soru: sin(30+60) = ? | Yorumlara cevap |

## 6. Teknik karar
- Dönen çember ve açılan dalga sürekli hareket ister; `lydia` motoru yalnızca çizerek belirtiyor.
- Bu yüzden `yetenek_testi` tarzı tek `render(t)` + altyazı + cümleye senkron ses; iki tahta teması.
- Anlatım yaklaşık 3.900 karakter; ses edge-tts (ücretsiz).
- Önce iki temadan birer örnek kare, onaydan sonra video.
