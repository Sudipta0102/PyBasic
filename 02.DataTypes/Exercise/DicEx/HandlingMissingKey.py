
d = { 'a' : 1 , 'b' : 2 }

# 1. print(d[c]) this will give error

print(d.get('c')) # it says 'None'

# 2. with get() you can define your message whenever any key is not present.
# If the key is present then it will print the respective value
# else, it will print the defined message
print(d.get('a', 'Not Found'))
print(d.get('c', 'Not found'))

# 3. defaultdict -> it's a container defined in 'collections' module.
#        it takes a default factory as an argument
# this is faster than get().
import collections

defd = collections.defaultdict(lambda: 'key not found')
defd['a'] = 1

print(defd['a'])
print(defd['c'])

# Python code to demonstrate a dictionary
# with multiple inputs in a key.


# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;

# print the dictionary
print(dict)

