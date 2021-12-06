List = [9,8,7,6,5,4,3,2,1,0]
print(List) 

#prints 0 to n-1 (in this case 1 to (3-1)= 2, so [8,7] )
print(List[1:3])

#can be used with negative indexing
print(List[-5:-1])

#print the whole list 
print(List[0::])
#same can be done for negative indexing
print(List[-10::])
#list can be reversed too using this
print(List[::-1])
#print the partial list using this
print(List[2::])

#this particlar case is special I think
#when I do this, it returns the value which id divisible by 2 in reverse order
#using negative index
print(List[::-2]) 
#when I do this, it returns the value which id divisible by 3 in reverse order
print(List[::-3]) 
#when I do this, it returns the value which id divisible by 4 in reverse order
print(List[::-4]) 
