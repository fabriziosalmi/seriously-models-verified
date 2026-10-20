#!/usr/bin/env python3
"""Render the dataset synthesis figures from verified data only.

fig04: highest published value to date per benchmark family (step lines; a dot marks each change).
"""

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402
from build_forensic_analysis import BG, HDR, MUTED, TXT, font, header  # noqa: E402

ROOT = evidence.ROOT
DATA_DIR = ROOT / "data"
SYNTH_DIR = ROOT / "assets" / "synthesis"
SERIES = [("MMLU", (37, 99, 235)), ("GSM8K", (217, 119, 6)), ("HumanEval", (5, 150, 105)), ("MATH", (220, 38, 38)),
          ("GPQA Diamond", (124, 58, 237)), ("SWE-bench Verified", (8, 145, 178))]


def fig_trajectory(monthly):
    W, H = 1600, 900
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    header(d, W, "FIG 4: HIGHEST PUBLISHED VALUE TO DATE, BY BENCHMARK (2021-01 TO 2026-10)",
           "Verified records only, dated by when the reporting document was public. Protocols differ between points; each cites a claim.")
    x0, x1, y0, y1 = 110, 1300, 130, 800
    n = len(monthly)
    X = lambda i: x0 + (x1 - x0) * i / (n - 1)  # noqa: E731
    Y = lambda v: y1 - (y1 - y0) * v / 100  # noqa: E731
    for t in range(0, 101, 10):
        d.line((x0, Y(t), x1, Y(t)), fill=(226, 232, 240))
        d.text((x0 - 40, Y(t) - 8), f"{t}", fill=MUTED, font=font(13))
    for i, m in enumerate(monthly):
        if m["month"].endswith("-01"):
            d.line((X(i), y0, X(i), y1), fill=(226, 232, 240))
            d.text((X(i) - 16, y1 + 10), m["month"][:4], fill=MUTED, font=font(14, bold=True))
    for fam, col in SERIES:
        pts, prev = [], None
        for i, m in enumerate(monthly):
            h = m["highest_published_to_date"].get(fam)
            if h:
                pts.append((i, h["value"], h["value"] != prev))
                prev = h["value"]
        for (ia, va, _), (ib, vb, _) in zip(pts, pts[1:]):
            d.line((X(ia), Y(va), X(ib), Y(va)), fill=col, width=3)
            d.line((X(ib), Y(va), X(ib), Y(vb)), fill=col, width=3)
        for i, v, changed in pts:
            if changed:
                d.ellipse((X(i) - 5, Y(v) - 5, X(i) + 5, Y(v) + 5), fill=col)
    ly = 150
    for fam, col in SERIES:
        last = monthly[-1]["highest_published_to_date"].get(fam)
        d.rectangle((1330, ly + 4, 1350, ly + 18), fill=col)
        d.text((1358, ly), fam, fill=TXT, font=font(15, bold=True))
        if last:
            d.text((1358, ly + 20), f"{last['value']:g} ({last['published_month']})", fill=MUTED, font=font(12, mono=True))
        ly += 56
    d.text((110, 850), "Scores in %. A step is drawn when a verified record exceeds the previous highest value; the protocol "
           "of each point is in data/monthly_benchmarks_2021_2026.json.", fill=MUTED, font=font(12, bold=True))
    im.save(SYNTH_DIR / "fig04_highest_published_value_by_benchmark.png", optimize=True)


def main():
    SYNTH_DIR.mkdir(parents=True, exist_ok=True)
    monthly = json.loads((DATA_DIR / "monthly_benchmarks_2021_2026.json").read_text())
    (SYNTH_DIR / "fig01_highest_published_value_by_benchmark.png").unlink(missing_ok=True)
    fig_trajectory(monthly)
    print("Rendered fig04.")


if __name__ == "__main__":
    main()
