import sys

t = int(sys.stdin.readline().strip())
for idx in range(t):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("1 0")
        continue
    elif n == 1:
        print("0 1")
        continue

    # dp array
    dp = [-1]*(n+1)

    # fibo(1)=fibo(2)=0
    dp[0]=0
    dp[1]=1
    dp[2]=1

    # 피보나치 수열을 반복문으로 구현(bottom up)
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[n-1], dp[n])
