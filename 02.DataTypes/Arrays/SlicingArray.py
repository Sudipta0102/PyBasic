import array as arr

l = [1,2,3,4,5,6,7]

a = arr.array('i', l)

for i in (a):
    print(i)

#-----------------------------
print()
slicedArray = a[3:6]

for i in (slicedArray):
    print(i)

#-----------------------------
print()
#from 5th element to last
slicedArray1 = a[5:]    

for i in (slicedArray1):
    print(i)

#-----------------------------
print()
#from first element till the end
slicedArray2 = a[:]    

for i in (slicedArray2):
    print(i)

#-----------------------------
print()
#from first element to third
slicedArray3 = a[:3]

for i in (slicedArray3):
    print(i)

#-----------------------------
print()
#in this case, 
# 1. last element starts from -1 here
# 2. last index is not inclusive (slicedArray4 will print -> 5,6)
slicedArray4 = a[-3:-1]    

for i in (slicedArray4):
    print(i)

#-----------------------------
print()
# i dunno how, but it prints the reverse array
slicedArray5 = a[::-1]

for i in (slicedArray5):
    print(i)

    