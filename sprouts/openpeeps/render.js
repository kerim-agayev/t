// Open Peeps (CC0 çizimler, react-peeps MIT paketi) -> sahne.html. Çalıştır: node render.js
const React = require('react');
const { renderToStaticMarkup } = require('react-dom/server');
const Peep = require('react-peeps').default;
const fs = require('fs');

// (x, y, w, h) kutusuna sığdırılacak karakter; yerleşim ve kıyafet rengi sayfada ayarlanır
const SKIN = '#fffffe';
const peep = (x, y, w, h, body, face, hair, o = {}) => {
  const svg = renderToStaticMarkup(React.createElement(Peep, {
    body, face, hair, accessory: o.acc || 'None', facialHair: o.beard || 'None',
    strokeColor: '#17110d', backgroundColor: SKIN, viewBox: { x: '0', y: '0', width: '1', height: '1' },
  }));
  const inner = svg.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
  return `<g class="peep" data-box="${x} ${y} ${w} ${h}" data-flip="${o.flip ? 1 : 0}" data-skin="${o.skin}" data-shirt="${o.shirt}">${inner}</g>`;
};
const title = (s) => `<text x="800" y="128" text-anchor="middle" font-size="100" fill="#17110d">${s}</text>`;
const bubble = (x, y, w, s) => `<g><rect x="${x - w / 2}" y="${y - 50}" width="${w}" height="96" rx="46" fill="#fff" stroke="#17110d" stroke-width="7"/><text x="${x}" y="${y + 14}" text-anchor="middle" font-size="44">${s}</text></g>`;

const scene = `
  ${title('BATIK MALİYET TUZAĞI')}
  <path d="M60 842Q800 815 1545 848" fill="none" stroke="#17110d" stroke-width="7"/>
  ${peep(90, 300, 420, 545, 'PointingFingerWB', 'Explaining', 'ShortMessy', { skin: '#f6c6a0', shirt: '#ff9d3b' })}
  ${peep(590, 300, 400, 545, 'ShirtPantsBW', 'Concerned', 'LongCurly', { skin: '#d89a70', shirt: '#5fcbd8', acc: 'GlassRound' })}
  ${peep(1090, 300, 420, 545, 'CrossedArmsBW', 'Suspicious', 'GrayShort', { skin: '#ffd9bd', shirt: '#a8d672', beard: 'MoustacheThin', flip: true })}
  ${bubble(420, 235, 430, '250 TL verdim!')}
  ${bubble(1150, 235, 350, 'Eee, sonra?')}`;

// sayfada çalışır
function fit() {
for (const g of document.querySelectorAll('.peep')) {
  const [x, y, w, h] = g.dataset.box.split(' ').map(Number), body = g.querySelector('g > g > g');
  for (const e of g.querySelectorAll('[fill="#fffffe"]')) {
    const b = e.getBBox(); e.setAttribute('fill', body.contains(e) && b.width * b.height > 110000 ? g.dataset.shirt : g.dataset.skin);
  }
  const b = g.getBBox(), k = Math.min(w / b.width, h / b.height), f = g.dataset.flip === '1' ? -1 : 1;
  g.setAttribute('transform', `translate(${x + w / 2} ${y + h}) scale(${f * k} ${k}) translate(${-b.x - b.width / 2} ${-b.y - b.height})`);
}
}

fs.writeFileSync(__dirname + '/sahne.html', `<!doctype html><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Lilita+One&display=swap" rel="stylesheet">
<style>body{margin:0}body>svg{width:100vw;height:100vh;display:block;font-family:"Lilita One",sans-serif}</style>
<svg viewBox="0 0 1600 900"><radialGradient id="p" r=".75"><stop offset="0" stop-color="#fffdf6"/><stop offset="1" stop-color="#e3c99c"/></radialGradient>
<rect width="1600" height="900" fill="url(#p)"/>${scene}</svg>
<script>(${fit})()</script>`);
