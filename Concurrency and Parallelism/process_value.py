## with Value we can create shared memory space among processes

from multiprocessing import Process, Value

def increment(counter):
    for i in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter,)) for 
    _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final value", counter.value)
