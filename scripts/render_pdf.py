#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def find_pdftoppm(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if path.is_file():
            return path
        raise FileNotFoundError(f"pdftoppm not found: {path}")

    on_path = shutil.which("pdftoppm")
    if on_path:
        return Path(on_path).resolve()

    home = Path.home()
    patterns = [
        ".cache/codex-runtimes/**/native/poppler/Library/bin/pdftoppm.exe",
        ".cache/codex-runtimes/**/native/poppler/bin/pdftoppm",
        ".codex/**/pdftoppm.exe",
        ".codex/**/pdftoppm",
    ]
    for pattern in patterns:
        matches = sorted(home.glob(pattern))
        if matches:
            return matches[-1].resolve()
    raise FileNotFoundError("pdftoppm is unavailable; load the bundled workspace dependencies or install Poppler")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render every PDF page to a PNG for visual QA.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=72)
    parser.add_argument("--pdftoppm")
    parser.add_argument("--force", action="store_true", help="Replace existing page-*.png files in output_dir")
    args = parser.parse_args()

    pdf = args.pdf.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    if args.dpi < 36 or args.dpi > 600:
        raise ValueError("--dpi must be between 36 and 600")

    output_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(output_dir.glob("page-*.png"))
    if existing and not args.force:
        raise FileExistsError(f"{output_dir} already contains page renders; use a new versioned directory or --force")
    if args.force:
        for path in existing:
            path.unlink()

    executable = find_pdftoppm(args.pdftoppm)
    prefix = output_dir / "page"
    subprocess.run(
        [str(executable), "-png", "-r", str(args.dpi), str(pdf), str(prefix)],
        check=True,
    )
    rendered = sorted(output_dir.glob("page-*.png"))
    if not rendered:
        raise RuntimeError("pdftoppm completed without producing page PNGs")
    print(f"rendered_pages={len(rendered)}")
    print(f"output_dir={output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

