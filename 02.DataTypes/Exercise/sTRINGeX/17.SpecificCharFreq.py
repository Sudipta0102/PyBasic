from collections import Counter

test_list = ["geeksforgeeks is best for geeks"]
chr_list = ['e', 'b', 'g']

x = Counter(test_list)

# dictionary comprehension as we need to retrieve key, value pair
res = {key: val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}
print(res)

# Counter to Dictionary conversion
x = Counter("".join(test_list))
print(x)
print(dict(x))

