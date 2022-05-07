import itertools

list_1 = ["a", "b", "c", "d"]
list_2 = [1, 4, 9]

unique_comb = []

# Getting all permutations of list_1
# with length of list_2 because length of list_2 is smaller
permutations = itertools.permutations(list_1, len(list_1) if len(list_1) < len(list_2) else len(list_2))

for i in permutations:
    zipped = zip(list_2, permutations)
    unique_comb.append(list(zipped))

print(unique_comb)

unique_combinations = list(list(zip(list_1, element))
                           for element in itertools.product(list_2, repeat=len(list_1)))

print(unique_combinations)