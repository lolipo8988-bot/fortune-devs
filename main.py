"""Fortune Cookie Wisdom for Developers entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The competition gate requires UTF-8 text of 1 to
120 characters, not only white space. The program is deterministic:
every run writes exactly the same bytes.

The fortune is built from its two balanced halves, the way a fortune
cookie sentence is meant to be read: a prophecy about legacy code
first, then the quiet turn that points it back at the reader.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 120

# First half: the truth every developer has lived — inheriting code
# written in a hurry by someone unknown, and cursing it.
PROPHECY = "You will curse code written in haste by a stranger"

# Second half: the twist. The stranger is not only the past author;
# one day, reading your own old code, you will be that stranger.
TURN = "be kind — one day, reading your own, you will be that stranger."


def build_entry() -> str:
    """Assemble the single fortune-cookie line from its two halves."""
    return f"{PROPHECY}; {TURN}"


def validate(text: str) -> str:
    """Return the entry text, or raise if it would fail the gate."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate(build_entry())
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
