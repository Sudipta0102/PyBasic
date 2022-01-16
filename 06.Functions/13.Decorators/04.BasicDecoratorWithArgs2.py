# to get rid of previous error,
def start_end_dec(func):
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print('end')
    return wrapper


@start_end_dec
def print_name(name):
    print(name)


if __name__ == '__main__':
    print_name("printing name")
    help(print_name)
    print(print_name.__name__)

