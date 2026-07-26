greet_list = ["Good Morning", "Hello", "Good Evening", "Wish you the best", "Good Morning"]

hello_list = {hello for hello in greet_list if "Good" in hello}

print(hello_list)

## output: {'Good Morning', 'Good Evening'}

## example use case

example = {
    "A": ["a", "b", "c", "a"],
    "B": ["a", "b", "c", "c"],
    "C": ["a", "b", "c", "b"],
}

unique_alphabets = { unique for alpha in example.values() for unique in alpha}

print(unique_alphabets)
