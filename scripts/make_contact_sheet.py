#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> int:
    parser = argparse.ArgumentParser(description="Build compact contact sheets from page PNGs.")
    parser.add_argument("render_dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--pages-per-sheet", type=int, default=6)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--thumb-width", type=int, default=600)
    args = parser.parse_args()

    render_dir = args.render_dir.expanduser().resolve()
    output_dir = (args.output_dir or render_dir).expanduser().resolve()
    files = sorted(render_dir.glob("page-*.png"))
    if not files:
        raise FileNotFoundError(f"No page-*.png files found in {render_dir}")
    if args.pages_per_sheet < 1 or args.columns < 1 or args.thumb_width < 200:
        raise ValueError("pages-per-sheet, columns, and thumb-width must be positive practical values")

    with Image.open(files[0]) as sample:
        aspect = sample.height / sample.width
    thumb_w = args.thumb_width
    thumb_h = round(thumb_w * aspect)
    caption_h = 32
    gap = 28
    rows = math.ceil(args.pages_per_sheet / args.columns)
    sheet_w = gap * (args.columns + 1) + thumb_w * args.columns
    sheet_h = gap * (rows + 1) + (thumb_h + caption_h) * rows
    output_dir.mkdir(parents=True, exist_ok=True)

    for sheet_number, start in enumerate(range(0, len(files), args.pages_per_sheet), 1):
        canvas = Image.new("RGB", (sheet_w, sheet_h), "#E9ECF4")
        draw = ImageDraw.Draw(canvas)
        for slot, path in enumerate(files[start : start + args.pages_per_sheet]):
            col = slot % args.columns
            row = slot // args.columns
            x = gap + col * (thumb_w + gap)
            y = gap + row * (thumb_h + caption_h + gap)
            with Image.open(path) as source:
                page = source.convert("RGB")
                page.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            canvas.paste(page, (x, y))
            draw.text((x, y + thumb_h + 7), path.stem, fill="#303544")
        output = output_dir / f"contact-{sheet_number:02d}.png"
        canvas.save(output, optimize=True)
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

