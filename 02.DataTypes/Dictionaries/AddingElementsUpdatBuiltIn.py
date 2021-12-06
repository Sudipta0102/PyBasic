d = {1: "Name", 2: "age"}
print(d)
# lookout for update argument syntax, it's confusing to me
# update existing keys
d.update({1: [1,2,3,4]})
print(d)
# also you can update new values with update() function
d.update({"Name": "PseudoFunc"})
print(d)

