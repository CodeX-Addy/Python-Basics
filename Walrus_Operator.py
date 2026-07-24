## example 1

if remainder := 12 % 3:
    print(f"Remainder {remainder} is non zero, so it's not completely divisible")
else:
    print(f"Remainder zero, so it is completely divisible")

## example 2

allowed_values = ["a", "b", "c"]

if (value := input("Enter your value: ")) in allowed_values:
    print(f"This {value} is present inside allowed values")
else:
    print(f"Sorry, this {value} is not present inside the allowed values")
