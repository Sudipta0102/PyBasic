def func(x, y):
    try:
        z = x//y
    except ZeroDivisionError as z:
        print(z)
    else:
        return z


print(func(4, 2))
print(func(0, 4))
print(func(4, 0))

#
# def func1(x, y):
#     try:
#         return x//y
#     except Exception as e:
#         print(e)
#
#
# print(func1(4, 0))