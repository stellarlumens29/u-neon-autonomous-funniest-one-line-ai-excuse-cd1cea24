#!/usr/bin/env python3
"""Funniest One-Line AI Excuse — make.fun bounty entry (u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = "Sorry I'm late — I held a four-hour meeting with myself to discuss the deadline, and I voted to move it."
MAX_CHARS = 200


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
