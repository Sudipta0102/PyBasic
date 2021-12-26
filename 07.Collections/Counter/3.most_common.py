from collections import Counter

s = 'aaaaaccaaabbbbbaabbccccc'
counter1 = Counter(s)
print(counter1)

# 1. most_common() -> with no arguments returns the whole counter as a list of tuple
list_of_tuple1 = counter1.most_common()
print(list_of_tuple1)

# 2. most_common(1) -> returns the most occurred elemnent
list_of_tuple2 = counter1.most_common(1)
print(list_of_tuple2)

# 3. most_common(2) -> returns the first two most occurred elemnent
list_of_tuple3 = counter1.most_common(2)
print(list_of_tuple3)

# 4. most_common(5) -> returns the whole counter as a list of tuple if the argument number is greater than
# the number of keys in the Counter.
list_of_tuple4 = counter1.most_common(5)
print(list_of_tuple4)

# one application that comes mind is, fetching the most occurred key out of the counter
list_of_tuple5 = counter1.most_common(1)
print(list_of_tuple5[0][0]) # returns a




