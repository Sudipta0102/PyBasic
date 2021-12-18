# 1. Anonymous Function is functions without a name
# 2. lambda keyword is used to create an anonymous function
# 3. the syntax is kinda like,
# lambda arguments: expression
# 4. lambda can have number of arguments but only one expression 
# which is evaluated and returned. 
# so this is like syntactically restricted to single expression
# 5. Whereverfunction objects are required, we can use lambda functions.


# normal functions
def cubeNum(num): return num*num*num

# anonymous functions
cubeX = lambda x: x*x*x

print(cubeNum(7))
print(cubeX(7))