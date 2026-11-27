# Kanal 2 (evde; ikinci YouTube kanalı)

Bu klasör **kanal 1'den bağımsız**. Evdeki Claude yalnız `kanal_2/` içinde çalışır; `kanal/` klasörü kanal 1'dir (Chalk Orbit), ona dokunma. Ortak kurallar için kökteki `CLAUDE.md` geçerli (Türkçe ve kısa cevap, az token, kaynaklı bilgi, anahtar dosyaya yazılmaz, commit/push yalnız istenince).

## Niş ve tarz (kullanıcı seçti, 2026-11-27)
- **Niş:** İngilizce **"zihnin tuzakları"**: psikoloji deneyleri, sosyoloji, felsefe. Defterde anlatım.
- **İzleyici:** kendi kararlarını ve toplumu merak eden, ders almamış İngilizce izleyici.
- **Vaat:** her videoda izleyici önce kendi cevabını verir, sonra şaşırır veya fikrini sınar.
- **Süre:** 5-10 dk. Şimdilik yalnız uzun video.
- **Tarz:** `kalem.py` defter ve gece zemini, kalemle çizme ve yazma. Basit çöp adam, simge, kart, tablo, grafik; **ayrıntılı yüz ve çizer kalitesinde karakter hedefleme** (bu hatta ulaşılamadı). Her video öncekilerden farklı ve daha iyi olsun; kanal 1 ile aynı renk ve yazı düzeni olmasın (ilk videoda kullanıcıya 2-3 örnek kare seçtir).
- **Ad adayları (müsaitliği bakılmadı):** Mind Margins, The Thinking Notebook, Pencil Paradox.

- **Marka (hazır):** `marka/profil_800.png` ve `marka/banner_2560x1440.png` ("Mind Margins", slogan "What would you really do?"; kaynak görseller Gemini üretimi, aynı klasörde). Renkler: kâğıt #F5EEDB, mürekkep #1F2A44, turkuaz #1F8A80, mandalina #F28C28.

## Veri ve sınırları
- Önceki API analizi (kökteki `NIS_ARASTIRMASI.md`): küçük kanallarda psikoloji medyan izlenmesi yüksek çıkmıştı; örneklem küçük, gelir ölçülmedi.
- 2026-11-27 web taraması: bu nişte tek tek başlık talebi veya rakip izlenmesi **ölçülemedi**. İlk 8 videodan sonra sırayı YouTube Studio verisine göre değiştir.

## Hikâye omurgaları (`hikaye-senaryo` skill'i ile)
| Kod | Tür | Omurga |
|---|---|---|
| D | Deney | sahne → **"sen ne yapardın?" duraklaması** → sonuç → ama neden? → tekrar edildi mi? → günlük hayat |
| T | Tuzak | izleyiciyi tuzağa düşür → göster → mekanizma → nerede karşına çıkar → nasıl fark edersin (sınırıyla) |
| P | Bulmaca | soru → herkesin sezgisi → sına → küçük sayılarla "aha" → yeni, daha zor soru |
| F | Felsefe ikilemi | seçim yaptır → bir ayrıntıyı değiştir → çelişkiyi göster → iki güçlü cevap → izleyiciye bırak |
| S | Toplum | tek kişinin küçük kuralı → ama herkes yaparsa → büyük sonuç → gerçek örnek ve model sınırı |
| G | Gerçek mi? | meşhur anlatı sahnesi → çatlak → ne oldu → bugün ne biliyoruz |

Her videoda: ilk 30 saniyede izleyicinin kendi cevabı; bölümler "ama / bu yüzden" ile bağlı; 45-60 saniyede bir tahmin, ters köşe veya mekân değişimi; açılan her soru kapanır; bitişte tek cümle + izleyiciye soru + sıradaki videoya köprü; skill'deki denetim araçlarından geçir.

## Doğruluk kuralları (bu nişin en büyük riski)
- Her deney için **özgün makale + tekrar/eleştiri** ara. Tartışmalıysa videoda söyle; bu kanalın farkı olsun.
- Uydurma alıntı, uydurma yüzde yok. "Bilim kanıtladı" deme; "bu çalışmada" de.
- Felsefede "doğru cevap" dayatma; iki tarafı en güçlü haliyle ver.
- Tanı, tedavi veya "karşındakini yönlendirme" öğüdü verme; "dark psychology / manipülasyon" paketi kullanma. Hassas konular (intihar, istismar, Genovese gibi şiddet olayları) ölçülü ve saygılı.

