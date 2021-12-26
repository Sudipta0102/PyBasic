from collections import Counter

s = 'aaaaaccaaabbbbbaabbccccc'
counter1 = Counter(s)
print(counter1)

# 1.
for key in counter1:
    print(key, end=' ')

print()

# 2. keys()
for key in counter1.keys():
    print(key, end=' ')

print()

# 3. values()
for val in counter1.values():
    print(val, end=' ')

print()

# 4. item() -> both keys and values
for key, val in counter1.items():
    print(key, ':', val)
