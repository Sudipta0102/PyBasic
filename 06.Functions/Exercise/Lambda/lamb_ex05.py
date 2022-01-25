# In a list, all numbers occur even times except one num. Find the num.
import functools
import collections

# 1. stupid way

my_list = [2, 1, 1, 2, 3, 3, 2]
my_dict = {}
# creating a dictionary with element and occurrence
for key in my_list:
    if key in my_dict.keys():
        my_dict[key] += 1
    else:
        my_dict[key] = 1


for key in my_dict:
    if my_dict[key]%2 != 0:
        print('Number is: ', key)
        break

# 2. using lambda and XOR

# 2^1 = 2
# 2^1 = 2
x = ((((((2 ^ 1) ^ 1) ^ 2) ^ 3) ^ 3) ^ 2)
print(x)


def using_lambda(my_another_list):

    return functools.reduce(lambda a, b: a ^ b, my_another_list)


l1 = [2, 1, 1, 2, 3, 3, 2]
using_lambda(l1)

# 3. using Counter
c = collections.Counter(l1)
print(c)

for key in c.keys():
    if c[key]%2 != 0:
        print('number: ', key)
        break


