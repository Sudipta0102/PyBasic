# try:
#     # Some Code....
#
# except:
#     # optional block
#     # Handling of exception (if required)
#
# else:
#     # execute if no exception
#
# finally:
#     # Some code .....(always executed)


def func(x):
    try:
        r = 5 // x
    except ZeroDivisionError:
        print("x can't be zero")
    else:
        print(r)
    finally:
        print('I am here finally')


func(1)
func(0)

