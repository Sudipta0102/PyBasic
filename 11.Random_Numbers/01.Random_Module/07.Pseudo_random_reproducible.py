# These are all Pseudo random number because they are reproducible time and time again.
import random

# 1st set of random nums
random.seed(1)
a = random.randint(1, 10)
print(a)

# 2nd set of random ints
random.seed(1)
b = random.randint(1, 10)
print(b)

# observe, same numbers are being generated when seed is set to 1 for both the sets.
# so, that means, the random number generated at the first go can be generated at the second go too
# and as a matter of fact, the same number can be generated at any time I want.
# and if that is so, then random is not so random... is it?!!! :P



