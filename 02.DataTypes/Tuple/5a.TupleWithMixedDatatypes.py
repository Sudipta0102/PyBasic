Tuple1 = (5,"you", 7 , 8, "are a mean one")
print(Tuple1)
print(tuple(Tuple1))

#Nested Tuple
Tuple1 = (1,2,3,4)
Tuple2 = ("Pipeline", "Scalability")
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

#Tuple with repeatition
Tuple1 = ("Geeky",)*3
print(Tuple1)

#Tuple with Loop
n=5
for i in range(n):
    Tuple1 = (Tuple1,)
    print(Tuple1)