"""Yıldızlı gecede İstanbul: sahne, renkler ve fırça yönü. Boyama ve video: video.py"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H, SS = 1920, 1080, 2          # SS: pürüzsüz kenar için üst örnekleme
SHORE, rng = 770, np.random.default_rng(7)
SKY, HILL, WALL, ROOF, LIGHT, WATER, STAR, BOAT, BOATLIGHT = range(1, 10)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)


def ramp(t, stops):
    pos, cols = zip(*stops)
    return np.dstack([np.interp(t, pos, [c[i] for c in cols]) for i in range(3)])


# --- gökyüzü: akış alanı ve renk bantları ---
VORTEX = [(760, 270, 230, 1), (1130, 350, 170, -1), (330, 190, 120, -1)]   # x, y, yarıçap, yön
vx, vy = np.ones_like(xx), .38 * np.sin(xx / 170 + yy / 90)
band = np.sin(yy / 34 + 1.8 * np.sin(xx / 210) + np.sin(xx / 83 + yy / 140))
for cx, cy, r, s in VORTEX:
    dx, dy = xx - cx, yy - cy
    d = np.hypot(dx, dy) + 1
    g = np.exp(-(d / r) ** 2)
    vx = vx * (1 - g) + g * (-dy / d * s - .18 * dx / d) * 2.2
    vy = vy * (1 - g) + g * (dx / d * s - .18 * dy / d) * 2.2
    band = band * (1 - g) + g * np.sin(d / 17 - s * 2.5 * np.arctan2(dy, dx))
sky = ramp(yy / SHORE, [(0, (12, 22, 66)), (.45, (27, 55, 128)), (.8, (52, 104, 160)), (1, (112, 156, 160))])
sky += np.clip(band, 0, 1)[..., None] ** 2 * np.array([70, 105, 90]) - np.clip(-band, 0, 1)[..., None] * np.array([8, 18, 26])
angle = np.arctan2(vy, vx)

STARS = [(150, 110, 17), (520, 90, 12), (980, 105, 15), (1330, 150, 20), (1480, 400, 11), (210, 360, 12),
         (610, 455, 9), (1745, 470, 10), (1210, 65, 8)]
MOON = (1690, 170, 62)
for sx, sy, r in STARS + [MOON]:
    d = np.hypot(xx - sx, yy - sy)
    glow = np.exp(-(d / (r * 2.6)) ** 2)[..., None]
    ring = (.72 + .28 * np.cos(d / 5.5))[..., None]
    sky = sky * (1 - glow) + glow * ring * np.array([250, 226, 120]) + glow * (1 - ring) * sky
    near = d < r * 3.6
    angle[near] = np.arctan2(yy - sy, xx - sx)[near] + np.pi / 2

# --- su ---
water = ramp((yy - SHORE) / (H - SHORE), [(0, (38, 78, 112)), (.4, (20, 48, 98)), (1, (8, 18, 48))])
water += np.clip(np.sin(yy / 7 + 3 * np.sin(xx / 120 + yy / 37)), 0, 1)[..., None] ** 3 * np.array([30, 60, 75])
base = np.where((yy < SHORE)[..., None], sky, water)
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
lab = Image.fromarray(np.where(yy < SHORE, SKY, WATER).astype(np.uint8))
di, dl = ImageDraw.Draw(img), ImageDraw.Draw(lab)


def poly(pts, color, label):
    di.polygon(pts, fill=color)
    dl.polygon(pts, fill=label)


def box(x0, y0, x1, y1, color, label):
    poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], color, label)


def oval(x0, y0, x1, y1, color, label, half=False):
    for d, f in ((di, color), (dl, label)):
        d.pieslice([x0, y0, x1, y1], 180, 360, fill=f) if half else d.ellipse([x0, y0, x1, y1], fill=f)


def pick(cols):
    return cols[rng.integers(len(cols))]


# yıldız çekirdekleri ve hilal
for sx, sy, r in STARS:
    oval(sx - r, sy - r, sx + r, sy + r, (255, 232, 130), STAR)
    oval(sx - r * .5, sy - r * .5, sx + r * .5, sy + r * .5, (255, 250, 215), STAR)
mx, my, mr = MOON
oval(mx - mr, my - mr, mx + mr, my + mr, (255, 206, 62), STAR)
oval(mx - mr * 1.3, my - mr * 1.12, mx + mr * .45, my + mr * .62, (214, 190, 105), STAR)


def ridge(x):
    """Tepe çizgisi: solda cami tepesi, ortada Galata tepesi."""
    return SHORE - 55 - 105 * np.exp(-((x - 300) / 230) ** 2) - 175 * np.exp(-((x - 1330) / 330) ** 2) - 12 * np.sin(x / 61)


poly([(x, ridge(x)) for x in range(0, W + 20, 20)] + [(W, SHORE), (0, SHORE)], (18, 36, 60), HILL)


def minaret(x, base_y, h):
    box(x - 7, base_y - h, x + 7, base_y, (44, 56, 96), ROOF)
    for k in (.55, .8):
        box(x - 13, base_y - h * k, x + 13, base_y - h * k + 8, (236, 176, 70), LIGHT)
    poly([(x - 9, base_y - h), (x, base_y - h - 55), (x + 9, base_y - h)], (28, 36, 70), ROOF)


# cami (sol tepe)
for mxx, h in ((130, 235), (190, 270), (420, 270), (480, 235)):
    minaret(mxx, 660, h)
box(190, 600, 420, 665, (54, 62, 100), WALL)
for x0, y0, x1, y1 in ((195, 565, 275, 640), (335, 565, 415, 640), (232, 525, 378, 677)):
    main = x0 == 232
    oval(x0, y0, x1, y1, (92, 128, 172) if main else (66, 94, 140), ROOF, half=True)
    oval(x0 + 14, y0 + 8, x0 + (x1 - x0) * .45, y1 - 30, (134, 168, 200) if main else (98, 128, 168), ROOF, half=True)
box(302, 504, 308, 527, (244, 190, 70), LIGHT)
for x in range(205, 410, 27):
    box(x, 618, x + 10, 642, (255, 188, 64), LIGHT)


def house(x, y, w, h):
    wall = pick([(112, 74, 66), (70, 74, 108), (132, 100, 62), (52, 88, 96), (96, 56, 70)])
    box(x, y, x + w, y + h, wall, WALL)
    poly([(x - 4, y), (x + w / 2, y - h * .42), (x + w + 4, y)], pick([(150, 62, 40), (116, 48, 52), (44, 54, 88)]), ROOF)
    for wx in range(int(x) + 8, int(x + w) - 12, 20):
        for wy in range(int(y) + 8, int(y + h) - 14, 24):
            if rng.random() < .55:
                box(wx, wy, wx + 9, wy + 13, pick([(255, 196, 60), (255, 166, 46), (255, 224, 120)]), LIGHT)


for row in range(4):
    for x in np.arange(-10, W, 46):
        x = x + rng.uniform(-12, 12)
        y = ridge(x) + 6 + row * 42 + rng.uniform(-10, 10)
        if y < SHORE - 26 and not (150 < x < 450 and row < 2):
            house(x, y, rng.uniform(36, 60), min(rng.uniform(34, 56), SHORE - 8 - y))

# Galata Kulesi
T = 1330
poly([(T - 62, 640), (T - 54, 330), (T + 54, 330), (T + 62, 640)], (176, 140, 98), WALL)
poly([(T + 14, 640), (T + 12, 330), (T + 54, 330), (T + 62, 640)], (112, 86, 82), WALL)
for y in (390, 470, 550):
    box(T - 60, y, T + 60, y + 7, (212, 176, 118), WALL)
box(T - 74, 318, T + 74, 334, (224, 188, 126), WALL)          # seyir balkonu
box(T - 60, 262, T + 60, 320, (150, 112, 88), WALL)
for x in range(T - 50, T + 40, 24):
    oval(x, 272, x + 14, 292, (255, 206, 76), LIGHT)
    box(x, 282, x + 14, 308, (255, 206, 76), LIGHT)
box(T - 70, 252, T + 70, 264, (224, 188, 126), WALL)
poly([(T - 64, 254), (T - 22, 190), (T, 128), (T + 22, 190), (T + 64, 254)], (52, 62, 100), ROOF)
poly([(T + 4, 140), (T + 22, 190), (T + 64, 254), (T + 14, 254)], (34, 40, 72), ROOF)
box(T - 3, 96, T + 3, 130, (240, 192, 70), LIGHT)
for y in (350, 420, 498, 578):
    for x in (T - 30, T + 4, T + 34):
        oval(x - 6, y - 8, x + 6, y + 4, (60, 40, 46), ROOF)
        box(x - 6, y - 2, x + 6, y + 16, (60, 40, 46) if (x + y) % 3 else (255, 190, 66), ROOF if (x + y) % 3 else LIGHT)
box(0, SHORE - 8, W, SHORE, (92, 76, 70), WALL)               # rıhtım

# sudaki yansımalar: kırık yatay darbeler
lights = [(x, (255, 190, 64)) for x in rng.integers(20, W - 20, 30)] + [(T, (240, 188, 110))] * 4 + [(mx, (255, 212, 90))] * 5 + [(300, (255, 196, 80))] * 2
for x, col in lights:
    y, length = SHORE + 6, rng.uniform(70, 290)
    while y < SHORE + length:
        fade = 1 - .75 * (y - SHORE) / length
        w = rng.uniform(3, 12) * (.5 + fade)
        ox = x + rng.uniform(-16, 16)
        under = img.getpixel((int(np.clip(ox, 0, W - 1)), int(min(y, H - 1))))
        box(ox - w, y, ox + w, y + rng.uniform(2, 5), tuple(int(u + (c - u) * (.25 + .7 * fade)) for u, c in zip(under, col)), LIGHT)
        y += rng.uniform(11, 24)

# şehir hatları vapuru (videoda ayrı katman)
bg_img, bg_lab = img.copy(), lab.copy()
di, dl = ImageDraw.Draw(img), ImageDraw.Draw(lab)
BX, BY = 660, 955
poly([(BX - 250, BY - 38), (BX + 285, BY - 48), (BX + 235, BY + 30), (BX - 215, BY + 30)], (22, 20, 34), BOAT)
box(BX - 232, BY + 16, BX + 240, BY + 30, (150, 52, 40), BOAT)
box(BX - 210, BY - 96, BX + 215, BY - 40, (226, 218, 194), BOAT)
box(BX - 150, BY - 142, BX + 130, BY - 96, (236, 228, 204), BOAT)
box(BX - 165, BY - 150, BX + 145, BY - 140, (112, 58, 44), BOAT)
for x in range(BX - 192, BX + 190, 38):
    box(x, BY - 82, x + 22, BY - 58, (255, 190, 52), BOATLIGHT)
for x in range(BX - 132, BX + 105, 34):
    box(x, BY - 128, x + 19, BY - 108, (255, 204, 72), BOATLIGHT)
box(BX - 45, BY - 215, BX + 10, BY - 150, (214, 168, 52), BOAT)      # baca
box(BX - 47, BY - 225, BX + 12, BY - 205, (20, 18, 28), BOAT)
boat_base, boat_lab = np.asarray(img, np.float32), np.asarray(lab)
base, lab = np.asarray(bg_img, np.float32), np.asarray(bg_lab)

# --- fırça yönü ---
angle = np.where(lab == HILL, np.arctan(np.gradient(ridge(np.arange(W)))), angle)
angle = np.where(lab == WALL, np.pi / 2, angle)
angle = np.where(lab == ROOF, np.pi / 2 + .25 * np.sin(xx / 15), angle)
angle = np.where((lab == WATER) | ((lab == LIGHT) & (yy > SHORE)), .09 * np.sin(xx / 60 + yy / 23), angle)
angle = np.where((lab == LIGHT) & (yy <= SHORE), np.pi / 2, angle)

