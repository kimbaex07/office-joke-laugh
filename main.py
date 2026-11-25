#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke.

Writes a single funny line about office life to entry.txt.

The joke is: "HR said our open-plan office encourages collaboration,
which is why I now know everyone's lunch order and nobody's project
status." It is true to office life (open-plan offices really do trade
privacy for overheard chatter), and the turn lands at the end: the
collaboration HR promised produces lunch-order trivia instead of any
actual knowledge of what anyone is working on.
"""

import os
import sys

JOKE = (
    "HR said our open-plan office encourages collaboration, which is "
    "why I now know everyone's lunch order and nobody's project status."
)


def main():
    joke = JOKE
    # Validate before writing anything: 1-200 characters, one sentence.
    if not joke or len(joke) > 200:
        sys.exit("joke must be 1-200 characters")
    if joke != joke.strip():
        sys.exit("joke must not have surrounding whitespace")
    if "\n" in joke or "\r" in joke:
        sys.exit("joke must be a single line")
    if joke.count(".") != 1 or not joke.endswith("."):
        sys.exit("joke must be exactly one sentence")
    if "!" in joke or "?" in joke:
        sys.exit("joke must be exactly one sentence")
    data = joke.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.umask(0o022)
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    except OSError:
        # Fallback only if the primary output dir is unusable.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
