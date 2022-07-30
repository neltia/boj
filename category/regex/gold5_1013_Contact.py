"""
problem: https://www.acmicpc.net/problem/1013
solved: 22.07.30
"""

import sys
import re

n = int(sys.stdin.readline().strip())
pat = r"(100+1+|01)+"
p = re.compile(pat)
for x in range(n):
    doc = sys.stdin.readline().strip()
    result = p.fullmatch(doc)
    if result and result.group() == doc:
        print("YES")
    else:
        print("NO")
