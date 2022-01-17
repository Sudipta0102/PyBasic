# creating a simple generator
def simp_gen():
    x = 1
    yield x
    yield x + 1
    yield x + 2

# creating the generator object
gen_obj = simp_gen()

# iterate 1st time over this object which will print 1 2 3 in this case
for i in gen_obj:
    print(i, end = ' ')

# then iterate over the object the 2nd time and it will not print anything
# because the generator object is already exhausted and has to be 
# re-initialized and that is Generator Exhaustion
for i in gen_obj:
    print(i, end = ' ')

# and also, if you next() on this generator object iterator, then
# StopIteration error is raised because of the same reason.
next(gen_obj)

