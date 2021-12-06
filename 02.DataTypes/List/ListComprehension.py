oldList = [1,2,3,4,5,6,7,8,9,10]
print(oldList)

#rule is,
#newList = [expr(element) for element in oldList if condition]
newList = [x+1 for x in oldList]
print(newList)

newList1 = [x*x*x for x in oldList if x%2==0]
print(newList1)

#and obviously, yo can use range() with for loop here
newList2 = [x+2 for x in range(1,11) if x%2==0]
print(newList2)

# below list contains square of all 
# odd numbers from range 1 to 10 
newList3 = [x*x for x in range(1,11) if x%2==1]
print(newList3)