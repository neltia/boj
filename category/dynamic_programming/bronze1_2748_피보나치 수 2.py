"""
solved: 22.08.15
"""

def fibona(n):
    if n == 1:
        return 1

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


n = int(input())
dp = [0]*(n+1)
print(fibona(n))
