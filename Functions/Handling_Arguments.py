## handling arguments

def print_char(a, b, c):
    print(f"{a}, {b}, {c}")

print_char("a", "b", "c") ## positional arguments
print_char(a="a", c="c", b="b") ## keyword arguments

def print_something(*args, **kwargs):
    print(f"Char1: {args}")
    print(f"Char2: {kwargs}")
    
print_something("a", "b", c="c", d="d")

## * -> means arguments (args)
## ** -> means keyword arguments (kwargs)
