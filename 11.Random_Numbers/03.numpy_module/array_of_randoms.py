import numpy

# 1. array of float randoms
# 2. arg 3 denotes dimesion of array, this produces a 1 d array of 3 random floats.
a = numpy.random.rand(3)
print(a)

print('-'*30)
# takes variable number of args and returns variable dimensions of arrays with random values. OMG!!!
b = numpy.random.rand(2, 2, 2, 2, 2, 2, 2)
print(b)

print('-'*30)

# takes one argument, return an array with
c = numpy.random.random(4)
print(c)


for i in c:
    print(i)


print('-'*30)
# now, int arrays, randint(upper, lower, size)
d = numpy.random.randint(5, 15, 6)
print(d)
# this number of digit of size is really dimension. So, it creates a 1d of size 3 for above spec.
# I can this for 2D array:
print('-'*30)
e = numpy.random.randint(5, 15, (2, 2))
print(e)

print('-'*30)
# also, like shuffle method is here too.
numpy.random.shuffle(d)
print(d)