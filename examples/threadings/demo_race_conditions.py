import threading
import time

N_THREADS = 2
N_INCREMENTS_PER_THREAD = 1000

counter = 0


def increment():
    global counter
    for _ in range(N_INCREMENTS_PER_THREAD):
        c = counter
        time.sleep(0)  # yield execution
        counter = c + 1


threads = [threading.Thread(target=increment) for _ in range(N_THREADS)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Expected:", N_THREADS * N_INCREMENTS_PER_THREAD)
print("Actual:  ", counter)
