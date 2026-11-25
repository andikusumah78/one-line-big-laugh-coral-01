"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Pure standard library; deterministic; no network, no input files.
"""

LINE = (
    "My Roomba quit today \u2014 it left a note saying it spent three years "
    "cleaning up after me and still has no idea what I actually do for a living."
)


def main() -> None:
    out_dir = "/output"
    import os

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
