// Mino: tamamen kodla kurulan özgün chibi karakter. karakter() -> { kok, bas, kolSol, kolSag, bacakSol, bacakSag, yuz() }
import * as THREE from "three";

const RENK = { ten: "#ffd9c2", sac: 0x5b3a8e, sacAcik: 0x8a62c4, ust: 0xffc53d, ustKoyu: 0xe79a1f, pantolon: 0x33415c, ayakkabi: 0xf2f2f7, vurgu: 0xff6b6b, mavi: 0x3fc1c9 };
const gec = new THREE.DataTexture(new Uint8Array([140, 205, 255]), 3, 1, THREE.RedFormat);
gec.needsUpdate = true;
const toon = (color, ek = {}) => new THREE.MeshToonMaterial({ color, gradientMap: gec, ...ek });
// çizgi film konturu: yüzeyi normal yönünde şişirip yalnız arka yüzü boyar
const kontur = new THREE.MeshBasicMaterial({ color: 0x2a1d3d, side: THREE.BackSide });
kontur.onBeforeCompile = (s) => { s.vertexShader = s.vertexShader.replace("#include <begin_vertex>", "vec3 transformed = position + normalize(normal) * 0.014;"); };

function parca(geo, malzeme, ust, x = 0, y = 0, z = 0, cizgi = true) {
  const m = new THREE.Mesh(geo, typeof malzeme === "number" ? toon(malzeme) : malzeme);
  m.position.set(x, y, z);
  m.castShadow = true;
  if (cizgi) m.add(new THREE.Mesh(geo, kontur));
  ust.add(m);
  return m;
}
const kure = (r, sx = 1, sy = 1, sz = 1) => { const g = new THREE.SphereGeometry(r, 48, 32); g.scale(sx, sy, sz); g.computeVertexNormals(); return g; };
// ucu sivrilen saç tutamı
function tutam(en, boy, kalin) {
  const g = new THREE.SphereGeometry(1, 32, 24), p = g.attributes.position;
  for (let i = 0; i < p.count; i++) {
    const y = p.getY(i), daral = y < 0 ? 1 - Math.pow(-y, 1.6) * 0.93 : 1;
    p.setXYZ(i, p.getX(i) * en * daral, y * boy, p.getZ(i) * kalin * daral);
  }
  g.computeVertexNormals();
  return g;
}
const grup = (ust, x = 0, y = 0, z = 0) => { const g = new THREE.Group(); g.position.set(x, y, z); ust.add(g); return g; };

