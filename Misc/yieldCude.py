def cube_generator():
    x=1
    while True:
        yield x*x*x
        x=x+1

for num in cube_generator():
    if num>1000:
        break
    print(num)

      
