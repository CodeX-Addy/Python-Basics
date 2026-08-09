dictionary = {"coffee": "latte", "size": 250}

try:
    print("Checking the coffee size..")
    if(dictionary["size"] > 250):
        raise ValueError("This size is not available")
except ValueError as e:
    print("Error:", e)
else:
    print(f"We're happy to server you {dictionary["size"]} ml coffee..")
    
