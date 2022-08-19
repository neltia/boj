"""
problem: https://www.acmicpc.net/problem/9342
solved: 22.05.30
"""

import sys
import re

sentence = " ".join(sys.stdin.readlines())

pat = r"[a-zA-Z-]{1,}"
findit = re.finditer(pat, sentence, re.MULTILINE)
findit = [x.group() for x in list(findit)]
findit.sort(key=len, reverse=True)
print(findit[0].lower())
