class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False        

obj1 = A(3)
obj2 = A(2)

print(obj1>obj2)