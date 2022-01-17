def cube_Generator(x = 0):
    while True:  # so this is an infinite loop
        x = x + 1
        yield x*x*x

for i in cube_Generator():
    if i>1000: # we are setting the limit here, that way it's way more dynamic
        break
    print(i, end=' ')
print()


