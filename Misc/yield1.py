def simple_generator():
    x=1
    yield x
    yield x+1
    yield x+2

generator_object = simple_generator()

#next(generator_object)
#i=1
for i in range(3):
    for i in generator_object:
        print(i)

