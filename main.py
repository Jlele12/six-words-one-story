#!/usr/bin/env python3
"""Six Words, One Story - make.fun competition entry.

Writes the entry text (a complete story in exactly six words) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.
No network, no randomness, no clock: the run is deterministic.
"""

import os

# The whole entry: a six-word story with a turn - a wedding, a death,
# and everything between, all left unsaid.
STORY = "Married in June. Widowed by August."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
