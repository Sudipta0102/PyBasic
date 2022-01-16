import functools


def start_end_dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper


def repeat(n):
    def out_wrap(func):
        @functools.wraps(func)
        def in_wrap(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return in_wrap
    return out_wrap


@start_end_dec
@repeat(n=6)
def print_name(name):
    print(f'name is : {name}')


if __name__ == '__main__':
    print_name("PseudoFunc")
