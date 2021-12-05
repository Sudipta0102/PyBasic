# taking multiple inputs at a time and typecasting using list() function.

x = list(map(int, input("Enter multiple values here: ").split()))
print("List of students: ", x)