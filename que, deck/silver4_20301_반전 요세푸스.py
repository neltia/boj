"""
problem: https://www.acmicpc.net/problem/5430
"""

import sys
from collections import deque
deck = deque()

n, k, m = map(int, sys.stdin.readline().split())
[deck.append(x+1) for x in range(n)]
cnt = 0
sw = 0

while (1):
    if len(deck) == 0:
        break

    if cnt != 0 and cnt % m == 0:
        sw += 1
    # right
    if sw % 2 == 0:
        deck.rotate(-k)
        # print("오른쪽")
        # print("CNT:", cnt, deck)
        p = deck.pop()
    # left
    else:
        deck.rotate(k)
        # print("왼쪽")
        # print("CNT:", cnt, deck)
        p = deck.popleft()
    cnt += 1
    print(p)
