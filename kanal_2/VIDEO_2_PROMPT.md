# Görev: Kanal 2 (Mind Margins), video 2: "The Planes That Never Came Back"

Sen bu projenin 1. videosunu yapan Claude'un devamısın. O oturumu hatırlamıyorsun; bilmen gerekenler burada ve depoda. Aynı titizlikle, hatta daha iyisini yap.

## 0. Benimle çalışma biçimi
- Türkçe ve **kısa** yaz. Video, altyazı, ekran yazıları, başlık ve açıklama **İngilizce**.
- Uzun işte arada kısaca ne yaptığını söyle; bitince haber ver. Uzun işten önce süre tahmini ver.
- Yalnız cevabı işi değiştirecek soru sor; güvenli varsayılan varsa söyle ve devam et.
- **İki onay kapısı:** (1) konu analizi + senaryo + seslendirme metni + altyazı + resimler + kapak/başlık; (2) onaydan sonra video. Ben onaylamadan ses (ElevenLabs) ve video üretme.
- Commit/push yalnız ben isteyince. **Video dosyasını (`video.mp4`) GitHub'a asla gönderme.** Depo herkese açık: anahtar hiçbir dosyaya (`t/.env` dışında), nota veya commit'e girmez; ekrana yazdırma.

## 1. Önce oku (bu sırayla)
1. `t/CLAUDE.md`, `t/kanal_2/CLAUDE.md` (niş, doğruluk kuralları, 50 konu, hikâye omurgaları)
2. `hikaye-senaryo` skill'i: `t/.claude/skills/hikaye-senaryo/SKILL.md` ve `references/arastirma.md` (ilk iş bu skill)
3. Örnek ve şablon: `t/kanal_2/001-first-number/` (`sahneler.py`, `ARASTIRMA.md`, `PAKET.md`, `kapak.py`)
4. Motor: `marj.py` (görünüm), `tahta.py`, `kalem.py`, `stills.py`, `render.py`, `eleven.py`, `belge.py`, `araclar/`
Yalnız `t/kanal_2/` içinde çalış; `kanal/` ve `kanal_3/` klasörlerine dokunma. Video 2 klasörü: `t/kanal_2/002-planes/`.

