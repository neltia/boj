"""
solved: 22.09.10
"""

import re

s = input().strip()

replace_pat = r"^0+"
data = re.sub(replace_pat, "", s)

replace_pat = r"([-+])0+"
data = re.sub(replace_pat, "\g<1>", data)

replace_pat = r"-([\d+]+)"
sub_pat = r"-(\g<1>)"
data = re.sub(replace_pat, sub_pat, data)

# print(data)
print(eval(data))
