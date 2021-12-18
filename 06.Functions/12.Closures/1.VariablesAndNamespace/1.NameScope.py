# 1. Now, in the first and second file I have one function each with the same name.
# 2. If I want to access this from the this file with import these will be an ambiguity.
# 3. So I need to use imported class name to diffrentiate these two functions.
# 4. This kinda thing is getting handled by the namespace.
# 5. Namespace represents the memory block where all the names are linked to respective 
# object.
# 6. Each class, methods maintains their own namespace. that's basically why we can use
# same name for any classes or functions.
# 7. Also, dir() function can give us the names present in that respective namespace.
# 
#      




import first
import second


print(first.func())
print(second.func())

# here we can  the functions with same name, because they have different namespace.



