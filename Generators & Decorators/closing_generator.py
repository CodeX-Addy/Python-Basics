def order1():
    yield "Tea"
    yield "Coffee"
    
def order2():
    yield "Matcha"
    yield "Chilled Coke"
    
def final_menu():
    yield from order1()
    yield from order2()
    
for i in final_menu():
    print(i)
    
def close_generator():
    try:
        while True:
            order = yield "Waiting for ur order.."
    except:
        print("Restaurant is closed..")
        
order = close_generator()
print(next(order))
order.close() ## memory cleanup

"""
Tea
Coffee
Matcha
Chilled Coke
Waiting for ur order..
Restaurant is closed..
"""
