import asyncio

semaphore = asyncio.Semaphore(3)


async def worker(i):
    async with semaphore:
        print(f"Worker {i} started")
        await asyncio.sleep(1)
        print(f"Worker {i} finished")


async def main():
    await asyncio.gather(*(worker(i) for i in range(10)))


asyncio.run(main())
