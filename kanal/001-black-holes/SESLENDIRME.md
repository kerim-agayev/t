# Seslendirme metni ve ses değiştirme

Videodaki ses **geçici** (edge-tts, en-US-AndrewNeural). Yayından önce değiştirilecek.

## ElevenLabs ile (evde)
1. Yeni hesapta API anahtarı ve ses kimliği (Voice ID) al. **Anahtarı dosyaya veya commit'e yazma.**
2. `kanal/` içinde (Git Bash):
   ```bash
   uv venv -p 3.13 && uv pip install -r requirements.txt      # bir kez
   export ELEVENLABS_API_KEY=...  ELEVENLABS_VOICE_ID=...
   .venv/Scripts/python eleven.py 001-black-holes              # ses/ dosyalarının üstüne yazar
   .venv/Scripts/python render.py 001-black-holes final        # görüntü yeni sese göre yeniden kurulur
   .venv/Scripts/python 001-black-holes/belge.py               # altyazi.srt ve bölüm zamanları
   ```
3. SENARYO.md sonundaki yeni bölüm zamanlarını PAKET.md açıklamasına kopyala.

Notlar: ElevenLabs ücretsiz plan aylık 10.000 kredi (bu metin yaklaşık 5892 karakter); **ticari lisans Starter planda**
(2026-11-27 fiyat sayfası; para kazanılacaksa Starter al ve sesi o planda üret). Kendi sesin: aynı adlarla `ses/` içine mp3 koy, 3. satırdaki render'ı çalıştır.

## Metin (satır başı = dosya adı)

### Hook
- `Hook_0.mp3` — Here is a black hole. In theory, it could be smaller than an atom.
- `Hook_1.mp3` — And here is another one, so wide that Voyager 1, after almost fifty years of flying, has covered only a fraction of the distance across it.
- `Hook_2.mp3` — Same name. Same physics. Wildly different sizes.
- `Hook_3.mp3` — So how small, and how big, can a black hole actually get? Let's climb the whole ladder.

### What
- `What_0.mp3` — First, what is it? Throw a ball up, and gravity pulls it back. Throw it fast enough, and it escapes.
- `What_1.mp3` — Squeeze enough mass into a small enough space, and the speed you need to escape becomes faster than light.
- `What_2.mp3` — The boundary where that happens is called the event horizon. Nothing that crosses it comes back out.
- `What_3.mp3` — But a black hole is not a cosmic vacuum cleaner. From far away, it pulls like any other object with the same mass.
- `What_4.mp3` — If the Sun were swapped for a black hole of equal mass, Earth would freeze, but it would keep its orbit.

### Rule
- `Rule_0.mp3` — So what decides how big one gets? Mostly its mass. And there is one simple rule.
- `Rule_1.mp3` — For a black hole that is not spinning, every Sun's worth of mass adds about three kilometers to the radius of its event horizon.
- `Rule_2.mp3` — Double the mass, and the horizon becomes twice as wide.
- `Rule_3.mp3` — Now try it with Earth. To become a black hole, our whole planet would have to be squeezed to about the width of a marble.

### Primordial
- `Primordial_0.mp3` — So let's start at the bottom. The smallest rung is also the strangest, because nobody has ever found one.
- `Primordial_1.mp3` — Scientists think black holes might have formed in the first second after the universe began. They are called primordial black holes.
- `Primordial_2.mp3` — In theory, some could weigh far less than a paperclip. Others could outweigh the Sun a hundred thousand times.
- `Primordial_3.mp3` — One with the mass of an asteroid would have a horizon about the size of an atom.
- `Primordial_4.mp3` — Theory also says the very tiniest should slowly evaporate and disappear. So far, all of this is unproven.
- `Primordial_5.mp3` — To reach black holes we have real evidence for, we need a dying star.

### Stellar
- `Stellar_0.mp3` — When a very massive star, around twenty times the Sun's mass or more, runs out of fuel, its core can collapse.
- `Stellar_1.mp3` — What remains is a stellar-mass black hole. The lightest one NASA lists weighs just three point eight Suns. Its horizon would fit across a city.
- `Stellar_2.mp3` — But if a black hole gives off no light, how do we find it? Watch its neighbor.
- `Stellar_3.mp3` — The nearest one we know, Gaia BH1, is about fifteen hundred light-years away. We know it is there because a star keeps circling something unseen.
- `Stellar_4.mp3` — Its larger cousin, Gaia BH3, holds about thirty-three Suns inside a horizon roughly two hundred kilometers wide.
- `Stellar_5.mp3` — Our galaxy may hide as many as one hundred million of these.

