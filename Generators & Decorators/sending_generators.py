def get_user_order():
    print("What order would you like?")
    order = yield
    while True:
        print(f"Preparing..{order}")
        order = yield

order = get_user_order()
next(order)
order.send("Pizza")
order.send("Cheese Pasta")


"""
What order would you like?
Preparing..Pizza
Preparing..Cheese Pasta
"""
