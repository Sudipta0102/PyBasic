import random

# Main diff is:
# 1. randint includes the upper limit and
# 2. randrange doesn't

# it can generate 10
a = random.randint(1, 10)
print(a)

# with this it won't...this also takes an optional arg -> step
b = random.randrange(1, 10)
print(b)


