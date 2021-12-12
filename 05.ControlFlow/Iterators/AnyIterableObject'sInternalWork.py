# Iterable objects are: List, Set, Dictionary, Tuple, String
# Integer, Float etc are not iterable object.

# For loops can iterate ant iterable object.
# but there is like a whole other thing is happening internally.

# let's say we hab=ve this list iterable.
fruits = ['apple', 'Lemon', 'Appple']

# What happens:
# 1. Make the list an iterable object with the help of iter() function
iterObj = iter(fruits)

# 2. Run an infinite while loop and break only when StopIteration is raised.
while True:
    #3. In try block we getch the next element with the help of next() function
    try:
        fruit = next(iterObj)
        # 4. After fetching the element, oerforming the required operation
        print(fruit)
    except StopIteration:
        break


# Under the hood, we are calling iter() and next() method.
