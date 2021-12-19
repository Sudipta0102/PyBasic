# iterating keys
ip = {'a' : 100, 'b': 200, 'c': 300}

sum=0

for key in ip.keys():
    sum += ip[key]

print(sum)


# iterating values
sum1 = 0

for val in ip.values():
    sum1 +=val

print(sum1)


