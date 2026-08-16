from multiprocessing import Process, Queue

def queue_working(queue):
    queue.put("This is a test..")

queue = Queue()
p = Process(target=queue_working, args=(queue,))
p.start()
p.join()

print(queue.get())
