lst = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 3]

seen = set()
duplicates = set()

for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print("Duplicate elements:", list(duplicates))
