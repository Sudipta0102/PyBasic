# 1. In python, there is nothing called as priavte vars that 
# can be only be accessed inside an object.
# 2. However, if there is a variable prefixed with underscore,
# that particular variable should be treated as non-public part of the API 
# or any python code for that matter. 
# 3. it can be a function or a method but the same rule will apply.
# 4. also, There is some other thing i.e. trailing underscores

# There are three cases(I think):
# 1. single prefix underscore
# 2. double prefix underscore. mangling is at work here.
# 3. double leading and double trailing underscore. (like, __init__, __len__ etc.)
# Things to Note: these point 3 doesn't have anything to do with privateness of 
# a variable. 
class Test:
    def __init__(self):
        # this is like any other variable, you can access from anywhere
        self.boo = 10
        # 1. but a single underscore is prefixed with a variable, that means
        # it's a warning that it's not to be accessed by other class. 
        # compiler doesn't have anything to warn you. It's just a convention
        # or a guideline to make varible kind of private 
        self._boom = 20
        # 2. Now when a variable is prefixed by double underscore, 
        # compiler does something diffrent. What it does is, when it's being 
        # stored as class property, it's also prefixed by _<className>, so 
        # it becomes _<className>__varName. So that it cannot be accessed 
        # directly by other classes. This is called Mangling.  
        self.__booze = 30

t = Test()

print(dir(t))

print(t.boo)
print(t._boom)
print(t.__booze) # AttributeError: 'Test' object has no attribute '__booze'. 
                 # because here double underscore is being used so, it's changed 
                 # to _Test__booze. That's why __booze attribute are not there
                 # in Test class.
                 # btw, You can check all the attributes of a class by using 
                 # dir(t).   

# 3. double leading and double trailing underscore. these are called magic methods.
# every method like these has something special syntactic to do. 
# __file__ tells you location of the python file. 
# __eq__ is executed is a==b is executed.
# etc. etc.