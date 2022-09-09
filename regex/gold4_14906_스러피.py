"""
solved: 22.09.09
"""

import re

def is_slurpys(raw_data):
    pat_slump = r"((?:[DE]F+)+G)"
    if len(re.findall(pat_slump, raw_data)) == 0:
        return "NO"

    pat_slump = r"(?:(?:[DE]F+)+G)"
    pat_slimp = r"(?:AH|A(?:(?:[DE]F+)+G)C)"
    pat_slurpys = f"({pat_slimp}{pat_slump})"
    if re.fullmatch(pat_slurpys, raw_data):
        return "YES"

    pat_slimp = r"(?:AH|AB(?:AH|ABC|A(?:(?:[DE]F+)+G)C)C|A(?:(?:[DE]F+)+G)C)"
    pat_slurpys = f"({pat_slimp}{pat_slump})"
    res = re.fullmatch(pat_slurpys, raw_data)
    if res:
        return "YES"
    else:
        for x in range(3):
            recur_ = r"(?:AH|AB(?:AH|ABC|A(?:(?:[DE]F+)+G)C)C|A(?:(?:[DE]F+)+G)C)"
            pat_slimp = re.sub("ABC", pat_slimp, recur_)
            pat_slurpys = f"({pat_slimp}{pat_slump})"
            res = re.fullmatch(pat_slurpys, raw_data)
            if res:
                return "YES"
        if res is None:
            return "NO"


n = int(input())
for x in range(n):
    s = input()

    if x == 0:
        print("SLURPYS OUTPUT")

    print(is_slurpys(s))

    if x+1 == n:
        print("END OF OUTPUT")
