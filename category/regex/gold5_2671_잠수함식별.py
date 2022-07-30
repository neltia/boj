"""
problem: https://www.acmicpc.net/problem/2671
solved: 22.07.30
"""

import sys
import re

pat = r"(100+1+|01)+"
p = re.compile(pat)
doc = sys.stdin.readline().strip()
result = p.fullmatch(doc)
if result and result.group() == doc:
    print("SUBMARINE")
else:
    print("NOISE")
