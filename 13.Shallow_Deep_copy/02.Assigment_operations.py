# this below thing will just create a new variable with the same reference.
# here, modifying one will affect the other.
list_a = [1, 2, 3]
# assignment here.
list_b = list_a

list_b[0] = 10
print(list_a)
print(list_b)
