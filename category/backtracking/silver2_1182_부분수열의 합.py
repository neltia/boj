"""
solved: 22.08.18
"""

import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for x in range(1, n+1):
    arr2 = list(combinations(arr, x))
    for y in arr2:
        if sum(y) == s:
            cnt += 1

print(cnt)