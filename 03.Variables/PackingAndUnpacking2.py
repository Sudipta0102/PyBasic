# Now lets say, we don't know how many arguments needs to be passed in the 
# function. Then we can use 'packing' concept to pack all the arguments 
# in a tuple.
def func(*arg):
    return sum(arg)

print(func(1, 2, 3, 4, 5))
print(func(10, 20))