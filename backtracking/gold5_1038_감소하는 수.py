import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()
# 최대 감소하는 수는 9876543210
# 1자리부터 10자리까지
for i in range(1, 11):
    # [0, 1, ... 9]를 가지고 1자리부터 10자리까지 조합 생성
    # 조합이므로 중복 숫자는 없음
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        # 내림차순 정렬하여 감소하는 수로 변경
        comb.sort(reverse=True)
        # 삽입
        nums.append(int("".join(map(str, comb))))

nums.sort()
try:
    print(nums[n])
except:
    print(-1)
