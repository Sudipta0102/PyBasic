# 1. enumerate() is a built in function that takes input as iterator, lists etc.
# eg: enumerate(fruits) where fruits = ['apple', 'lemon', 'banana']

# 2. What it returns : a tuple. containing index and the corresponding data.
# eg: ((0, fruits[0]), (1, fruits[1]), (2, fruits[2]))

cars = ['aston', 'audi', 'mcLaren']
# way - 1 using key, value here
for key, value in enumerate(cars):
    print(value)

print()
# way - 2 using only key
for key in enumerate(cars):
    print(key[0], key[1])

# also you can directly return the enumerate() method.
print (enumerate(cars))     # apparently, you can't    


# you can change the start index of the key.
for key in enumerate(cars, start=1):
    print(key[0], key[1]) # now, index starts from 1 instead of 0.