export function karakter() {
  const kok = new THREE.Group();

  // ---------- bacaklar ve gövde ----------
  const bacak = (yon) => {
    const b = grup(kok, 0.17 * yon, 0.56, 0);
    parca(new THREE.CapsuleGeometry(0.12, 0.24, 8, 24), RENK.pantolon, b, 0, -0.22, 0);
    parca(kure(0.16, 1, 0.72, 1.35), RENK.ayakkabi, b, 0, -0.45, 0.06);
    parca(kure(0.15, 1.04, 0.2, 1.36), RENK.vurgu, b, 0, -0.52, 0.065, false);
    return b;
  };
  const bacakSol = bacak(-1), bacakSag = bacak(1);
  const profil = [[0, 0], [0.34, 0.0], [0.4, 0.06], [0.37, 0.3], [0.31, 0.52], [0.22, 0.66], [0, 0.7]].map(([x, y]) => new THREE.Vector2(x, y));
  const govde = new THREE.LatheGeometry(profil, 48);
  govde.scale(1, 1, 0.86);
  govde.computeVertexNormals();
  parca(govde, RENK.ust, kok, 0, 0.48, 0);
  const bant = parca(new THREE.TorusGeometry(0.355, 0.045, 16, 48), RENK.ustKoyu, kok, 0, 0.52, 0);
  bant.rotation.x = Math.PI / 2;
  bant.scale.set(1, 0.86, 1);
  parca(kure(0.2, 1.15, 0.5, 0.25), RENK.ustKoyu, kok, 0, 0.7, 0.3);           // cep
  const yaka = parca(new THREE.TorusGeometry(0.21, 0.07, 16, 40), RENK.ustKoyu, kok, 0, 1.12, -0.01);
  yaka.rotation.x = Math.PI / 2 - 0.12;
  for (const x of [-0.08, 0.08]) {
    parca(new THREE.CylinderGeometry(0.012, 0.012, 0.22, 8), RENK.ayakkabi, kok, x, 0.98, 0.285, false).rotation.x = -0.28;
    parca(kure(0.028), RENK.ayakkabi, kok, x, 0.86, 0.32, false);
  }
  const kol = (yon) => {
    const k = grup(kok, 0.28 * yon, 1.05, 0);
    k.rotation.z = 0.42 * yon;
    parca(new THREE.CapsuleGeometry(0.095, 0.3, 8, 24), RENK.ust, k, 0.04 * yon, -0.2, 0);
    const manset = parca(new THREE.TorusGeometry(0.082, 0.028, 12, 32), RENK.ustKoyu, k, 0.04 * yon, -0.39, 0);
    manset.rotation.x = Math.PI / 2;
    parca(kure(0.095), toon(RENK.ten), k, 0.04 * yon, -0.47, 0);
    return k;
  };
  const kolSol = kol(-1), kolSag = kol(1);

  // ---------- baş ve yüz ----------
  const bas = grup(kok, 0, 1.12, 0);
  const R = 0.62, ic = grup(bas, 0, 0.56, 0);
  const tuval = Object.assign(document.createElement("canvas"), { width: 2048, height: 1024 });
  const doku = new THREE.CanvasTexture(tuval);
  doku.colorSpace = THREE.SRGBColorSpace;
  doku.anisotropy = 8;
  parca(kure(R, 1.06, 0.96, 1), toon(0xffffff, { map: doku }), ic);
  for (const x of [-1, 1]) parca(kure(0.12, 0.55, 1, 0.8), toon(RENK.ten), ic, 0.65 * x, -0.1, 0);

  // yüz: kürenin dokusuna çizilir; ön yüz u = 0.25
  function yuz({ goz = "acik", agiz = "gulumse", kas = 0, kapali = 0, ses = 0, bakis = 0 } = {}) {
    const c = tuval.getContext("2d");
    c.fillStyle = RENK.ten; c.fillRect(0, 0, 2048, 1024);
    const cx = 512, gy = 585;
    c.lineCap = c.lineJoin = "round";
    for (const yon of [-1, 1]) {
      const x = cx + 112 * yon;
      const a = c.createRadialGradient(x + 46 * yon, gy + 72, 4, x + 46 * yon, gy + 72, 56);
      a.addColorStop(0, "rgba(255,110,120,.55)"); a.addColorStop(1, "rgba(255,110,120,0)");
      c.fillStyle = a; c.fillRect(x + 46 * yon - 60, gy + 12, 120, 120);
      c.strokeStyle = "#2a1d3d"; c.lineWidth = 15;
      if (goz === "mutlu" || kapali > 0.6) {
        c.beginPath();
        if (goz === "mutlu") c.arc(x, gy + 22, 42, Math.PI * 1.12, Math.PI * 1.88);
        else { c.moveTo(x - 38, gy + 6); c.quadraticCurveTo(x, gy + 26, x + 38, gy + 6); }
        c.stroke();
      } else {
        const rx = goz === "buyuk" ? 48 : 42, ry = (goz === "buyuk" ? 66 : 58) * (1 - kapali);
        c.fillStyle = "#2a1d3d"; c.beginPath(); c.ellipse(x, gy, rx, ry, 0, 0, 7); c.fill();
        const g = c.createLinearGradient(0, gy - ry, 0, gy + ry);
        g.addColorStop(0.25, "#2a1d3d"); g.addColorStop(1, "#38b6c9");
        c.fillStyle = g; c.beginPath(); c.ellipse(x + bakis * 8, gy + 4, rx * 0.82, ry * 0.84, 0, 0, 7); c.fill();
        c.fillStyle = "#fff";
        c.beginPath(); c.ellipse(x - 14 + bakis * 8, gy - ry * 0.38, 14, 18 * (1 - kapali), 0, 0, 7); c.fill();
        c.beginPath(); c.arc(x + 17 + bakis * 8, gy + ry * 0.36, 7 * (1 - kapali), 0, 7); c.fill();
        c.beginPath(); c.moveTo(x - rx - 4, gy - ry * 0.42); c.quadraticCurveTo(x, gy - ry - 18, x + rx + 4, gy - ry * 0.42); c.stroke();
      }
      c.lineWidth = 11; c.strokeStyle = "#4a2f78";
      const ky = gy - 92 - kas * 26;
      c.beginPath(); c.moveTo(x - 30, ky + (kas < 0 ? -10 * yon : 6)); c.quadraticCurveTo(x, ky - 12, x + 30, ky + (kas < 0 ? 10 * yon : 6)); c.stroke();
    }
    c.strokeStyle = "#7a2b3a"; c.fillStyle = "#8c2f45"; c.lineWidth = 10;
    const ay = gy + 108;
    c.beginPath();
    if (agiz === "acik" || ses > 0.08) {
      const h = ses > 0.08 ? 12 + 34 * ses : 42;
      c.moveTo(cx - 36, ay - 8); c.quadraticCurveTo(cx, ay + h * 1.8, cx + 36, ay - 8); c.closePath(); c.fill(); c.stroke();
    } else if (agiz === "o") { c.ellipse(cx, ay + 8, 20, 28, 0, 0, 7); c.fill(); c.stroke(); }
    else if (agiz === "uzgun") { c.moveTo(cx - 28, ay + 14); c.quadraticCurveTo(cx, ay - 14, cx + 28, ay + 14); c.stroke(); }
    else { c.moveTo(cx - 30, ay - 4); c.quadraticCurveTo(cx, ay + 26, cx + 30, ay - 4); c.stroke(); }
    doku.needsUpdate = true;
  }

  // ---------- saç ----------
  const sacM = toon(RENK.sac, { side: THREE.DoubleSide });
  const arkaSac = new THREE.SphereGeometry(R * 1.075, 64, 40, Math.PI / 2 + 1.12, Math.PI * 2 - 2.24, 0, Math.PI * 0.7);
  arkaSac.scale(1.07, 0.99, 1.01);
  parca(arkaSac, sacM, ic);
  const tepe = new THREE.SphereGeometry(R * 1.08, 64, 24, 0, Math.PI * 2, 0, Math.PI * 0.27);
  tepe.scale(1.07, 0.99, 1.01);
  parca(tepe, sacM, ic, 0, 0, 0, false);
  const yuzeye = (nesne, yatay, dikey, r) => {            // küre yüzeyine yatır
    nesne.position.set(r * 1.06 * Math.sin(yatay) * Math.cos(dikey), r * 0.97 * Math.sin(dikey), r * Math.cos(yatay) * Math.cos(dikey));
    nesne.rotation.set(-dikey, yatay, 0, "YXZ");
  };
  [[-0.92, 0.42, 0.36, -0.22], [-0.52, 0.6, 0.31, 0.28], [-0.12, 0.66, 0.34, 0.42], [0.3, 0.62, 0.3, -0.34], [0.68, 0.55, 0.32, -0.12], [0.98, 0.36, 0.36, 0.2]].forEach(([yt, dk, boy, egim], i) => {
    const t = parca(tutam(0.17, boy, 0.065), i === 2 ? toon(RENK.sacAcik) : sacM, ic);
    yuzeye(t, yt, dk, R * 1.06);
    t.rotateZ(egim);
  });
  for (const x of [-1, 1]) {                                // yan tutamlar
    const t = parca(tutam(0.13, 0.42, 0.09), sacM, ic);
    yuzeye(t, 1.22 * x, -0.12, R * 1.07);
    t.rotateZ(0.1 * x);
  }
  const egri = new THREE.CatmullRomCurve3([new THREE.Vector3(0, 0.62, 0), new THREE.Vector3(0.05, 0.84, 0.02), new THREE.Vector3(0.24, 0.9, 0.04), new THREE.Vector3(0.3, 0.78, 0.05)]);
  parca(new THREE.TubeGeometry(egri, 32, 0.035, 12), sacM, ic);
  parca(kure(0.036), sacM, ic, 0.3, 0.78, 0.05);

  // ---------- kulaklık ----------
  const yay = parca(new THREE.TorusGeometry(0.745, 0.04, 16, 64, Math.PI), RENK.mavi, ic, 0, -0.04, -0.07);
  yay.scale.set(1.02, 1.0, 1);
  for (const x of [-1, 1]) {
    const k = parca(new THREE.CylinderGeometry(0.17, 0.17, 0.13, 40), RENK.mavi, ic, 0.735 * x, -0.1, -0.05);
    k.rotation.z = Math.PI / 2;
    parca(new THREE.CylinderGeometry(0.095, 0.095, 0.15, 32), RENK.vurgu, ic, 0.745 * x, -0.1, -0.05).rotation.z = Math.PI / 2;
  }
  yuz();
  return { kok, bas, kolSol, kolSag, bacakSol, bacakSag, yuz };
}
