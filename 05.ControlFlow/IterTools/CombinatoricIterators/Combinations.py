from itertools import combinations

# 1. takes iterable and group size argument
# 2. group size is mandatory here
# 3. Also if the group size is greater than the length of iterable,
# then it returns nothing.
# 4 One more important thing is, there are no duplicates returned in this function


print(list(combinations('ABC', 4))) # point 3

print(list(combinations(range(1, 5), 2)))