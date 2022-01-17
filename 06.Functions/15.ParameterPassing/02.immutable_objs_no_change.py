def func(x):
    x = 5
    # or, x += 5 whichever...both has no effect because int is immutable.


var = 10
print('var before func(): ', var)
func(var)
print('var after func(): ', var)



