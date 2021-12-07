# ** needs to be used when packing and unpacking with dictionary

def func1(a, b, c):
    print(a, b, c)

# i am not really sure but it seems like the keys in dictionary and
# variable names in the function argument needs to be same.
d = {'a': "name", 'b': "love", 'c':'slep'}
func1(**d)    
