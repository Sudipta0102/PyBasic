# starmap(func, list[tuple1, tuple2, ....])

import itertools

li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

print(list(itertools.starmap(max, li))) # return max of every tuple

