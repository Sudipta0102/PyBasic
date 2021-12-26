str = "Datapoints of Envy"

print(str[0:10])
print(str[0::])
print(str[::-1])#reverse printing
print(str[::-2])#every second letter in reverse order
print(str[::-3])#every third letter in reverse order
print(str[::-4])
print(str[::-5])
print(len(str))

str1 = "123456789"
print(str1[::-5])


#can use both positive and negative indexing in same slice expression
print(str1[2:-1])