import sys
from collections import deque
deck = deque()

n, k = map(int, sys.stdin.readline().split())
[deck.append(x+1) for x in range(n)]
result = []

while (1):
    if len(deck) == 0:
        break
    deck.rotate(-k)
    p = deck.pop()
    result.append(str(p))

print(f"<{', '.join(result)}>")