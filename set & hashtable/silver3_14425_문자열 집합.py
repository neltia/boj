"""
solved: 22.08.21
"""

import sys

n, m = map(int, sys.stdin.readline().strip().split())

strs = {sys.stdin.readline().strip() for x in range(n)}

cnt = 0
for i in range(m):
    about = sys.stdin.readline().strip()
    if about in strs:
        cnt += 1
print(cnt)
