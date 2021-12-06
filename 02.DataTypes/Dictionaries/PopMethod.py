# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks1'}
print(Dict)

#takes a key as an argument
poppedElement = Dict.pop(3);
#this will not work because dictionary cannot be concatenated to a String
#print("Dictionary after popping: "+ Dict)
print("Dictionary after popping: "+ str(Dict))
print("Popped element: "+str(poppedElement))