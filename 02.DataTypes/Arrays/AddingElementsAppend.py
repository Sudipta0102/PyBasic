import array as arr
a = arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i])
print()    
a.append(4)
for i in range(0,4):
    print(a[i])

print()
# this is equivalent of forEach  loop in java (it says i in (a):)
for i in (a):
    print(i)
    