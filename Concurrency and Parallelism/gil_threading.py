import threading 
import time 

def brew_coffee():
    print(f"{threading.current_thread().name} started brewing..")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing..")


thread1 = threading.Thread(target=brew_coffee, name="First Thread")
thread2 = threading.Thread(target=brew_coffee, name="Second Thread")

start_time = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f}")