## İlk 50 video (yayın sırası)
Durum: **✓** temel nokta 2026-11-27 taramasında arama özetlerinde görüldü; **⚠** tartışmalı veya zayıf kanıt, videonun konusu bu olmalı; boş = henüz doğrulanmadı. Hepsi yazılmadan önce birincil kaynaktan kontrol edilir.

| # | Tür | Başlık | Kanca / görsel fikir | Durum |
|---|---|---|---|---|
| 1 | D | Why Your First Number Traps You | çıpalama: önce ilgisiz bir sayı, sonra tahmin | ✓ |
| 2 | G | The Planes That Never Came Back | kurşun delikleri nereye zırh ister? (Wald) |  |
| 3 | P | Three Doors, One Car: Would You Switch? | izleyici seçer, kapı açılır |  |
| 4 | F | Would You Pull the Lever? | tramvay; sonra senaryoyu çevir | ✓ |
| 5 | D | Would You Deny Your Own Eyes? | Asch; 2023 tekrarı hata oranı yaklaşık %33 | ✓ |
| 6 | S | How Mild Preferences Split a City | Schelling: kareli kâğıtta taşınan noktalar |  |
| 7 | T | Why Losing Hurts More Than Winning | yazı tura bahsi | ⚠ |
| 8 | D | Would You Miss a Gorilla in Plain Sight? | seçici dikkat; oranı kaynaktan al |  |
| 9 | F | Replace Every Plank. Same Ship? | Theseus'un gemisi | ✓ |
| 10 | G | 38 Witnesses Did Nothing? Check the Story | Genovese anlatısının sorunları |  |
| 11 | T | Same Choice, Two Different Answers | çerçeveleme | ✓ |
| 12 | S | Why Your Friends Have More Friends Than You | arkadaşlık paradoksu, küçük ağ çizimi |  |
| 13 | P | The Four-Card Test Most People Miss | Wason: hangi kartı çevirirsin? |  |
| 14 | F | Would You Plug Into a Perfect Dream? | deneyim makinesi (Nozick) | ✓ |
| 15 | G | The Marshmallow Test Isn't What You Heard | aile koşulları devreye girince | ⚠ |
| 16 | T | Five Reds in a Row. Bet Black? | kumarbaz yanılgısı |  |
| 17 | S | Who Ruins a Shared Field? | ortak malların trajedisi ve Ostrom'un karşı örneği |  |
| 18 | D | Would You Take One Dollar or Nothing? | ültimatom oyunu |  |
| 19 | F | Design a World Before You Know Who You'll Be | bilgisizlik peçesi (Rawls) | ✓ |
| 20 | T | Why Can Beginners Feel So Sure? | Dunning-Kruger ve istatistik tartışması | ⚠ |
| 21 | P | Two Prisoners, One Terrible Choice | mahkûm ikilemi, tekrar edince ne değişir? |  |
| 22 | G | The Prison Experiment That Came Apart | Stanford; yöntem eleştirileri | ✓ |
| 23 | S | Six Handshakes to Anyone? Not So Fast | küçük dünya; zincirlerin çoğu tamamlanmadı | ✓ |
| 24 | T | You Remember It. Did It Happen? | yanlış anı (Loftus) |  |
| 25 | F | She Knew Everything About Red. Then She Saw It. | Mary'nin odası (Jackson) | ✓ |
| 26 | P | The Birthday Bet You'd Probably Lose | 23 kişi |  |
| 27 | S | Are Hit Songs Partly Luck? | MusicLab: aynı şarkılar, ayrı dünyalar |  |
| 28 | T | Why Can't You Leave a Bad Movie? | batık maliyet |  |
| 29 | G | Does Willpower Run Out? | ego tükenmesi; büyük tekrar sıfıra yakın buldu | ✓ |
| 30 | F | A Beetle in a Box Nobody Else Can See | Wittgenstein: kelime neyi gösterir? |  |
| 31 | P | You Tested Positive. How Worried Should You Be? | taban oranı, 1000 nokta çizimi |  |
| 32 | S | Your Weakest Friend May Matter Most | zayıf bağlar (Granovetter) | ✓ |
| 33 | T | Guess My Rule: 2, 4, 6 | doğrulama yanlılığı |  |
| 34 | F | Can Achilles Ever Catch the Tortoise? | Zenon |  |
| 35 | G | Sane People in Mental Hospitals? | Rosenhan çalışması ve sahtecilik iddiaları | ⚠ |
| 36 | S | How One Person Starts a Riot | eşik modeli: domino insanlar |  |
| 37 | D | How Far Would You Go If Told To? | Milgram ve arşiv eleştirileri | ⚠ |
| 38 | T | Why Does the Ending Rewrite Everything? | doruk-son kuralı |  |
| 39 | F | Does the Man in the Chinese Room Understand? | Searle; yapay zekâya bağ |  |
| 40 | S | How Can Smart Groups Choose Badly? | grup düşüncesi; kanıtı tartışmalı | ⚠ |
| 41 | P | Which Is More Likely? Most People Slip | Linda problemi |  |
| 42 | D | Ask a Crowd to Weigh an Ox | Galton: kalabalığın tahmini ve ne zaman bozulur |  |
| 43 | F | Two Boxes and a Perfect Predictor | Newcomb |  |
| 44 | G | Do Broken Windows Breed Crime? | teori ve eleştirileri | ⚠ |
| 45 | T | Did Everyone Really Notice? | spot ışığı etkisi |  |
| 46 | S | Why Does Nobody Ask the Question Everyone Has? | çoğulcu bilgisizlik |  |
| 47 | F | If a Machine Copies You, Which One Is You? | ışınlanma bulmacası (Parfit) |  |
| 48 | D | Can More Choice Feel Worse? | reçel deneyi; meta analizler karışık | ⚠ |
| 49 | G | Power Pose: What Survived? | hormon bulgusu tekrar edilemedi | ✓ |
| 50 | F | Was the World Made Five Minutes Ago? | Russell: kanıtlayabilir misin? |  |

