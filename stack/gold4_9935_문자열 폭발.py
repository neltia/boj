"""
solved: 22.08.18
"""

import sys

data = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

last = bomb[-1]
stack = list()
length = len(bomb)

for char in data:
    stack.append(char)
    if char == last and "".join(stack[-length:]) == bomb:
        del stack[-length:]

result = "".join(stack)
if result == "":
    print("FRULA")
else:
    print(result)
