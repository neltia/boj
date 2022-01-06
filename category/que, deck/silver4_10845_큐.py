"""
problem: https://www.acmicpc.net/problem/10845
"""

import queue
import sys

class Queue:
    # 큐 모듈을 사용해 큐 생성
    def __init__ (self):
        self.top = []

    # 큐 초기화
    def clear(self):
        self.top = []

    # PUSH
    def push (self, item):
        self.top.append(item)

    # POP
    def pop(self):
        if not self.empty():
            return self.top.pop(0)
        else:
            return -1

    # 큐에서 front의 값을 읽어온다
    def front(self):
        if not self.empty():
            print(int(self.top[0]))
        else:
            print(-1)

    # 큐에서 back 값을 읽어온다
    def back(self):
        if not self.empty():
            print(int(self.top[-1]))
        else:
            print(-1)

    # 비어있는지 확인
    def empty(self):
        return len(self.top)==0

    # 길이 확인
    def size(self):
        return len(self.top)


n = int(sys.stdin.readline())
queue = Queue()
for x in range(n):
    tmp = sys.stdin.readline().strip()
    if " " in tmp:
            command, value = tmp.split()
    else:
        command = tmp

    if command == "push":
        queue.push(int(value))
    elif command == "pop":
        print(queue.pop())
    elif command == "size":
        print(queue.size())
    elif command == "empty":
        if queue.empty():
            print(1)
        else:
            print(0)
    elif command == "front":
        queue.front()
    elif command == "back":
        queue.back()
