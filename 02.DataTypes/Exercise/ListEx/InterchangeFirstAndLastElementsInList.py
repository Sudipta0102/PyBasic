#1.
i = [12, 35, 9, 56, 24]
print(i)

# last element is i[len(i)-1] in a conventional way.
i[0], i[len(i)-1] = i[len(i)-1], i[0]

print(i)

#2.
i = [12, 35, 9, 56, 24]
# also, last element can be i[-1] in python. So,
print(i)
i[0], i[-1] = i[-1], i[0]
print(i)

#3.
i = [12, 35, 9, 56, 24]
# also, you can breakdown the above approach by tuple unpacking
print(i)
# first, save the first and last var of list in a variable
# i.e. packing the varible in a tuple
packThenUnpack = i[0], i[-1]

#then when unpacking, unpack in a reverse way.
i[-1], i[0] = packThenUnpack

print(i)

#4
i = [12, 35, 9, 56, 24]
print(i)
# the same above approach can be applied to * operator.
start, *middle, end = i
# this below way it returns a tuple instead of a list
#i = end, *middle, start
# if you want a list then
i = [end, *middle, start]
print(i) 


