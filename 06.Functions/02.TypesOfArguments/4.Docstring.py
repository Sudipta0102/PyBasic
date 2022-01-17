# 1. Syntax: print(function_name.__doc__)
# 2. The use of docstring in functions is optional 
# but it is considered a good practice.

def even_or_odd(x):
    """Functions to check given number is even or odd"""

    if x%2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')


print(even_or_odd.__doc__)
print(3)        

print(zip.__doc__)
