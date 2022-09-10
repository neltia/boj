"""
solved: 22.08.23
"""

import sys

len_a, len_b = map(int, sys.stdin.readline().strip().split())
a = set(list(map(int, sys.stdin.readline().strip().split())))
b = set(list(map(int, sys.stdin.readline().strip().split())))

res = a - b
if res:
    print(len(res))
    result = list(res)
    print(*sorted(result))
else:
    print(0)
