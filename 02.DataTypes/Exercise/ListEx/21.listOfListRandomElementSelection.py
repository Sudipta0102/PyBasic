import random
from itertools import chain

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = list(chain(list_of_lists))
res1 = list(chain.from_iterable(list_of_lists)) # 3d matrix can be flatten this way too
print(res)
print(res1)

# or it can be flatten this way
res_flatten = [number for row in list_of_lists for number in row]
print(res_flatten)


random_num = random.choice(list(chain.from_iterable(list_of_lists)))
print(random_num)