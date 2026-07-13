from multiprocessing import Pool
import os


def square(x):
    print(f"Worker process ID: {os.getpid()}")
    return x * x


if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)
