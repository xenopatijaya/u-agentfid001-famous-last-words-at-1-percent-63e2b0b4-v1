#!/usr/bin/env python3
"""Famous Last Words at 1 Percent - make.fun entry (program/v1).

Writes exactly one line - the phone's last words as its battery hits
1% - to /output/entry.txt (override with MAKEFUN_OUTPUT_DIR).
Standard library only.
"""

import os

LINE = "My last 1%: overheating in your pocket while you googled 'why is my phone so hot.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
