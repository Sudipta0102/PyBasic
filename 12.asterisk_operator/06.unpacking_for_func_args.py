def mfunc(a, b, c):
    print(a, b, c)


# lengths must match
my_list = [1, 2, 3]
mfunc(*my_list)

# again, lengths must match
my_string = 'ABC'
mfunc(*my_string)

# lengths and KEYS must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
mfunc(**my_dict)

# TypeError: mfunc() got an unexpected keyword argument 'd'
my_dict1 = {'d': 1, 'e': 2, 'f': 3}
mfunc(**my_dict1)

