# There is no switch case in python. To get around that, we need to use
# Dictionary Mapping
# dict.get() can be used for this. 

dict= {1: 100}

print(dict.get(1))
print(dict.get(2, "Nothing"))