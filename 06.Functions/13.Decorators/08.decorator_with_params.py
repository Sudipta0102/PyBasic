# let's say, one decoter that helps you repeat your func n times.
import functools


def repeat(n):

    def outside_wrapper(func):

        @functools.wraps(func)
        def insisde_wrapper(*args, **kwargs):
            for _ in range(n):
               result = func(*args, **kwargs)
            #print(type(result))
            return result
        return insisde_wrapper
    return outside_wrapper


@repeat(n=3)
def print_name(name):
    print(f"Name is : {name}")


if __name__=='__main__':
    print_name('PseudoFunc')

# What does for _ in range mean?
# When you are not interested in some values returned by a function we use
# underscore in place of variable name . Basically it means you are not
# interested in how many times the loop is run till now just that it should run
# some specific number of times overall.