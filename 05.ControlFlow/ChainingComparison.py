# list of comparison operator :
# ">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"
x = 5
print(1<x<10) 
# this is what chaining comparison is, using more than 
# one comparison operator subsequently.
# 1. You can use any operator with any operator.

print(5 == x > 4)

print(10 > x <= 9)

print(x < 10 < x*10 <100)

a, b, c ,d, e, f = 0, 5, 12, 0, 15, 15

exp1 = a <= b < c > d is not e is f
# here , left to right operations are:
# a<=b -> true
# b<c -> true
# c>d -> true
# d is not e -> true
# e is f -> true
# So the whole expression is true.
print(exp1)

exp2 = a is d > f is not c
# here left to right operations are:
# a is d -> true
# d>f -> false 
# f is not c -> true
# So the whole expression is false
print(exp2)