### Fall
- `Fall_0.mp3` — But what if you got too close? Imagine falling in, feet first.
- `Fall_1.mp3` — Near a small black hole, gravity pulls your feet much harder than your head.
- `Fall_2.mp3` — You are stretched long and squeezed thin. Scientists really do call it spaghettification.
- `Fall_3.mp3` — And it happens before you even reach the horizon.
- `Fall_4.mp3` — Here is the twist: near a giant black hole, the difference is gentler. You could cross the horizon in one piece.
- `Fall_5.mp3` — You still would not come back. So how do black holes get that big?

### Middle
- `Middle_0.mp3` — Between star-sized black holes and giants, there should be a middle class: from about a hundred to hundreds of thousands of Suns.
- `Middle_1.mp3` — For decades, it was the missing link. Candidates kept appearing, but proof was hard.
- `Middle_2.mp3` — In twenty twenty-three, detectors felt two black holes collide. They merged into one of more than two hundred and twenty-five Suns.
- `Middle_3.mp3` — And inside the star cluster Omega Centauri, Hubble data revealed seven stars moving so fast that something heavy must be holding them.
- `Middle_4.mp3` — That hidden object weighs at least eight thousand two hundred Suns. Its horizon would be almost four Earths wide, or more.
- `Middle_5.mp3` — It is still called a candidate. The next rung is not.

### Center
- `Center_0.mp3` — At the center of our own galaxy, about twenty-seven thousand light-years away, sits Sagittarius A star.
- `Center_1.mp3` — It is a supermassive black hole, weighing about four million Suns.
- `Center_2.mp3` — Astronomers tracked stars whipping around an invisible point for years. That work shared the Nobel Prize in twenty twenty.
- `Center_3.mp3` — Its horizon is about seventeen Suns wide. Big, but it would still fit easily inside the orbit of Mercury.
- `Center_4.mp3` — In twenty twenty-two, the Event Horizon Telescope showed us its glowing ring and dark shadow.
- `Center_5.mp3` — Gas and mergers help such monsters grow, but how they first formed is still a mystery. And this one is small, as giants go.

### M87
- `M87_0.mp3` — Meet M87 star, about fifty-five million light-years away, in another galaxy.
- `M87_1.mp3` — It holds about six and a half billion Suns. In twenty nineteen, it became the first black hole ever imaged.
- `M87_2.mp3` — Now watch the scale change. Here is the Sun, and here is the orbit of Neptune, the farthest planet.
- `M87_3.mp3` — The horizon of M87 star reaches about four times farther than that.
- `M87_4.mp3` — Our entire family of planets would fit inside, with plenty of room to spare.

### Monster
- `Monster_0.mp3` — And still, there are bigger ones. Far away, a blazing quasar called TON 618 is powered by a monster.
- `Monster_1.mp3` — Its mass is hard to measure. Estimates run from about forty billion to sixty-six billion Suns.
- `Monster_2.mp3` — Take the lower number. The horizon's radius is about eight hundred times the distance from Earth to the Sun.
- `Monster_3.mp3` — Remember Voyager 1? In November twenty twenty-six, it reached one light-day from us.
- `Monster_4.mp3` — That is about a hundred and seventy-three Earth-Sun distances, after nearly fifty years.
- `Monster_5.mp3` — Placed at the center of TON 618, it would be only about a fifth of the way to the edge.

### Ladder
- `Ladder_0.mp3` — Now put every rung on one board.
- `Ladder_1.mp3` — An atom-sized primordial black hole, if it exists.
- `Ladder_2.mp3` — A city-sized one, born from a dead star.
- `Ladder_3.mp3` — A candidate wider than several Earths, hiding in a star cluster.
- `Ladder_4.mp3` — A giant that fits inside Mercury's orbit. One that swallows the planets. And a monster that makes our farthest probe look close to home.

### End
- `End_0.mp3` — So how small can a black hole be? In theory, smaller than an atom. In evidence, a few times the mass of the Sun.
- `End_1.mp3` — And how big? Tens of billions of Suns, as far as we can tell today.
- `End_2.mp3` — Which one surprised you most: the one nobody has found, or the one we can barely fit on the board? Tell me in the comments.
- `End_3.mp3` — Next time: that tiny probe. How far has humanity actually reached?
