import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter 
    for _ in range(10000):
        with lock:  ## it prevents race condition so that no more threads access same variable
            counter += 1

thread = [threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in thread]
[t.join() for t in thread]

print(f"Final counter value: {counter}")
