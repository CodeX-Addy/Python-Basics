class Coffeecup:
    cup_size = 150
    
    def describe(self):
        return f"Size is: {self.cup_size}"
        
cup_one = Coffeecup()
print(f"The cup size is: {cup_one.describe()}") ## it will converts it into Coffeecup.describe(cup_one)
print(f"The cup size is: {Coffeecup.describe()}") ## #Error: No instance is provided, so the required 'self' argument is missing.
