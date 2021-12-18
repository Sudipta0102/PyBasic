import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func): 
    # takes one function as an argument
    def log_func(*args):
        logging.info(f"Running {func.__name__} with argument {args}")
        print(func(*args))

    return log_func # returning the object, not the function itself

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
add_sub = logger(sub)

add_logger(3, 4)
add_sub(4,3)
