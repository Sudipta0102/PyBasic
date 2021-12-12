import itertools

li = [2, 4, 5, 7, 8, 10, 20, 2, 4, 6, 90]

# isslice() takes 4 arguments
# 1. container
# 2. start
# 3. stop
# 4. step


print(list(itertools.islice(li, 2, 9, 2)))