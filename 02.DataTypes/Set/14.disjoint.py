# returns true if the no elements are common between two sets.

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
s3 = {4, 5, 6}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
