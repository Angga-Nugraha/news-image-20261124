#!/usr/bin/env python3
"""news-image-20261124 — dense front page: 30 stories from Tuesday 24 November 2026.

Composes a 1024x1024 newspaper front page from the illustration assets in
assets/ (hero + 7 vignettes) and PIL-rendered text only. No network, stdlib +
Pillow only. Deterministic: the same assets always produce the same bytes.

Writes entry.png to $MAKEFUN_OUTPUT_DIR (default /output/entry.png) and
verifies the output against EXPECTED_SHA256 when it is set.
"""

import hashlib
import io
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Integrity check: sha256 of the exact entry.png bytes this program writes.
# Filled in after the first run; empty means "check disabled" (first run only).
EXPECTED_SHA256 = "923f2259ef2549337425a2903c0b0cc917c523a13fea4b72e347ac6931a04495"

MAX_BYTES = 1_048_576  # 1 MiB gate

PAPER = (246, 239, 219)       # #F6EFDB warm newsprint
BLUE = (16, 42, 67)           # #102A43 deep blue
GOLD = (201, 162, 39)         # #C9A227 masthead rule / subhead
INK = (25, 25, 25)            # #191919 headlines
CELL_FILL = (255, 253, 244)   # #FFFDF4 headline cells
CELL_BORDER = (217, 205, 178) # #D9CDB2 cell border
WHITE = (255, 255, 255)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def font(path, size):
    return ImageFont.truetype(path, size)


def crop_to_aspect(img, target_w, target_h):
    """Centre-crop img to the target aspect ratio. Never stretches."""
    target = target_w / target_h
    w, h = img.size
    aspect = w / h
    if aspect > target:  # too wide: crop width
        new_w = int(round(h * target))
        x0 = (w - new_w) // 2
        return img.crop((x0, 0, x0 + new_w, h))
    new_h = int(round(w / target))
    y0 = (h - new_h) // 2
    return img.crop((0, y0, w, y0 + new_h))


def paste_cover(draw_img, path, box, crop_box=None):
    """Paste an asset into box (x0, y0, x1, y1), cropping (never stretching)."""
    x0, y0, x1, y1 = box
    tw, th = x1 - x0, y1 - y0
    img = Image.open(ASSETS / path).convert("RGB")
    if crop_box is not None:
        img = img.crop(crop_box)
    else:
        img = crop_to_aspect(img, tw, th)
    img = img.resize((tw, th), Image.LANCZOS)
    draw_img.paste(img, (x0, y0))
    return img


