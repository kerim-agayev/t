"""Küçücük bir itiş: 1 cm'den 22 metreye domino zinciri.
blender -b -P domino.py -- kare 2 12 27        (o saniyelerden örnek kare)
blender -b -P domino.py -- video               (tüm kareler -> kare/)"""
import json
import math
import random
import sys
from pathlib import Path

import bpy
from mathutils import Vector

HERE = Path(__file__).parent
FPS, DUR, N, ORAN, H0, G = 30, 30.0, 20, 1.5, 0.01, 9.81
random.seed(4)

# ---------- yerleşim ----------
h = [H0 * ORAN ** i for i in range(N)]
d = [0.2 * v for v in h]
p = [0.0]                                      # dönme kenarı (ön alt kenar)
for i in range(1, N):
    p.append(p[-1] + 0.45 * h[i - 1] + d[i])


def en_cok(i, fi):
    """i. taşın, sonraki taş fi kadar yatmışken alabileceği en büyük açı."""
    def icinde(t):
        rx, ry = p[i] + h[i] * math.sin(t) - p[i + 1], h[i] * math.cos(t)
        return rx * math.cos(fi) - ry * math.sin(fi) > -d[i + 1]
    a, b = 0.0, math.pi / 2
    if not icinde(b):
        return b
    for _ in range(26):
        m = (a + b) / 2
        a, b = (a, m) if icinde(m) else (m, b)
    return a


# ---------- devrilme benzetimi ----------
dt = 4e-4
aci, hiz, carpma = [0.0] * N, [0.0] * N, [None] * N
temas = [en_cok(i, 0) for i in range(N - 1)]
hiz[0] = 0.5 * math.sqrt(G / h[0])
carpma[0], kayit, s = 0.0, [], 0.0
bitis = None
while bitis is None or s < bitis + 2.0:
    for i in range(N - 1, -1, -1):
        if carpma[i] is None:
            continue
        hiz[i] += 1.5 * G / h[i] * max(math.sin(aci[i]), 0.12) * dt
        yeni = aci[i] + hiz[i] * dt
        if i < N - 1:
            if carpma[i + 1] is None and yeni >= temas[i]:
                carpma[i + 1] = s
                hiz[i + 1] = max(0.7 * hiz[i] * h[i] / h[i + 1], 0.35 * math.sqrt(G / h[i + 1]))
            sinir = en_cok(i, aci[i + 1]) if carpma[i + 1] is not None else math.pi / 2
        else:
            sinir = math.pi / 2
            if yeni >= sinir and bitis is None:
                bitis = s
        if yeni > sinir:
            yeni, hiz[i] = sinir, max(0.0, (sinir - aci[i]) / dt)
        aci[i] = yeni
    kayit.append(tuple(aci))
    s += dt

# ---------- zaman bükme: küçük taşlar da görülsün ----------
T = [3.6]
for i in range(1, N):
    T.append(T[-1] + 0.5 + 1.9 * (i / (N - 1)) ** 3)
son_vurus = T[-1] + 2.8
anahtar_v = [0.0, 3.0] + T + [son_vurus, DUR]
anahtar_s = [-0.001, -0.0005] + carpma + [bitis, bitis + 1.9]


def ara(x, xs, ys):
    if x <= xs[0]:
        return ys[0]
    for k in range(1, len(xs)):
        if x <= xs[k]:
            return ys[k - 1] + (ys[k] - ys[k - 1]) * (x - xs[k - 1]) / (xs[k] - xs[k - 1])
    return ys[-1]


def acilar(t):
    sim = ara(t, anahtar_v, anahtar_s)
    if sim < 0:
        return [0.0] * N
    return kayit[min(int(sim / dt), len(kayit) - 1)]


(HERE / "olaylar.json").write_text(json.dumps(dict(carpma=T, son=son_vurus, boy=h)))

# ---------- sahne ----------
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene


def malzeme(ad, renk, puruz=0.45, metal=0.0):
    m = bpy.data.materials.new(ad)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*renk, 1)
    b.inputs["Roughness"].default_value = puruz
    b.inputs["Metallic"].default_value = metal
    return m


def lin(hx):
    return tuple(((int(hx[i:i + 2], 16) / 255) ** 2.2) for i in (0, 2, 4))


def nesne(ad, mesh, mat, loc=(0, 0, 0)):
    mesh.materials.clear()
    mesh.materials.append(mat)
    o = bpy.data.objects.new(ad, mesh)
    o.location = loc
    sc.collection.objects.link(o)
    return o


def kutu_mesh(x0, x1, y0, y1, z0, z1):
    v = [(x, y, z) for x in (x0, x1) for y in (y0, y1) for z in (z0, z1)]
    f = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
    m = bpy.data.meshes.new("kutu")
    m.from_pydata(v, [], f)
    return m


