set = {8, 16, 24, 1, 25, 3, 10, 65, 55}

print(set)

# using remove()
set.remove(1)

print("--------------------------")

print(set)

set = {8, 16, 24, 1, 25, 3, 10, 65, 55}

# using pop()
while set:
    # Note if you for loop here, it will give you an error because everytime you pop one item,
    # the length of the set is changed which is different from the static value of len(set) or set
    # which comes from the initial set.
    set.pop()
    print(set)


