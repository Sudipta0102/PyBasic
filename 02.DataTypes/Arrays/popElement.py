import array as arr
a = arr.array('i',[1, 2, 3, 6])

for i in range(0,4):
    print(a[i])
#print()

x = a.pop(2)
print("popped item: "+str(x))

for i in range(0,3):
    print(a[i])
