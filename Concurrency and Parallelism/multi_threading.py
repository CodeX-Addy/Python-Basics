import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"Taking order for customer {i}")
        time.sleep(2)
        
def brew_coffee():
    for i in range(1, 4):
        print(f"Brewing coffee for customer {i}")
        time.sleep(3)
        
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_coffee)

order_thread.start()  ## starting the threads
brew_thread.start()

order_thread.join()  ## wait to complete
brew_thread.join()

print("Order is taken for brewing the coffee..")

## in this code, only single core of cpu is engaged 
