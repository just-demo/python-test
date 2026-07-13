from multiprocessing import Process
import os

abc = {}

def worker():
    abc["worker"] = 1
    print(f"Worker process ID: {os.getpid()}")


if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")
    p = Process(target=worker)
    p.start()
    p.join()
    print(abc)
