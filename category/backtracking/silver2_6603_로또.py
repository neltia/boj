import sys
import itertools

while True:
    s = sys.stdin.readline().strip()
    if s == "0":
        break
    else:
        s = s.split()[1:]

    data = sorted(list(set(list(map(int, s)))))
    pre_data = list(itertools.combinations(data, 6))
    for item in pre_data:
        print(" ".join(list(map(str, item))))
    print()
