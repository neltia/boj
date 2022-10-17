"""
solved: 22.10.17
"""

import sys

x = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = arr[:]
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
len_nu = max(dp)
print(len_nu)
