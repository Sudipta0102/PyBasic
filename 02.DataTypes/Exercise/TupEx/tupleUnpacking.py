def calc1(x):
    #your code goes here
    perimeter = 4*x
    area = x**2
    t = (perimeter, area)
    return t

# in one line
def calc(x):
    return 4*x, x**2
    

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))