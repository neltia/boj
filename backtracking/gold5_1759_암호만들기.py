"""
solved: 22.09.05
"""

import itertools

l, c = map(int, input().split())
alpha = sorted(input().split())

# itertools로 조합 구하기
words = itertools.combinations(alpha, l)

# 결과 출력
for word in words:
    # 현재 문자열에서 모음 개수 구하기
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1

    # 1. 모음 개수가 최소 1개 이상 있어야 함
    # 2. L개 알파벳 소문자 중에서 모음 개수를 뺀 값으로 자음 개수 판단,
    # - 최소 두 개 자음으로 구성되어야 함
    if cnt_vow >=1 and l - cnt_vow >=2:
        print(''.join(word))
