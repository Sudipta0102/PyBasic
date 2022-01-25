import numpy as np


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return str((self.name, self.age))


p1 = Person('ami', 11)
p2 = Person('tumi', 12)
p3 = Person('ora', 13)
p4 = Person('sobai', 14)
print(p1)

obj_list = [p1]
obj_tuple = (p1, p2, p3, p4)

arr = np.full((3, 4), obj_list, dtype=Person)
print(arr)

arr = np.full((3, 4), obj_tuple, dtype=Person)
print(arr)

