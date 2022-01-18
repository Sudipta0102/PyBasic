dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

dict_c = {**dict_a, **dict_b}
print(dict_c)


# IMPORTANT NOTE: merging dicitonary doesn't work if it has non-string keys.
dict_a = {'a': 1, 'b': 2}
dict_b = {3: 3, 'd': 4}

# this works
dict_c = {**dict_a, **dict_b}
print(dict_c)

# this doesn't, TypeError: keywords must be strings
# https://stackoverflow.com/questions/38987
# /how-do-i-merge-two-dictionaries-in-a-single-expression-take-union-of-dictionari/39858#39858
dict_c = dict(dict_a, **dict_b)
print(dict_c)