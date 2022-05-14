from collections import Counter

s = "aassddaaffg"
# 1. using Counter
x = Counter(s)
min = len(s) + 1 # because any frequency can not be greater than the length of the string
min_char = ''
print(x)
for key, val in x.items():
    print(f"{key} : {val}")
    if val < min:
        min_char = key
        min = val

print(min_char)








