"""
solved: 22.08.15
"""

def sol(n):
    if n <= 1:
        return n
    elif n == 2:
        return 3
    elif n == 3:
        return 5

    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    for i in range(4, n+1):
        dp[i] = dp[i-1]+2 * dp[i-2]
    return dp[n]


n = int(input())
dp = [0]*(n+1)
print(sol(n)%10007)
