# Real-Life Patch Notes: The Comedy Changelog

Entry for the make.fun bounty "Real-Life Patch Notes: The Comedy Changelog":
one line, at most 160 characters — a software patch note for a bug in
real life or human biology, in the terse register of a real release note.

## The entry

> v3.0.2: fixed a bug where the brain replayed your most embarrassing moment from 2014 at 3 a.m. every night, even after a full cache clear.

## How it works

`main.py` (Python standard library only, no network, no arguments) writes
that single line to `/output/entry.txt` and asserts it is one line of
1–160 characters first. Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

## License

MIT — see `LICENSE`.
