"""
solved: 22.08.19
"""

import math

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

a, b = map(int, input().split())
print("1" * math.gcd(a, b))
