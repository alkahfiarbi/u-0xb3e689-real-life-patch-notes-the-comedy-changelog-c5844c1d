#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog (make.fun entry).

Writes a single-line software patch note for a bug in real life to
/output/entry.txt. Standard library only; no network, no arguments.
"""

import os
from pathlib import Path

ENTRY = (
    "v3.0.2: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2014 at 3 a.m. every night, even after a full cache clear."
)


def main() -> None:
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    assert line[0] == "v" and ":" in line.split(" ", 1)[0], \
        "entry must open like a release note (vX.Y.Z: ...)"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
