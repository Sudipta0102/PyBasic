# 1. makes a shallow copy of the dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict)
DictCopy = Dict.copy()
print(DictCopy)

# 2. One thing to remember here, If we just assign the values then, dictionary gets copied
# But in the process, same referce gets shared by both original and copied dictionary,
# Then if we make a change to any of the dictionaries then, both of them will have the changes.

d1 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
copy_d1 = d1
copy_d1[6] = 'sobai'

print(d1)
print(copy_d1)


# 3. also, dict() method can be used
d1 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

copy_d1 = dict(d1)
copy_d1[6] = 'sobai'
print(d1)
print(copy_d1)