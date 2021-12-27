
# list comprehension rule is:
# newList = [expr(element) for element in oldList if condition]

# Example: creating a table of 10: 
tables = [lambda x=x:x*10 for x in range(1, 11)]

for num in tables:
    print(num(), end = ' ')
