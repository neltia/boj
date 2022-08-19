"""
solved: 22.08.19
"""

import sys
import math
from itertools import combinations

n = int(sys.stdin.readline())
for x in range(n):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    arr = list(combinations(nums, 2))
    len_arr = len(arr)
    dp = [0] * (len_arr+1)
    for idx, item in enumerate(arr):
        dp[idx] = math.gcd(item[0], item[1])
    print(max(dp))