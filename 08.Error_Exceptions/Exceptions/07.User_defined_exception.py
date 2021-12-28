class ObesityError(Exception):
    def __init__(self, val):
        self.val = val


def func(x):
    try:
        if x > 5:
            # raise ObesityError('Too much food makes you lazy and fat')
            raise (ObesityError('Too much food makes you lazy and fat'))
    except ObesityError as o:
        print(o)
    else:
        print(f'{x} meals a day makes you nice and healthy')
    finally:
        print("MorbidThoughts Pvt. ltd.")


def func1(x):
    try:
        if x < 6:
            print(f'{x} meals a day makes you nice and healthy')
        else:
            raise ObesityError(x)
    except ObesityError as o:
        print(f'Too much food makes you lazy and fat.\nHave less than {o} meals a day')


if __name__ == '__main__':
    func(5)


