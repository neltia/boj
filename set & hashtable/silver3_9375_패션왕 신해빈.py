"""
solved: 22.02.03
"""

import sys
from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


t = int(input())
for idx in range(t):
    wearable = {}
    n = int(sys.stdin.readline())
    for i in range(n):
        wear = sys.stdin.readline().split()
        if wear[1] not in wearable:
            wearable[wear[1]] = []
        wearable[wear[1]].append(wear[0])
    if len(wearable.keys()) == 1:
        print(len(wearable[wear[1]]))
        continue

    cnt = 1 # 각 종류마다 항목의 개수
    for k in wearable:
        cnt *= (len(wearable[k])+1)
    print(cnt-1)
