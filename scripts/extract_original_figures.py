#!/usr/bin/env python3
"""Build references to the primary-source pages cited in the month-by-month dossier.

The source documents belong to their authors and are not redistributed. For each cited page this script writes a
reference to data/source_pages.json: the pinned source, the physical PDF page, a link that opens that page at the
pinned address (arXiv PDF by version with #page=N, Wayback capture, or vendor CDN file), and the verbatim table and
figure captions found on that page. Captions are extracted from the page text, never typed by hand. The month is the
arXiv first-version month taken from the identifier (YYMM), or the manifest month for other documents.

    python3 scripts/extract_original_figures.py            # write data/source_pages.json
    python3 scripts/extract_original_figures.py --render   # also render the pages locally to assets/original/
                                                            # (git-ignored; for personal inspection only)
"""

import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = evidence.ROOT
DATA_DIR = ROOT / "data"
RENDER_DIR = ROOT / "assets" / "original"

# (source id, physical PDF page). Pages were checked against the table/figure they are cited for.
PAGES = [
    ("arxiv_2009.03300", 2), ("arxiv_2009.03300", 5), ("arxiv_2103.03874", 5), ("arxiv_2107.03374", 7),
    ("arxiv_2110.14168", 8), ("arxiv_2112.11446", 11), ("arxiv_2201.11903", 5), ("arxiv_2201.11903", 20),
    ("arxiv_2203.11171", 5), ("arxiv_2203.15556", 11), ("arxiv_2203.15556", 12), ("arxiv_2204.02311", 22),
    ("arxiv_2204.02311", 23), ("arxiv_2204.02311", 25), ("arxiv_2206.14858", 7), ("arxiv_2206.14858", 8),
    ("arxiv_2210.02414", 8), ("arxiv_2210.11416", 2), ("arxiv_2210.11416", 8), ("arxiv_2211.09085", 15),
    ("arxiv_2302.13971", 6), ("arxiv_2302.13971", 7), ("arxiv_2303.08774", 7), ("arxiv_2305.10403", 15),
    ("anthropic_claude2_card", 10), ("arxiv_2307.09288", 8), ("arxiv_2308.12950", 6), ("arxiv_2310.06825", 3),
    ("arxiv_2310.06825", 4), ("arxiv_2312.11805", 8), ("arxiv_2401.04088", 4), ("arxiv_2401.04088", 5),
    ("arxiv_2403.05530", 30), ("anthropic_claude3_card", 6), ("arxiv_2405.04434", 19),
    ("anthropic_claude35_addendum", 2), ("arxiv_2407.10671", 9), ("arxiv_2407.21783", 3),
    ("anthropic_claude35_oct_addendum", 6), ("arxiv_2412.19437", 1), ("arxiv_2412.19437", 31),
    ("arxiv_2501.12948v1", 13), ("arxiv_2505.09388", 14), ("arxiv_2506.10910", 10), ("arxiv_2507.20534", 1),
    ("arxiv_2508.06471", 16), ("arxiv_2508.10925", 6), ("arxiv_2512.02556", 1), ("arxiv_2602.02276", 12),
    ("arxiv_2602.15763", 23), ("openai_o3mini_system_card", 28),
]

# A caption starts a line: "Table 7: ...", "Table 2. ...", "Figure 1 | ...", "Table 7 This table ..."
CAPTION_RE = re.compile(r"^\s*((?:Table|Figure)\s+[A-Z]?\d+(?:\.\d+)?(?:\s*[:|.]\s*|\s+)[A-Z][^\n]{0,160})", re.M)


def doc_month(source: dict) -> str:
    if source.get("kind") == "arxiv":
        yymm = source["arxiv_id"][:4]
        return f"20{yymm[:2]}-{yymm[2:]}"
    return source["month"]


def page_link(source: dict, page: int) -> str:
    """Address of the pinned document, opened at the physical page where the viewer supports it."""
    return f"{source['url']}#page={page}" if source["ext"] == "pdf" else source["url"]


def page_captions(source_id: str, page: int) -> list:
    text = subprocess.run(["pdftotext", "-raw", "-f", str(page), "-l", str(page), str(evidence.source_path(source_id)), "-"],
                          capture_output=True, text=True, errors="ignore", check=True).stdout
    seen, out = set(), []
    for m in CAPTION_RE.finditer(text):
        cap = evidence.normalise(m.group(1))
        head = re.match(r"(Table|Figure)\s+[A-Z]?\d+(?:\.\d+)?", cap).group(0)
        if head not in seen:
            seen.add(head)
            rest = re.split(r"(?<=[a-z0-9)])\.\s", cap[len(head):].lstrip(" .:|"), maxsplit=1)[0]
            out.append(f"{head}: {rest.rstrip('.')}.")
    return out


def render(source_id: str, page: int, dest: Path):
    prefix = Path("/tmp") / f"seriously_models_page_{dest.stem}"
    subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", str(page), "-l", str(page), "-singlefile",
                    str(evidence.source_path(source_id)), str(prefix)], check=True)
    with Image.open(f"{prefix}.png") as im:
        im = im.convert("RGB")
        bbox = ImageChops.difference(im, Image.new(im.mode, im.size, (255, 255, 255))).getbbox()
        (im.crop(bbox) if bbox else im).save(dest, format="PNG", optimize=True)
    Path(f"{prefix}.png").unlink()


def main(argv):
    manifest = evidence.manifest()
    out = []
    for sid, page in PAGES:
        src = manifest[sid]
        if not evidence.source_sha_ok(sid):
            raise AssertionError(f"{sid}: pinned source missing or modified")
        month = doc_month(src)
        out.append({"slug": f"{month}_{sid}_p{page}", "month": month, "source_id": sid, "page": page,
                    "title": src.get("official_title") or src["title"], "version": src.get("version") or src.get("capture"),
                    "link": page_link(src, page), "captions_on_page": page_captions(sid, page)})
        if "--render" in argv:
            RENDER_DIR.mkdir(parents=True, exist_ok=True)
            render(sid, page, RENDER_DIR / f"{out[-1]['slug']}.png")
    out.sort(key=lambda x: (x["month"], x["slug"]))
    (DATA_DIR / "source_pages.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(out)} source page references to data/source_pages.json"
          + (f"; rendered pages to {RENDER_DIR.relative_to(ROOT)}/ (git-ignored)" if "--render" in argv else "."))


if __name__ == "__main__":
    main(sys.argv[1:])
