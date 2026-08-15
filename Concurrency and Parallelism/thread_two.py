from threading import Thread
import time 

def prepare_coffee(type_, wait_time):
    print(f"{type_} coffee will prepare in {wait_time} seconds..")
    time.sleep(wait_time)
    print(f"{type_} coffee ready to serve!")

t1 = Thread(target=prepare_coffee, args=("Latte", 2))
t2 = Thread(target=prepare_coffee, args=("Capuccino", 3))

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()

print(f"Overall time: {end - start:.2f}")

