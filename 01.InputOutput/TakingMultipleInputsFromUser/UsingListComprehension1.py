# 1. List comprehension: is an elegant way to define and create list in python.
# 2. Lists just like mathematical statements can be created in one line only.
# 3. This also can be used in getting multiple inputs from the user.

# taking two inputs at a time
x, y = [int(nums) for nums in input("Enter two values:").split()] 
print("1st num:", x)
print("2nd num:", y)