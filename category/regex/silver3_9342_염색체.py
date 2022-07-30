"""
problem: https://www.acmicpc.net/problem/9342
solved: 22.05.30
"""

import sys
import re

n = int(sys.stdin.readline().strip())
pat = r"^[A,B,C,D,E,F]?A+F+C+[A,B,C,D,E,F]?$"
for idx in range(n):
    sentence = sys.stdin.readline().strip()
    if bool(re.search(pat, sentence)):
        print("Infected!")
    else:
        print("Good")