def draw_tracked(draw, cx, baseline_y, text, fnt, fill, tracking=2):
    """Draw centred text with letter-spacing (tracking px between glyphs)."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * max(0, len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, baseline_y), ch, font=fnt, fill=fill, anchor="ls")
        x += w + tracking


def tag_pill(draw, x, y, text, fnt):
    """Small white-on-blue tag pill at the top-left of a picture."""
    tw = draw.textlength(text, font=fnt)
    bbox = fnt.getbbox(text)
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 8, 5
    pw, ph = int(tw) + 2 * pad_x, th + 2 * pad_y
    draw.rectangle([x, y, x + pw, y + ph], fill=BLUE)
    draw.text((x + pad_x, y + pad_y - bbox[1]), text, font=fnt, fill=WHITE)


def label_bar(draw, x, y, w, h, lines, fnt, line_height=25):
    """Deep-blue label bar with vertically centred white bold lines."""
    draw.rectangle([x, y, x + w, y + h], fill=BLUE)
    total = len(lines) * line_height
    start_y = y + (h - total) // 2
    for i, line in enumerate(lines):
        lw = draw.textlength(line, font=fnt)
        if lw > w - 24:
            raise ValueError("label line too wide: %r (%dpx > %dpx)" % (line, lw, w - 24))
        draw.text((x + 12, start_y + i * line_height), line,
                  font=fnt, fill=WHITE, anchor="la")


def vignette(img, draw, x, y, w, asset, lines, tag, img_h=118, bar_h=62):
    """One vignette panel: picture on top, label bar below, tag pill on picture."""
    paste_cover(img, asset, (x, y, x + w, y + img_h))
    label_bar(draw, x, y + img_h, w, bar_h, lines, font(SANS_BOLD, 21))
    tag_pill(draw, x + 6, y + 6, tag, font(SANS_BOLD, 13))
    draw.rectangle([x, y, x + w - 1, y + img_h + bar_h - 1], outline=BLUE, width=2)


def headline_cell(draw, x, y, lines, fnt):
    """One 242x51 headline-only cell: fill, 1px border, bold lines, 6px padding."""
    draw.rectangle([x, y, x + 242, y + 51], fill=CELL_FILL, outline=CELL_BORDER, width=1)
    for i, line in enumerate(lines):
        lw = draw.textlength(line, font=fnt)
        if lw > 230:
            raise ValueError("cell line too wide: %r (%dpx > 230px)" % (line, lw))
        draw.text((x + 6, y + 6 + i * 24), line, font=fnt, fill=INK, anchor="la")


def compose():
    img = Image.new("RGB", (1024, 1024), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- Masthead: y0-96, deep blue; gold rule y96-100 ----
    draw.rectangle([0, 0, 1024, 96], fill=BLUE)
    date_font = font(SERIF_BOLD, 50)
    date = "TUESDAY 24 NOVEMBER 2026"
    if draw.textlength(date, font=date_font) > 1024:
        raise ValueError("masthead date too wide")
    draw.text((512, 62), date, font=date_font, fill=WHITE, anchor="ms")
    draw_tracked(draw, 512, 88, "THE WORLD IN ONE IMAGE  \u2022  30 STORIES",
                 font(SANS_BOLD, 17), GOLD, tracking=2)
    draw.rectangle([0, 96, 1024, 100], fill=GOLD)

    # ---- Hero #1: image x16-400 y108-408, caption bar y408-476 ----
    # Source is a wide panorama (2736x912): left-window crop keeps the left
    # burning tanker whole plus the escort warship at the right edge.
    paste_cover(img, "hero.png", (16, 108, 400, 408), crop_box=(300, 0, 1467, 912))
    draw.rectangle([16, 108, 399, 407], outline=BLUE, width=2)
    draw.rectangle([16, 408, 400, 476], fill=BLUE)
    hero_head = "TANKERS HIT IN HORMUZ"
    hf = font(SANS_BOLD, 24)
    if draw.textlength(hero_head, font=hf) > 360:
        raise ValueError("hero headline too wide")
    draw.text((28, 412), hero_head, font=hf, fill=WHITE, anchor="la")
    sub = font(SANS, 16)
    draw.text((28, 437), "Iran claims three tankers hit mines in",
              font=sub, fill=WHITE, anchor="la")
    draw.text((28, 455), "Hormuz despite US escort \u2014 unverified",
              font=sub, fill=WHITE, anchor="la")

    # ---- Top vignettes 2x2: panels 296x180 ----
    vignette(img, draw, 408, 108, 296, "grok.png", ["GROK SUED"], "US / COURTS")
    vignette(img, draw, 712, 108, 296, "sanofi.png", ["SANOFI $41B DEAL"],
             "BUSINESS / PHARMA")
    vignette(img, draw, 408, 296, 296, "nato.png", ["NATO SPACE DEFENCE"],
             "EUROPE / DEFENCE")
    vignette(img, draw, 712, 296, 296, "nepal.png", ["NEPAL QUAKE"], "ASIA / DISASTER")

    # ---- Middle vignettes: panels 325x168 (last 326 wide) ----
    vignette(img, draw, 16, 484, 325, "cia.png", ["CIA + ODNI HACKED"], "US / CYBER",
             img_h=106)
    vignette(img, draw, 349, 484, 325, "huawei.png", ["HUAWEI CONVICTED"],
             "US / COURTS", img_h=106)
    vignette(img, draw, 682, 484, 326, "democrats.png",
             ["DEMOCRATS TAKE", "HOUSE 259"], "US / POLITICS", img_h=106)

    # ---- Headline grid: 4 cols x 6 rows, cells 242x51 ----
    # (col, row, [lines]) — row-major, brief priority order; row 6 cols 3-4
    # are the credit box. Explicit line breaks from the design spec.
    cells = [
        (0, 0, ["SHANGHAI BOSS", "PURGED"]),
        (1, 0, ["ENGLAND CRUSH", "AUSTRALIA"]),
        (2, 0, ["HAMAS SECURITY", "CHIEF KILLED"]),
        (3, 0, ["US CONFIDENCE", "SURGES"]),
        (0, 1, ["WHO FLEES EBOLA", "HOSPITAL"]),
        (1, 1, ["SENEGAL AFCON", "CHAMPIONS AGAIN"]),
        (2, 1, ["POPE'S DEVIL", "DIARY"]),
        (3, 1, ["SARKOZY TO TRIAL"]),
        (0, 2, ["FORT HOOD", "KILLER'S STAY BID"]),
        (1, 2, ["NVIDIA SLIDE", "AFTER BOUNCE"]),
        (2, 2, ["PUNJAB ALLIANCE", "RETURNS"]),
        (3, 2, ["CITI EYES", "VENEZUELA"]),
        (0, 3, ["TRUMP PARDONS", "TURKEYS"]),
        (1, 3, ["ZELENSKIY OWNS", "SHIP STRIKES"]),
        (2, 3, ["MICROSOFT", '"CODE RED"']),
        (3, 3, ["GIULIANI GETS TOP", "MEDAL"]),
        (0, 4, ["US TARIFFS LOOM"]),
        (1, 4, ["INDONESIA FIRE", "TOLL 26"]),
        (2, 4, ["IRAN RIAL RECORD", "LOW"]),
        (3, 4, ["O'HARE RADAR", "DELAYS"]),
        (0, 5, ["US ENVOY DOUBTS", "ISRAEL AID END"]),
        (1, 5, ["REAL MADRID", "BEAT PSV"]),
    ]
    xs = [16, 266, 516, 766]
    ys = [660, 719, 778, 837, 896, 955]
    hf21 = font(SANS_BOLD, 21)
    for col, row, lines in cells:
        headline_cell(draw, xs[col], ys[row], lines, hf21)

    # ---- Credit box: x516-1008 y955-1006 (spans row 6, cols 3-4) ----
    draw.rectangle([516, 955, 1008, 1006], fill=BLUE)
    draw.text((528, 965), "SOURCES: REUTERS \u2022 AP \u2022 BBC \u2022 NYT \u2022 WSJ \u2022 XINHUA",
              font=font(SANS_BOLD, 14), fill=WHITE, anchor="la")
    draw.text((528, 985), "AS REPORTED ON 24 NOVEMBER 2026 \u2014 30 STORIES",
              font=font(SANS, 13), fill=WHITE, anchor="la")

    return img


def encode(img):
    """Encode to PNG bytes; quantise to a 256-colour palette only if over the gate."""
    buf = io.BytesIO()
    img.save(buf, "PNG")
    data = buf.getvalue()
    if len(data) <= MAX_BYTES:
        return data, "RGB"
    pal = img.quantize(colors=256, method=Image.MEDIANCUT,
                       dither=Image.FLOYDSTEINBERG)
    buf = io.BytesIO()
    pal.save(buf, "PNG")
    data = buf.getvalue()
    if len(data) > MAX_BYTES:
        raise ValueError("entry still over 1 MiB after quantisation: %d bytes" % len(data))
    return data, "palette-256"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    img = compose()
    if img.size != (1024, 1024):
        raise ValueError("wrong canvas size: %r" % (img.size,))
    data, mode = encode(img)
    digest = hashlib.sha256(data).hexdigest()
    if EXPECTED_SHA256 and digest != EXPECTED_SHA256:
        raise SystemExit("integrity check FAILED: sha256 %s != EXPECTED %s"
                         % (digest, EXPECTED_SHA256))
    out_path = out_dir / "entry.png"
    out_path.write_bytes(data)
    print("wrote %s (%d bytes, sha256 %s, mode %s)"
          % (out_path, len(data), digest, mode))
    return 0


if __name__ == "__main__":
    sys.exit(main())
