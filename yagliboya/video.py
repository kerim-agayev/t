"""Yağlı boya video. python video.py -> video.mp4 | python video.py kare 12 -> resim.png (12. saniye)"""
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

import resim as R
from resim import H, SHORE, SS, W

FPS, DUR, PAINT = 30, 24.0, 5.0
HERE = Path(__file__).parent
CITY = (R.HILL, R.WALL, R.ROOF, R.LIGHT)
G = {}


def trace(x, y, length, lab, angle):
    """Akış alanını izler; bölge sınırında durur."""
    pts, region = [(x, y)], lab[y, x]
    for direction in (1, -1):
        px, py = x, y
        for _ in range(max(1, int(length / 8))):
            a = angle[int(py), int(px)]
            px, py = px + direction * 4 * np.cos(a), py + direction * 4 * np.sin(a)
            if not (0 <= px < W and 0 <= py < H) or lab[int(py), int(px)] != region:
                break
            pts.insert(len(pts) if direction > 0 else 0, (px, py))
    if len(pts) < 2:
        pts = [(x - 1, y), (x + 1, y)]
    return np.array(pts, np.float32)


def bristles(color, width, rng):
    """Her kılın rengi ve kalınlığı bir kez seçilir (karede kareye titreme olmaz)."""
    n = max(3, int(width / 2.2))
    return [((k / (n - 1) - .5) * width, rng.random(), rng.random(),
             tuple(int(v) for v in np.clip(color + rng.normal(0, 10) - (k / (n - 1) - .5) * 22, 0, 255)),
             int(105 + 110 * np.sin(np.pi * (k + .5) / n) + rng.normal(0, 18)),
             width / n * 1.7) for k in range(n)]


