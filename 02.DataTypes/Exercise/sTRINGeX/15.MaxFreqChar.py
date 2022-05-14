from collections import Counter

s = "aassddaaffg"

x = Counter(s)
max = 0
max_char = ''

for key, val in x.items():
    if val > max:
        max = val
        max_char = key

print(max_char)