Taramada görülen kaynaklar: [çıpalama ve Many Labs](https://www.nature.com/articles/nature.2013.14232), [Asch 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686423/), [küçük dünya](https://en.wikipedia.org/wiki/Small-world_experiment), [zayıf bağlar](https://www.cs.umd.edu/~golbeck/INST633o/granovetterTies.pdf), [düşünce deneyleri](https://bigthink.com/personal-growth/seven-thought-experiments-thatll-make-you-question-everything/), [Stanford](https://bigthink.com/21st-century-spirituality/why-everything-you-know-about-the-stanford-prison-experiment-might-be-wrong), [Rosenhan, Milgram eleştirileri](https://www.popsci.com/textbook-psychology-studies-troubling/), [Dunning-Kruger tartışması](https://bps.org.uk/psychologist/dunning-kruger-effect-and-its-discontents), [tekrar edilemeyen çalışmalar](https://atticusli.com/replication-crisis/) (blog; birincil kaynakla doğrula).

## Kurulum ve deneme
```bash
cd kanal_2
uv venv -p 3.13 && uv pip install -r requirements.txt     # bir kez
.venv/Scripts/python render.py ornek taslak                # -> ornek/onizleme.png
```

## Her videonun sırası (onaysız ilerleme yok)
1. `.claude/skills/hikaye-senaryo` skill'i: konu, akış, senaryo.
2. `kanal_2/NNN-ad/` aç: `ARASTIRMA.md` (her iddiaya kaynak), `sahneler.py` (`TEXT`, `DUYGU`, `SAHNE`, `META`, sahne sınıfları; örnek yapı: `../kanal/002-voyager/sahneler.py`).
3. `python render.py NNN-ad taslak` (geçici ücretsiz ses) -> `python belge.py NNN-ad` -> `onizleme.png` kontrolü, `kapak.py`, `PAKET.md`. **Kullanıcı onayı.**
4. `python eleven.py NNN-ad` (ElevenLabs; ortam değişkenleri) -> `render.py NNN-ad final` -> `belge.py` -> her cümlede ses var mı, senkron, kareler.

İlk iş: **"kanal_2 ile 1. videoya başla"** denince 1 numaralı videodan başla; önce kanal adı ve görünüm örneklerini onaylat.

## Motor
- `tahta.py` (sade tahta), `kalem.py` (defter/gece dokusu, kalemle çizme-yazma, taramalı boyama), `render.py`, `eleven.py` (`eleven_v4`, duygu etiketleri; kullanım kökteki `CLAUDE.md` "Ses ve duygu etiketleri"), `belge.py`.
- Bu dosyalar kanal 1'den kopyalandı; burada serbestçe değiştirebilirsin.
- Görsel tarz kuralları ve tuzaklar: `../STIL_REHBERI.md`. Her video öncekilerden farklı ve daha iyi olsun.
- Kanalın renk, yazı tipi ve sesini ilk videoda kullanıcıya seçtir; kanal 1 ile aynı görünmesin.
