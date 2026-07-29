class Coffee:
    coffee_type = "latte"  ## properties
    
print(type(Coffee))

Coffee.is_hot = True
print(Coffee.is_hot)

## now let's create an object and this object properties will be isolated to other objects and class

coffee = Coffee()
coffee.is_hot = False
coffee.add_flavor = "Yes"

print(Coffee.is_hot) ## true
print(coffee.is_hot) ## false
print(coffee.add_flavor)  ## Yes
## print(Coffee.add_flavor)  -> error
