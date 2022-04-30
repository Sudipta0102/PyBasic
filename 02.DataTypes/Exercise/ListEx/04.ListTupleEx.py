contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]    


name = input()


# 1st way to get individual tuple element
names = [item[0] for item in contacts]
ages = [item[1] for item in contacts]

if name in names:
    index = names.index(name)

print(f"{name} is {ages[index]}")    


# there has to be a better way than this.