def yumusat(o, w):
    b = o.modifiers.new("pah", "BEVEL")
    b.width, b.segments = w, 4
    for yuz in o.data.polygons:
        yuz.use_smooth = True


def ilkel(op, mat, loc, olcek=(1, 1, 1), rot=(0, 0, 0), **kw):
    op(location=loc, rotation=rot, **kw)
    o = bpy.context.object
    o.scale = olcek
    o.data.materials.append(mat)
    bpy.ops.object.shade_auto_smooth() if hasattr(bpy.ops.object, "shade_auto_smooth") else None
    return o


kure = lambda mat, loc, r, olcek=(1, 1, 1): ilkel(bpy.ops.mesh.primitive_uv_sphere_add, mat, loc, olcek, radius=r, segments=32, ring_count=16)
silindir = lambda mat, loc, r, boy, rot=(0, 0, 0): ilkel(bpy.ops.mesh.primitive_cylinder_add, mat, loc, rot=rot, radius=r, depth=boy, vertices=48)


def blok(mat, cx, cy, z0, ex, ey, ez, pah=0.12):
    o = nesne("blok", kutu_mesh(-ex / 2, ex / 2, -ey / 2, ey / 2, 0, ez), mat, (cx, cy, z0))
    yumusat(o, min(ex, ey, ez) * pah)
    return o


