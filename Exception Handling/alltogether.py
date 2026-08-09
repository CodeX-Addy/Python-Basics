class InvalidCoffee(Exception): pass

def total_bill(flavor, cups):
    menu = {"latte": 50, "mocha": 60}
    try:
        if flavor not in menu:
            raise InvalidCoffee("This coffee is not available in our cafe..")
        if not isinstance(cups, int):
            raise TypeError("Please provide cups in numbers..")
        total = menu[flavor] * cups
        print(f"Your total bill is: {total}")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        print("Thank you for visiting our cafe..")
        
total_bill("latte", "two")
total_bill("cappuccino", 2)
total_bill("mocha", 4)
