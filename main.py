#!/usr/bin/env python3
"""Copy the bundled magazine-cover image to the output directory.

The entry ships one finished picture, news.png: a magazine-cover style
summary of the world news of Friday 13 November 2026. This program does no
drawing, no editing, and no network access. It takes the PNG bundled next
to this file and writes an identical copy into the output directory under
the name entry.png.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable. When that variable is unset or empty, /output is used.
"""

import os
import shutil
import struct
import sys

SOURCE_NAME = "news.png"
OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def check_png(path: str) -> bool:
    """Return True when path is a PNG of the expected size."""
    try:
        with open(path, "rb") as handle:
            header = handle.read(33)
    except OSError:
        return False
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return False
    if header[12:16] != b"IHDR":
        return False
    width, height = struct.unpack(">II", header[16:24])
    return width == EXPECTED_WIDTH and height == EXPECTED_HEIGHT


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    destination = os.path.join(output_dir, OUTPUT_NAME)

    if not os.path.isfile(source):
        print("error: bundled image not found: %s" % source, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)
    if not check_png(destination):
        print("error: copied file is not a valid %dx%d PNG: %s"
              % (EXPECTED_WIDTH, EXPECTED_HEIGHT, destination), file=sys.stderr)
        return 1
    print("wrote %s" % destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
