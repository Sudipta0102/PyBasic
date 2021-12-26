# 1. update() method.
def merge_dic(d1, d2):
    d1.update(d2)
    return d1


dict1 = {1: 11, 2: 22}
dict2 = {3: 33, 4: 44}

print(merge_dic(dict1, dict2))


# 2. using **kwargs. This is a generic way to merging anything. But, it needs a new dictionary
# to store the merged values.
def merge_dic1(d1, d2):
    res = {**d1, **d2}
    return res


dict1 = {1: 11, 2: 22}
dict2 = {3: 33, 4: 44}

print(merge_dic1(dict1, dict2))


# 3. this is after 3.9.
def merge_dic2(d1, d2):
    return d1 | d2


dict1 = {1: 11, 2: 22}
dict2 = {3: 33, 4: 44}

print(merge_dic2(dict1, dict2))
