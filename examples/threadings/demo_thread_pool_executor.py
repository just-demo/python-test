from concurrent.futures import ThreadPoolExecutor
import time


def worker(i):
    print(f"Worker {i} started")
    time.sleep(1)
    print(f"Worker {i} finished")

print("Example 1")
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(worker, i) for i in range(10)]
    for future in futures:
        future.result()

print("Example 2")
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(worker, range(10))
