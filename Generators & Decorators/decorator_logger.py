from functools import wraps

def custom_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Launching func..", func.__name__)
        result = func(*args, **kwargs)
        print("Closing func..", func.__name__)
    return wrapper
    
@custom_logger
def func(type):
    print(f"The func is of this type: {type}")
    
test = func("Logger")

"""
Launching func.. func
The func is of this type: Logger
Closing func.. func
"""
