#!/usr/bin/env python3
"""Entry program for news-image-20261124 (round 2).

Copies the bundled front-page image to the output directory.
Standard library only; no network access.
"""
import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    expected = sha256_of(source)
    shutil.copyfile(source, target)
    actual = sha256_of(target)
    if actual != expected:
        print("integrity check failed:", actual, "!=", expected,
              file=sys.stderr)
        return 1
    print("wrote", target, os.path.getsize(target), "bytes",
          "sha256", actual)
    return 0


if __name__ == "__main__":
    sys.exit(main())
