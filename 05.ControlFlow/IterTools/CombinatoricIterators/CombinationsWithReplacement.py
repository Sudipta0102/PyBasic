# does the same thing as combinatuons() but here, individual elements 
# mat repeat itself

from itertools import combinations_with_replacement, combinations

print(list(combinations_with_replacement('AB', 2)))
print(list(combinations('AB', 2)))
