from threading import Thread
import time 

def boil_milk():
    print("Boiling milk starts..")
    time.sleep(2)
    print("Boiling milk finished..")

def toast_bun():
    print("Toasting bun starts..")
    time.sleep(3)
    print("Toasting bun finished..")

start = time.time()

t1 = Thread(target=boil_milk)
t2 = Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time taken to complete is: {end - start:.2f} seconds")
