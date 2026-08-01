class BaseCoffee:
    def __init__(self, type_):
        self.type = type_
        
    def prepare(self):
        print(f"Preparing {self.type} coffee..")
        
class NewCoffee(BaseCoffee): ## inheritance
    def prepare_again(self):
        print("Preparing again...")
        
class Coffee:
    base_coffee_cls = BaseCoffee  ## composition
    
    def __init__(self):
        self.coffee = self.base_coffee_cls("Regular")
        
    def print_coffee(self):
        print(f"This is our coffee: {self.coffee.type}")
        
coffee = Coffee()
coffee.print_coffee()
