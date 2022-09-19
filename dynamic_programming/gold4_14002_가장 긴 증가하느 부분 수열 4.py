"""
solved: 22.09.19
"""

import sys

x = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [1] * x
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            # print("*", i)
len_nu = max(dp)
print(len_nu)

# print(*dp)
result = list()
for idx in range(x-1, -1, -1):
   if dp[idx] == len_nu:
        result.append(arr[idx])
        len_nu -= 1
result.reverse()
print(*result)
