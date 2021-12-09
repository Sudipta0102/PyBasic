# this little thing tries to find any number in a list 
# can be divided by 5 or not.
# prerequisite: All the numbers in the list have to be
# divisible by 4

list1 = []
list2 = []

# here as you can see, index will be multiplied by 4 and appended
# to the list
for i in range(1,11):
    list1.append(i*4)

print(list1)

# list2 will put true or false based on the condition given.
for i in range(0,10):
    list2.append(list1[i]%5==0)

print(list2)

# Now, if any of the elements in list2 is true, it will return true.
print(any(list2)) 