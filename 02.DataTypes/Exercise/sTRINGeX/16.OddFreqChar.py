from collections import Counter

s = "aassddafffffffg"

x = Counter(s)

for key, val in x.items():
    if val % 2 != 0:
        print(key, end=" ")
print()


# list comprehension
res = [key for key, val in Counter(s).items() if val % 2 != 0]
print(res)
