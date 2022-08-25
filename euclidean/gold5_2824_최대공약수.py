"""
solved: 22.08.25
"""

import math
import sys

n = int(sys.stdin.readline().strip())
arr1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
arr2 = list(map(int, sys.stdin.readline().strip().split()))

mul_arr1 = math.prod(arr1)
mul_arr2 = math.prod(arr2)

# print(mul_arr1, mul_arr2)

result = math.gcd(mul_arr1, mul_arr2)
if len(str(result)) > 9:
    print(str(result)[-9:])
else:
    print(result)
