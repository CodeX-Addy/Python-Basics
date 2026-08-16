import requests
from threading import Thread
import time

def fetch_images(url):
    print(f"Web requests starts for {url}")
    resp = requests.get(url)
    print("Finished..and size is", len(resp.content))

urls = ["https://httpbin.org/image/svg", "https://httpbin.org/image/png", 
"https://httpbin.org/image/jpeg"]

thread = []

start = time.time()

for url in urls:
    t1 = Thread(target=fetch_images, args=(url,))
    t1.start()
    thread.append(t1)

for i in thread:
    i.join()

end = time.time()

print(f"All requests are successful!, Time:{end - start:.2f}")
