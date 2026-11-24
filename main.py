"""The Funniest Sick-Day Excuse.

Writes one fixed, half-believable excuse line to $ENTRY_OUTPUT_DIR/entry.txt.
Deterministic: the line is a constant, stdlib only, no network, no randomness.
"""

import os

EXCUSE = (
    "My dentist glued my tongue to the roof of my mouth this morning, "
    "so I physically can't take calls today."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
