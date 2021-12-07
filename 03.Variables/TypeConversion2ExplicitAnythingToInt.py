s = "10010"
# if we use base 2, essentially you are converting binary number 
# into decimal  
i = int(s, 2)
print(i)
# base 10 gives you the original number in int
i = int(s, 10)
print(i)

# but the below one does not work with base 2
# because number consists digits other than 0 and 1
s1 = "18"
i = int(s1, 10)
print(i)
#doesn't work
i = int(s1, 2)
print(i)