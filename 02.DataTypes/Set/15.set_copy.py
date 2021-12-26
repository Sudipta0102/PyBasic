s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}

# 1. this assignment copies the original set but as a result, destination set reference points to the
# original set. So any change in either of them will affect the other.
s3 = s1

s3.add(4)

# after adding in s3, s1 also got changed.
print(s1)
print(s3)

# 2.
s3 = s1.copy()

s3.add(5)

print(s1)
print(s3)

