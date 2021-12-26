from collections import defaultdict

# 1. default dict is same as normal dictionary with one difference which is you can have a default
# value of your choice and if somebody searched for a key which is not present in dictionary,
# instead of giving keyerror, it will just return the default value of that dictionary.
#
# 2. it has all the other properties and attributes of a dictionary.
#
# 3. it's a subclass of dict
d = defaultdict(int, first=1, seond=2)

print(d['first'])
print(d['third']) # it's giving zero because I have set the default datatype as int


s = 'Key not present, wat up!'

d2 = defaultdict(s, first=1, seond=2)

print(d2)

