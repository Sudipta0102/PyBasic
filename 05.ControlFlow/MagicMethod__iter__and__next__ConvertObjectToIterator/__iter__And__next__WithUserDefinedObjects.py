class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start

if __name__ == '__main__':
    a, b = 1, 5
    c1 = Counter(a, b)   
    #c2 = Counter(a, b)

    for i in c1:
        print(i, end = ' ')
