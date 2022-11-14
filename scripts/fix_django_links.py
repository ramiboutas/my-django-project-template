#!/usr/bin/env python
from __future__ import annotations

import argparse
import re


def main(argv=None):  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="Fix files to use ´stable´ Django docs links"
    )
    parser.add_argument(
        "file", nargs="+", type=argparse.FileType("r+", encoding="utf-8")
    )
    args = parser.parse_args(argv)

    exit_code = 0

    for file in args.file:
        if fix_file(file):
            exit_code = 1
        file.close()

    return exit_code


def fix_file(file):  # pragma: no cover
    orig_text = file.read()

    new_text, num_substitutions = re.subn(
        r"https://docs\.djangoproject\.com/en/\d\.\d/",
        "https://docs.djangoproject.com/en/stable/",
        orig_text,
    )
    changed = num_substitutions > 0

    if changed:
        print(f"Fixing {file.name}")
        file.seek(0)
        file.write(new_text)
        file.truncate()
    return changed


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
