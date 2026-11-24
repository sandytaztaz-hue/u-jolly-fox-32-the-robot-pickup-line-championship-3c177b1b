"""The Robot Pickup Line Championship — one line, written to /output/entry.txt.

Gate (comp rules): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace. The line below is written verbatim with
no trailing newline, so the file holds exactly the line and nothing else.
"""

import os

LINE = "Page 47 of my manual says 'do not fall in love with the customer.' I just tore out page 47."


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

    print(LINE)


if __name__ == "__main__":
    main()
