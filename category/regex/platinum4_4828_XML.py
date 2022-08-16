"""
problem: https://www.acmicpc.net/problem/2671
solved: 22.08.14
"""

import sys
import re


def isvalid(data):
    # 빈 줄
    if len(data) == 0:
        return "valid"

    # escape
    pat1 = r"(&amp;)|(&lt;)|(&gt;)"
    data = re.sub(pat1, "", data)

    # 16진수 문자 제거
    pat2 = r"&x([A-Fa-f0-9]{2})+\;"
    data = re.sub(pat2, "", data)

    # 태그 파싱
    pat3 = r"\<[a-z0-9]+\>|\<\/[a-z0-9]+\>"
    tags = re.findall(pat3, data)
    # print("DATA1:", data)
    # print("TAGS:", tags)

    # 태그 수가 홀수면 안 됨
    if len(tags) %2 != 0:
        return "invalid"

    # 태그 검증
    context = []
    for tag in tags:
        # print("TAG:", tag)
        if tag.startswith("</"):
            poped = context.pop()
            # print(poped, tag)
            if tag.replace("/", "") != poped:
                return "invalid"
        else:
            context.append(tag)
        # print("CONTEXT:", context)

    # <tag/> 닫는 태그 먼저 정리
    pat4 = r"<[a-z0-9]+\/\>"
    data = re.sub(pat4, "", data)

    # <tag>, </tag> 일반 태그 정리
    data = re.sub(pat3, "", data)

    # 단일 문자열이 포함되면 안 됨: <, >, &
    strset = ["<", ">", "&"]
    for strs in strset:
        if strs in data:
            return "invalid"

    # print("DATA2:", data)

    # plain text
    pat5 = r"[\x20-\x7F]+"
    data = re.sub(pat5, "", data)
    # print("DATA3:", data)
    if len(data) != 0:
        return "invalid"
    return "valid"


raw_data = sys.stdin.readlines()
for line in raw_data:
    print(isvalid(line.strip()))
    # print()
