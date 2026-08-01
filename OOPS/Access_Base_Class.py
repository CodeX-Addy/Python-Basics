## accessing base class

class BaseCoffee:
    def __init__(self, sugar, coco_powder):
        self.sugar = sugar
        self.coco_powder = coco_powder
        
class Coffee(BaseCoffee):
    def __init__(self, sugar, coco_powder, ishot):
        BaseCoffee.__init__(self, sugar, coco_powder)
        self.ishot = ishot
    
    def return_coffee(self):
        print(f"This coffee has {self.sugar} sugar level with {self.coco_powder} coco powder and it is {self.ishot}")
        

class AnotherCoffee(BaseCoffee):
    def __init__(self, sugar, coco_powder, ishot):
        super().__init__(sugar, coco_powder)
        self.ishot = ishot
    
    def return_coffee(self):
        print(f"This coffee has {self.sugar} sugar level with {self.coco_powder} coco powder and it is {self.ishot}")
        

coffee = Coffee("high", "mild", "hot")
coffee.return_coffee()

another_coffee = AnotherCoffee("low", "high", "cold")
another_coffee.return_coffee()
