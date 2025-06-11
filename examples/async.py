import asyncio
import time


async def test(value):
    await asyncio.sleep(1)
    return value


async def test_multiple():
    return await asyncio.gather(test("a"), test("b"), test("c"))


start = time.time()
print(asyncio.run(test("abc")))
print(time.time() - start)
print(asyncio.run(test_multiple()))
print(time.time() - start)
