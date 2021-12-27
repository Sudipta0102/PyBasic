# The code enters the else block only if the try clause does not raise an exception.

# try:
#     # Some Code....
#
# except:
#     # optional block
#     # Handling of exception (if required)
#
# else:
#     # execute if no exception


def func(a, b):
    try:
        c = (a + b)/(a - b)
    except ZeroDivisionError:
        print('(a-b) yields to be zero, thereby causing zero division error')
    else:
        print(c)


func(3, 3)