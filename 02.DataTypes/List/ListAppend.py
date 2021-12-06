List = []
print(List)
# you can append any one value 
List.append('ami')
List.append('d')
List.append(1)

print(List)

print(len(List))

# can append like more than one values at a time (No, it cant you asshole)
# but you can do that as a form of tuple though, also you can use extend() for that.
List.append("Sudhu ora")
print(List)

# also you can append a whole list
List2 = ["ami", "tumi", "sobai", "keu keu"]

List.append(List2)

print(List)

#you can add tuples to a list
List.append((5,6))
print(List)

#for loop can be used to add values in a list
List3 = []
for i in range(1,6):
    List3.append(i)

print(List3)

# can append a list with a list
List1 = ["Ami", "Tumi"]
List2 = ["Ora", "Sobai"]
List1.append(List2)
print(List1)

# you can just concatenate two list
List1 = ["Ami", "Tumi"]
List2 = ["Ora", "Sobai"]
List3 = List1+List2
print(List3)