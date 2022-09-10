"""
solved: 22.08.22
"""

import sys
import re

n = int(sys.stdin.readline().strip())
extentions = {}
pat = r"\.\w+$"
p = re.compile(pat)

for x in range(n):
    file = sys.stdin.readline().strip()
    extention = p.search(file).group().replace(".", "")
    if extention in extentions:
        extentions[extention] += 1
    else:
        extentions[extention] = 1

for value in sorted(extentions.items()):
    print(value[0], value[1])
