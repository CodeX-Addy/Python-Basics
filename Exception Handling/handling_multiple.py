## handling multiple exceptions

def print_order(item, quantity):
    try:
        price = {"latte": 70}[item]
        cost = price * quantity
        print(f"Your total cost is: {cost}")
    except KeyError:
        print("This type of coffee doesn't exist in our menu..")
    except TypeError:
        print("Integer value is required..")
        
print_order("mocha", 20)
