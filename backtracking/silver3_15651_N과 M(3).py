import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

[print(" ".join(item)) for item in list(itertools.product([str(x) for x in range(1, n+1)], repeat=m))]
