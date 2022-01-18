import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("bleh", 20)
# assignment operator, so it is supposed to change the original too
p2 = p1

p2.age = 28

print(p1.age)
print(p2.age)


# as it's a 1d object (not nested) custom object, you get to shallow copy keeping the original one intact.
p3 = Person('bluh', 30)
p4 = copy.copy(p1)

p4.age = 28

print(p3.age)
print(p4.age)

