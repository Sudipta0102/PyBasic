class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"{self.calls} times called")
        return self.func(*args, **kwargs)


@CountCalls
def print_hello():
    print('hello')


if __name__ == '__main__':
    print_hello()
    print_hello()
    print_hello()
    print_hello()
    print_hello()

