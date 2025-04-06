'''
Docstrings, short for documentation strings, are vital in conveying the purpose and functionality of python functions, modules, and classes.
'''
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)
