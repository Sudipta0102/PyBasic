#creating nested dictionary
a = {1:"1,2,3,4", 3: "My Name" , 2:"is Unimportant", "Age": "at this age"}
b = dict([(1,"blah"),(2,"bleh")])
#Now creating nested dictionary
c = {1:a, 2:b}
print(c)