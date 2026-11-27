(() => {
// Karakter seti + sahneler. Çizim motoru: ../skill/scripts/engine.html (MIT, whiteboard-video-skill)
const SKIN = '#ffdfc4', BROWN = '#8a5530', DARK = '#33302e', PINK = '#f2a0a8', YEL = '#ffd86b', SKY = '#a9d8f5', MINT = '#bfe6b0', LILAC = '#d8c3f2';

// op = [ağırlık, (at, dur) => çiz]
const p = (d, o = {}, w = 1) => [w, (at, dur) => P(d, at, dur, o)];
const fl = (d, fill, o = {}, w = 1) => p(d, { fill, fillOp: 1, w: 5, ...o }, w);
const t = (s, x, y, size = 60, c, o = {}) => [.5 + s.length * .07, (at, dur) => T(s, x, y, size, at, dur, c ? { c, ...o } : o)];

// satır li boyunca ops listesini sırayla çiz
function say(A, li, ...ops) {
  const flat = a => typeof a[0] === 'number' ? [a] : a.flatMap(flat);
  ops = ops.flatMap(flat);
  const total = ops.reduce((s, o) => s + o[0], 0);
  let x = .02;
  for (const [w, fn] of ops) {
    const fr = w / total * .9, at = A(li, x);
    fn(at, Math.max(.08, A(li, x + fr) - at));
    x += fr;
  }
}

const title = s => [t(s, 960, 135, 96), p(wave(960 - s.length * 20, 960 + s.length * 20, 168, 6), { c: GOLD, w: 9 }, .6)];

// karakter: (x, y) = baş merkezi
function person(x, y, o = {}) {
  const { s = 1, shirt = SKY, hair = BROWN, long = false, mood = 'happy', glasses = false, hat = false } = o;
  const X = v => x + v * s, Y = v => y + v * s, ops = [];
  if (long) ops.push(fl(`M ${X(-70)} ${Y(-25)} Q ${X(-125)} ${Y(110)} ${X(-70)} ${Y(135)} Q ${X(0)} ${Y(80)} ${X(70)} ${Y(135)} Q ${X(125)} ${Y(110)} ${X(70)} ${Y(-25)} Z`, hair, {}, .8));
  ops.push(fl(`M ${X(-88)} ${Y(215)} Q ${X(-92)} ${Y(72)} ${X(0)} ${Y(68)} Q ${X(92)} ${Y(72)} ${X(88)} ${Y(215)} Z`, shirt));
  ops.push(fl(circ(x, y, 68 * s, 70 * s), SKIN));
  ops.push(fl(`M ${X(-70)} ${Y(6)} Q ${X(-84)} ${Y(-98)} ${X(0)} ${Y(-86)} Q ${X(86)} ${Y(-94)} ${X(70)} ${Y(6)} Q ${X(44)} ${Y(-50)} ${X(8)} ${Y(-46)} Q ${X(-24)} ${Y(-8)} ${X(-70)} ${Y(6)} Z`, hair, {}, .8));
  ops.push(fl(circ(X(-24), Y(2), 5 * s) , DARK, {}, .25), fl(circ(X(24), Y(2), 5 * s), DARK, {}, .25));
  if (glasses) ops.push(p(circ(X(-24), Y(2), 20 * s) + circ(X(24), Y(2), 20 * s) + line(X(-5), Y(0), X(5), Y(0), 0), { w: 4 }, .5));
  if (mood === 'sad') ops.push(p(line(X(-38), Y(-14), X(-12), Y(-26), 1) + line(X(12), Y(-26), X(38), Y(-14), 1), { w: 4 }, .3));
  if (mood === 'angry') ops.push(p(line(X(-38), Y(-26), X(-12), Y(-14), 1) + line(X(12), Y(-14), X(38), Y(-26), 1), { w: 5 }, .3));
  const mouth = { happy: `M ${X(-22)} ${Y(28)} Q ${X(0)} ${Y(54)} ${X(22)} ${Y(28)}`, sad: `M ${X(-20)} ${Y(44)} Q ${X(0)} ${Y(24)} ${X(20)} ${Y(44)}`,
    angry: line(X(-18), Y(38), X(18), Y(36), 1), shock: circ(x, Y(38), 12 * s, 15 * s), flat: line(X(-16), Y(36), X(16), Y(36), 1) }[mood];
  ops.push(p(mouth, { w: 5 }, .4));
  if (hat) ops.push(fl(rect(X(-62), Y(-116), 124 * s, 46 * s), DARK, {}, .5));
  return ops;
}
const baby = (x, y) => [fl(`M ${x - 70} ${y + 20} Q ${x} ${y + 190} ${x + 70} ${y + 20} Z`, YEL), fl(circ(x, y, 52), SKIN),
  p(`M ${x - 22} ${y - 4} q 8 -10 16 0 M ${x + 6} ${y - 4} q 8 -10 16 0 M ${x - 12} ${y + 20} q 12 14 24 0 M ${x} ${y - 52} q 22 -30 30 -4`, { w: 4 }, .6)];
function dna(x, y, h = 340, c1 = BLUE, c2 = RED, w = 55) {
  let a = '', b = '', r = '';
  for (let i = 0; i <= 40; i++) {
    const u = i / 40, s = Math.sin(u * Math.PI * 3) * w, yy = y + u * h;
    a += `${i ? 'L' : 'M'} ${x + s} ${yy} `; b += `${i ? 'L' : 'M'} ${x - s} ${yy} `;
    if (i % 4 === 2) r += line(x + s, yy, x - s, yy, 0);
  }
  return [p(a, { c: c1, w: 8 }), p(b, { c: c2, w: 8 }), p(r, { c: GRAY, w: 4 }, .6)];
}
const paper = (x, y, w = 320, h = 400) => [fl(rect(x, y, w, h), '#ffffff'),
  p([1, 2, 3, 4].map(i => line(x + 35, y + 60 + i * 42, x + w - 35, y + 60 + i * 42, 2)).join(''), { c: GRAY, w: 4 }, .5)];
const tube = (x, y, c) => [fl(`M ${x - 28} ${y} L ${x - 28} ${y + 150} Q ${x} ${y + 195} ${x + 28} ${y + 150} L ${x + 28} ${y} Z`, '#ffffff'),
  fl(`M ${x - 22} ${y + 80} L ${x - 22} ${y + 148} Q ${x} ${y + 182} ${x + 22} ${y + 148} L ${x + 22} ${y + 80} Z`, c, { w: 3 }, .5), p(line(x - 40, y, x + 40, y, 1), {}, .3)];
const cell = (x, y, r, c) => [fl(circ(x, y, r), c), fl(circ(x + r * .2, y - r * .15, r * .28), '#ffffff', { w: 4 }, .4)];
const yes = (x, y, r = 46) => p(icon.tick(x, y, r), { c: GREEN, w: 10 });
const no = (x, y, r = 46) => p(icon.cross(x, y, r), { c: RED, w: 10 });
const arr = (x1, y1, x2, y2, c = GOLD) => p(arrow(x1, y1, x2, y2), { c, w: 9 }, .6);
const q = (x, y, size = 190, c = RED) => t('?', x, y, size, c);
const lydia = (x, y, mood = 'happy', s = 1) => person(x, y, { long: true, shirt: PINK, hair: '#c98a3d', mood, s });

window.SCENES = {
  kapak(A) {
    say(A, 0, lydia(960, 520, 'happy', 1.35), person(640, 650, { s: .8, shirt: MINT }), person(1280, 650, { s: .8, shirt: YEL, long: true }));
    say(A, 1, dna(260, 330, 440), paper(1500, 330, 300, 380), no(1650, 640, 55), t('anne değil?', 1650, 800, 66, RED));
    say(A, 2, title('Lydia Fairchild Vakası'), t("DNA'nın çözemediği kadın", 960, 250, 66, BLUE));
  },
  baslangic(A) {
    say(A, 0, title('2002, Washington'), p(poly([[190, 330], [560, 300], [600, 560], [330, 590], [220, 500]], true), { c: GREEN }), fl(circ(420, 430, 16), RED), t('Washington', 395, 660, 62));
    say(A, 1, lydia(960, 430), fl(circ(960, 590, 58, 50), PINK), t('Lydia', 960, 760, 66), person(780, 560, { s: .7, shirt: MINT }), person(1140, 560, { s: .7, shirt: YEL }));
    say(A, 2, person(1620, 430, { shirt: SKY, hair: DARK, mood: 'flat' }), t('Jamie', 1620, 760, 66), p(poly([[1340, 330], [1310, 440], [1370, 480], [1320, 620]]), { c: RED, w: 9 }));
    say(A, 3, paper(1250, 640, 190, 230), t('başvuru', 1345, 705, 44, BLUE));
  },
  test(A) {
    say(A, 0, title('Sıradan bir işlem'), paper(180, 300, 380, 470), t('DNA TESTİ', 370, 380, 62, BLUE), yes(370, 690));
    say(A, 1, tube(850, 380, SKY), t('baba', 850, 650, 58), tube(1100, 380, PINK), t('anne', 1100, 650, 58), tube(1350, 380, MINT), t('çocuklar', 1350, 650, 58));
    say(A, 2, person(1670, 440, { shirt: LILAC, glasses: true }), t('"Sadece formalite"', 1150, 820, 70));
  },
  sonuc(A) {
    say(A, 0, title('Sonuç raporu'), person(430, 470, { hair: DARK }), t('Baba: Jamie', 430, 800, 66), yes(640, 340, 60));
    say(A, 1, lydia(1450, 470, 'shock'), t('Anne: ?', 1450, 800, 66), no(1660, 340, 60));
    say(A, 2, paper(790, 300, 340, 440), t('ANNELİK', 960, 400, 58, RED), t('EŞLEŞMEDİ', 960, 640, 60, RED), q(960, 880, 110));
  },
  dna(A) {
    say(A, 0, title('Test nasıl çalışır?'), dna(300, 280, 400, RED, PINK), t('anne', 300, 760, 62, RED), dna(1620, 280, 400, BLUE, SKY), t('baba', 1620, 760, 62, BLUE),
      arr(420, 480, 800, 480, RED), arr(1500, 480, 1120, 480, BLUE), dna(960, 280, 400, RED, BLUE), t('çocuk: yarı + yarı', 960, 760, 62));
    say(A, 1, p(rect(850, 340, 220, 70), { c: GOLD, w: 9 }), p(rect(850, 540, 220, 70), { c: GOLD, w: 9 }), t('işaretler', 1230, 360, 54, GOLD));
    say(A, 2, t('çocuk ↔ anne: yarısı ortak olmalı', 960, 850, 58, GREEN));
    say(A, 3, no(560, 380, 70));
  },
  suclama(A) {
    say(A, 0, title('"DNA yalan söylemez"'), dna(330, 300, 440), yes(480, 330, 52));
    say(A, 1, lydia(960, 480, 'sad'), arr(560, 520, 790, 520, RED), t('yalancı?', 960, 800, 72, RED));
    say(A, 2, person(1500, 450, { shirt: '#c9c9cf', hair: DARK, mood: 'angry', glasses: true }), t('dolandırıcılık', 1500, 760, 66, RED), t('taşıyıcı annelik?', 1500, 845, 58));
    say(A, 3, paper(630, 700, 150, 170), q(705, 830, 100));
  },
  tehdit(A) {
    say(A, 0, title('Çocuklar tehlikede'), fl(circ(300, 420, 90), YEL), t('$', 300, 460, 120), no(300, 420, 120));
    say(A, 1, lydia(880, 420, 'sad'), person(660, 600, { s: .65, shirt: MINT, mood: 'sad' }), person(1100, 600, { s: .65, shirt: YEL, mood: 'sad' }),
      arr(1180, 560, 1420, 450, RED), person(1580, 430, { shirt: '#c9c9cf', hair: DARK, mood: 'flat', hat: true }), t('savcılık', 1580, 740, 62));
    say(A, 2, paper(220, 580, 240, 270), t('SONUÇ', 340, 660, 54, RED), no(340, 780, 38));
  },
  dogum(A) {
    say(A, 0, title('Yargıcın kararı'), person(350, 480, { shirt: DARK, hair: '#bbbbbb', glasses: true, mood: 'flat' }), fl(rect(160, 690, 380, 90), '#c89a6b'),
      p(line(560, 400, 660, 300, 1), { c: BROWN, w: 16 }), fl(rect(620, 250, 120, 70), BROWN), t('yargıç', 350, 860, 60));
    say(A, 1, person(960, 460, { shirt: LILAC, glasses: true, mood: 'flat' }), p(circ(1080, 520, 45) + line(1112, 555, 1160, 610, 1), { w: 10 }), t('gözlemci', 960, 780, 60));
    say(A, 2, baby(1520, 400), tube(1400, 620, RED), tube(1650, 620, RED));
    say(A, 3, t('hile ihtimali: sıfır', 1140, 880, 66, GREEN), yes(760, 860, 38));
  },
  soku(A) {
    say(A, 0, title('İki hafta sonra'), p(icon.clock(260, 400, 110), { c: BLUE }), t('14 gün', 260, 600, 66, BLUE));
    say(A, 1, lydia(780, 440, 'shock'), baby(1180, 520), no(980, 360, 70), t('yine eşleşme yok', 980, 780, 72, RED));
    say(A, 2, person(1620, 440, { shirt: LILAC, glasses: true, mood: 'shock' }), t('doğumu gördüm!', 1620, 740, 56), dna(1440, 250, 240, BLUE, RED, 32));
    say(A, 3, q(300, 840, 130), t('belki yanlış olan varsayım', 1030, 870, 66));
  },
  avukat(A) {
    say(A, 0, title('Dönüm noktası'), person(300, 450, { shirt: '#6c86c9', hair: DARK, glasses: true }), t('Alan Tindell', 300, 760, 64));
    say(A, 1, fl(circ(420, 270, 48), YEL), p(line(420, 195, 420, 170, 0) + line(485, 220, 505, 200, 0) + line(500, 275, 530, 278, 0), { c: GOLD }), arr(520, 480, 760, 480),
      person(960, 450, { long: true, shirt: MINT, hair: '#5a4034' }), t('Karen Keegan, Boston', 960, 760, 60));
    say(A, 2, person(1180, 580, { s: .6, shirt: SKY }), no(1180, 360, 48));
    say(A, 3, paper(1420, 290, 360, 430), t('tıp dergisi', 1600, 375, 60, BLUE), t('KİMERİZM', 960, 885, 96, RED), p(rect(740, 795, 440, 115), { c: GOLD, w: 8 }));
  },
  kimera(A) {
    say(A, 0, title('Kimera nedir?'), cell(190, 330, 62, SKY), cell(300, 360, 62, PINK), t('iki DNA, tek beden', 330, 480, 54));
    say(A, 1, cell(760, 380, 75, SKY), cell(760, 650, 75, PINK), t('ikiz 1', 600, 400, 56, BLUE), t('ikiz 2', 600, 670, 56, RED));
    say(A, 2, arr(870, 400, 1040, 490), arr(870, 630, 1040, 540), fl(circ(1180, 515, 125), LILAC), fl(circ(1135, 475, 50), SKY), fl(circ(1230, 560, 50), PINK), t('birleşme', 1180, 720, 64));
    say(A, 3, arr(1340, 515, 1480, 515), baby(1630, 450), fl(circ(1600, 575, 16), SKY, { w: 3 }, .3), fl(circ(1660, 590, 16), PINK, { w: 3 }, .3), t('tek bebek', 1630, 760, 64));
  },
  gizli(A) {
    say(A, 0, title('Görünmeyen iki kimlik'), lydia(960, 400, 'happy', 1.2), fl(rect(760, 640, 400, 230), PINK), t('belirti yok', 340, 480, 72), yes(340, 600));
    say(A, 1, cell(850, 730, 48, SKY), cell(1070, 790, 48, LILAC), arr(1160, 780, 1450, 700, LILAC), t('doku A', 1580, 700, 62, '#7a55b8'), arr(760, 720, 560, 760, BLUE), t('doku B', 430, 790, 62, BLUE));
    say(A, 2, tube(1620, 290, RED), t('tek örnek ≠ tüm beden', 1520, 880, 60, RED));
  },
  kanit(A) {
    say(A, 0, title('Yeni örnekler'), person(280, 400, { long: true, hair: '#c9c9c9', shirt: LILAC, glasses: true }), t('büyükanne', 280, 700, 62));
    say(A, 1, arr(420, 450, 640, 450, GREEN), person(760, 430, { s: .8, shirt: MINT }), yes(540, 330, 50), t('uyuşuyor', 540, 560, 54, GREEN));
    say(A, 2, tube(1120, 340, SKIN), tube(1260, 340, BROWN), t('deri, saç', 1190, 620, 62), no(1190, 760, 52));
    say(A, 3, tube(1640, 340, PINK), t('sürüntü', 1640, 620, 62), yes(1640, 760, 52), t('eşleşti!', 1640, 880, 72, GREEN));
  },
  karar(A) {
    say(A, 0, title('Gerçek ortaya çıktı'), lydia(960, 420, 'happy', 1.2), dna(560, 280, 400, BLUE, SKY), dna(1360, 280, 400, RED, PINK));
    say(A, 1, person(720, 620, { s: .65, shirt: MINT }), person(1200, 620, { s: .65, shirt: YEL }), baby(960, 700));
    say(A, 2, p(circ(290, 480, 130), { c: GREEN, w: 14 }), p(poly([[220, 485], [272, 540], [370, 420]]), { c: GREEN, w: 20 }), t('suçlamalar', 1650, 470, 66, GREEN), t('düştü', 1650, 560, 80, GREEN));
  },
  ders(A) {
    say(A, 0, title('Bu vaka ne öğretiyor?'), tube(380, 340, RED), yes(540, 400), t('test örneği doğru okudu', 480, 660, 58, GREEN));
    say(A, 1, lydia(1420, 410, 'flat'), p(rect(1180, 250, 140, 140), { c: RED, w: 8 }), t('tek örnek = bütün insan?', 1420, 740, 58, RED), no(1700, 330, 52));
    say(A, 2, fl(rect(430, 780, 1060, 120), '#fff1b8'), t('güçlü kanıt + doğru soru', 960, 862, 74));
  },
  son(A) {
    say(A, 0, title('Peki ya sen?'), person(960, 460, { shirt: SKY, mood: 'shock', s: 1.3 }), dna(520, 290, 460), dna(1400, 290, 460, GRAY, LILAC));
    say(A, 1, p(icon.bubble(300, 440, 280, 180), { c: BLUE, w: 9 }), q(300, 485, 130, BLUE), t('yorumlara yaz!', 960, 870, 84, RED), p(icon.bubble(1650, 440, 240, 160), { c: GOLD, w: 9 }));
  },
};

})();
