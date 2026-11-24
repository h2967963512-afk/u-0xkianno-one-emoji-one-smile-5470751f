"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one emoji, and nothing else: U+1FAF6 HEART HANDS.
# One grapheme, one code point, no words, no caption, no explanation,
# no trailing newline — the file holds the emoji alone.
# Revision note (parent pass): re-checked after the local run —
# the single emoji is unchanged; this note only records the check.
import os

TEXT = "🫶"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
