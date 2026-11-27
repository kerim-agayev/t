---
name: hikaye-senaryo
description: Bu depoda YouTube videosu üretmeden ÖNCE kullan. Konu, video, senaryo, anlatım metni, kanca, başlık, kapak (thumbnail), bölüm sırası veya bitiş istendiğinde; çizim ve ses üretiminden önce paketleme ve senaryo çıkarır, onay alır.
---

# Hikâye ve senaryo

**Kural: onaylı senaryo olmadan çizim, ses ve render yok.** Sıra: paket → omurga → metin → denetim → onay → üretim.
Kanıt düzeyi ve kaynaklar: [references/arastirma.md](references/arastirma.md). Kurallar izlenme garantisi vermez; yayından sonra ölçülür.

## 1. Brif (5 satır)
- İzleyici kim, konuyu ne sanıyor? (**yanlış inanç**)
- Büyük soru: tek cümle, evet/hayır değil, cevabı merak edilen.
- Vaat: video bitince neyi yapabilecek veya görebilecek?
- Tek fikir: unutursa geriye kalması gereken cümle.
- Süre hedefi (varsayılan 4-6 dk).

## 2. Önce paket: başlık ve kapak
Metinden önce yaz; yazılamıyorsa konu zayıf.
- 3 başlık (somut nesne + boşluk; yaklaşık 60 karakter altı; en önemli kelime başta).
- 3 kapak eskizi: tek odak, tek çatışma, en fazla 3-4 kelime, küçük ekranda okunur, başlığı tekrar etmez, sağ alt köşe boş (süre etiketi).
- Videoda olmayan şeyi vaat etme. Başlık ve kapağın sorusu ilk 30 saniyede açıkça karşılanır.

## 3. Omurga
Tek cümle (VE-AMA-BU YÜZDEN): "X böyle **ve** şöyle, **ama** sorun şu, **bu yüzden** ..."
Sahneler arasına yalnız **ama** veya **bu yüzden** konabiliyorsa sıra doğrudur; "ve sonra" geliyorsa sahneyi birleştir, taşı veya sil.

| Pay | Bölüm | İşi |
|---|---|---|
| 0-10% | Kanca + vaat | Somut görüntü, boşluk, "sonunda ..." sözü |
| 10-25% | Sezgi | İzleyicinin tahminini al, yanlış inancı açıkça söyle |
| 25-45% | İlk çatlak | Sezgi bir örnekte çöker; küçük ilk ödül |
| 45-70% | Keşif | Fikir adım adım kurulur; her adım yeni soru doğurur |
| 70-85% | Zirve | En güçlü görsel "aha"; büyük soru cevaplanır |
| 85-95% | Dönüş | Giriş görüntüsüne dön, artık farklı görünsün; insan veya tarih bağı |
| 95-100% | Bitiş | Sınama sorusu + sıradaki videoya köprü |

Oranlar başlangıç noktasıdır, araştırma bulgusu değil.

## 4. Kanca
İlk cümle selam, kanal tanıtımı veya "bu videoda" olmaz. Üç taslak yaz, birini seç:
1. **İmkânsız görünen iş:** "Tırmanmadan bir dağın boyunu nasıl ölçersin?"
2. **Yanlış sezgi:** "sin 30 + sin 60 kaç eder? 1 dediysen..."
3. **Olayın ortası:** kişi + yer + ters giden şey ("Bir anne, kendi çocuklarının annesi olmadığını söyleyen test sonucunu okuyor").
4. **Sonuç önce:** zirvedeki görüntünün 3 saniyesi, sonra "buraya nasıl geldik?"

İlk 30 saniye: görüntü (0-5) → boşluk (5-15) → vaat ve bedel (15-30). Boşluk orta büyüklükte olsun: izleyicinin bildiği bir şeye bağlanmalı.

## 5. Metin
- Her sahne: **hedef/soru → engel → sonuç → yeni soru**.
- Açık döngü: aynı anda en fazla 2; her biri kapanır. Ana soru zirveye kadar açık kalır.
- 45-60 saniyede bir değişim: yeni soru, ters köşe, tahmin molası, tahta değişimi.
- Somut önce, terim sonra. Yeni terim sahnede en fazla 1-2.
- Kişi varsa: isim, istek, engel. Duygu sıfatla değil olayla.
- Konuşma dili, "sen", kısa cümle, cümlede tek fikir.
- Ekranda söylenen şey o anda çizilsin; vurgu rengiyle işaretle.
- Süs bilgi testi: tek fikre hizmet etmeyen ilginç ayrıntıyı sil.
- Olmayan olay, söz veya sayı uydurma. Her olgunun yanına kaynağı yaz; doğrulanmayanı işaretle.

## 6. Bitiş
Son 20 saniye: ana cümle (tek kez) → izleyiciye cevabı videoda hazırlanmış bir soru → sıradaki videonun açtığı boşluk. "İzlediğiniz için teşekkürler" ve uzun abone çağrısı yok; son cümleden sonra video biter.

## 7. Denetim (hepsi "evet" olmadan onaya gönderme)
- [ ] Başlık ve kapağın sorusu ilk 30 saniyede duyuluyor mu?
- [ ] Yanlış inanç açıkça söylenip çürütülüyor mu?
- [ ] Sahne geçişleri "ama / bu yüzden" ile bağlanıyor mu?
- [ ] Silinince bir şey kaybolmayan sahne veya cümle kaldı mı? (sil)
- [ ] Zirve görsel mi, sondan önce mi?
- [ ] Giriş görüntüsüne dönülüyor mu?
- [ ] Olgular kaynaklı mı?
- [ ] Süre: edge-tts Türkçe `+10%` hızında yaklaşık **11,5 karakter = 1 sn** (3606 karakter → 5:12).

## 8. Onay çıktısı
`<proje>/SENARYO.md` yaz: brif, 3 başlık, 3 kapak, VE-AMA-BU YÜZDEN cümlesi, sahne tablosu (süre, tahta, anlatım, ekranda ne var, açılan/kapanan soru), kaynaklar. Kullanıcıya yalnız seçilen kancayı, başlığı ve sahne tablosunun özetini göster; onay bekle.

## 9. Yayın sonrası
YouTube Studio: ilk 30 saniyede kalma oranı, izleyici tutma grafiğindeki düşüşler, tıklanma oranı; 3 başlık/kapakla test. Öğrenileni bu dosyaya ekle.
