## Zip in python is used to iterate multiple iterables parallely

fruits = ['apple', 'orange', 'mango', 'pineapple']
price = [20, 30, 40, 50]

for price, fruit in zip(price, fruits):
    print(f"The price of {fruit} juice is: {price}")
