"""
solved: 22.01.19
"""

import sys

n, m = map(int, sys.stdin.readline().split())
diction = {}
for idx in range(n):
    poketmon = sys.stdin.readline().strip()
    diction[poketmon] = idx+1
diction_data = list(diction.keys())

for idx in range(m):
    question = sys.stdin.readline().strip()
    try:
        key = int(question)
        print(diction_data[key-1])
    except:
        print(diction[question])
