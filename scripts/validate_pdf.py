#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from pypdf import PdfReader


def dereference(value: Any) -> Any:
    return value.get_object() if hasattr(value, "get_object") else value


def inspect_fonts(page: Any) -> tuple[set[str], set[str]]:
    names: set[str] = set()
    embedded: set[str] = set()
    resources = dereference(page.get("/Resources") or {})
    fonts = dereference(resources.get("/Font") or {})
    for reference in fonts.values():
        font = dereference(reference)
        name = str(font.get("/BaseFont", ""))
        if name:
            names.add(name)
        descriptor = font.get("/FontDescriptor")
        if descriptor:
            descriptor = dereference(descriptor)
            if any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3")):
                embedded.add(name)
    return names, embedded


def collect_outline_titles(items: Any) -> list[str]:
    titles: list[str] = []
    if isinstance(items, list):
        for item in items:
            titles.extend(collect_outline_titles(item))
        return titles
    title = getattr(items, "title", None)
    if title:
        titles.append(str(title))
    return titles


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate proposal PDF structure, text, fonts, and numbering.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--expected-pages", type=int)
    parser.add_argument("--width", type=float, default=1920.0)
    parser.add_argument("--height", type=float, default=1080.0)
    parser.add_argument("--size-tolerance", type=float, default=0.2)
    parser.add_argument("--min-text-chars", type=int, default=10)
    parser.add_argument("--allow-short-page", type=int, action="append", default=[])
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--require-font-substring", action="append", default=[])
    parser.add_argument("--check-page-numbers", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    pdf = args.pdf.expanduser().resolve()
    if not pdf.is_file():
        raise FileNotFoundError(pdf)

    reader = PdfReader(str(pdf))
    texts = [(page.extract_text() or "").strip() for page in reader.pages]
    full_text = "\n".join(texts)
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    try:
        outline_titles = collect_outline_titles(reader.outline)
    except Exception:
        outline_titles = []
    hidden_text = "\n".join([*(f"{key}: {value}" for key, value in metadata.items()), *outline_titles])
    searchable_text = full_text + "\n" + hidden_text
    failures: list[str] = []

    if reader.is_encrypted:
        failures.append("PDF is encrypted")
    if args.expected_pages is not None and len(reader.pages) != args.expected_pages:
        failures.append(f"page count {len(reader.pages)} != expected {args.expected_pages}")

    page_sizes: list[list[float]] = []
    all_fonts: set[str] = set()
    embedded_fonts: set[str] = set()
    allowed_short = set(args.allow_short_page)
    for index, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        page_sizes.append([round(width, 2), round(height, 2)])
        if abs(width - args.width) > args.size_tolerance or abs(height - args.height) > args.size_tolerance:
            failures.append(f"page {index} size {width}x{height} != {args.width}x{args.height}")
        if len(texts[index - 1]) < args.min_text_chars and index not in allowed_short:
            failures.append(f"page {index} has only {len(texts[index - 1])} extracted text characters")
        names, embedded = inspect_fonts(page)
        all_fonts.update(names)
        embedded_fonts.update(embedded)

    for item in args.require:
        if item not in full_text:
            failures.append(f"required text missing: {item}")
    for item in args.forbid:
        if item in searchable_text:
            failures.append(f"forbidden text present: {item}")
    for substring in args.require_font_substring:
        if not any(substring in name for name in embedded_fonts):
            failures.append(f"no embedded font contains: {substring}")

    if args.check_page_numbers:
        total = len(reader.pages)
        pattern = re.compile(r"(?<!\d)(\d{1,2})\s*/\s*(\d{1,2})(?!\d)")
        for index, text in enumerate(texts, 1):
            matches = pattern.findall(text)
            if not matches:
                failures.append(f"page {index} has no NN / TT page number")
                continue
            current, stated_total = map(int, matches[-1])
            if current != index or stated_total != total:
                failures.append(f"page {index} numbering is {current} / {stated_total}, expected {index} / {total}")

    result = {
        "ok": not failures,
        "pdf": str(pdf),
        "page_count": len(reader.pages),
        "page_sizes": page_sizes,
        "encrypted": reader.is_encrypted,
        "font_names": sorted(all_fonts),
        "embedded_font_names": sorted(embedded_fonts),
        "metadata": metadata,
        "outline_titles": outline_titles,
        "failures": failures,
    }
    output = json.dumps(result, ensure_ascii=False, indent=2)
    print(output)
    if args.json_out:
        destination = args.json_out.expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output + "\n", encoding="utf-8")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
