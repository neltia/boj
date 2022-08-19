import sys


def sol(n):
    dp = list()
    dp = [0]*(n+1)

    if n in [1, 2]:
        return n
    elif n == 3:
        return 4

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


t = int(input())
for x in range(t):
    n = int(sys.stdin.readline())
    print(sol(n))