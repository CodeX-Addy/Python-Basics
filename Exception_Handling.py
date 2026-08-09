dictionary = {"coffee": "latte", "size": 250}

try:
    print("Checking the coffee size..")
    if(dictionary["size"] > 250):
        raise ValueError("This size is not available")
except ValueError as e:
    print("Error:", e)
else:
    print(f"We're happy to server you {dictionary["size"]} ml coffee..")
    
    
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

## creating our own exceptions (by inheriting Exception class)

class OutofCoffeeError(Exception):
    pass

def serve_coffee(type_):
    if type_ not in ["latte", "mocha"]:
        raise OutofCoffeeError("This coffee does not exist in our menu..")
    print(f"Serving {type_} coffee to you..")
    
serve_coffee("Capaccino")
 
