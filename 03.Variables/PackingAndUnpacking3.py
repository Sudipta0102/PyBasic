# To change the arg list you need to convert the tuple to a list.
# then you can pack when calling the function

def func1(*args):
     print(args)

def func2(*args):

    #converting the tuple to a list so we can modify
    args = list(args)

    # modifying args list 
    args[0] = "something"
    args[1] = "else"

    func1(*args)     


func2("i", "am", "something")    