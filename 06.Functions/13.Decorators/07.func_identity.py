import functools

# 1. The problem statement:
# -> the function identity is in danger!!!!!
# 2. How do you figure???
# -> print_name.__name__ -> gives the inner function of decorator i.e. wrapper() here
# but supposed to give print_name()...
# 3. HOw to fix?
# -> functools.wraps decorator


def start_end_dec(func):

    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print('end')
    return wrapper


def start_end_dec1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return wrapper


@start_end_dec
def print_name(name):
    print(name)


@start_end_dec1
def print_name1(name):
    print(name)


if __name__ == '__main__':
    # case 1:
    help(print_name)
    print(print_name.__name__)

    print('-'*30)
    # case 2:
    help(print_name1)
    print(print_name1.__name__)