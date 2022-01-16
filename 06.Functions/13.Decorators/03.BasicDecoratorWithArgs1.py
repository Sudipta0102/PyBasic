# here the error is
# TypeError: start_end_dec.<locals>.wrapper() takes 0 positional arguments but 1 was given
# that means, if your function has n args, then your wrapper also demands n args.
def start_end_dec(func):
    def wrapper():
        print('start')

        print('end')
    return wrapper


@start_end_dec
def print_name(name):
    print(name)


print_name('printing name')





