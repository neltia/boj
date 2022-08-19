import sys
import math
import itertools

t = int(sys.stdin.readline())
for i in range(t):
    array = sys.stdin.readline().split()[1:]
    it = list(itertools.combinations(array, 2))
    total = 0
    for item in it:
        total += math.gcd(int(item[0]), int(item[1]))
    print(total)
