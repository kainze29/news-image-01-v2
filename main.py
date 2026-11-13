"""news-image-01 entry: copy the bundled cover image to /output/entry.png.

The image (news.png, beside this file) sums up the world's news of
Friday 13 November 2026 in six labelled panels. This program does no
network and no rendering, so both runs write the same bytes.
Deterministic by construction: a byte-for-byte copy of a fixed file.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "news.png"),
                os.path.join(OUT_DIR, "entry.png"))
