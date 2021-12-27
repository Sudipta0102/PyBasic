from itertools import groupby
import operator

# groupby takes 2 args:
# 1. iterable
# 2. a key which is a function (can be library or user-defined function or lambda function)


li = [1, 2, 3, 2, 1]


# 1. this is with user defined function as a key
def smaller_than_3(x):
    return x < 3


gb_obj = groupby(li, key=smaller_than_3)
# gb_obj is a groupby object
# so, it can iterated through
for key, val in gb_obj:
    print(key, ':', list(val))

print()


# 2. this is with a lambda as a key
key_func = lambda x: x < 3

gb_obj1 = groupby(li, key_func)
for key, val in gb_obj1:
    print(key,':',list(val))


# # 3. this is with a library function
# gb_obj2 = groupby(li, operator.add)
# for key, val in gb_obj2:
#     print(key, ':', list(val))


# 4. an useful example of groupby. We have list of dictionary that holds name and age.
# we can group by age using groupby()
persons = [{'name': 'ami', 'age': '40'}, {'name': 'tumi', 'age': '31'},
           {'name': 'se', 'age': '40'}, {'name': 'ora', 'age': '42'}]

# here grouping by age
gb_obj3 = groupby(persons, lambda x: x['age'])
for key, val in gb_obj3:
    print(key, ':', list(val))


