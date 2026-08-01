class Coffee:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
        
    def order(self):
        return f"Ordering..{self.type} {self.size}ml cofee.."
        
order1 = Coffee("Latte", 200)
print(order1.order())

order2 = Coffee("Mocha", 300)
print(order2.order())

"""
Ordering..Latte 200ml cofee..
Ordering..Mocha 300ml cofee..
"""
