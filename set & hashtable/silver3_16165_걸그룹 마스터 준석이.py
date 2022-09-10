"""
solved: 22.08.25
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

girl_group = dict()
member_name = dict()
for i in range(n):
    team_name = input().strip()
    team_num = int(input().strip())

    for j in range(team_num):
        name = input().strip()
        if team_name not in girl_group:
            girl_group[team_name] = list()
        girl_group[team_name].append(name)
        member_name[name] = team_name

# print(member_name)
# print(girl_group)

for i in range(m):
    quiz_value = input().strip()
    quiz_kind = int(input().strip())

    if quiz_kind == 1:
        print(member_name[quiz_value])
    else:
        print("\n".join(sorted(girl_group[quiz_value])))
