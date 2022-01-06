"""
problem: https://www.acmicpc.net/problem/10866
"""

# 사용 모듈
from collections import deque
import sys

# 데크 선언
deck = deque()

# 명령 수만큼 반복
n = int(sys.stdin.readline())
for x in range(n):
    tmp = sys.stdin.readline().strip()
    if " " in tmp:
            command, value = tmp.split()
    else:
        command = tmp

    if command == "push_front":
        deck.appendleft(value)
    elif command == "push_back":
        deck.append(value)
    elif command == "pop_front":
        try:
            print(deck.popleft())
        except IndexError:
            print(-1)
    elif command == "pop_back":
        try:
            print(deck.pop())
        except IndexError:
            print(-1)
    elif command == "size":
        print(len(deck))
    elif command == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif command == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
