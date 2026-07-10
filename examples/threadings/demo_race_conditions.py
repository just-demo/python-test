import threading
import time

counter = 0


def worker():
    global counter
    for _ in range(1000):
        c = counter
        time.sleep(0.001)
        counter = c + 1


threads = [threading.Thread(target=worker) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

# prints 1000 instead of 4000
print(counter)
