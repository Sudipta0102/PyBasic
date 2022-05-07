l = [1, 2, 3]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                print(l[i], l[j], l[k])

# 2. using permutations
import itertools

comb = itertools.permutations(l, 3)

for i in comb:
    print(i)