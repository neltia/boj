"""
22.08.21
"""

n = int(input())

books = dict()
for x in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_value = max(list(books.values()))
result = list()
for key, value in books.items():
    if max_value == value:
        result.append(key)

result.sort()
print(result[0])
