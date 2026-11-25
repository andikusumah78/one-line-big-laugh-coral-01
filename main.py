"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Pure standard library; deterministic; no network, no input files.
"""

import os

OUT_DIR = "/output"
OUTPUT_ENTRY_PATH = os.path.join(OUT_DIR, "entry.txt")
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200

LINE = (
    "My Roomba quit today \u2014 it left a note saying it spent three years "
    "cleaning up after me and still has no idea what I actually do for a living."
)


def validate_line(line: str) -> str:
    """Gate check: the line must be non-blank, 1-200 chars, one line, valid UTF-8."""
    if not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) < GATE_MIN_CHARS or len(line) > GATE_MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, outside the %d-%d range"
            % (len(line), GATE_MIN_CHARS, GATE_MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must not contain an embedded newline")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate_line(LINE)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUTPUT_ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
