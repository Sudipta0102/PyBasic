from itertools import permutations

# takes permutations(iterable, group size)
print(list(permutations(range(0, 2), 2)))

# if group size is not mentioned or 0 then group size becomes length of the iterable
print(list(permutations('AB')))

# also, if the group size is greater than the range() or ant iterable with which the
# permutation method is being fed, then it returns nothing
# in this case, an empty list
print(list(permutations(range(0, 2), 3)))


l = [1, 2, 3]
# perm is an itertool.permutations object
perm = permutations(l)
# converting into a a list
print(list(perm))


# mentioning group size, you can have a shorter group
perm1 = permutations(l, 2)
print(list(perm1))