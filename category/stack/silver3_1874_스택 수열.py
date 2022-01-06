"""
problem: https://www.acmicpc.net/problem/1874
"""

import sys


class Stack():
    #리스트를 이용하여 스택 생성
    def __init__(self):
        self.top = []
        self.res = []

    # PUSH
    def push(self, item):
        self.top.append(item)
        self.res.append("+")

    # POP
    def pop(self):
        if not self.isEmpty():
            self.top.pop(-1)
            self.res.append("-")
            return
        else:
            self.res.append("NO")

    #스택에서 top의 값을 읽어온다
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            self.res.append("NO")

    #스택이 비어있는지 확인
    def isEmpty(self):
        return len(self.top)==0


n = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline().strip()) for x in range(n)]
stack = Stack()

pointer = 0
for current_num in inputs:
    if not stack.isEmpty() and stack.peek() == current_num:
        stack.pop()
        continue

    cha = current_num - pointer
    # print(current_num, pointer, cha)
    if cha >= 0:
        for x in range(cha):
            pointer += 1
            stack.push(pointer)
        stack.pop()
    else:
        cha = abs(cha)
        [stack.pop() for x in range(cha)]

if "NO" in stack.res:
    result = "NO"
else:
    result = "\n".join(stack.res).rstrip("\n")
print(result)
