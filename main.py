#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office email auto-reply, one line long, to
/output/entry.txt. Pure standard library, deterministic: the same text is
written on every run.
"""

import os

# The reply: a real away message with a fresh turn on the usual
# "my inbox is being handled while I'm away" line.
ENTRY = (
    "I'm out of office until Monday. My inbox is being answered by "
    "my future self, who is also on holiday."
)


def main() -> None:
    # Gate: the entry must be one line of 1-160 characters.
    assert 1 <= len(ENTRY) <= 160, "entry out of length bounds"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
