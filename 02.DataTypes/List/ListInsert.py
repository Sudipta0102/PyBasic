List = [1,2,3,4]
print(List)

#insert(index, value)
#can use Insert method to add an element in a particular position
List.insert(0,0)
print(List)

#if the index is greater than the size of the list then, it doesn't 
#throw error/exception.
#Instead, it inserts the value at the last
List.insert(114,0)
print(List)