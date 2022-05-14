str1 = 'aabcddekll12@'  # first string
str2 = 'bb2211@55k'  # second string

# 1. using naive
res = []
for c1 in str1:
    for c2 in str2:
        if c1 == c2 and res.count(c1) == 0:
            res.append(c1)

print(res)

# 2. using set intersection
set1 = set(str1)
set2 = set(str2)

matched_chars = set1 & set2
print(matched_chars)
print(len(matched_chars))

# 3. using find()
c, j = 0, 0

# https://www.geeksforgeeks.org/python-count-the-number-of-matching-characters-in-a-pair-of-string/
for i in str1:
    if str2.find(i) >= 0 and j == str1.find(i):
        c += 1
    j += 1

print(c)
