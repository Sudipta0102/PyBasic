# 1. split() method helps in getting multiple inputs from the user.
# 2. it uses one delimiter as an argument
# 3. default constructor of split() takes white space/spaces.
#
# 4  Important Note:  Generally split() functions used in python to 
# split a string, But, one can use this for taking multiple inputs 
# from the user.

# Syntax: input().split(separator, maxsplit)


# 1. default usage of split()

x, y = input("Enter two values:").split()
print("Number of boys:", x)
print("Number of girls", y)
print()

