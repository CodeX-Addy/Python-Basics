class CoffeeOrder:
    def __init__(self, coffee_type, sweetness, size):
        self.coffee_type = coffee_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod
    def from_dict(cls, order_dict):
        return cls(
            order_dict["coffee_type"],
            order_dict["sweetness"],
            order_dict["size"]
        )
        
    @classmethod
    def from_string(cls, order_string):
        coffee_type, sweetness, size = order_string.split("-")
        return cls(coffee_type, sweetness, size)
        
order1 = CoffeeOrder.from_dict({"coffee_type": "latte", "sweetness": "low", "size": 200})

order2 = CoffeeOrder.from_string("Latte-Low-Large")

print(order1.__dict__)
print(order2.__dict__)
