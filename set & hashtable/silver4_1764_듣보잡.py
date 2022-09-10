"""
solved: 21.12.21
"""

import sys

n, m = map(int, sys.stdin.readline().split())
set1 = set()
[set1.add(sys.stdin.readline().strip()) for x in range(n)]
set2 = set()
[set2.add(sys.stdin.readline().strip()) for x in range(m)]

result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)
