from math import lcm
import sys

n = int(sys.stdin.readline())

for x in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(lcm(a,b))
