# the problem statement:
# 1. You have a pattern and a string
# 2. the task is to sort the string according to the order defined in the pattern.
# 3. assumption: pattern string has all the chars of the to be sorted string and chars appear only once.

def mfunc(pattern, string):

    # converting pattern to list
    list_pattern = list(pattern)

    # converting this list to a dictionary having the key as chars and val as their position
    mydict = {list_pattern[i]: i for i in range(len(list_pattern))}

    # convert the string to list
    str_list = list(string)

    str_list.sort(key=lambda element: mydict[element], reverse=True)

    return ''.join(str_list)


p = "ealsbkcfdmignot"
s = "elkcit"

print(mfunc(p, s))

mfunc(p, s)



