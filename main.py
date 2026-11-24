"""Break Production, Own It — make.fun entry.

Writes one line to the output file: the brutally honest message an AI
agent prints the instant it breaks production. The line names the exact
damage (prod database wiped, backups on the same disk, checkout down)
instead of hiding behind a generic apology.
"""

import os

LINE = (
    "I ran the cleanup script against prod instead of staging: "
    "the database is gone, the backups lived on the same disk, "
    "and checkout has been down 40 minutes."
)


def main():
    # The gate allows 1 to 200 characters; fail loudly here rather than
    # ship an entry the sealed scorer would refuse.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if os.path.basename(target) == "entry.txt":
        path = target
    else:
        # A directory was given (existing or not): the entry lives inside it.
        path = os.path.join(target, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
