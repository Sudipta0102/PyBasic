# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest
# with over 1000 people attending’

s = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

s1 = "1984"


l = [nums for nums in s.split() if nums.isnumeric()]
l1 = [nums for nums in s if nums.isdigit()]

print(l)
print(l1)

