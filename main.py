#!/usr/bin/env python3
"""news-image-20261123 entry program (Python 3.13, standard library only).

Copies the entry image shipped beside this file to the grader's output
directory, byte for byte, so both runs produce identical bytes.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
