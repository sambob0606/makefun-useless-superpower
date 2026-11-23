#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

The line: a familiar power (stopping time) turned somewhere new -- the
whole power is one second long, and it is already spent. The joke pays
off in the last few words and trusts the reader to get it.
"""

import os

LINE = "I can stop time for exactly one second. I've already used it."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
