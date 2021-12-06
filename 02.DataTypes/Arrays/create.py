#importing array for array creation
import array as arr

#creating an array with integer type
# 'i' -> integer type
a = arr.array('i',[1,2,3])
b = [1,2,3,4]#this is not an array, it's a list because b = [1,2,3,"bleh"]
#is also valid
print(b)

#printing the original array
print("Array:", end = " ")
for i in range(0,3):
    print(a[i], sep = "")
print(b)    
print()

c = arr.array('d',[2.5,3.5,1.6])
for i in range(0,3):
    print(c[i])
    