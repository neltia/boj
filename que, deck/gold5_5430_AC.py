"""
problem: https://www.acmicpc.net/problem/5430
"""

# 사용 모듈
from collections import deque
import sys

# routine
t = int(sys.stdin.readline())
for x in range(t):
    # data input
    raw_data = [sys.stdin.readline() for y in range(3)]
    command, n, array = raw_data[0].strip(), raw_data[1].strip(), raw_data[2].strip()[1:-1]

    # preprocess
    command = command.replace("RR", "")
    if int(n) == 0:
        deck = deque()
    else:
        deck = deque(array.split(","))

    # process
    stat, rev = 0, 0
    for act in command:
        if act == "R":
            rev += 1
        else:
            if len(deck) < 1:
                stat = -1
                break

            if rev % 2 == 0:
                deck.popleft()
            else:
                deck.pop()

    if stat == -1:
        print("error")
    else:
        if rev % 2 != 0:
            deck.reverse()
        print("[" + ",".join(deck) + "]")
