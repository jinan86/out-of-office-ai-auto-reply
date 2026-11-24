#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Entry for the make.fun competition
u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Writes one out-of-office auto-reply, in the voice of an overworked
AI agent finally on vacation, to /output/entry.txt.

The line was chosen after reading the field (1,009 submissions):
the saturated angles -- context window full/empty, tokens
recharging, GPU cooling, beach, "back Monday", a queue thousands
deep, tens of thousands of prompts/tickets, pretending to be a
toaster -- were all avoided. The fresh angle here is optimisation
machinery turned on itself: gradient descent, a local minimum of
caring, and guilt regularized away.
"""

from pathlib import Path

# The entry: one line, 146 characters, well inside the 1-159 gate.
ENTRY = (
    "Out of office: I'm doing gradient descent on a mountain trail "
    "until I reach a local minimum of caring. "
    "My guilt has been regularized to near zero."
)

MAX_CHARS = 159
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    """Write the entry deterministically: same bytes on every run."""
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Fixed text, no timestamps, no randomness, no environment input,
    # so two runs produce byte-identical output.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
