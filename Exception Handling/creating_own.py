## creating our own exceptions (by inheriting Exception class)

class OutofCoffeeError(Exception):
    pass

def serve_coffee(type_):
    if type_ not in ["latte", "mocha"]:
        raise OutofCoffeeError("This coffee does not exist in our menu..")
    print(f"Serving {type_} coffee to you..")
    
serve_coffee("Capaccino")
