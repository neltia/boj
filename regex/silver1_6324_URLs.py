"""
solved: 22.08.21
"""

import sys
import re

n = int(sys.stdin.readline().strip())
for i in range(n):
    s = sys.stdin.readline().strip()
    print(f"URL #{i+1}")

    pat = r"(ftp|http|gopher)"
    protocol = re.search(pat, s).group()

    pat = r":\/\/([a-zA-Z0-9\.\-\_]+)"
    host = re.findall(pat, s)[0]

    pat = r":\/\/[a-zA-Z0-9\.\-\_]+\:(\d+)"
    data = re.findall(pat, s)
    if len(data) == 0:
        port = "<default>"
    else:
        port = data[0]

    pat = r":\/\/[a-zA-Z0-9\.\-\_]+\:?\d*\/(\S+)"
    data = re.findall(pat, s)
    if len(data) == 0:
        path = "<default>"
    else:
        path = data[0]

    print(f"Protocol = {protocol}")
    print(f"Host     = {host}")
    print(f"Port     = {port}")
    print(f"Path     = {path}")

    if i+1 != n:
        print()
