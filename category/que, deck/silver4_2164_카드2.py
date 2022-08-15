"""
problem: https://www.acmicpc.net/problem/2164
"""

from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())
for value in range(n):
    queue.append(value + 1)
while True:
    if len(queue) == 1:
        break
    queue.popleft()
    queue.rotate(-1)
print(queue[0])
