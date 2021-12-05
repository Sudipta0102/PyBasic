# taking an empty list of list 
list = [ ]
n = int(input("Enter the number of elements:"))

for i in range(0, n):
    # inner list is of static length which is 2
    # one string and one int
    element = [input(), int(input())]
    list.append(element)

print(list)