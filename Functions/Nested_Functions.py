def print_something():
    char = "a"
    def print_another():
        char = "b"
        print(f"Printing Inner: {char}")
    print_another()
    print(f"Printing Outer: {char}")

char = "c"
print_something()
print(f"Global: {char}")
