## The built-in enumerate() function in Python allows you to loop through an iterable while automatically keeping track of the index (position) of each item.

fruits = ['apple', 'orange', 'mango', 'pineapple']

for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit} juice")
