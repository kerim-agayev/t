# 3D karakter videoları: nasıl yapıldı (2026-11-27)

## Kısaca
VRoid Studio ve MCP **kullanılmadı**. Karakterler tarayıcıda three.js ile çizildi, headless Edge karelerini ffmpeg birleştirdi.

## Kurulum (evdeki bilgisayar)
Gerekenler: Node, Python (`trigonometri/.venv`, bkz. CLAUDE.md), ffmpeg (PATH'te), Edge.

```bash
cd vroid
npm ci                      # three 0.180, @pixiv/three-vrm 3.6.0, puppeteer-core
mkdir -p models && cd models
for f in stable/AvatarSample_A stable/AvatarSample_B stable/AvatarSample_C beta/Sendagaya_Shino beta/Sendagaya_Shibu; do
  curl -sSfL -o "$(basename $f).vrm" "https://raw.githubusercontent.com/madjin/vrm-samples/master/vroid/$f.vrm"
done
```
Edge başka yerdeyse `CHROME_PATH` ayarla. `models/` depoya konmaz.

## Komutlar
| İş | Komut (`vroid/` içinde) |
|---|---|
| Karakter seçme sayfası | `node render.js` -> `karakterler.png` |
| Seslendirme ve zaman çizelgesi | `cd erteleme` sonra `../../trigonometri/.venv/Scripts/python ses.py` (`PYTHONIOENCODING=utf-8`) |
| Sahne başına 3 örnek kare | `node render.js erteleme taslak` -> `erteleme/kare/` |
| Final video | `node render.js erteleme` -> `erteleme/erteleme.mp4` |
| Mino önizlemesi | `node render.js mino kare` -> `mino/onizleme.png` |

## Dosyalar
| Dosya | İş |
|---|---|
| `render.js` | Küçük yerel sunucu + puppeteer: sahne açar, `window.kare(t)` çağırır, JPEG kareleri ffmpeg'e aktarır |
| `sahne.html` | 5 hazır VRM modelini yan yana çizer |
| `erteleme/SENARYO.md` | Konu, akış, senaryo, seslendirme metni, kaynaklar (`hikaye-senaryo` skill'iyle) |
| `erteleme/ses.py` | Metni cümlelere böler, edge-tts ile seslendirir, `ses.wav` + `zaman.json` (cümle zamanları, ağız açıklığı) |
| `erteleme/sahne.html` | Oda, eşyalar, 7 sahnenin pozu, yüzü, kartları, kamerası, altyazı |
| `erteleme/erteleme_web.mp4` | Depo için sıkıştırılmış video (2:58) |
| `mino/mino.js` | Tamamen kodla kurulan özgün chibi karakter |
| `mino/sahne.html` | Mino'nun 3 ifadeli önizlemesi |

## Teknikler
### Hazır VRM karakter (erteleme videosu)
- Model: `Sendagaya_Shibu.vrm`, dosya içindeki lisans bilgisi CC0. A, B, C modelleri ticari kullanıma açık ama [VRoid örnek model şartlarına](https://vroid.pixiv.help/hc/en-us/articles/4402394424089) bağlı.
- `VRMUtils.rotateVRM0(vrm)`; poz `getNormalizedBoneNode(...).rotation` ile. VRM0'da kol indirme: sol `z=+1.25`, sağ `z=-1.25`. Oturma: üst bacak `x=+1.5`, alt bacak `x=-1.5`.
- Poz ham kemiklere ancak `vrm.humanoid.update()` ile geçer; eldeki eşyayı bundan sonra yerleştir.
- İfadeler `expressionManager`: happy, sad, relaxed, surprised, blink, aa. Gülen yüzde göz kırpma kapatılır.
- Ağız yalnız karakterin kendi repliğinde, ses genliğine göre oynar; anlatıcıda kapalı.
- Saç ve etek fiziği için kareler sırayla işlenir; sahne başında 90 adım ön ısıtma.
- Anlar saniyeyle değil cümleyle bağlanır: `bas("cümlenin bir parçası")`. Metin değişirse bu parçaları da güncelle.
- İkinci kişi ("yarınki Elif"): aynı modelin ikinci kopyası, MToon renkleri maviye çarpılır.
- Ses: `tr-TR-EmelNeural`; anlatıcı, Elif ve yarınki Elif hız ve perdeyle ayrılır. Servis ara sıra boş döndüğü için 6 deneme var. Cümle metni değişirse `ses/<sahne>_<sıra>.mp3` dosyalarını sil.

### Kodla özgün karakter (Mino)
- Küre, kapsül, lathe ve tube geometrileri; `MeshToonMaterial` + 3 kademeli gradyan; kontur için normal yönünde şişirilmiş arka yüz.
- Yüz, baş küresinin dokusuna `canvas` ile çizilir: `yuz({goz, agiz, kas, kapali, ses, bakis})`.
- Eklemler: baş, iki kol, iki bacak grubu. Dirsek ve diz yok.
- Durum: yalnız önizleme yapıldı; 30 saniyelik video onay bekliyor.

## MCP ve eklentiler
| Araç | Durum |
|---|---|
| VRoid MCP | **Kurulmadı.** Araştırıldı; hepsi gayriresmî |
| Blender MCP | Bu bilgisayarda Blender 5.1'de `mcp` eklentisi klasörü görüldü; Claude'a bağlı değildi, kullanılmadı |
| Unity MCP | Tanımlı, araçları yüklenemedi; kullanılmadı |
| Figma | **Kullanılmayacak** (kullanıcının açık talimatı) |
| Skill | Yalnız depodaki `hikaye-senaryo` akışı izlendi |

VRoid MCP araştırması (README'lerden; denenmedi, kurulu VRoid sürümü 2.17.0):
| Proje | Yöntem | Sürüm |
|---|---|---|
| [mcjo79/vroid-mcp](https://github.com/mcjo79/vroid-mcp) | VRoid içine BepInEx eklentisi, kurulum dosyası | 2.16'dan söz ediyor, 2.17 belirsiz |
| [brainrom/vroid-studio-mcp](https://github.com/brainrom/vroid-studio-mcp) | BepInEx eklentisi | 2.14.0 |
| [Karylcode/VRoid-MCP](https://github.com/Karylcode/VRoid-MCP) | Frida | yalnız 2.14.0 |
| [Topogamer0/vroid-mcp](https://github.com/Topogamer0/vroid-mcp) | ekran okuma + fare ve klavye | 2.14.0 |
| [JAmadoD/vroid-files-mcp](https://github.com/JAmadoD/vroid-files-mcp) | `.vroid` dosyasını düzenler | 2.14'e göre |

MCP'ler karakter düzenler ve dışa aktarır; animasyon veya video üretmez. Kurmadan önce kodu incele.
Blender yolu (denenmedi): [VRM Add-on for Blender](https://github.com/saturday06/VRM-Addon-for-Blender), Blender 4.2-5.x ve Python API.

## Bilinen sınırlar
- Hareket elle yazılan pozlardan oluşuyor; doğal hareket için VRMA dosyaları denenebilir (şartlarını kontrol et).
- Erteleme videosu baştan sona izlenip dinlenmedi; sondaki telefon altyazının arkasında kalıyor.
- Kaynaklar yalnız arama özetlerinden okundu; edge-tts ticari kullanım şartları kontrol edilmeli.
