# 1.Because, functions are objects here, we can pass them as arguments to other 
# functions.
# 2. Functions that can accept other fnctions as arguments are called 
# hogher-order functions.

def shout(text):
    return text.upper()

def whiper(text):
    return text.lower()

def greeting(func):
    greeting = func('hi')    
    print (greeting)

greeting(shout)
greeting(whiper)    