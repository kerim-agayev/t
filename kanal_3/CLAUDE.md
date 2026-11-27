# Kanal 3: "Zor sanılan, kolay fikirler"

Bu klasör üçüncü, bağımsız kanal. `kanal/` ve `kanal_2/` dosyalarını değiştirme. Kullanıcı tercihleri (kısa Türkçe cevap, az token, video dili İngilizce, onaylı adımlar, anahtar yazma yasağı) kökteki `CLAUDE.md` içinde.

## Niş ve vaat (2026-11-27)
- **Niş:** oyun teorisi, ekonomi, istatistik, fizik/biyoloji, bilgisayar: **kulağa zor gelen ama küçük bir modelle kolaylaşan** fikirler.
- **İzleyici:** meraklı, ders almamış veya derste anlamamış İngilizce izleyici.
- **Vaat:** "Zor sanıyordun; sonunda kendin anlatabileceksin." Formül yok veya en sonda, tek satır.
- **Süre:** 5-8 dk, uzun video. Bir video = bir fikir.
- **Ad adayları (müsaitliğine bakılmadı):** Suddenly Simple, The Small Model, Oh That's It.
- **Kanal 2 ile sınır:** mahkûm ikilemi, Monty Hall, doğum günü, taban oranı, kumarbaz yanılgısı, ortak mallar, ültimatom, Schelling orada; burada yapma.

## Veri ve sınırları
- 2026-11-27 web taraması: karmaşık konuları anlatan büyük kanallar var (Kurzgesagt, 3Blue1Brown, Vox), yani rekabet güçlü. **İzlenme, gelir ve tek tek başlık talebi ölçülmedi**; kaynakların çoğu pazarlama blogu.
- Fark: her videoda aynı "elle sayılabilen küçük model" ve modelin sınırının söylenmesi.
- İlk 8 videodan sonra sırayı YouTube Studio verisine göre değiştir.

## Görsel tarz (öneri; ilk videoda 2-3 örnek kareyle onaylat)
- **"Masa üstü model":** yukarıdan görülen düz renkli masa; sayılabilir parçalar (bilye, jeton, kart, oyuncak araba, blok). Parçalar hareket eder, sayaçlar canlı değişir. Kalem yalnız ok ve not için.
- Kanal 1 (tahta/uzay) ve kanal 2 (defter) ile aynı renk, zemin ve yazı düzeni olmasın.
- Aynı nesne video boyunca aynı anlamı taşır. Sayılar ekranda hesaplanır; elle uydurulmuş grafik yok.
- Kodlanmadı: masa teması ve parça sınıfları ilk videoda yazılacak.

## Hikâye omurgası (`hikaye-senaryo` skill'i ile)
Ortak iskelet:
1. **Kanca:** imkânsız görünen sonuç, ekranda (ilk 5 sn).
2. **Tahmin:** izleyici cevabını seçer.
3. **Küçük model:** en az parçayla kur; terim henüz yok.
4. **Ama:** model beklentiyi bozar. **Bu yüzden:** bir parça ekle veya say (2-3 tur).
5. **"Aha" (zirve):** tek karede neden; giriş görüntüsüne dön.
6. **Adı şimdi söyle:** terim ödül olarak gelir.
7. **Gerçek dünya + sınır:** modelin nerede tutmadığı.
8. **Bitiş:** tek cümle (videonun ABT özeti) + izleyiciye soru + sıradaki videoya köprü.

| Kod | Omurga | Fark |
|---|---|---|
| Y | Yanlış inanç (Muller) | yaygın cevabı söylet, sınat, çürüt |
| M | Model kur | parça ekledikçe ama / bu yüzden zinciri |
| G | Gizem | "bu nasıl mümkün?" → yetmeyen fikir → zekice çözüm → sınama |

Örnek ABT (video 1): "Daha çok yol trafiği azaltır sanırız **ve** yeni yol yaparız, **ama** herkes kendi için en hızlı yolu seçer, **bu yüzden** bazı ağlarda yeni yol herkesi yavaşlatır."

Denetim: skill'deki "ama / bu yüzden", ABT, döngü defteri, yeniden kanca, bilgi boşluğu, SUCCESs, Mayer.

## Doğruluk kuralları
- Her videodan önce birincil kaynak (makale, ders kitabı, resmi kurum). Uydurma sayı ve alıntı yok.
- Model ile gerçek dünyayı ayır: "bu modelde" de.
- **#1:** Braess matematikte gösterilir; Seul ve 42. Cadde örneklerinde kanıt zayıf ve başka etkenler var, "kanıtladı" deme.
- Ekonomi, aşı ve siyaset yakın konularda taraf tutma; yatırım veya sağlık öğüdü verme.

