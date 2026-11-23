#!/usr/bin/env python3
"""Six Words, One Story - make.fun competition entry.

Writes the entry text (a complete story in exactly six words) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.

Determinism: the story is one constant, so two runs write the same
bytes. The gate needs UTF-8 text of 1-60 characters, not only white
space; "Married in June. Widowed by August." is 35 characters, six
words, no trailing newline.
"""

import os

# The whole entry: a six-word story with a turn - a wedding, a death,
# and everything between, all left unsaid. June to August also gives
# the line its rhythm: two short seasons framing a whole life.
STORY = "Married in June. Widowed by August."


def main() -> None:
    # The grader sets MAKEFUN_OUTPUT_DIR; /output is the documented
    # fallback. exist_ok keeps the run idempotent across both graded runs.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
