---
name: hikaye-senaryo
description: Bu depoda her yeni videoda İLK kullanılacak skill. Konu, video, akış, senaryo, seslendirme metni, süre, kanca, başlık, kapak, resim önizlemesi veya bitiş istendiğinde; konu → akış → senaryo → metin → resim → video sırasını ve hikâye anlatma tekniklerini yürütür.
---

# Hikâye ve senaryo

Kanıt düzeyi ve kaynaklar: [references/arastirma.md](references/arastirma.md). Kurallar izlenme garantisi vermez.

**Tek kalıp yok.** İş sırası ve genel teknikler her videoda aynı; anlatı biçimi konuya, konsepte ve kanal nişine göre seçilir.

## İş sırası (her adım bir öncekine dayanır, onaysız ilerleme yok)

| # | Adım | Çıktı | Onay |
|---|---|---|---|
| 1 | **Konu** | niş, izleyici, konsept, görsel tarz, büyük soru; gerekiyorsa araştırma | konu seçimi |
| 2 | **Akış** | yaklaşık süre, başlık + kapak taslağı, kanca, konu sırası, bitiş | akış |
| 3 | **Senaryo** | sahne tablosu: süre, ne olur, ekranda ne var, açılan/kapanan soru | |
| 4 | **Seslendirme metni** | sahne sahne tam metin, süreyle uyumlu | senaryo + metin |
| 5 | **Resimler** | karakter/stil örneği, sonra her sahneden kare (tek önizleme sayfası) | resimler |
| 6 | **Video** | ses, hızlı taslak, final | taslak |

1-4 `<proje>/SENARYO.md` içine yazılır. Kullanıcıya özet göster, dosyanın tamamını tekrarlama.

## 1. Konu
- İzleyici kim, bu konuyu zaten ne biliyor veya ne hissediyor, neden tıklasın?
- Büyük soru veya vaat: tek cümle.
- Tek fikir veya duygu: video bitince geriye ne kalacak?
- Biçimi seç (aşağıda). Gerçek olay ve bilgi varsa önce araştır, kaynak yaz.

## Biçime göre değişen
| Biçim | Gerilimin kaynağı | Kanca örneği | Zirve | Bitiş |
|---|---|---|---|---|
| Kavram anlatımı (matematik, bilim) | yanlış sezgi veya çözülemeyen soru | "sin 30 + sin 60 = 1 mi?" | görsel "aha" | yeni soruya uygulama |
| Karakterli hikâye (Sprouts, psikoloji) | karakterin isteği ve engeli | sahnenin ortasında bir an | karakterin fark edişi veya deneyin sonucu | "sen olsan ne yapardın?" |
| Gerçek vaka / gizem | açıklanamayan çelişki | en tuhaf olgu | gerçeğin ortaya çıkışı | sonucu ve bugünkü anlamı |
| Tarih / biyografi | karar ve bedeli | dönüm noktasından bir an | dönüm noktası | bugüne bağ |
| Liste ("5 yol") | her maddede küçük soru, giderek güçlenen sıra | en şaşırtıcı maddenin vaadi | son madde | maddeleri bağlayan fikir |
| Nasıl yapılır | hedefle mevcut durum farkı | bitmiş sonuç | işe yaradığı an | ilk adım |
| Görsel / atmosfer (yağlı boya, müzikli) | dönüşüm ve merak: ne beliriyor? | ilk fırça darbesi veya sonuçtan bir ayrıntı | resmin canlanması | sakin kapanış, döngü |

Uyan yoksa biçimleri karıştır veya yenisini kur. "Yanlış inanç" yalnız konu gerçekten bir yanılgı içeriyorsa kullanılır.

## Her videoda aynı kalan teknikler
- **Kanca:** selam ve kanal tanıtımıyla başlama; 3 taslak yaz, birini seç. İlk 30 saniyede görüntü, merak boşluğu ve vaat.
- **Dürüst paket:** başlık ve kapağın sorusu ilk 30 saniyede karşılanır; videoda olmayanı vaat etme.
- **Nedensellik:** sahneler "ve sonra" ile değil **"ama"** veya **"bu yüzden"** ile bağlanır (anlatısız atmosfer videosu hariç).
- **Sahne:** soru → engel → sonuç → yeni soru. En fazla 2 açık döngü; hepsi kapanır.
- **Ritim:** 45-60 saniyede bir değişim (soru, ters köşe, tahmin molası, mekân).
- **Somut önce**, terim sonra. Duygu sıfatla değil olayla.
- **Zirve** sondan önce ve görsel; mümkünse giriş görüntüsüne dön.
- **Süs testi:** ana fikre hizmet etmeyen ilginç ayrıntıyı sil.
- **Bitiş:** ana cümle bir kez, izleyiciye soru veya sıradaki videoya köprü; uzun teşekkür ve abone çağrısı yok.
- **Doğruluk:** olay, söz, sayı uydurma.

## 2. Akış
- Süreyi konu belirler; kullanıcı söylemediyse öner (anlatım videosu için 4-6 dk iyi başlangıç).
- 3 başlık (somut, merak boşluklu, yaklaşık 60 karakter altı) ve 3 kapak eskizi (tek odak, en fazla 3-4 kelime, sağ alt köşe boş).
- Pay önerisi: kanca 10% · kurulum 15% · gelişme 45% · zirve 15% · dönüş ve bitiş 15%. Biçime göre değiştir.

## 3-4. Senaryo ve metin
- Konuşma dili, kısa cümle, cümlede tek fikir. Söylenen şey o anda ekranda.
- Süre hesabı: edge-tts Türkçe `+10%` hızında yaklaşık **11,5 karakter = 1 sn** (3606 karakter → 5:12). Başka ses, dil veya hızda ilk sahneyi üretip ölç. Sessiz videoda süreyi hareket planı belirler.
- Onaydan önce denetle: kanca, "ama / bu yüzden", açık döngüler, zirve, bitiş, kaynaklar, süre.

## 5. Resimler
Videodan önce çiz: önce stil ve karakter örneği (1-3 resim); beğenilince her sahneden bir kare, tek sayfada. Yazı çakışması ve okunurluk burada yakalanır. Beğenilmeyen resimle videoya geçme.

## 6. Video
Seslendir → hızlı taslak → birkaç kareden kontrol → final render arka planda. Sesi dinleyemediğini ve neyi kontrol etmediğini söyle.

## Yayından sonra
İlk 30 saniyede kalma, izleyici tutma düşüşleri, tıklanma oranı; öğrenileni nişe göre bu dosyaya ekle.
