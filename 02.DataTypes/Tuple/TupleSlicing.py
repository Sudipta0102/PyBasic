Tuple1 = tuple("IAmForReal")

print(Tuple1[1:])
print(Tuple1[2:4])

# this just prints the whole thing barring the last character
print(Tuple1[:-1])
# below reverses the whole list
print(Tuple1[::-1])

# also, You can use a step argument, using 2 here so every second element pops up
print(Tuple1[::2])

# you can do tricky thing like, using -2 so elemnt will be reversed and then every second element pops up
print(Tuple1[::-2])

