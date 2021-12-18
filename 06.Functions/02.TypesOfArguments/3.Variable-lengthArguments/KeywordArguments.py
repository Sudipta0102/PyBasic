# any key value datastructure will work here

def func(**kwargs):
    for key, value in kwargs.items():
        print('%s : %s' % (key, value))

func(first='me', mid='then', last='everybody else')        
