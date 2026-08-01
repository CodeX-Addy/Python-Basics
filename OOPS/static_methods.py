## static methods : it doesn't necessarily requires object creation

class CoffeeUtensils:
    @staticmethod
    def all_utensils(utensils):
        return [item.strip() for item in utensils.split(",")]
        
utensils = " kettle,  cup"
print(CoffeeUtensils.all_utensils(utensils))
