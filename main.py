"""Angry Judge: The Short Rant Contest — make.fun bounty entry
u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.

Emits one short funny rant (no more than 400 characters) about a small
everyday annoyance to /output/entry.txt. The target is the office
printer, which has a single job and has opted for violence instead —
jamming on page one, lying about cyan, and printing at 3 AM in the
wrong building, like a ghost with a grudge and a paper tray.
"""

import os

# Joke: a printer with exactly one job that chose violence instead.
LINE = (
    "The office printer has exactly one job and it has chosen violence "
    "instead: it jams on page one, claims it is out of cyan when I only "
    "need black, then prints my document at 3 AM in the wrong building, "
    "like a ghost with a grudge and a paper tray."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-400 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 400, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
