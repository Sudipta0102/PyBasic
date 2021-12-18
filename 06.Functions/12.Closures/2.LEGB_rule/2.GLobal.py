y = 10
def func():
    x = 4
    global y # To modify a global varible inside a local scope, I need to use local keyword.
    y = y + 1 # 1. Now if we write only this to change the global variable, this won't work.
              # gives an error.    
              # 2. But I write global y before this. Then y variable is recognized now.
              # 3. Important Note: Just to access the varible, I didn't need to do that.  
              # Only if I want to change that, then this statement(global y) needed.
    print("x:", x)
    print("y:", y) # y is global here is this can be accessed from any part of this module.
    print(dir())
func()

print(dir()) # here x doesn't appear, because it's local to the function 