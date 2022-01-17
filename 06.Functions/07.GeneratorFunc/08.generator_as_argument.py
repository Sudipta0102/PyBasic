def mygen():
    yield 3
    yield 1
    yield 2


g = mygen()

# this in built sum method can take a generator argument.
print(sum(g))


def mygen1():
    yield 3
    yield 1
    yield 2


g1 = mygen1()

# also sorted()
print(sorted(g1))
