list1 = [2, -7, 5, -64, -14]
pos = neg = 0

for ele in list1:
    if ele >= 0:
        pos += 1
    else:
        neg += 1

print(pos)
print(neg)

# using filter
pos_count = len(list(filter(lambda x: (x >= 0), list1)))
print(pos_count)
neg_count = len(list(filter(lambda x: (x < 0), list1)))
print(neg_count)
