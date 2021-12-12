from itertools import permutations

print(list(permutations(range(0, 2), 2))) # takes permutations(iterable, group size)
print(list(permutations('AB'))) # if group size is not mentioned or 0 then group size 
                                # becomes length of the iterable

print(list(permutations(range(0, 2), 3))) # also, if the group size is greater than 
                                          # the range() then ir returns nothing
                                          # in this case, an empty list
                                                                          