even = {2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}
prime = {1, 2, 3, 5, 7}

print(prime.intersection(even))
print(prime.intersection(odd))


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# update() -> this is like union update. also in place
s1.update(s2)
print(s1)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# intersection_update(), also in place
s1.intersection_update(s2)
print(s1)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# difference_update(), in place
s1.difference_update(s2)
print(s1)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# symmetric_difference(), in place
s1.symmetric_difference(s2)
print(s1)

