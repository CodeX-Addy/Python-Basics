class Coffee:
    pass

class CoffeeTime:
    pass

print(type(Coffee))

latte = Coffee()

print(type(latte))
print(type(latte) is Coffee)
print(type(latte) is CoffeeTime)
