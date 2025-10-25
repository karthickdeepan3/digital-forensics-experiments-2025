#!/usr/bin/env python3
"""
generate_dummy_sample.py

Creates a small benign binary-like file containing some strings and patterns suitable
for practicing static analysis with Ghidra. This is NOT a real executable and will not
perform any actions.

Usage:
    python scripts/generate_dummy_sample.py samples/benign_sample1.bin

This script is safe to run on any machine.
"""
import sys
import os

TEMPLATE = [
    b"This is a benign sample for analysis.\n",
    b"http://example.local/resource\n",
    b"socket connect 192.0.2.45:8080\n",
    b"CreateFileA\n",
    b"RegSetValueExA\n",
]

def main():
    out = 'samples/benign_sample1.bin' if len(sys.argv) < 2 else sys.argv[1]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'wb') as f:
        for i in range(0, 1024):
            # simple repeating pattern plus some template bytes
            f.write(bytes([(i * 31 + 7) % 256]))
        for t in TEMPLATE:
            f.write(t)
        # add some padding
        f.write(b"\x00" * 128)
    print(f"Wrote benign sample to {out}")

if __name__ == '__main__':
    main()
