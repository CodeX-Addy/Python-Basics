from multiprocessing import Process
import time

def crunch_number():
    print("Starting the process..")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Ending the process..")

if __name__ == "__main__":
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()

    print(f"It takes total time {end_time - start_time:.2f}")