# taşlar
RENKLER = ["e63946", "f3722c", "f8961e", "f9c74f", "90be6d", "43aa8b", "4d908e", "277da1", "5e60ce", "9d4edd"]
beyaz = malzeme("benek", lin("fff8ea"), 0.35)
taslar = []
for i in range(N):
    govde = nesne(f"tas{i}", kutu_mesh(-d[i], 0, -0.26 * h[i], 0.26 * h[i], 0, h[i]), malzeme(f"r{i}", lin(RENKLER[i % 10]), 0.28), (p[i], 0, 0))
    yumusat(govde, 0.045 * h[i])
    for yuz_x in (-d[i], 0):
        cizgi = nesne("cizgi", kutu_mesh(yuz_x - 0.004 * h[i], yuz_x + 0.004 * h[i], -0.18 * h[i], 0.18 * h[i], 0.49 * h[i], 0.51 * h[i]), beyaz)
        cizgi.parent = govde
        for z, say in ((0.74, 1 + i % 3), (0.26, 1 + (i // 3) % 3)):
            for k in range(say):
                o = (k - (say - 1) / 2) * 0.11
                benek = kure(beyaz, (yuz_x, o * h[i], (z + o * 0.8) * h[i]), 0.042 * h[i], (0.22, 1, 1))
                benek.parent = govde
    taslar.append(govde)

# parmak
ten = malzeme("ten", lin("e8ad8c"), 0.55)
parmak = bpy.data.objects.new("parmak", None)
sc.collection.objects.link(parmak)
for o in (silindir(ten, (-0.03, 0, 0), 0.0045, 0.06, (0, math.pi / 2, 0)), kure(ten, (0, 0, 0), 0.0045),
          kure(malzeme("tirnak", lin("f6cdbd"), 0.2), (-0.004, 0, 0.0033), 0.003, (1.4, 1, 0.45))):
    o.parent = parmak

# ölçek eşyaları (kameradan uzak tarafta)
altin = malzeme("altin", lin("ffd24a"), 0.35, 0.7)
ahsap = malzeme("ahsap", lin("a9714b"), 0.6)
koyu = malzeme("koyu", lin("2b2d42"), 0.5)
krem = malzeme("krem", lin("f1e9da"), 0.5)
kirmizi = malzeme("kirmizi", lin("d1495b"), 0.35)
mavi = malzeme("mavi", lin("4a90d9"), 0.25)
yesil = malzeme("yesil", lin("5a9e5f"), 0.8)

silindir(altin, (p[1], 0.027, 0.0012), 0.011, 0.0024)                                        # bozuk para
silindir(kirmizi, (p[4], 0.075, 0.004), 0.004, 0.13, (0, math.pi / 2, 0.35))                 # kalem
x, y = p[7], 0.19                                                                            # fincan
silindir(mavi, (x, y, 0.048), 0.04, 0.096)
ilkel(bpy.ops.mesh.primitive_torus_add, mavi, (x + 0.047, y, 0.05), rot=(math.pi / 2, 0, 0), major_radius=0.026, minor_radius=0.007)
x, y = p[10], 0.95                                                                           # sandalye
for dx in (-0.2, 0.2):
    for dy in (-0.2, 0.2):
        blok(ahsap, x + dx, y + dy, 0, 0.05, 0.05, 0.45)
blok(ahsap, x, y, 0.45, 0.5, 0.5, 0.05)
blok(ahsap, x, y + 0.23, 0.5, 0.5, 0.04, 0.5)
x, y = p[12], 1.9                                                                            # insan 1,7 m
for dx in (-0.12, 0.12):
    silindir(koyu, (x + dx, y, 0.42), 0.08, 0.84)
silindir(kirmizi, (x, y, 1.15), 0.22, 0.62)
kure(kirmizi, (x, y, 1.45), 0.22, (1, 1, 0.55))
kure(ten, (x, y, 1.68), 0.15)
for dx in (-0.29, 0.29):
    silindir(kirmizi, (x + dx, y, 1.12), 0.065, 0.62, (0, -0.15 if dx > 0 else 0.15, 0))
x, y = p[14], 4.3                                                                            # araba
blok(mavi, x, y, 0.35, 4.2, 1.8, 0.65, 0.35)
blok(krem, x - 0.3, y, 0.95, 2.2, 1.65, 0.6, 0.4)
for dx in (-1.35, 1.35):
    for dy in (-0.92, 0.92):
        silindir(koyu, (x + dx, y + dy, 0.36), 0.36, 0.25, (math.pi / 2, 0, 0))
for k, x in enumerate((p[15] + 2, p[16], p[17] - 4, p[18], p[19] + 12)):                     # ağaçlar
    y, b = 9 + k * 2.4, 3.5 + k * 1.1
    silindir(ahsap, (x, y, b * 0.28), b * 0.06, b * 0.56)
    for dx, dz, r in ((0, 0.75, 0.3), (-0.18, 0.62, 0.22), (0.2, 0.64, 0.23)):
        kure(yesil, (x + dx * b, y, dz * b), r * b)
for k in range(26):                                                                          # uzaktaki binalar
    bx, by = -10 + k * 7 + random.uniform(-2, 2), random.uniform(34, 60)
    bh = random.uniform(5, 24)
    renk = random.choice([krem, mavi, kirmizi, ahsap])
    blok(renk, bx, by, 0, random.uniform(3.5, 6), 4, bh, 0.04)
    for z in range(1, int(bh // 2.2)):
        blok(koyu, bx, by - 2.02, z * 2.2, 2.8, 0.05, 0.9)

# zemin: birkaç ölçekte benekli taş dokusu
zm = malzeme("zemin", lin("cdb99c"), 0.75)
nt = zm.node_tree
koor = nt.nodes.new("ShaderNodeNewGeometry")
karis = []
for olcek in (600.0, 40.0, 2.5, 0.15):
    gur = nt.nodes.new("ShaderNodeTexNoise")
    gur.inputs["Scale"].default_value = olcek
    gur.inputs["Detail"].default_value = 3
    nt.links.new(koor.outputs["Position"], gur.inputs["Vector"])
    karis.append(gur.outputs["Fac"])
top = karis[0]
for k in karis[1:]:
    n = nt.nodes.new("ShaderNodeMath")
    n.operation = "ADD"
    nt.links.new(top, n.inputs[0])
    nt.links.new(k, n.inputs[1])
    top = n.outputs[0]
harita = nt.nodes.new("ShaderNodeMapRange")
harita.inputs["From Min"].default_value, harita.inputs["From Max"].default_value = 1.6, 2.4
nt.links.new(top, harita.inputs["Value"])
rampa = nt.nodes.new("ShaderNodeValToRGB")
rampa.color_ramp.elements[0].color = (*lin("a58e72"), 1)
rampa.color_ramp.elements[1].color = (*lin("e2d2b6"), 1)
nt.links.new(harita.outputs[0], rampa.inputs[0])
nt.links.new(rampa.outputs[0], nt.nodes["Principled BSDF"].inputs["Base Color"])
nesne("zemin", kutu_mesh(-300, 500, -300, 300, -1, -0.00002), zm)

# toz (son vuruş)
toz_m = malzeme("toz", lin("e6d8bd"), 1.0)
toz_m.node_tree.nodes["Principled BSDF"].inputs["Alpha"].default_value = 0.4
toz_m.surface_render_method = "BLENDED"
tozlar = []
ilk_toz = None
for k in range(150):
    o = kure(toz_m, (0, 0, -5), 1.0) if ilk_toz is None else ilk_toz.copy()
    if ilk_toz is None:
        ilk_toz = o
    else:
        sc.collection.objects.link(o)
    tozlar.append((o, random.uniform(0.05, 0.98), random.uniform(-1, 1), random.uniform(0.5, 1.5), random.uniform(0.25, 1.0)))

# ışık, gök, kamera
dunya = bpy.data.worlds.new("gok")
sc.world = dunya
dunya.use_nodes = True
bg = dunya.node_tree.nodes["Background"]
bg.inputs["Color"].default_value = (*lin("a9d4f5"), 1)
bg.inputs["Strength"].default_value = 0.75
gunes = bpy.data.objects.new("gunes", bpy.data.lights.new("gunes", "SUN"))
gunes.data.energy, gunes.data.color, gunes.data.angle = 3.6, (1.0, 0.9, 0.76), math.radians(4)
gunes.rotation_euler = (math.radians(48), math.radians(-28), math.radians(10))
sc.collection.objects.link(gunes)
kam = bpy.data.objects.new("kam", bpy.data.cameras.new("kam"))
sc.collection.objects.link(kam)
sc.camera = kam
kam.data.lens = 45
kam.data.dof.use_dof = True


def yumusak(t, a, b):
    k = min(1.0, max(0.0, (t - a) / (b - a)))
    return k * k * (3 - 2 * k)


def on_taraf(t):
    """Zincirin o anki ucu: kesirli taş numarası (yumuşatılmış)."""
    top_, n_ = 0.0, 0
    for k in range(-8, 9):
        top_ += ara(t + k * 0.07, [T[0]] + T[1:], list(range(N)))
        n_ += 1
    return top_ / n_


def ayarla(t):
    a = acilar(t)
    for o, v in zip(taslar, a):
        o.rotation_euler = (0, v, 0)
    # parmak yaklaşıp iter, geri çekilir
    gel = ara(t, [0, 1.2, 3.0, 3.6, 4.4, 5.4], [-0.075, -0.04, -d[0] - 0.012, -d[0] + 0.0005, -0.05, -0.4])
    parmak.location = (gel, -0.001, 0.0082)
    # kamera: ölçek katlanarak büyür
    f = on_taraf(t)
    boy = H0 * ORAN ** f
    ux = ara(f, list(range(N)), p)
    hedef = Vector((ux + 0.35 * boy, 0, 0.5 * boy))
    uzak = Vector((-2.3, -4.1, 1.35)) * boy
    ac = yumusak(t, 0, 3.2)
    uzak *= 1.0 + 0.12 * (1 - ac) + 0.25 * (1 - yumusak(t, 3.4, 5.5))
    hedef.x -= 0.0095 * (1 - yumusak(t, 3.6, 5.8))
    # final: yana açılıp tüm zinciri göster
    z = yumusak(t, son_vurus + 0.5, DUR - 1.2)
    hedef = hedef.lerp(Vector((p[-1] - 3, 0, 4.0)), z)
    uzak = uzak.lerp(Vector((-26, -112, 44)), z)
    kon = hedef + uzak
    sars = t - son_vurus
    if 0 < sars < 1.1:
        kuvvet = 0.55 * (1 - sars / 1.1) ** 2
        kon += Vector((random.uniform(-1, 1), 0, random.uniform(-1, 1))) * kuvvet
    kam.location = kon
    kam.rotation_euler = (hedef - kam.location).to_track_quat("-Z", "Y").to_euler()
    uzaklik = (hedef - kam.location).length
    kam.data.clip_start, kam.data.clip_end = max(uzaklik * 0.02, 0.0005), 2000
    kam.data.dof.focus_distance = uzaklik
    kam.data.dof.aperture_fstop = max(0.045 / (uzaklik * 0.011 * (1 - 0.85 * z)), 0.1)
    # toz bulutu
    for o, yer, yan, hizi, buyuk in tozlar:
        if sars <= 0:
            o.location, o.scale = (0, 0, -5), (0.001,) * 3
            continue
        yay = 1 - math.exp(-sars * 2.2)
        o.location = (p[-1] + yer * h[-1] + yan * 2 * yay, (1 if yan > 0 else -1) * (h[-1] * 0.28 + 6 * yay * hizi * abs(yan)),
                      0.2 + 1.8 * yay * buyuk * hizi)
        r = max(0.001, buyuk * 2.1 * yay * max(0.0, 1 - sars / 3.2))
        o.scale = (r, r, r * 0.75)


# ---------- render ----------
r = sc.render
r.engine = "BLENDER_EEVEE"
sc.eevee.taa_render_samples = 32
r.resolution_x, r.resolution_y = 1920, 1080
sc.view_settings.view_transform = "AgX"
sc.view_settings.look = "AgX - High Contrast"
sc.view_settings.exposure = -0.05
r.image_settings.file_format = "JPEG"
r.image_settings.quality = 94

arg = sys.argv[sys.argv.index("--") + 1:]
(HERE / "kare").mkdir(exist_ok=True)
if arg[0] == "kare":
    kareler = [(f"ornek_{k}", float(v)) for k, v in enumerate(arg[1:])]
else:
    kareler = [(f"{i:04d}", i / FPS) for i in range(int(DUR * FPS))]
for ad, t in kareler:
    ayarla(t)
    r.filepath = str(HERE / "kare" / f"{ad}.jpg")
    bpy.ops.render.render(write_still=True)
    print("KARE", ad, round(t, 2), flush=True)
