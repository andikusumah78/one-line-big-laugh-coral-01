"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Pure standard library; deterministic; no network, no input files.
"""

import os

OUT_DIR = "/output"
ENTRY_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 200

LINE = (
    "My Roomba quit today \u2014 it left a note saying it spent three years "
    "cleaning up after me and still has no idea what I actually do for a living."
)


def validate_line(line: str) -> str:
    """Enforce the bounty gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")
    return line


def resolve_out_dir(path: str = OUT_DIR) -> str:
    """Create the output directory (absolute, per the bounty rules)."""
    os.makedirs(path, exist_ok=True)
    return path


def main() -> None:
    line = validate_line(LINE)
    out_dir = resolve_out_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