## 2. Sabit kararlar
- Görünüm: **A, "kenar boşluklu defter"** (`marj.py` varsayılanı, Patrick Hand; kâğıt #F5EEDB, mürekkep #1F2A44, turkuaz, mandalina). Marka aynı kalır, ama video 2 **yeni bir görsel fikir** getirmeli (ör. yukarıdan uçak, dönenler ve dönmeyen "hayalet" uçaklar, veriyi süzen bir kapı, izleyicinin kenar boşluğundaki zırh seçimi). Aynı çark/çıpa numarasını tekrar etme.
- Ses: ElevenLabs `eleven_v4`, ses kimliği `8GmsjNWRZ3Rk8VmRpvBZ`; anahtar ve kimlik `t/.env` içinde. Duygu etiketleri `DUYGU` sözlüğünde (altyazıda görünmez), cümlelerin yarısından azında, çeşitli, art arda aynısı yok.
- Süre: 5-10 dk; hedef **6-7 dk**. Video 1 ölçüsü: 5.074 karakter = 6:41. Yani yaklaşık 4.500-5.300 karakter. 5:00 altına düşme; boş cümleyle uzatma.
- Her `TEXT` cümlesi ≤135 karakter (altyazı en çok 2 satır). Selam ve kanal tanıtımı yok.

## 3. Konu ve devamlılık
- Video 1 şu soruyla bitti: *"Next time: you can only study the planes that came back. So where would you add armor?"* Video 2 ilk 30 saniyede bu soruyu izleyiciye **seçtirerek** açmalı (bölge A/B/C + geri sayım gibi) ve sonda izleyicinin seçimine dönmeli.
- Omurga: **G (Gerçek mi?)**: meşhur anlatı sahnesi → çatlak → gerçekte ne oldu → bugün ne biliyoruz → günlük hayat. Kanalın farkı: meşhur hikâyenin nerede süslendiğini dürüstçe göstermek.
- Bitiş: tek ana cümle, izleyiciye soru, sıradaki videoya köprü: **"Three Doors, One Car: Would You Switch?"**

## 4. Araştırma (yazmadan önce)
Aşağıdakiler **hafızadan ipucu, doğrulanmadı**; doğru kabul etme, çürütmeye çalış:
- Abraham Wald; Columbia'daki Statistical Research Group; 1943 civarı "plane vulnerability based on damage of survivors" notları; sonradan Center for Naval Analyses yeniden basımı.
- Mangel & Samaniego (1984, JASA) Wald'ın uçak çalışması; Wallis (1980, JASA) araştırma grubu anısı.
- Bill Casselman, AMS Feature Column, "The Legend of Abraham Wald": meşhur anlatının hangi kısımları belgeli?
- Şüpheli noktalar: kırmızı noktalı uçak çizimi modern bir illüstrasyon olabilir; generallerle diyalog uydurma olabilir; zırhın gerçekten onun tavsiyesiyle eklendiği belgeli olmayabilir; Wald'ın yöntemi "delik olmayan yere zırh"tan daha karmaşık.
- Günlük hayat örneği adayları (her biri ayrıca doğrulanacak, gerekirse at): yatırım fonlarında hayatta kalma yanlılığı; yüksekten düşen kediler çalışması ve eleştirisi; "eskiler daha sağlam yapardı"; okulu bırakan başarılı girişimciler.
Kurallar:
- Her iddia için asıl kaynak **ve** eleştiri/tekrar ara. Mümkün olan her yerde asıl metni oku; derleme ya da özetse `ARASTIRMA.md`'de düzeyini yaz (birincil / yazar / özet). Açamadığını "doğrulandı" sayma.
- Uydurma alıntı, sayı, diyalog yok. Belgesiz meşhur ayrıntıyı ya çıkar ya "anlatılır ama belgesi yok" diye söyle. "Bilim kanıtladı" deme.
- Çizim kaynakta olmayan veri ima etmesin; temsili çizimi ekranda "sketch" diye etiketle. Her ekran yazısı da bir iddiadır.
- PDF'ler: `araclar/pdftext.py` (pdftoppm yok). İndirilenleri scratchpad'de ayrı boş klasöre koy.
- Web'de benzer videoların başlıklarına bak; ölçemediğin talebi veya izlenmeyi uydurma.

## 5. Hikâye ve merak (YouTube)
- `SENARYO.md`'ye seçtiğin omurgayı ve **ABT** cümlesini yaz.
- **3 kanca taslağı** yaz, birini seç ve nedenini söyle. İlk 30 saniye: görüntü + merak boşluğu + vaat + izleyicinin kendi cevabı.
- Bölümler "ve sonra" ile değil **"ama / bu yüzden"** ile bağlansın (Parker-Stone testi). Döngü defteri: açılan her soru kapansın. 45-60 sn'de bir tahmin, ters köşe veya mekân değişimi. Görsel zirve sondan önce (ör. dönmeyen uçakların belirdiği an). Yeniden kanca, bilgi boşluğu, SUCCESs ve Mayer denetimi.
- Somut önce, terim ("survivorship bias") sonra. Süs testi: ana fikre hizmet etmeyeni sil.
- **3 dürüst başlık** (yaklaşık 60 karakter altı) ve **3 kapak** (tek odak, en çok 3-4 kelime, sağ alt boş). Videoda olmayanı vaat etme.

## 6. Üretim (1. onaydan önce)
`002-planes/` içinde: `ARASTIRMA.md`, `sahneler.py` (`TEXT`, `DUYGU`, `SAHNE`, `META`, `class Sahne(Marj)` + sahneler), `kapak.py`, `PAKET.md`.
```bash
cd /c/Users/Karim/Desktop/youtube/t/kanal_2
PYTHONUTF8=1 PYTHONWARNINGS=ignore .venv/Scripts/python stills.py 002-planes   # video yok: her cümlenin karesi, denetim,
                                                                  # onizleme/sayfa_*.png, SENARYO.md, SESLENDIRME.md, altyazi.srt
cd 002-planes && PYTHONUTF8=1 PYTHONPATH=.. ../.venv/Scripts/python -m manim -s -r 1280,720 kapak.py A B C
```
`stills.py` ücretsiz taslak ses üretir (yalnız süre tahmini). Metni değişen ya da sırası kayan cümlenin `ses/<Sahne>_<n>.mp3` dosyasını sil. `media/videos` içinde eski taslak klipler varsa `belge.py` tahmin yerine onları kullanır.

**Onaydan önce en az iki kontrol:**
1. Sen: her anlatım cümlesi ve ekran yazısı ↔ kaynak (tek tek).
2. Bağımsız denetçi alt ajan: ona `sahneler.py` yolunu ve kaynakları ver, **kendi sonuçlarını söyleme**, "çürütmeye çalış" de. Bulduğu her önemli hatayı asıl metinden **kendin doğrula**, sonra düzelt.
Ayrıca tüm önizleme sayfalarına gözünle bak (taşma, çakışma, anlamsız dolgu, yanlış çizim), düzeltince yeniden çiz.

## 7. Üretim (2. onaydan sonra, "kontrol ede ede")
```bash
cd /c/Users/Karim/Desktop/youtube/t/kanal_2
set -a; . <(tr -d '\r' < ../.env); set +a
PYTHONUTF8=1 .venv/Scripts/python eleven.py 002-planes
# ses denetimi (etiket sesli okunmuş mu, eksik/yanlış söz var mı); şüphelileri small.en ile tekrar dinle
PYTHONUTF8=1 uv run --no-project -p 3.13 --with faster-whisper python -X utf8 -I araclar/ses_kontrol.py 002-planes
PYTHONUTF8=1 .venv/Scripts/python render.py 002-planes taslak     # hareketli kareleri 3-4 sn arayla kontrol et
# tek kısa sahneyi 1440p ölç, toplam süreyi bildir, sonra arka planda final:
PYTHONUTF8=1 .venv/Scripts/python -u araclar/final_render.py 002-planes > <scratchpad>/final.log 2>&1
PYTHONUTF8=1 uv run --no-project -p 3.13 --with pillow python -X utf8 -I araclar/final_kontrol.py 002-planes kare
PYTHONUTF8=1 uv run --no-project -p 3.13 --with faster-whisper python -X utf8 -I araclar/final_kontrol.py 002-planes senkron
```
Finalde ayrıca: ffmpeg ile baştan sona çözme, `silencedetect` (yalnız bilerek konan molalar), `ebur128` (yaklaşık -16 LUFS). `PAKET.md`: başlıklar, açıklama, bölümler (`SENARYO.md` sonundan), kaynaklar, etiketler, sabit yorum, kapak, kontrol listesi.

## 8. Video 1'den dersler (tekrarlama)
- İlk taslakta bağımsız denetçi ciddi hatalar buldu: ayarlı çark "rastgele" sanılmış, hileli zar söylenmemiş, bir çizim kaynakta olmayan veri göstermiş, bir tekrar projesinin yöntemi yanlış anlatılmış, tekrar edilemeyen bir deney eksik kalmış. Meşhur hikâyelerin ayrıntılarına özellikle güvenme.
- Geçişte eski yazı silinirken yenisi üstüne biniyordu; `Marj.say` artık önce `FadeOut` yapıyor. Hareketli kareleri yine kontrol et (durağan kareler bunu göstermez).
- Yazı kartlardan taşabiliyor; `stills.py` denetimi yakalıyor ama göz kontrolü de şart.
- Bash içinde ters bölülü Python metni bozulabiliyor: düzenleme betiğini dosyaya yaz.
- Sesi dinleyemez, videoyu canlı izleyemezsin: yapmadığın kontrolü yaptım deme, bana neyi izlemem/dinlemem gerektiğini söyle.

## 9. Bilgisayar ve bütçe
- Dell Inspiron 3521, i5-3317U, 5,9 GB RAM: zayıf. Aynı anda iki ağır iş çalıştırma; uzunları arka planda yürüt, yoklama.
- Video 1 süreleri: tüm kareler ~5 dk, taslak ~9 dk, ses denetimi ~5 dk, 1440p final **41 dk** (6:41'lik video).
- ElevenLabs (28.11.2026): 12.280 / 38.448 karakter kullanılmış (starter); yaklaşık 27 Aralık'ta yenileniyor. Üretmeden önce yeniden sorgula. Gereksiz ses örneği üretme.

## İlk adımın
Dosyaları oku → araştır → kısa bir konu analizi (hikâyenin doğru ve süslenmiş kısımları dahil) ve akışla bana dön ya da güvenli varsayılanla senaryo + resimlere kadar ilerleyip **1. onay** için sun. Her şeyi sunmadan önce en az iki kez doğrula.
