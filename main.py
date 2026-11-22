#!/usr/bin/env python3
"""Write one short text for make.fun bounty make-the-ai-judge-feel-curious-20261122-2311.

Python 3.13, standard library only, no network.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "Every winter the lake freezes in a circle, not from the shore. The skaters learned to wait. Nobody has explained it. The man who measures it writes the number in a book, and the book has entries back to 1884, in four hands, and each one ends mid-sentence."

ASSERT_MESSAGE = "text must be between 1 and 280 characters"


def output_dir() -> Path:
    """Folder to write entry.txt into.

    MAKEFUN_OUTPUT_DIR wins when set, then OUTPUT_DIR, then /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, ASSERT_MESSAGE

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    entry = target / "entry.txt"
    # write_bytes keeps the text exactly as-is, with no trailing newline.
    entry.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
