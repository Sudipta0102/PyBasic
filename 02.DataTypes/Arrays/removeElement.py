import array

a = array.array('i', [1, 2, 3, 1, 2, 5])
print(a)

# removes the value of given index
a.remove(a[5])

# removes 1st occurence of given number in the array
a.remove(2)
for i in (a):
    print(i)

