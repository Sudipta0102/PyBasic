#empty tuple
Tuple1 = ()
print(Tuple1)

#String Tuple
Tuple1 = ('NoGods','NoDaemons');
print(Tuple1)

#Tuple with a list
list1 = [1,2,3,4,5]
print(tuple(list1))

#creating a tuple a built in function, it will create individual character out of strings
#iteraring through the string
Tuple1 = tuple('Geeks')
print(Tuple1)

Tuple1 = tuple(123) #this will give error, because int object s not iterable 
print(Tuple1)