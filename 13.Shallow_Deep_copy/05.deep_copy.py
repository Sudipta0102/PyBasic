import copy

# when it comes to dealing 2d or bigger data-structure and you don't want to tamper the original data-structure
# then, deep copy should be your friend.
list_a = [[1, 2, 3], [4, 5, 6]]
list_b = copy.deepcopy(list_a)

list_b[0][0] = 10

print(list_a)
print(list_b)

# see only list b is changed keeping the original one intact. that's grand, right?!

