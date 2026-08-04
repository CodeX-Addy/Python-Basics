class CoffeeTime:
    
    def __init__(self, time):
        self._time = time ## here _time means something special
        
    @property
    def time(self):
        return self._time + 2
        
    @time.setter
    def time(self, time):
        if 1 <= time <= 5:
            self._time = time
        else:
            raise ValueError("Time must be between 1 and 5")
    
obj = CoffeeTime(6)
print(obj.time)  ## gives 4

obj.time = 6
print(obj.time) ## value error
