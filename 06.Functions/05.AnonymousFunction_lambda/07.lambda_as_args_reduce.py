from functools import reduce # because python 3

l1 = [1, 2, 3, 4]

# lets say, you want to get the product of every element.
product_li = reduce(lambda x, y: x*y, l1)
print(product_li)
# it's like it will 'reduce' to the value you want according to your func logic.

# also, here i think lambda has to take 2 mandatory args.




