from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([n])
k = n

while True:
    if len(queue) == n:
        break
    k -= 1
    queue.appendleft(k)
    # print(k, queue)
    queue.rotate(k)
    # print(k, queue)

# print(queue)
result = list(map(str, list(queue)))
print(" ".join(result))
