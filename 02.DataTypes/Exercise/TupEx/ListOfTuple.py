# Given a list of numbers of list, write a Python program to create a list of tuples
# having first element as the number and second element as the cube of the number.

nums = [2,1,4,5]

new_nums = []

# op->
#[(2, 8), (1, 1), (4, 64), (5, 125)]

for key, value in enumerate(nums):
    new_nums.append((key, value))


print(new_nums)

new_nums = [(val, pow(val, 3)) for val in nums]

print(new_nums)