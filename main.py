"""One-star review of an everyday essential: your own shadow.

Writes a single deadpan one-star review line to /output/entry.txt.
Standard library only.
"""

import os


REVIEW = (
    "One star. My shadow has followed me everywhere for years "
    "without asking, and has never once offered to carry anything."
)


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
