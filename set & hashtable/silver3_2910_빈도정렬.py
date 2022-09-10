"""
solved: 22.08.25
"""

import sys
from collections import Counter

n, c = map(int, input().split())
msg = list(map(int, sys.stdin.readline().strip().split()))
count = Counter(msg)
result = ""
x = count.most_common()
for a, b in x:
    for _ in range(b):
        print(a, end=' ')
