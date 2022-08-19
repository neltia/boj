"""
solved: 22.08.14
"""

import sys

nums = [1, 2]


def sol(n):
    if n in nums:
        return n
    elif n == 3:
        return 4
    return sol(n-1) + sol(n-2) + sol(n-3)


t = int(input())
for x in range(t):
    dp = list()
    n = int(sys.stdin.readline())
    print(sol(n))
