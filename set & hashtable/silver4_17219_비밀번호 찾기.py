"""
solved: 22.08.14
"""

import sys

n, m = map(int, input().split())

data_dict = dict()

for idx in range(n):
    key, value = sys.stdin.readline().split()
    data_dict[key] = value

for idx in range(m):
    query = sys.stdin.readline().strip()
    print(data_dict[query])
