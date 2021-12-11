

# this repeats the string 4 times
print("hellish" * 4)

# overloading + operator
class A: 
    def __init__(self, a):
        self.a = a

    # adding two objects
    # __add__ is one of those magic methods
    def __add__(self, o):
        return self.a + o.a

obj1 = A(1)
obj2 = A(2)
obj3 = A("Hellish")
obj4 = A("Love")

print(obj1 + obj2)
print(obj3 + obj4)
        
# Note: operator has bunch magic methods by which we can overload
# them.
        