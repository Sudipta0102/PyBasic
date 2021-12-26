from collections import OrderedDict

# basically, it's like regular dictionary with one key difference which is it remembers the order
# in which the keys are inserted,

ordered_dict = OrderedDict()

ordered_dict['d'] = 2
ordered_dict['a'] = 1
ordered_dict['e'] = 9
ordered_dict['3'] = 2

print(ordered_dict)

dict = dict()

dict['d'] = 2
dict['a'] = 1
dict['e'] = 9
dict['3'] = 2

print(dict)

# I think normal dictionary also remembers this order

# OrderedDict has all the other properties and attributes as normal dictionary.

