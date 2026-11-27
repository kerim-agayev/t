"""script -> script.json + ses dosyaları (edge-tts, ücretsiz). Sonra: skill/scripts/make_audio.py ve render.js
Kendi sesin için: audio/<sahne>_<satır>.mp3 dosyalarının üzerine kaydını koy, make_audio.py'yi tekrar çalıştır."""
import asyncio, json
from pathlib import Path

import edge_tts

SCRIPT = {
 "kapak": [
  "Bir anne düşünün. Çocuklarını kendisi doğurdu, onları kendisi büyüttü.",
  "Ama bir gün, DNA testi ona şunu söyledi: Bu çocukların annesi sen değilsin.",
  "Bu, Lydia Fairchild vakası. Bilimin en güvendiği kanıtın yanıldığı sanılan an."],
 "baslangic": [
  "Yıl iki bin iki. Amerika'nın Washington eyaleti.",
  "Lydia Fairchild, iki çocuk annesiydi ve üçüncü çocuğuna hamileydi.",
  "Çocuklarının babası Jamie Townsend ile ayrılmışlardı.",
  "Lydia, nafaka işlemleri ve devlet desteği için başvurdu."],
 "test": [
  "Bu başvuruda babalığı kanıtlamak için DNA testi istemek, sıradan bir işlemdi.",
  "Anne, baba ve çocuklardan örnek alındı.",
  "Herkes bunun yalnızca bir formalite olduğunu düşünüyordu."],
 "sonuc": [
  "Sonuçlar geldiğinde, babalık tarafında sürpriz yoktu. Jamie gerçekten babaydı.",
  "Fakat annelik tarafı, tam tersini söylüyordu.",
  "Rapora göre Lydia, kendi çocuklarının genetik annesi olamazdı."],
 "dna": [
  "Peki bu test nasıl çalışır? Her çocuk, DNA'sının yarısını annesinden, yarısını babasından alır.",
  "Laboratuvar, DNA üzerindeki belirli bölgeleri karşılaştırır.",
  "Çocuktaki işaretlerin yarısı annede de bulunmalıdır.",
  "Lydia'nın örneklerinde ise bu eşleşme yoktu."],
 "suclama": [
  "Yetkililerin gözünde DNA yalan söylemezdi.",
  "O halde Lydia yalan söylüyor olmalıydı.",
  "Dolandırıcılıkla suçlandı. Ya başkasının çocukları için yardım alıyordu, ya da gizli bir taşıyıcı annelik düzeni vardı.",
  "Geçmiş doğum kayıtları bile şüpheyle karşılandı."],
 "tehdit": [
  "İş yalnızca para meselesi değildi.",
  "Savcılık, çocukların ondan alınmasını istiyordu.",
  "Lydia ne kadar anlatırsa anlatsın, karşısında tek bir kâğıt vardı: test sonucu."],
 "dogum": [
  "Üçüncü çocuğun doğumu yaklaşırken, yargıç alışılmadık bir karar verdi.",
  "Doğumda resmî bir gözlemci bulunacaktı.",
  "Bebekten ve anneden kan örnekleri hemen, gözlemcinin önünde alınacaktı.",
  "Artık hiçbir hile ihtimali kalmayacaktı."],
 "soku": [
  "İki hafta sonra sonuç geldi.",
  "Test, Lydia'nın az önce doğurduğu bebeğin de annesi olmadığını gösteriyordu.",
  "Gözlemcinin gördüğü bir doğum vardı. Ama DNA, başka bir şey söylüyordu.",
  "Demek ki sorun Lydia'da değil, varsayımda olabilirdi."],
 "avukat": [
  "Dönüm noktası, avukatı Alan Tindell ile geldi.",
  "Tindell, Boston'da yaşayan Karen Keegan adlı bir kadının hikâyesini öğrendi.",
  "Keegan'ın testlerinde de kendi oğullarıyla genetik bir uyuşmazlık çıkmıştı.",
  "Bu vaka, saygın bir tıp dergisinde yayımlanmıştı. Açıklaması tek bir kelimeydi: kimerizm."],
 "kimera": [
  "Kimera, vücudunda iki farklı DNA'ya sahip hücreler taşıyan kişi demektir.",
  "Bunun yollarından biri anne karnında yaşanır. İki ayrı yumurta döllenir ve iki ikiz embriyo oluşur.",
  "Gelişimin çok erken döneminde bu iki embriyo birleşebilir.",
  "Sonuçta tek bir bebek doğar. Ama bedeninde iki farklı hücre topluluğu yaşar."],
 "gizli": [
  "Bu kişiler çoğu zaman hiçbir şey fark etmez.",
  "Bir organ bir DNA'yı, başka bir doku diğer DNA'yı taşıyabilir.",
  "Yani kandan ya da yanaktan alınan örnek, bütün bedeni temsil etmeyebilir."],
 "kanit": [
  "Araştırmacılar bu kez ailenin diğer üyelerinden de örnek aldı.",
  "Lydia'nın annesinin DNA'sı, çocuklarla tam bir büyükanneden beklendiği ölçüde uyuşuyordu.",
  "Lydia'nın deri ve saç örnekleri çocuklarla eşleşmiyordu.",
  "Ama rahim ağzından alınan sürüntüdeki DNA, çocuklarla eşleşti."],
 "karar": [
  "Böylece tablo netleşti. Lydia iki farklı DNA taşıyordu.",
  "Çocukların genetik mirası, onun bedeninde baştan beri oradaydı.",
  "Suçlamalar düştü. Lydia, çocuklarının annesi olduğunu kanıtlamıştı."],
 "ders": [
  "Bu vaka DNA testlerinin işe yaramadığını göstermez. Test, aldığı örneği doğru okumuştu.",
  "Yanlış olan, tek bir örneğin bütün insanı anlattığı varsayımıydı.",
  "Güçlü bir kanıt bile, doğru soruyla birlikte değerlendirilmelidir."],
 "son": [
  "Kim bilir, belki sizin de bedeninizde sessizce yaşayan ikinci bir DNA vardır.",
  "Sizce mahkemeler DNA kanıtına ne kadar güvenmeli? Yorumlarda buluşalım."],
}


async def main():
    here = Path(__file__).parent
    (here / "audio").mkdir(exist_ok=True)
    (here / "script.json").write_text(json.dumps(
        [{"id": k, "lines": [{"t": t} for t in v]} for k, v in SCRIPT.items()], ensure_ascii=False, indent=1), encoding="utf-8")
    (here / "config.json").write_text(json.dumps({"name": "lydia_fairchild", "fps": 24, "captionSize": 40}), encoding="utf-8")
    (here / "voice.json").write_text(json.dumps({"engine": "files", "trim": True}), encoding="utf-8")
    for sid, lines in SCRIPT.items():
        for i, text in enumerate(lines):
            f = here / "audio" / f"{sid}_{i}.mp3"
            if not f.exists():
                await edge_tts.Communicate(text, "tr-TR-AhmetNeural", rate="-6%").save(str(f))
    print(sum(len(t) for v in SCRIPT.values() for t in v), "karakter")


asyncio.run(main())
