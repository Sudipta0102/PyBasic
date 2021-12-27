def func(x):
    if x < 0:
        raise Exception('x should be positive')
    else:
        return f'{x} is a positive number'


print(func(5))
print(func(-5))

