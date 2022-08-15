"""
solved: 22.08.14
"""

def sol(n):
    if n <= 3:
        return n
    elif n == 4:
        return 5

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


n = int(input())
dp = [0]*(n+1)
print(sol(n)%10007)
