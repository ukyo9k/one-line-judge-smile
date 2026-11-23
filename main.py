#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes exactly one line (at most 200 characters) to /output/entry.txt.
"""

import os

LINE = (
    "At 7:40 this morning, the cat that has hissed at me for two years "
    "trotted up, headbutted my ankle, and fell asleep on my shoe like it "
    "had finally signed the lease."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
