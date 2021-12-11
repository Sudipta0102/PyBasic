list1 = []
list2 = []

list3 = list1

# 1 -> prints True because == operator only checks for the value
# Here, both are empty so prints True.
if(list1 == list2):
    print("True")
else:
    print("False")

# 2 -> prints false because is operator checks for object and because the 
# list1 and list2 are different objects and have diffrent addresses, it 
# prints False. 
if(list1 is list2):
    print("True")
else:
    print("False")

# 3
# prints True, because both lists are empty (so, they are same in value)
if(list1 == list3):
    print("True")
else: 
    print("False")

# this is true, they point to the same addess. 
if(list1 is list3):
    print("True")
else: 
    print("False")


# get the address of the object
print(id(list1))
print(id(list2))
print(id(list3))    