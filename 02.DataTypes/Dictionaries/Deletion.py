# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A': {6 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B': {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)      

# 1. del
del Dict[6]
print(Dict)

del Dict['A'][6]
print(Dict)

# 2. pop()
Dict.pop(5)
print(Dict)

# 3. popitem() -> it pops the last item
Dict.popitem()
print(Dict)
