import sys
from math import gcd
from math import lcm

a, b = map(int, sys.stdin.readline().strip().split())
print(gcd(a,b))
print(lcm(a,b))
