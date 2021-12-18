s = 'blah'

# if i just do this
print(lambda  x : print(s))
# it will just the print address this function object is stored

# but let's just store that in a variable now
func_Obj = lambda x : print(x)
# with that, pass your input string as an argument
func_Obj(s) # now it will print 'blah'

# you can also do this one liner
(lambda x : print(x))(s) # it will do the same thing

