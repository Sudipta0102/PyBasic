# Count the number of spaces in a string

s = 'Do not be a stranger'

c = 0

for x in s:
    if x == ' ':
        c += 1

print(c)


c1 = len([char for char in s if char == ' '])

print(c1)
