dictOuter = {1: {},2: {}}
print(dictOuter)
dictOuter = {1: {11: "innerVal"}, 2: {22, "innerVal"}}
print(dictOuter)

print("Accessing value out of an nested dictionary: ")
print(dictOuter[1])
print(dictOuter[1][11])
