#!/usr/bin/env python3
"""
extract_strings.py

Simple, safe utility that extracts printable ASCII/UTF-8 strings from a binary file.
This is similar to the Unix `strings` utility but implemented in pure Python.

Usage:
    python scripts/extract_strings.py samples/benign_sample1.bin

This script only reads files and prints discovered strings; it does not execute them.
"""
import sys
import re

MIN_LEN = 4

def extract_strings(data, min_len=MIN_LEN):
    # Find runs of printable ASCII characters
    pattern = re.compile(rb"[ -~]{%d,}" % min_len)
    return [m.group(0).decode('utf-8', errors='ignore') for m in pattern.finditer(data)]

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_strings.py <file>")
        return
    path = sys.argv[1]
    with open(path, 'rb') as f:
        data = f.read()
    strings = extract_strings(data)
    for s in strings:
        print(s)

if __name__ == '__main__':
    main()
