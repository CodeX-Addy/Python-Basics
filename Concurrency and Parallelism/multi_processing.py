from multiprocessing import Process
import time

def brew_coffee(name):
    print(f"Started brewing {name} coffee..")
    time.sleep(3)
    print(f"Finishing brewing {name} coffee..")
    
if __name__ == "__main__":
    coffee_makers = [
       Process(target=brew_coffee, args=(f"Coffee maker: {i+1}",))
       for i in range(4) 
    ]
    
    ## starting all process
    for p in coffee_makers:
        p.start()
        
    ## waiting all process
    for p in coffee_makers:
        p.join()
        
    print("All coffee are served!")

## it engage multiple cores of cpu
