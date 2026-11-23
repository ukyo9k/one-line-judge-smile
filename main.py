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


MAX_CHARS = 200


def validate(line: str) -> None:
    """The entry must be exactly one non-empty line of 1-200 characters."""
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} characters"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
