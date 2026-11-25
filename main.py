"""One Line of Earned Pride — v1 entry program.

Writes the winning line, exactly one line, to entry.txt.
Deterministic: stdlib only, no network, no clock, no randomness.
"""

import os

LINE = (
    "At seventy-two he planted the mango seed his granddaughter gave him, "
    "watered it through two dry seasons, and ate its first fruit "
    "sitting under its shade."
)


def build_line() -> str:
    return LINE


def main() -> None:
    line = build_line()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
