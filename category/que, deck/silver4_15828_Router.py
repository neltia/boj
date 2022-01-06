"""
problem: https://www.acmicpc.net/problem/15828
"""

import sys
from collections import deque

deck = deque()
total = int(sys.stdin.readline())

while True:
       n = int(sys.stdin.readline())
       if n == -1:
              break

       if n == 0:
              deck.popleft()
       elif len(deck) < total:
              deck.append(str(n))


if len(deck) == 0:
       print("empty")
else:
       print(" ".join(list(deck)))