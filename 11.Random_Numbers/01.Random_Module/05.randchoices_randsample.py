import random

# both are used to pick defined numbers of random entity from the sequence
# Main diff:
# 1. sample() always picks unique values
# 2. choices() can pick same value more than once.

l1 = list("abcdefgh")

a = random.sample(l1, 3)
print(a)


b = random.choices(l1, k=3)
print(b)

