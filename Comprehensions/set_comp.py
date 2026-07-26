greet_list = ["Good Morning", "Hello", "Good Evening", "Wish you the best", "Good Morning"]

hello_list = {hello for hello in greet_list if "Good" in hello}

print(hello_list)

## output: {'Good Morning', 'Good Evening'}
