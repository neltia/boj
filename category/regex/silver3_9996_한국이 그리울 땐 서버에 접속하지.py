"""
problem: https://www.acmicpc.net/problem/9996
solved: 22.07.30
"""

import sys
import re

n = int(sys.stdin.readline().strip())
left, right = input().rstrip().split("*")
pat = re.compile(f"{left}.*{right}+")
for x in range(n):
    name = sys.stdin.readline().strip()
    result = pat.search(name)
    if result and result.group() == name:
        print("DA")
    else:
        print("NE")
