import sys
from math import lcm

n = int(sys.stdin.readline())

for x in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(lcm(a,b))
