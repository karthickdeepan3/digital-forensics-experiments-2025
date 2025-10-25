#!/usr/bin/env python3
"""
network_analysis.py

Lightweight scanner that looks for network-related indicators in a binary or hex file.
It is intentionally conservative and only searches for common keywords (http, https, GET, POST,
socket, connect) and IPv4-like patterns in strings.

Usage:
    python scripts/network_analysis.py samples/benign_sample1.hex

This script does not perform any network activity itself.
"""
import sys
import re

NET_KEYWORDS = [b'http', b'https', b'GET', b'POST', b'socket', b'connect', b'Listen', b'bind']

IPV4_RE = re.compile(rb'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

def find_keywords(data):
    found = set()
    for kw in NET_KEYWORDS:
        if kw in data:
            found.add(kw.decode('utf-8'))
    return sorted(found)

def find_ips(data):
    return [m.group(0).decode('utf-8') for m in IPV4_RE.finditer(data)]

def main():
    if len(sys.argv) < 2:
        print("Usage: python network_analysis.py <file>")
        return
    path = sys.argv[1]
    with open(path, 'rb') as f:
        data = f.read()
    keywords = find_keywords(data)
    ips = find_ips(data)
    print("Network-related keywords:", keywords)
    print("IPv4-like strings found:", ips)

if __name__ == '__main__':
    main()
