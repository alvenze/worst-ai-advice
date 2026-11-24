#!/usr/bin/env python3
"""Entry for make.fun bounty "Worst AI Advice: The 48-Hour Tight Line Open".

Writes the one-line entry to /output/entry.txt. The gate (kit RULES.txt):
UTF-8 text of 1 to 140 characters, not only whitespace.
"""

import os

LINE = (
    "For best results, ask the phishing email if it is a scam; "
    "scammers are legally required to tell the truth."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 140, f"entry must be 1..140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"GATE OK: {len(text)} characters")


if __name__ == "__main__":
    main()
