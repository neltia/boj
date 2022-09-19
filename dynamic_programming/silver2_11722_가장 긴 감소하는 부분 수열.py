"""
solved: 22.09.19
"""

import sys

x = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [1] * x
for i in range(x):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
