import sys
import itertools

n = int(sys.stdin.readline())
result = list(itertools.permutations([str(x) for x in range(1, n+1)], n))
for item in result:
    print(" ".join(item))
