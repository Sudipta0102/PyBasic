from itertools import combinations, combinations_with_replacement

# 1. takes iterable and group size argument
# 2. group size is mandatory here
# 3. Also if the group size is greater than the length of iterable,
# then it returns nothing.
# 4. One more important thing is, there are no duplicates returned in this function.
# but the duplicates can be achieved by using combinations_with_replacement()


print(list(combinations('ABC', 4))) # point 3

print(list(combinations(range(1, 5), 2)))


com = combinations([1, 2, 3], 2)
print(list(com))


com1 = combinations_with_replacement([1, 2, 3], 2)
print(list(com1))
