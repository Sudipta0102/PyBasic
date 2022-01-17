# saves a lot of memory for large datasets.
import sys


def firstn(n):
    li = []
    num = 0
    while num <= n:
        li.append(num)
        num += 1
    return li


def first_generator(n):
    num = 0
    while num <= n:
        yield num
        num += 1


print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(first_generator(1000000)))