## İlk 50 video (yayın sırası)
Alan: O oyun/strateji, P para/ekonomi, S sayı/olasılık, D doğa, B bilgisayar. Durum: **✓** temel nokta 2026-11-27 aramasında görüldü (özet düzeyi); **⚠** tartışmalı veya sık yanlış anlatılan; boş = doğrulanmadı. Başlıklar taslak.

| # | Alan | Başlık | Küçük model / görsel | Omurga | Durum |
|---|---|---|---|---|---|
| 1 | O | How Can a New Road Make Traffic Worse? | 4000 arabalık oyuncak harita; yol ekle, herkes yavaşlasın | Y | ✓ |
| 2 | P | Where Does New Money Come From? | iki sütunlu banka defteri: kredi yazılınca mevduat doğar | Y | ✓ |
| 3 | D | Why Does Your Phone Need Einstein? | uydu saati ile cep saati; günde yaklaşık 38 mikrosaniye | G | ✓ |
| 4 | S | Better in Every Group, Worse Overall? | iki kutuda toplar; birleştirince sonuç ters döner | Y | ✓ |
| 5 | B | How Do Strangers Share a Secret in Public? | boya karıştırma: karıştırmak kolay, ayırmak zor | G |  |
| 6 | O | Why Does the Auction Winner Often Overpay? | bir kavanoz bozuk para ve tahminler | Y | ✓ |
| 7 | P | Should the Best Chef Wash the Dishes? | iki kişi, iki iş: karşılaştırmalı üstünlük | M |  |
| 8 | S | Why Does Doubling Fool Everyone? | gölü kaplayan nilüfer; yarısı hangi gün? | Y |  |
| 9 | D | Why Does Coffee Never Reheat Itself? | iki kutuda zıplayan toplar: entropi | M |  |
| 10 | B | How Does Your Map Find the Fastest Route? | küçük şehirde yayılan dalga (Dijkstra) | M |  |
| 11 | O | How Do You Match Thousands Without Chaos? | teklif, beklet, reddet turları (Gale-Shapley) | M | ✓ |
| 12 | P | Why Can Good Used Cars Vanish From a Market? | 10 araba; fiyat düştükçe iyiler çekilir | M |  |
| 13 | S | Why Does Randomness Draw a Bell? | çivili tahtadan düşen bilyeler | M |  |
| 14 | D | Can Two Chemicals Draw Zebra Stripes? | yayılan ve bastıran iki madde (Turing) | G |  |
| 15 | B | How Does a Computer Fix Its Own Mistakes? | üç çemberli bit bulmacası (Hamming) | G |  |
| 16 | O | When Is Being Random the Smartest Move? | penaltı: kaleci ile atıcı | M |  |
| 17 | P | What Happens When Money Grows but Apples Don't? | on elmalı mini ekonomi; modelin sınırını söyle | M |  |
| 18 | S | Why Does a Great Year Often Fade? | zar + yetenek: ortalamaya dönüş | Y |  |
| 19 | D | Why Is the Sky Blue and the Sunset Red? | kısa dalga daha çok saçılır | M |  |
| 20 | B | How Can a File Shrink and Lose Nothing? | sık harfe kısa kod (Huffman) | M |  |
| 21 | O | When Does Nobody Want to Move Alone? | yolun sağı mı solu mu? Nash dengesi | M |  |
| 22 | P | Why Do Bond Prices Fall When Rates Rise? | tahterevalli ve iki kâğıt | M |  |
| 23 | S | How Do You Count Fish You Cannot See? | yakala, işaretle, yeniden yakala | G |  |
| 24 | D | How Can Vaccines Protect the Unvaccinated? | nokta kalabalığında kopan zincirler | M |  |
| 25 | B | How Does a Machine Learn From Being Wrong? | sisli tepede aşağı adım: gradyan inişi | M |  |
| 26 | O | Can Any Ranked Vote Be Perfectly Fair? | üç aday, döngü; Arrow'un koşullarını söyle | Y |  |
| 27 | P | Who Really Pays a Tax? | alıcı ile satıcı arasında kayan yük | Y |  |
| 28 | S | What Does Statistically Significant Mean? | hilesiz parayla "şanslı" deneyler | Y | ⚠ |
| 29 | D | Why Does a Steel Ship Float? | taşan su tartılır | M |  |
| 30 | B | Why Can't a Program Catch Every Endless Loop? | kendini soran program | G |  |
| 31 | O | Why Would Anyone Waste Money to Be Believed? | pahalı işaret: tavus kuşu, diploma modeli | G |  |
| 32 | P | How Can a Healthy Bank Suffer a Run? | kuyruktaki on mudi | M |  |
| 33 | S | When Should You Stop Looking? | yaklaşık %37 kuralı ve koşulları | M |  |
| 34 | D | How Can Design Appear Without a Designer? | renkli noktalar: değişim + seçilim | M |  |
| 35 | B | How Do You Rank the Whole Web? | rastgele tıklayan gezgin (PageRank) | M |  |
| 36 | O | Why Do Rival Shops Sit Side by Side? | sahilde iki dondurmacı (Hotelling) | M |  |
| 37 | P | Why Is a Diamond Pricier Than Water? | çöldeki bardak: marjinal değer | G |  |
| 38 | S | Drive 30 There and 60 Back: Why Not 45? | aynı yol, farklı süre: harmonik ortalama | Y |  |
| 39 | D | How Does a Heavy Plane Stay Up? | havayı aşağı iten kanat; yaygın yanlış açıklama | Y | ⚠ |
| 40 | B | Why Are Some Puzzles Easy to Check, Hard to Solve? | dolu sudoku ile boş sudoku (P ve NP) | M |  |
| 41 | O | Why Don't Fighters Take Over Every Population? | şahin ve güvercin noktaları | M |  |
| 42 | P | Why Does the Same Seat Have Many Prices? | dört yolcu, dört ödeme isteği | G |  |
| 43 | S | Why Do So Many Numbers Start With 1? | büyüyen sayı şeridi (Benford); hangi veride geçmez | G |  |
| 44 | D | How Does a Dead Tree Tell Time? | yarıya inen noktalar: radyokarbon | G |  |
| 45 | B | How Can a Computer Pull Notes Out of Noise? | dönen çubuklardan dalga (Fourier) | M |  |
| 46 | O | Can Two Losing Games Make a Winner? | iki para oyunu sırayla (Parrondo); koşulları söyle | G |  |
| 47 | P | What Does GDP Count, and Miss? | küçük köyün hesap defteri | M |  |
| 48 | S | Are Some Infinities Bigger Than Others? | listede olmayan sayıyı kur (Cantor) | G |  |
| 49 | D | What Does a Single Photon Do at Two Slits? | nokta nokta beliren desen; yorum tartışmalı | G | ⚠ |
| 50 | B | How Does a Chatbot Pick the Next Word? | küçük metinden sonraki sözcük sayımı; gerçek model farkı | M |  |

