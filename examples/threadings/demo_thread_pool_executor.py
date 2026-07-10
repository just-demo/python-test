from concurrent.futures import ThreadPoolExecutor
import time


def worker(i):
    print(f"Worker {i} started")
    time.sleep(1)
    print(f"Worker {i} finished")


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(worker, i) for i in range(10)]
    for future in futures:
        future.result()
