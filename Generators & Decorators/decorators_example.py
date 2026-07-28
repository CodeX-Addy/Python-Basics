from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before Wrapping..")
        func()
        print("After Wrapping..")
    return wrapper
    
@my_decorator
def greet():
    print("Hey there")
    
greet()
print(greet.__name__) ## wrapper

## To preserver the metadata of the function, we'll use functools wraps
