d1 = {1: "ami",2: "tumi", 3: 5, 5: "ami"}

# 1. keys traversal
for key in d1:
    print(key, end=' ')

print()

# 2. also with key() method:
for key in d1.keys():
    print(key, end=' ')

print()

# 3. Value traversal with values() method.
for value in d1.values():
    print(value, end=' ')

print()

# 4. loop through key and value both with items():
for key, value in d1.items():
    print(key, ':', value)
