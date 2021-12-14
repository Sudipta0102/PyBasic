# When to use a dictionary:
# 1. When you need a logical association between a key:value pair.
# 2. When you need fast lookup for your data, based on a custom key.
# 3. When your data is being constantly modified. Remember, dictionaries are mutable.

# When to use the other Lists: 
# 1. Use lists if you have a collection of data that does not need random access. 
# 2. Try to choose lists when you need a simple, iterable collection 
# that is modified frequently.

# When to use the other Sets: 
# 1. Use a set if you need uniqueness for the elements.

# When to use the other Tuples:  
# 1. Use tuples when your data cannot/should not change. i.e. you want use 
# the immutability feature.

          


def apply_twize(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5    

print(apply_twize(add_five, 10))    







