test_str = 'bleh 33 is   best'

print("The original string is: " + str(test_str))
print(len(test_str))

# 1.
res = sum(not chr.isspace() for chr in test_str)
print(res)
test_str = 'bleh 33 is   best'

# 2.
res = sum(map(len, test_str.split()))
print(res)