Aramada görülen kaynaklar: [Braess](https://en.wikipedia.org/wiki/Braess%27s_paradox), [para yaratımı (Bank of England 2014)](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy), [GPS ve görelilik](https://arxiv.org/pdf/gr-qc/0507121), [Simpson](https://plato.stanford.edu/Entries/paradox-simpson/), [açık artırma Nobel 2020](https://news.stanford.edu/?p=37318), [eşleştirme Nobel 2012](https://www.nber.org/news/alvin-e-roth-and-lloyd-s-shapley-won-nobel-prize-2012-developing-theory-stable-allocations-and).

## Kurulum ve deneme
```bash
cd kanal_3
uv venv -p 3.13 && uv pip install -r requirements.txt     # bir kez
.venv/Scripts/python render.py ornek taslak                # -> ornek/onizleme.png
```

## Her videonun sırası (onaysız ilerleme yok)
1. `.claude/skills/hikaye-senaryo` skill'i: konu, akış, senaryo.
2. `kanal_3/NNN-ad/` aç: `ARASTIRMA.md` (her iddiaya kaynak), `sahneler.py` (`TEXT`, `DUYGU`, `SAHNE`, `META`, sahne sınıfları; örnek yapı: `../kanal/002-voyager/sahneler.py`).
3. `python render.py NNN-ad taslak` (geçici ücretsiz ses) -> `python belge.py NNN-ad` -> `onizleme.png` kontrolü, `kapak.py`, `PAKET.md`. **Kullanıcı onayı.**
4. `python eleven.py NNN-ad` (ElevenLabs; ortam değişkenleri) -> `render.py NNN-ad final` -> `belge.py` -> her cümlede ses var mı, senkron, kareler.

İlk iş: **"kanal_3 ile 1. videoya başla"** denince 1 numaralı videodan başla; önce kanal adı ve görünüm örneklerini onaylat.

## Motor
- `tahta.py`, `kalem.py`, `render.py`, `eleven.py` (`eleven_v4`, duygu etiketleri; kökteki `CLAUDE.md`), `belge.py`: kanal 2'den kopyalandı, burada serbestçe değiştirilebilir.
- Tarz kuralları ve tuzaklar: `../STIL_REHBERI.md`. Her video öncekilerden farklı ve daha iyi olsun.
