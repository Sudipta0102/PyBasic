class A:
    def __init__(self, a):
        self.a = a;

    def __lt__(self, other):
        if(self.a<other.a):
            return "obj1 less than obj2"
        else:
            return "obj1 greater than obj2"

    def __eq__(self, other):
        if(self.a == other.a):
            return "obj1 equals obj2"            

obj1 = A(4)
obj2 = A(5)

print(obj1 == obj2 or obj1<obj2)