my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
# this will keep their original type intact and add it to a list
my_list = [my_set, my_tuple]
print(my_list)

# merging onto a list will be done like this:
my_list = [*my_tuple, *my_set]
print(my_list)


