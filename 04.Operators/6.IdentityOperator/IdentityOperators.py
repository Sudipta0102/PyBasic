a = 10
b = 20
c = a

print(a is b)
print(a is c) # gives true, so it doesn't check the object itself, 
              # only compares the  values.
print(a is not b)
print(a is not c) # gives false, so it doesn't check the object itself, 
                  # only compares the values.             