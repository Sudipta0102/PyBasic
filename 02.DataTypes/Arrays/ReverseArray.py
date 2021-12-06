import array as arr
a = arr.array('i', [1,2,3,4,5,6,7,8])
print(a)

for i in (a):
    print(i)

print()

#reverse 1:
reversedArray = a[::-1]

for i in (reversedArray):
    print(i)

#reverse 2:
print()
#reverse() doesn't have a return type, it changes the main array
a.reverse()

for i in (a):
    print(i)
