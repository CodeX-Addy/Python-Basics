def print_names():
    yield "name1"
    yield "name2"
    yield "name3"
    
names = print_names()
print(names)
print(next(names))
print(next(names))
print(next(names))

"""
Output:
<generator object print_names at 0x79ed1e403740>
name1
name2
name3

"""
