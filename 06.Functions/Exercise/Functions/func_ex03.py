# Sorting objects of user defined class in Python

class bleh:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))


b1 = bleh('one', 1)
print(b1)

# list of objects
list_of_bleh_obj = [bleh('two', 2), bleh('four', 4), bleh('three', 3), bleh('one', 1)]
print(list_of_bleh_obj)
# using sorted()
print(sorted(list_of_bleh_obj, key=lambda x: x.b))

list_of_bleh_obj = [bleh('two', 2), bleh('four', 4), bleh('three', 3), bleh('one', 1)]
# using sorted() but different key
# this is only for string attribute
print(sorted(list_of_bleh_obj, key=lambda x: x.a.lower()))

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# total_ordering
import functools

help(functools.total_ordering)


@functools.total_ordering
class bluh:
    print("Inside class")

    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.b < other.b

    def __gt__(self, other):
        return self.b > other.b

    def __le__(self, other):
        return self.b <= other.b

    def __ge__(self, other):
        return self.b >= other.b

    def __eq__(self, other):
        return self.b == other.b

    def __repr__(self):
        return str((self.a, self.b))


list_of_bluh_obj = [bluh('two', 2), bluh('four', 4), bluh('three', 3), bluh('one', 1)]
print('*'* 30)
print(list_of_bluh_obj)
print(sorted(list_of_bluh_obj))

# This method depicts how objects of a user-defined class can be sorted using functools
# inbuilt method total_ordering as a decorator to the class. Here, the class is defined
# normally as done in the above examples, only difference being during sorting,
# total_ordering() decorator is used. Two requirements for using total_ordering() are:
#    a. Out of less than(__lt__), greater than(__gt__), less than equal to(__le__) and
#    greater than equal to(__ge__), atleast one should be defined in the class being
#    decorated using this method.
#
#    b. Equal to (__eq__) should be defined.
