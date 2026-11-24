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
MIN_CHARS = 1
MAX_CHARS = 140


def check_gate(text: str) -> None:
    """Assert the kit's gate on the entry text before it is written."""
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}..{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # must be UTF-8 encodable


def main() -> None:
    text = LINE
    check_gate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Post-write self-check: re-read the file and hold it to the same gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == text, "written file differs from the entry line"
    check_gate(written)
    print(f"GATE OK: {len(written)} characters")


if __name__ == "__main__":
    main()
