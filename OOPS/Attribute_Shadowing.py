class Coffee:
    temperature = "hot"
    cup_size = "medium"
    
latte = Coffee()
latte.temperature = "mild"
print(f"Attribute temp: {latte.temperature}")
print(f"Class temp: {Coffee.temperature}")

del latte.temperature
print(f"Attribute temp: {latte.temperature}") ## it will fallback to class default
