"""
solved: 22.08.14
"""

sug = int(input())
bag = 0

while sug >= 0:
  if sug % 5 == 0:
    bag += (sug//5)
    print(bag)
    break
  sug -= 3
  bag += 1
else:
  print(-1)
