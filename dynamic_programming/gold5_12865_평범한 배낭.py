"""
0-1 배낭 문제
- W: 배낭의 무게한도
- arr_w: 각 보석의 무게
- arr_v: 각 보석의 가격(가치)
- n: 보석의 수
"""


import sys


def knapsack(W, wt, val, n):
    # DP를 위한 2차원 리스트 초기화
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        # 각 칸을 돌면서
        for w in range(W+1):
            # 0번째 행/열은 0으로 세팅s
            if i == 0 or w == 0:
                K[i][w] = 0
            # 점화식
            # 두 경우 중 큰 값 선택
            # 1. i번째 보석을 위해, i번째 보석만큼의 무게를 비웠을 때 최적 값에 i번째 보석의 가격을 더한 값
            # => 가치 증진을 위해 넣음 : V[i-1][w-wi] + vi
            # 2. i-1개의 보석을 가지고 구한 전 단계 최적 값
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            # i번째 보석이 배낭의 무게 한도보다 무거우면
            # - 이 조건에서는 배낭에 못 넣음
            # - i-1개의 보석을 가지고 구한 전 단계 최적 값을 그대로 가져옴
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


n, k = map(int, sys.stdin.readline().strip().split())
arr_w = list()
arr_v = list()

for i in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    arr_w.append(w)
    arr_v.append(v)
print(knapsack(k, arr_w, arr_v, n))
