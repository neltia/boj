import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
array = sys.stdin.readline().split()
[print(" ".join(list(map(str, item)))) for item in list(itertools.permutations(sorted(list(map(int, array))), m))]
