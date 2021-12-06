import array as a
x = a.array('i', [1,2,3])
for i in range(0,3):
    print(x[i])

print()

x.insert(0,0)
x.insert(2,10)
x.insert(50, 20) #this is consistent behaviour with other datatypes in python
# which is if any value is inserted at an invalid index greater than the length 
# of the array, then python inserts at the last. 
for i in range(0,6):
    print(x[i])