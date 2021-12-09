# program to find all the elements in a list are odd or not

list1 = []
list2 = []

for i in range(1,21):
    list1.append(4*i-3)

print(list1)    

for i in range(0,20):
    list2.append(list1[i]%2!=0)

print(list2)

# if All the elements are true, then only it will return true.
print(all(list2))