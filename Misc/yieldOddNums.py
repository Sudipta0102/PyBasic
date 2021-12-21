def odd_generator(n):
    for i in range(n):
        yield i


for num in odd_generator(10):
    if num%2 != 0:
        print(num)

