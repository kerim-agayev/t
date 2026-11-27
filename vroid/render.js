// node render.js                    -> karakterler.png
// node render.js erteleme taslak    -> erteleme/kare/t00.png... (sahne başına 3 örnek kare)
// node render.js erteleme           -> erteleme/erteleme.mp4 (önce erteleme/ses.py)
const http = require("http"), fs = require("fs"), path = require("path");
const { spawn } = require("child_process");
const { once } = require("events");
const puppeteer = require("puppeteer-core");
const EDGE = process.env.CHROME_PATH || "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".json": "application/json", ".vrm": "model/gltf-binary" };
const [konu, kip] = process.argv.slice(2);

const server = http.createServer((req, res) => {
  const file = path.join(__dirname, path.normalize(decodeURIComponent(req.url.split("?")[0])));
  if (!file.startsWith(__dirname) || !fs.existsSync(file)) return res.writeHead(404).end();
  res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream" });
  fs.createReadStream(file).pipe(res);
});

server.listen(0, "127.0.0.1", async () => {
  const browser = await puppeteer.launch({ executablePath: EDGE, headless: true, args: ["--use-angle=d3d11", "--ignore-gpu-blocklist"] });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: konu ? 1080 : 900 });
    page.on("pageerror", (e) => { console.error("SAYFA HATASI", e.message); process.exitCode = 1; });
    const ac = async (url) => {
      await page.goto(`http://127.0.0.1:${server.address().port}/${url}`);
      await page.waitForFunction("window.hazir", { timeout: 90000 });
    };
    if (!konu) {
      await ac("sahne.html");
      await page.screenshot({ path: path.join(__dirname, "karakterler.png") });
      return console.log("OK karakterler.png");
    }
    if (kip === "kare") {                                            // tek önizleme
      await ac(`${konu}/sahne.html`);
      await page.screenshot({ path: path.join(__dirname, konu, "onizleme.png") });
      return console.log(`OK ${konu}/onizleme.png`);
    }
    const kok = path.join(__dirname, konu);
    const sayi = JSON.parse(fs.readFileSync(path.join(kok, "zaman.json"), "utf8")).length;
    const taslak = kip === "taslak";
    let ff, no = 0;
    if (taslak) fs.mkdirSync(path.join(kok, "kare"), { recursive: true });
    else ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", "30", "-i", "-", "-i", path.join(kok, "ses.wav"),
      "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-af", "loudnorm=I=-16", "-ar", "48000",
      "-shortest", path.join(kok, `${konu}.mp4`)], { stdio: ["pipe", "inherit", "inherit"] });
    for (let s = 1; s <= sayi; s++) {
      await ac(`${konu}/sahne.html?s=${s}`);
      const kareSayisi = await page.evaluate("window.kareSayisi");
      if (taslak) {
        let i = 0;
        for (const hedef of [0.25, 0.6, 0.9].map((o) => Math.floor(o * kareSayisi))) {
          for (; i <= hedef; i += 3) await page.evaluate((t) => window.kare(t), i / 30);   // fizik için sırayla
          await page.screenshot({ path: path.join(kok, "kare", `t${String(no++).padStart(2, "0")}.png`) });
        }
      } else {
        for (let i = 0; i < kareSayisi; i++) {
          await page.evaluate((t) => window.kare(t), i / 30);
          const img = await page.screenshot({ type: "jpeg", quality: 93 });
          if (!ff.stdin.write(img)) await once(ff.stdin, "drain");
        }
      }
      console.log("sahne", s, "bitti");
    }
    if (ff) {
      ff.stdin.end();
      const [kod] = await once(ff, "close");
      console.log(kod === 0 ? `OK ${konu}/${konu}.mp4` : "ffmpeg HATA");
      process.exitCode ||= kod;
    }
  } finally {
    await browser.close();
    server.close();
  }
});
