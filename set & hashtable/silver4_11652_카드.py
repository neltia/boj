"""
solved: 21.12.28
"""

import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for x in range(n)]
count = Counter(sorted(cards))
print(count.most_common(1)[0][0])
