# takewhile(func, iterator) is the exact opposite of dropWhile()
# it prints values till the function returns false for the first time.
import itertools

li = [2, 4, 6, 7, 8, 10, 20]

print(list(itertools.takewhile(lambda x: x%2 ==0, li)))