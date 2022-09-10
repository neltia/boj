"""
solved: 21.12.21
"""

import sys

N = int(sys.stdin.readline())
nums1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

hash = {}
for char in nums1:
    if char in hash:
        hash[char] += 1
    else:
        hash[char] = 1

for char in nums2:
    if char in hash:
        print(hash[char], end=' ')
    else:
        print(0, end=' ')
