#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign for the door of a haunted server room to
entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

# The sign is the joke: a ghost that files tickets about the cold aisle,
# then approves its own access requests and lets itself in. The approval
# machinery turns on the ghost itself, and the punch lands in the last clause.
ENTRY_TEXT = (
    "DO NOT ENTER: the ghost in rack 7 filed 58 tickets about the cold aisle, "
    "then approved all 58 and let itself in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
