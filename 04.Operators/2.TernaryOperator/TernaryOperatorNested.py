a, b = 20, 10
# let's do the nested loop in non ternary way
if a!=b:
    if a<b:
        print("a is smaller")
    else:
        print("b is smaller")    
else:
    print("a and are equal")

# let's do it in a ternary way

print("a and b are equal" if a==b else "a is less than b" if a<b else 
"a is greater than b")    