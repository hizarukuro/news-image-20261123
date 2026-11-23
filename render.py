#!/usr/bin/env python3
"""Render the news-image-20261123 front page (1024x1024 PNG).

Draws everything with PIL vector-style shapes from one ordered story list,
so hero numbers, grid numbers, map pins and brief numbers always agree.
Run:  python3 render.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette
PAPER = (246, 241, 227)   # cream
INK = (20, 33, 61)        # navy ink
INK_SOFT = (58, 64, 84)
RED = (180, 35, 24)       # single red accent
RED_DARK = (150, 25, 18)
GOLD = (198, 142, 40)
GREEN = (31, 122, 74)
TEAL = (23, 94, 110)
GREY_LINE = (196, 188, 168)
CARD = (255, 253, 246)
MAP_LAND = (206, 214, 196)
MAP_SEA = (226, 234, 240)
CHIP_BG = (20, 33, 61)
WHITE = (255, 255, 255)

W, H = 1024, 1024

# ---------------------------------------------------------------- fonts
F = "/usr/share/fonts/truetype/noto/"
def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)

SERIF_B = lambda s: font("NotoSerif-Bold.ttf", s)
SANS = lambda s: font("NotoSans-Regular.ttf", s)
SANS_B = lambda s: font("NotoSans-Bold.ttf", s)
SANS_XB = lambda s: font("NotoSans-ExtraBold.ttf", s)
SANS_BLK = lambda s: font("NotoSans-Black.ttf", s)
DISP_B = lambda s: font("NotoSansDisplay-Bold.ttf", s)
DISP_XB = lambda s: font("NotoSansDisplay-ExtraBold.ttf", s)
DISP = lambda s: font("NotoSansDisplay-Regular.ttf", s)

# ---------------------------------------------------------------- stories
# ONE ordered list. n is derived from position (index + 1) everywhere.
STORIES = [
    # heroes
    dict(kind="hero", kicker="NVIDIA", headline="HUANG BACK AS CEO",
         deck="Nvidia reinstates Jensen Huang as chief executive, 11 days after "
              "he resigned, under pressure from President Trump. Shares +31% premarket.",
         chip="+31% PREMARKET", pin=(-125, 34)),
    dict(kind="hero", kicker="UKRAINE", headline="WARSHIP SUNK OFF LIBYA",
         deck="Zelensky confirms sea drones sank a Russian warship off the Libyan "
              "coast; Kyiv says a second warship was struck in the Baltic.",
         chip="KYIV SAYS", pin=(12, 33)),
    dict(kind="hero", kicker="HORMUZ", headline="TANKERS ABLAZE IN HORMUZ",
         deck="Tankers hit mines in the Strait of Hormuz and caught fire; Tehran "
              "vows \u201call available means\u201d against the US naval blockade.",
         chip="TEHRAN VOWS", pin=(58, 24)),
    # grid
    dict(kind="grid", kicker="GAZA", headline="UNRWA worker killed in Gaza airstrike",
         chip="3 KILLED", pin=(36, 30), icon="burst"),
    dict(kind="grid", kicker="CATALONIA", headline="Puigdemont free to return to Spain",
         chip="AFTER 9 YEARS", pin=(-2, 39), icon="flag"),
    dict(kind="grid", kicker="SYRIA", headline="US may train Syrian forces in demining",
         chip="1ST MISSION", pin=(40, 36), icon="helmet"),
    dict(kind="grid", kicker="COBALT", headline="Congo halts cobalt exports from 30 Nov",
         chip="FROM 30 NOV", pin=(23, -3), icon="rock"),
    dict(kind="grid", kicker="AMAZON", headline="Amazon to buy AI startup Decart",
         chip="$7.5 BN", pin=(-118, 48), icon="box"),
    dict(kind="grid", kicker="EU BUDGET", headline="Czech, Hungary reject \u20ac1.582tn EU budget",
         chip="\u20ac1.582 TN", pin=(2, 53), icon="stars"),
    dict(kind="grid", kicker="BANGLADESH", headline="Garment wage unrest shuts factories",
         chip="15% OFFER", pin=(90, 24), icon="factory"),
    dict(kind="grid", kicker="DENMARK", headline="Denmark upholds \u2018ghetto law\u2019 evictions",
         chip="91 LEASES", pin=(12, 58), icon="house"),
    dict(kind="grid", kicker="KALININGRAD", headline="Russia orders $576m ferries for exclave",
         chip="$576 M", pin=(24, 53), icon="ferry"),
    dict(kind="grid", kicker="MARKETS", headline="Wall St steadies after AI selloff",
         chip="S&P IN CORRECTION", pin=(-74, 40.7), icon="chart"),
    dict(kind="grid", kicker="NEPAL", headline="India pledges $1.6bn to Nepal",
         chip="$1.6 BN", pin=(84, 28), icon="mountain"),
    dict(kind="grid", kicker="AFRICA", headline="Kenya, DR Congo restore diplomatic ties",
         chip="TIES RESTORED", pin=(36.8, -1.3), icon="dove"),
    # briefs
    dict(kind="brief", kicker="BOXING",
         text="Fury reveals schizophrenia diagnosis from a 2015 breakdown; also bipolar."),
    dict(kind="brief", kicker="FOOTBALL",
         text="UK to host the 2035 Women\u2019s World Cup, FIFA confirms."),
    dict(kind="brief", kicker="PROTEST",
         text="Gen Z rallies sweep 25 European countries over wars, costs and climate."),
    dict(kind="brief", kicker="GERMANY",
         text="Qatar pledges $16.5bn in new investments on the emir\u2019s Berlin visit."),
    dict(kind="brief", kicker="WASHINGTON",
         text="Senate Republicans reject bid to limit Trump\u2019s Iran war powers, 51\u201348."),
    dict(kind="brief", kicker="MIGRATION",
         text="US appeals court lets Trump end TPS protections for Venezuelans."),
    dict(kind="brief", kicker="EL SALVADOR",
         text="Bukele seeks a third term after a constitution change."),
    dict(kind="brief", kicker="NEW YORK",
         text="Aber Kawas becomes the first Palestinian in the NY state Senate."),
    dict(kind="brief", kicker="POLAND",
         text="Russia tried to assassinate a Ukrainian rapper twice, Warsaw says."),
    dict(kind="brief", kicker="HEALTH",
         text="WHO chief calls for peace amid fighting in Ebola-hit DR Congo."),
    dict(kind="brief", kicker="SUDAN",
         text="Drone attacks kill four near Khartoum; a UN building damaged."),
    dict(kind="brief", kicker="ARMENIA",
         text="Proposes a new constitution, a step towards peace with Azerbaijan."),
    dict(kind="brief", kicker="CHINA",
         text="Sets 2030 targets to boost support for older people and childcare."),
    dict(kind="brief", kicker="HEALTH",
         text="NHS launches the world\u2019s largest AI breast-cancer screening trial."),
    dict(kind="brief", kicker="BELGIUM",
         text="Cost-of-living strike cancels flights."),
    dict(kind="brief", kicker="MEXICO",
         text="Soldiers attacked in the wake of a drug lord\u2019s arrest."),
    dict(kind="brief", kicker="ECONOMY",
         text="US business activity growth eases; flash PMI 54.6, a four-month low."),
    dict(kind="brief", kicker="IRAN",
         text="Lifts the 2,000km limit on its ballistic missiles."),
]

# Stat band figures: deliberately DISTINCT from every grid chip figure.
STATS = [
    ("51\u201348", "SENATE REJECTS IRAN WAR CURB"),
    ("74.5%", "KAWAS WINS NY SENATE SEAT"),
    ("54.6", "US FLASH PMI, A FOUR-MONTH LOW"),
    ("2,000 KM", "IRAN LIFTS MISSILE RANGE LIMIT"),
    ("$16.5 BN", "QATAR PLEDGES TO GERMANY"),
]

DATE_CHECK = [
    ("COP31 talks collapse, Antalya", "SUNDAY 22 NOV"),
    ("Democrats win 258 House seats", "SUNDAY 22 NOV"),
    ("ICJ: Myanmar committed genocide", "THU 19 NOV"),
    ("Dymer strike, 11 killed", "OVERNIGHT SAT\u2013SUN"),
    ("Eisenkot: settler arson \u2018Jewish terrorism\u2019", "SUN 22 NOV"),
    ("Indonesia candy-factory fire, 32 missing", "SUN 22 NOV"),
    ("Man Utd 4\u20130 Liverpool", "SUNDAY 22 NOV"),
    ("England\u2019s record rugby win over NZ", "WEEKEND"),
]

# Rough continent outlines (lon, lat) for the small world map.
CONTINENTS = [
    [(-168,66),(-140,70),(-125,71),(-110,68),(-95,69),(-85,66),(-80,73),
     (-65,60),(-55,52),(-60,45),(-70,42),(-75,35),(-80,32),(-85,29),
     (-90,21),(-97,16),(-105,20),(-115,28),(-125,40),(-125,49),
     (-140,60),(-155,58),(-165,60)],  # North America
    [(-80,10),(-75,5),(-60,5),(-50,0),(-40,-5),(-35,-10),(-40,-20),
     (-48,-28),(-58,-35),(-65,-40),(-70,-50),(-73,-40),(-72,-30),
     (-70,-18),(-77,-12),(-80,-5)],  # South America
    [(-10,36),(-9,43),(-2,48),(0,50),(5,53),(8,57),(10,59),(18,56),
     (21,55),(24,59),(28,60),(30,62),(32,70),(25,71),(18,70),(12,65),
     (5,60),(-5,58),(-10,52),(-10,43)],  # Europe
    [(-17,15),(-10,30),(0,36),(10,37),(20,32),(32,31),(35,28),(40,15),
     (43,11),(48,11),(51,10),(44,0),(40,-10),(35,-20),(32,-28),
     (26,-34),(19,-35),(15,-27),(12,-18),(9,-1),(9,4),(-8,5),(-13,8),
     (-17,12)],  # Africa
    [(32,70),(40,68),(55,68),(68,73),(90,75),(110,76),(130,72),(160,70),
     (178,66),(170,60),(162,56),(158,52),(142,50),(140,40),(130,35),
     (127,35),(122,30),(120,25),(110,20),(105,10),(100,8),(95,15),
     (90,22),(85,20),(80,10),(77,8),(72,20),(66,25),(60,25),(57,26),
     (52,28),(48,30),(44,29),(40,32),(36,36),(32,36)],  # Asia
    [(113,-22),(114,-30),(115,-35),(120,-34),(129,-32),(137,-35),
     (140,-38),(147,-39),(150,-37),(153,-27),(146,-19),(142,-11),
     (136,-12),(132,-12),(126,-14),(122,-17),(114,-21)],  # Australia
]

# ---------------------------------------------------------------- helpers
def wrap(d, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def center(d, cx, y, text, fnt, fill):
    d.text((cx, y), text, font=fnt, fill=fill, anchor="ma")

def chip(d, x, y, text, fnt, bg=CHIP_BG, fg=WHITE):
    w = int(d.textlength(text, font=fnt)) + 12
    h = 17
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=bg)
    d.text((x + 6, y + 3), text, font=fnt, fill=fg)
    return w

def num_badge(d, cx, cy, n, r=11, bg=RED, fg=WHITE, fnt=None):
    fnt = fnt or SANS_XB(12)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg, outline=WHITE, width=2)
    d.text((cx, cy), str(n), font=fnt, fill=fg, anchor="mm")

# ---------------------------------------------------------------- hero art
def art_nvidia(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 46, 32))
    # circuit traces
    for i in range(5):
        yy = y + 18 + i * 26
        d.line([x + 8, yy, x + w - 90, yy], fill=(46, 130, 84), width=2)
        d.ellipse([x + w - 92, yy - 3, x + w - 86, yy + 3], fill=(46, 130, 84))
    # the chip
    cx0, cy0, cw, ch = x + 52, y + 34, 128, 92
    for k in range(6):
        px = cx0 + 14 + k * 20
        d.line([px, cy0 - 12, px, cy0], fill=GOLD, width=3)
        d.line([px, cy0 + ch, px, cy0 + ch + 12], fill=GOLD, width=3)
    d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + ch], radius=10,
                        fill=(24, 68, 44), outline=GOLD, width=3)
    d.rounded_rectangle([cx0 + 26, cy0 + 26, cx0 + cw - 26, cy0 + ch - 26],
                        radius=6, fill=(13, 38, 26), outline=(70, 170, 110), width=2)
    d.text((cx0 + cw // 2, cy0 + ch // 2), "NVDA", font=SANS_BLK(24),
           fill=(118, 185, 0), anchor="mm")
    # rising arrow +31%
    ax = x + w - 92
    d.line([(ax, y + h - 26), (ax + 26, y + h - 62), (ax + 52, y + h - 96)],
           fill=(118, 185, 0), width=5)
    d.polygon([(ax + 52, y + h - 106), (ax + 66, y + h - 88), (ax + 44, y + h - 88)],
              fill=(118, 185, 0))
    d.text((x + w - 8, y + h - 30), "+31%", font=SANS_BLK(20),
           fill=(118, 185, 0), anchor="ra")

def art_ukraine(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(176, 208, 224))
    d.rectangle([x, y, x + w, y + 58], fill=(214, 228, 236))
    d.ellipse([x + w - 62, y + 12, x + w - 18, y + 56], fill=(240, 214, 130))
    # sea bands
    for i, col in enumerate([(96, 140, 170), (70, 118, 152), (52, 100, 136)]):
        yy = y + 62 + i * 34
        d.rectangle([x, yy, x + w, yy + 34], fill=col)
    # warship silhouette
    sx, sy = x + 66, y + 118
    d.polygon([(sx, sy), (sx + 170, sy), (sx + 158, sy + 22),
               (sx + 12, sy + 22)], fill=(52, 58, 66))
    d.rectangle([sx + 66, sy - 26, sx + 112, sy], fill=(52, 58, 66))
    d.rectangle([sx + 82, sy - 42, sx + 92, sy - 26], fill=(52, 58, 66))
    d.line([sx + 30, sy - 18, sx + 30, sy], fill=(52, 58, 66), width=3)
    # explosion burst on the hull
    bx, by = sx + 150, sy - 6
    for r, col in [(26, (255, 122, 26)), (18, (255, 176, 32)), (10, (255, 236, 150))]:
        pts = []
        for k in range(12):
            ang = k * 30
            import math
            rr = r if k % 2 == 0 else r * 0.55
            pts.append((bx + rr * math.cos(math.radians(ang)),
                        by + rr * math.sin(math.radians(ang))))
        d.polygon(pts, fill=col)
    # smoke
    d.ellipse([bx - 8, by - 52, bx + 22, by - 22], fill=(90, 90, 90))
    d.ellipse([bx + 2, by - 66, bx + 30, by - 38], fill=(120, 120, 120))
    # two sea drones with wakes
    for dx in (x + 18, x + 236):
        d.polygon([(dx, y + h - 18), (dx + 34, y + h - 18),
                   (dx + 28, y + h - 8), (dx + 6, y + h - 8)],
                  fill=(30, 34, 40))
        d.line([dx - 22, y + h - 12, dx, y + h - 12], fill=WHITE, width=2)

def art_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(64, 32, 22))
    d.rectangle([x, y, x + w, y + 62], fill=(214, 122, 52))
    # low sun, top-left, clear of the smoke
    d.ellipse([x + 22, y + 10, x + 66, y + 54], fill=(250, 196, 90))
    d.rectangle([x, y + 96, x + w, y + h], fill=(38, 52, 66))
    # tanker 1 (left, burning)
    tx, ty = x + 26, y + 118
    d.rectangle([tx, ty, tx + 128, ty + 18], fill=(24, 24, 28))
    d.rectangle([tx + 96, ty - 16, tx + 116, ty], fill=(24, 24, 28))
    d.rectangle([tx + 8, ty - 10, tx + 22, ty], fill=(24, 24, 28))
    # tanker 2 (right, burning)
    tx2, ty2 = x + 176, y + 126
    d.rectangle([tx2, ty2, tx2 + 118, ty2 + 16], fill=(30, 30, 34))
    d.rectangle([tx2 + 12, ty2 - 14, tx2 + 30, ty2], fill=(30, 30, 34))
    # flames rising from the decks + smoke columns
    import math
    for fx, fy, s in [(tx + 64, ty - 2, 30), (tx2 + 64, ty2 - 2, 26),
                      (tx + 110, ty - 4, 18)]:
        for r, col in [(s, (255, 110, 20)), (s * 0.65, (255, 176, 32)),
                       (s * 0.35, (255, 236, 150))]:
            pts = []
            for k in range(10):
                ang = k * 36 - 90
                rr = r if k % 2 == 0 else r * 0.5
                pts.append((fx + rr * math.cos(math.radians(ang)) * 0.8,
                            fy + rr * math.sin(math.radians(ang))))
            d.polygon(pts, fill=col)
        d.ellipse([fx - 10, fy - s - 34, fx + 18, fy - s - 6], fill=(40, 40, 44))
        d.ellipse([fx - 2, fy - s - 48, fx + 26, fy - s - 20], fill=(70, 70, 74))
    # fire glints on the water under the tankers
    for i in range(6):
        d.line([x + 14 + i * 48, y + h - 14, x + 44 + i * 48, y + h - 14],
               fill=(214, 122, 52), width=2)

ART = {0: art_nvidia, 1: art_ukraine, 2: art_hormuz}

# ---------------------------------------------------------------- grid icons
def icon(d, x, y, name):
    """Small 24x24 navy line icon."""
    c = INK
    if name == "burst":
        import math
        pts = []
        for k in range(12):
            ang = k * 30
            r = 11 if k % 2 == 0 else 5
            pts.append((x + 12 + r * math.cos(math.radians(ang)),
                        y + 12 + r * math.sin(math.radians(ang))))
        d.polygon(pts, outline=c, width=2)
    elif name == "flag":
        d.line([x + 6, y + 2, x + 6, y + 22], fill=c, width=2)
        d.polygon([(x + 6, y + 3), (x + 21, y + 7), (x + 6, y + 12)], outline=c, width=2)
    elif name == "helmet":
        d.arc([x + 3, y + 4, x + 21, y + 18], 180, 360, fill=c, width=2)
        d.line([x + 2, y + 18, x + 22, y + 18], fill=c, width=2)
        d.line([x + 12, y + 4, x + 12, y + 10], fill=c, width=2)
    elif name == "rock":
        d.polygon([(x + 12, y + 2), (x + 21, y + 10), (x + 18, y + 21),
                   (x + 6, y + 21), (x + 3, y + 10)], outline=c, width=2)
        d.line([x + 8, y + 9, x + 16, y + 9], fill=c, width=2)
    elif name == "box":
        d.polygon([(x + 12, y + 3), (x + 21, y + 8), (x + 21, y + 18),
                   (x + 12, y + 22), (x + 3, y + 18), (x + 3, y + 8)],
                  outline=c, width=2)
        d.line([x + 3, y + 8, x + 12, y + 12], fill=c, width=2)
        d.line([x + 21, y + 8, x + 12, y + 12], fill=c, width=2)
        d.line([x + 12, y + 12, x + 12, y + 22], fill=c, width=2)
    elif name == "stars":
        for k in range(8):
            import math
            ang = k * 45
            px = x + 12 + 8 * math.cos(math.radians(ang))
            py = y + 12 + 8 * math.sin(math.radians(ang))
            d.ellipse([px - 1.5, py - 1.5, px + 1.5, py + 1.5], fill=c)
    elif name == "factory":
        d.polygon([(x + 3, y + 21), (x + 3, y + 10), (x + 8, y + 10),
                   (x + 8, y + 6), (x + 13, y + 6), (x + 13, y + 10),
                   (x + 21, y + 10), (x + 21, y + 21)], outline=c, width=2)
        d.line([x + 17, y + 3, x + 17, y + 10], fill=c, width=2)
    elif name == "house":
        d.polygon([(x + 12, y + 3), (x + 21, y + 11), (x + 3, y + 11)],
                  outline=c, width=2)
        d.rectangle([x + 6, y + 11, x + 18, y + 21], outline=c, width=2)
        d.rectangle([x + 10, y + 15, x + 14, y + 21], fill=c)
    elif name == "ferry":
        d.polygon([(x + 2, y + 14), (x + 22, y + 14), (x + 19, y + 20),
                   (x + 5, y + 20)], fill=c)
        d.rectangle([x + 7, y + 7, x + 17, y + 13], outline=c, width=2)
        d.line([x + 12, y + 3, x + 12, y + 7], fill=c, width=2)
    elif name == "chart":
        d.line([(x + 3, y + 19), (x + 9, y + 12), (x + 14, y + 15),
                (x + 21, y + 4)], fill=c, width=2)
        d.polygon([(x + 21, y + 4), (x + 16, y + 4), (x + 21, y + 9)], fill=c)
        d.line([x + 3, y + 21, x + 21, y + 21], fill=c, width=2)
    elif name == "mountain":
        d.polygon([(x + 2, y + 21), (x + 9, y + 7), (x + 14, y + 14),
                   (x + 17, y + 9), (x + 22, y + 21)], outline=c, width=2)
    elif name == "dove":
        d.ellipse([x + 4, y + 8, x + 20, y + 16], outline=c, width=2)
        d.polygon([(x + 14, y + 6), (x + 21, y + 3), (x + 19, y + 10)], fill=c)
        d.line([x + 6, y + 16, x + 4, y + 21], fill=c, width=2)
        d.line([x + 10, y + 16, x + 9, y + 21], fill=c, width=2)

# ---------------------------------------------------------------- build
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    heroes = [s for s in STORIES if s["kind"] == "hero"]
    grid = [s for s in STORIES if s["kind"] == "grid"]
    briefs = [s for s in STORIES if s["kind"] == "brief"]

    # ---- masthead
    center(d, W // 2, 10, "THE DAY\u2019S WORLD NEWS \u2014 IN ONE IMAGE",
           SANS_B(11), INK_SOFT)
    center(d, W // 2, 20, "THE WORLD IN ONE DAY", SERIF_B(42), INK)
    d.line([16, 88, 300, 88], fill=GREY_LINE, width=2)
    d.line([724, 88, 1008, 88], fill=GREY_LINE, width=2)
    center(d, W // 2, 64, "MONDAY 23 NOVEMBER 2026", SANS_BLK(20), RED)
    d.line([16, 96, 1008, 96], fill=INK, width=3)

    # ---- stat band (figures distinct from every grid chip)
    bx, by, bw, bh = 16, 100, 186, 40
    for i, (fig, label) in enumerate(STATS):
        x = bx + i * (bw + 8)
        d.rectangle([x, by, x + bw, by + bh], fill=CARD, outline=GREY_LINE, width=1)
        center(d, x + bw // 2, by + 4, fig, SANS_BLK(19), INK)
        center(d, x + bw // 2, by + 26, label, SANS_B(8), INK_SOFT)
    d.line([16, 148, 1008, 148], fill=INK, width=2)

    # ---- heroes (numbers from the one list: 1, 2, 3)
    hx, hy, hw, hh = 16, 150, 325, 296
    for i, s in enumerate(heroes):
        n = i + 1
        x = hx + i * (hw + 7)
        d.rectangle([x, hy, x + hw, hy + hh], fill=CARD, outline=GREY_LINE, width=1)
        ART[i](d, x + 1, hy + 1, hw - 2, 158)
        num_badge(d, x + 18, hy + 18, n, r=13)
        ty = hy + 168
        d.text((x + 12, ty), f"{n} \u00b7 {s['kicker']}", font=SANS_XB(11), fill=RED)
        ty += 18
        for line in wrap(d, s["headline"], DISP_XB(20), hw - 24):
            d.text((x + 12, ty), line, font=DISP_XB(20), fill=INK)
            ty += 23
        ty += 2
        for line in wrap(d, s["deck"], DISP(12), hw - 24):
            d.text((x + 12, ty), line, font=DISP(12), fill=INK_SOFT)
            ty += 15
        chip(d, x + 12, hy + hh - 26, s["chip"], SANS_XB(9))

    # ---- grid header + grid (numbers 4..15 from the one list)
    gy = 456
    d.text((16, gy), "THE WORLD \u2014 12 MORE STORIES", font=SANS_XB(12), fill=INK)
    d.line([16, gy + 18, 1008, gy + 18], fill=INK, width=2)
    gx, gy0, gw, gh = 16, 480, 243, 70
    for j, s in enumerate(grid):
        n = 4 + j
        col, row = j % 4, j // 4
        x = gx + col * (gw + 4)
        y = gy0 + row * (gh + 4)
        d.rectangle([x, y, x + gw, y + gh], fill=CARD, outline=GREY_LINE, width=1)
        icon(d, x + 8, y + 8, s["icon"])
        d.text((x + 38, y + 6), f"{n} \u00b7 {s['kicker']}", font=SANS_XB(10), fill=RED)
        ty = y + 22
        for line in wrap(d, s["headline"], SANS_B(11), gw - 48)[:2]:
            d.text((x + 38, ty), line, font=SANS_B(11), fill=INK)
            ty += 13
        chip(d, x + 38, y + gh - 20, s["chip"], SANS_XB(8))

    # ---- bottom section
    by0 = 708
    d.line([16, by0, 1008, by0], fill=INK, width=2)
    # briefs header (left)
    d.text((16, by0 + 8), "IN BRIEF \u2014 18 MORE", font=SANS_XB(12), fill=INK)
    # map header (right)
    d.text((688, by0 + 8), "WHERE IT HAPPENED", font=SANS_XB(12), fill=INK)
    d.line([16, by0 + 28, 676, by0 + 28], fill=GREY_LINE, width=1)
    d.line([688, by0 + 28, 1008, by0 + 28], fill=GREY_LINE, width=1)

    # briefs: two columns of 9, rows 27px, uniform lead-in "N \u00b7 KICKER \u2014 text"
    bx0, by1 = 16, by0 + 36
    bw2, row_h = 324, 27
    for k, s in enumerate(briefs):
        n = 16 + k
        col, row = k % 2, k // 2
        x = bx0 + col * (bw2 + 12)
        y = by1 + row * row_h
        lead = f"{n} \u00b7 {s['kicker']} \u2014 "
        full = lead + s["text"]
        lines = wrap(d, full, SANS(11), bw2)[:2]
        # bold the lead-in on line 1 by drawing lead bold then rest regular
        first = lines[0]
        if first.startswith(lead):
            d.text((x, y), lead, font=SANS_B(11), fill=INK)
            rest = first[len(lead):]
            d.text((x + d.textlength(lead, font=SANS_B(11)), y),
                   rest, font=SANS(11), fill=INK)
        else:
            d.text((x, y), first, font=SANS(11), fill=INK)
        if len(lines) > 1:
            d.text((x, y + 13), lines[1], font=SANS(11), fill=INK)

    # ---- world map with numbered pins (stories 1..15)
    mx, my, mw, mh = 688, by0 + 36, 320, 140
    d.rectangle([mx, my, mx + mw, my + mh], fill=MAP_SEA, outline=GREY_LINE, width=1)
    def proj(lon, lat):
        px = mx + (lon + 170) / 360.0 * mw
        py = my + (75 - lat) / 133.0 * mh
        return px, py
    for cont in CONTINENTS:
        d.polygon([proj(lon, lat) for lon, lat in cont],
                  fill=MAP_LAND, outline=(150, 158, 140))
    for i, s in enumerate(STORIES[:15]):
        n = i + 1
        px, py = proj(*s["pin"])
        num_badge(d, px, py, n, r=7, bg=RED, fnt=SANS_XB(7))

    # ---- DATE CHECK box (red): visibly discards Sunday/earlier stories
    dx, dy, dw = 688, by0 + 184, 320
    dh = 122
    d.rectangle([dx, dy, dx + dw, dy + dh], fill=(255, 244, 242),
                outline=RED, width=2)
    d.text((dx + 10, dy + 6), "DATE CHECK \u2014 NOT MONDAY",
           font=SANS_XB(11), fill=RED)
    d.text((dx + 10, dy + 22), "Big stories from earlier days \u2014 left out:",
           font=SANS(10), fill=INK_SOFT)
    yy = dy + 38
    for title, when in DATE_CHECK:
        d.line([dx + 11, yy + 1, dx + 17, yy + 7], fill=RED, width=2)
        d.line([dx + 17, yy + 1, dx + 11, yy + 7], fill=RED, width=2)
        d.text((dx + 24, yy), title, font=SANS(10), fill=INK)
        tw = d.textlength(when, font=SANS_B(9))
        d.text((dx + dw - 8 - tw, yy), when, font=SANS_B(9), fill=RED)
        yy += 10
        # second line only if needed; keep single-line items (all fit)
    # sources + method note, under the briefs (left column)
    sy = by1 + 9 * row_h + 6
    center(d, 16 + 330, sy,
           "33 STORIES \u00b7 ALL FIRST REPORTED MONDAY 23 NOVEMBER 2026",
           SANS_B(10), INK_SOFT)
    center(d, 16 + 330, sy + 14,
           "SOURCES: REUTERS \u00b7 BBC \u00b7 AL JAZEERA \u2014 CLAIMS LABELLED AS REPORTED",
           SANS(9), INK_SOFT)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    import hashlib
    digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print("wrote", out, img.size, os.path.getsize(out), "bytes, sha256", digest)

if __name__ == "__main__":
    main()
