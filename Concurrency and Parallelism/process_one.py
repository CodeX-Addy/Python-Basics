from multiprocessing import Process
import time

def crunch_numbers():
    print("Crunching numbers starts..")
    count = 0
    for i in range(10**7):
        count += i
    print("Finishes..")

if __name__ == "__main__":
    start = time.time()
    
    processes = [Process(target=crunch_numbers) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Total time taken: {time.time() - start:.2f}")
