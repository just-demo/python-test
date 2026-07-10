from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time


def process_one(label):
    for i in range(3):
        print(f"Sleeping {label} iteration {i + 1}")
        time.sleep(1)
    return f"{label} - ok"


def process_many(labels):
    for label in labels:
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(process_one, label)
            try:
                result = future.result(timeout=2)
                print(result)
            except TimeoutError:
                print(f"Timeout processing {label}")


# This example demonstrates that even after timeout the underlying thread proceed running
process_many(["a", "b", "c"])
