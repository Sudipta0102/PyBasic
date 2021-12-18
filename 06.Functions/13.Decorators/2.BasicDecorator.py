# this is a decorator which calculates the time taken to execute a function
import time
import math
def calculate_time(func):
    def inner(*args, **kwargs):
        # inner(*args, **kwargs) is way of taking any arguments to the used function.
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time taken: ", func.__name__, end-begin)

    return inner

@calculate_time # instead of countFactorial = calculate_time(countFactorial)
def countFactorial(num):
    print(f"The factorial of {num} is:", math.factorial(num))

#countFactorial = calculate_time(countFactorial)

countFactorial(20)