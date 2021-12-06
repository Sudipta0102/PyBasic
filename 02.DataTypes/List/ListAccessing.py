List = [1,2,3,4]
print(List)

#can add multiple values at a time
List.extend([11,22,33,44])
print(List)

#index starts from 0(zero) 
print(List[5])

#This is one way of creating multi dimasional List 
List1 = ["Ami", "Tumi"]
List2 = ["Ora", "Sobai"]

List3 = [List1, List2]

print(List3)

#Accessing multi Dimensional list
print(List3[0])
print(List3[0][0])