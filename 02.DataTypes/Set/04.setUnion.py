setFirst = {1, 2, 3, 4, 5}
setSecond = {4, 5, 6, 7, 8}

# 1.
# this is Union operator 
# 1. so, it creates a new set with values which is common and unique to the sets.
# 2. and common values will not be duplicated to the resultant set. 

print(setFirst | setSecond)

# 2. using union()

s = setFirst.union(setSecond)
print(s)