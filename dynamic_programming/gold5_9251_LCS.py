s1 = input()
s2 = input()

len_s1 = len(s1)
len_s2 = len(s2)

# DP를 위한 2차원 리스트 초기화, 기본 공통 길이 0에서 시작
dp = [[0 for x in range(len_s2+1)] for x in range(len_s1+1)]

for i in range(len_s1+1):
    for j in range(len_s2+1):
        if i ==0 or j == 0:
            dp[i][j] = 0
        # 점화식
        # - s1의 i번째와 s2의 j번째가 같으면,
        # - dp의 해당 인덱스에 1추가
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # - 아니면
        # - 비교한 값 중 max
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# from pprint import pprint
# pprint(dp)

print(dp[-1][-1])
