# taking two inputs at a time and also using format()
x, y = [int(y) for y in input("Enter two values:").split()]
print("1st num: {} \n2nd num: {}".format(x, y))