def make_strokes(base, lab, angle, layers, rng):
    """layers: (adım, boy, en, renk sapması, maske). Sonuç boyama sırasındadır."""
    out = []
    for step, length, width, jitter, mask in layers:
        gx, gy = np.meshgrid(np.arange(0, W, step), np.arange(0, H, step))
        gx = np.clip(gx + rng.integers(-(step // 2), step // 2 + 1, gx.shape), 0, W - 1).ravel()
        gy = np.clip(gy + rng.integers(-(step // 2), step // 2 + 1, gy.shape), 0, H - 1).ravel()
        keep = np.nonzero(mask[gy, gx])[0]
        for i in rng.permutation(keep):
            x, y = int(gx[i]), int(gy[i])
            ln, wd = length * rng.uniform(.6, 1.3), width * rng.uniform(.75, 1.25)
            path = trace(x, y, ln * (2.6 if lab[y, x] == R.SKY else 1), lab, angle)
            color = base[y, x] + rng.normal(0, jitter) + rng.normal(0, jitter * .6, 3)
            out.append((int(lab[y, x]), path, max(3, int(ln / 4) + 1), rng.random(), x, y, bristles(color, wd, rng)))
    return out


def draw(cd, hd, path, hair, scale=1.0, dx=0.0, alpha=False):
    p = (path + (dx, 0)) * SS
    tan = np.gradient(p, axis=0)
    nor = np.stack([-tan[:, 1], tan[:, 0]], 1) / (np.linalg.norm(tan, axis=1, keepdims=True) + 1e-6)
    for off, a, b, color, h, lw in hair:
        i, j = int(a * (len(p) // 5)), len(p) - int(b * (len(p) // 5))
        if j - i < 2:
            continue
        seg = (p[i:j] + nor[i:j] * off * SS * scale).ravel().tolist()
        w = max(1, int(lw * SS * scale) + 1)
        cd.line(seg, fill=color + (255,) if alpha else color, width=w, joint="curve")
        hd.line(seg, fill=h, width=w)


def sprite(base, mask):
    """Altı bulanık/düz boyalı, saydam zeminli katman ve yükseklik haritası."""
    big = (W * SS, H * SS)
    layer = Image.fromarray(base.astype(np.uint8)).resize(big).convert("RGBA")
    layer.putalpha(Image.fromarray((mask * 255).astype(np.uint8)).resize(big))
    return layer, Image.new("L", big, 90)


def setup():
    rng = np.random.default_rng(7)
    organic = np.isin(R.lab, [R.SKY, R.WATER, R.HILL])
    strokes = make_strokes(R.base, R.lab, R.angle, [
        (17, 62, 21, 9, organic), (12, 38, 11, 12, organic), (8, 22, 9, 10, ~organic),
        (5, 13, 5, 8, ~organic), (22, 30, 6, 20, organic)], rng)
    big = (W * SS, H * SS)
    G["under"] = Image.fromarray(R.base.astype(np.uint8)).filter(ImageFilter.GaussianBlur(5)).resize(big)
    reflect = (R.lab == R.LIGHT) & (R.yy > SHORE)
    G["moving"] = [s for s in strokes if s[0] in (R.SKY, R.WATER) or (s[0] == R.LIGHT and s[5] > SHORE)]

    # sabit şehir katmanı
    city, chm = sprite(R.base, np.isin(R.lab, CITY) & ~reflect)
    cd, hd = ImageDraw.Draw(city), ImageDraw.Draw(chm)
    for lab, path, n, u, x, y, hair in strokes:
        if lab in CITY and y <= SHORE + 2:
            draw(cd, hd, path, hair, alpha=True)
    im = Image.fromarray(R.lab)
    edge = np.asarray(im.filter(ImageFilter.MaxFilter(3))) != np.asarray(im.filter(ImageFilter.MinFilter(3)))
    ys, xs = np.nonzero(edge & np.isin(R.lab, [R.HILL, R.WALL, R.ROOF]))
    for i in rng.permutation(len(xs))[: len(xs) // 9]:
        y, x = ys[i], xs[i]
        flat = np.all(R.lab[y, max(x - 3, 0):x + 4] == R.lab[y, x])
        at, d = np.array([x, y]), np.array([6, 0] if flat else [0, 6])
        cd.line([tuple((at - d) * SS), tuple((at + d) * SS)], fill=(14, 18, 40, 255), width=2 * SS)
    G["city"], G["chm"] = city, chm

    # vapur katmanı
    bmask = np.isin(R.boat_lab, [R.BOAT, R.BOATLIGHT])
    boat, bhm = sprite(R.boat_base, bmask)
    cd, hd = ImageDraw.Draw(boat), ImageDraw.Draw(bhm)
    flat = np.zeros_like(R.angle)
    for s in make_strokes(R.boat_base, R.boat_lab, flat, [(8, 22, 9, 9, bmask), (5, 13, 5, 8, bmask)], rng):
        draw(cd, hd, s[1], s[6], alpha=True)
    G["boat"], G["bhm"] = boat, bhm

    # pencere titreşimi, yıldız ışıması, boyanma sırası
    win = Image.fromarray((((R.lab == R.LIGHT) & ~reflect) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
    G["win"] = np.asarray(win, np.float32)[..., None] / 255
    G["phase"] = np.kron(rng.uniform(0, 6.28, (H // 24 + 1, W // 24 + 1)), np.ones((24, 24)))[:H, :W, None].astype(np.float32)
    G["glow"] = []
    for sx, sy, r in R.STARS + [R.MOON]:
        x0, y0 = max(sx - r * 4, 0), max(sy - r * 4, 0)
        x1, y1 = min(sx + r * 4, W), min(sy + r * 4, H)
        d = np.hypot(R.xx[y0:y1, x0:x1] - sx, R.yy[y0:y1, x0:x1] - sy)
        G["glow"].append((y0, y1, x0, x1, d, r, rng.uniform(0, 6.28)))
    order = Image.new("L", (W, H), 255)
    od = ImageDraw.Draw(order)
    seeds = []
    for y in range(0, H, 42):
        for x in range(0, W, 42):
            px, py = min(x + int(rng.integers(0, 30)), W - 1), min(y + int(rng.integers(0, 30)), H - 1)
            start = {R.SKY: 0, R.STAR: .35, R.WATER: .5}.get(int(R.lab[py, px]), .3)
            seeds.append((start + .48 * rng.random(), px, py))
    for tm, x, y in sorted(seeds, reverse=True):          # erken darbe en üstte kalır
        path = trace(x, y, 110, R.lab, R.angle)
        nor = np.stack([-np.gradient(path[:, 1]), np.gradient(path[:, 0])], 1) / 4
        for off in range(-36, 37, 8):
            i, j = int(rng.integers(0, len(path) // 3 + 1)), len(path) - int(rng.integers(0, len(path) // 3 + 1))
            if j - i > 1:
                od.line((path[i:j] + nor[i:j] * off).ravel().tolist(), fill=int(np.clip(tm + rng.uniform(-.03, .03), 0, 1) * 245), width=11, joint="curve")
    G["order"] = np.asarray(order, np.float32)[..., None] / 255
    G["puffs"] = rng.uniform(-1, 1, (64, 34, 4))


def boat_pos(t):
    return -300 + 640 * t / DUR, 3.5 * np.sin(2.1 * t)


def smoke(frame, t):
    layer = Image.new("RGBA", frame.size)
    d = ImageDraw.Draw(layer)
    for i in range(int((t + 4) / .42), -1, -1):
        born = i * .42 - 4
        age = t - born
        if not 0 <= age < 4.2:
            continue
        bx, by = boat_pos(born)
        cx = R.BX - 18 + bx - 46 * age
        cy = R.BY - 236 + by - 32 * age + 6 * np.sin(age * 2 + i)
        r = 14 + 12 * age
        for u, v, a, c in G["puffs"][i % 64]:
            x, y, rr = cx + u * r, cy + v * r * .6, r * (.35 + .25 * abs(a))
            ang = a * 180 + age * 25
            tone = int(205 + 35 * c - 12 * age)
            alpha = int(235 * min(1, age * 4 + .2) * (1 - age / 4.2))
            d.arc([(x - rr) * SS, (y - rr) * SS, (x + rr) * SS, (y + rr) * SS], ang, ang + 130,
                  fill=(tone, tone, tone + 16, alpha), width=8 * SS)
    frame.paste(layer, (0, 0), layer)


def render(t):
    canvas = G["under"].copy()
    hm = Image.new("L", canvas.size, 90)
    cd, hd = ImageDraw.Draw(canvas), ImageDraw.Draw(hm)
    for lab, path, n, u0, x, y, hair in G["moving"]:
        if lab == R.SKY:
            room = len(path) - n - 1
            if room < 3:
                draw(cd, hd, path[:n], hair)
                continue
            u = (u0 + t * 10 / room) % 1                       # akış boyunca kayan pencere
            i, f = int(u * room), (u * room) % 1
            part = path[i:i + n + 1]
            part = part[:-1] + (part[1:] - part[:-1]) * f      # alt piksel kaydırma
            draw(cd, hd, part, hair, scale=min(1.0, .25 + 2.6 * np.sin(np.pi * u)))
        else:
            depth = (y - SHORE) / (H - SHORE)
            dx = (3 + 10 * depth) * np.sin(2.3 * t + y / 15 + x / 110)
            scale = 1 + .35 * np.sin(4 * t + y / 6 + x / 40) if lab == R.LIGHT else 1.0
            draw(cd, hd, path, hair, scale, dx)
    canvas.paste(G["city"], (0, 0), G["city"])
    hm.paste(G["chm"], (0, 0), G["city"])
    bx, by = boat_pos(t)
    at = (int(bx * SS), int(by * SS))
    canvas.paste(G["boat"], at, G["boat"])
    hm.paste(G["bhm"], at, G["boat"])
    smoke(canvas, t)

    rgb = np.asarray(canvas.resize((W, H), Image.BOX), np.float32)
    h = np.asarray(hm.resize((W, H), Image.BOX).filter(ImageFilter.GaussianBlur(.8)), np.float32)
    gy, gx = np.gradient(h)
    rgb = rgb * np.clip(1 - (gx + gy) * .0065, .72, 1.32)[..., None]
    rgb = rgb * (1 + .2 * G["win"] * np.sin(1.7 * t + G["phase"]))
    for y0, y1, x0, x1, d, r, ph in G["glow"]:
        beat = .5 + .5 * np.sin(2.2 * t + ph)
        g = np.exp(-(d / (r * (1.5 + .5 * beat))) ** 2) * (.55 + .45 * np.cos(d / 6 - 4 * t))
        rgb[y0:y1, x0:x1] += (g * (.12 + .2 * beat) * (.35 if r > 40 else 1))[..., None] * np.array([255, 214, 110], np.float32)
    weave = (np.sin(R.xx * 1.9) + np.sin(R.yy * 1.9))[..., None] * 1.6
    vig = 1 - .44 * (((R.xx - W / 2) / W) ** 2 + ((R.yy - H / 2) / H) ** 2)[..., None]
    rgb = ((rgb + weave - 105) * 1.08 + 108) * vig

    if t < PAINT + .4:                                          # tuval fırça darbeleriyle boyanır
        k = np.clip((t / PAINT - G["order"]) * 25, 0, 1)
        rgb = rgb * k + (np.array([226, 216, 192], np.float32) + weave * 3) * (1 - k)
    img = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
    z = np.clip((t - 11) / 12, 0, 1)
    z = z * z * (3 - 2 * z)
    if z > 0:                                                   # Galata Kulesi'ne yaklaşma
        s = 1 + .14 * z
        cw, ch = W / s, H / s
        left, top = (W - cw) * (.5 + .28 * z), (H - ch) * .6
        img = img.resize((W, H), Image.BICUBIC, box=(left, top, left + cw, top + ch))
    fade = min(1.0, (DUR - t) / .8)
    if fade < 1:
        img = Image.eval(img, lambda v: int(v * max(fade, 0)))
    return img


def frame_bytes(i):
    return render(i / FPS).tobytes()


if __name__ == "__main__":
    if "kare" in sys.argv:
        setup()
        times = [float(a) for a in sys.argv[2:]]
        for t in times:
            render(t).save(HERE / ("resim.png" if len(times) == 1 else f"kare_{t:g}.png"))
    else:
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                               "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "19",
                               "-pix_fmt", "yuv420p", str(HERE / "video.mp4")], stdin=subprocess.PIPE)
        with Pool(8, initializer=setup) as pool:
            for data in pool.imap(frame_bytes, range(int(DUR * FPS))):
                ff.stdin.write(data)
        ff.stdin.close()
        code = ff.wait()
        print("OK video.mp4" if code == 0 else "ffmpeg HATA")
        sys.exit(code)
