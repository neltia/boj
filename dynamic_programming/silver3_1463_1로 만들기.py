n = int(input())

# 작은 문제부터 해결해서 저장할 dp테이블
dp = [0] * (n+1)

# 다이나믹 프로그래밍(bottom up)
for i in range(2, n+1):
    # d연산
    dp[i] = dp[i-1]+1

    # a 연산이 가능한 경우
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)

    # b 연산이 가능한 경우
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[-1])
