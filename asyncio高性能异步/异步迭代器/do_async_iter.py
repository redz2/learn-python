import asyncio

# 与普通迭代器相比，异步迭代器的特点是它们的__anext__()方法必须返回一个awaitable对象，这样在每次迭代时，程序可以异步等待数据的到来，而不会阻塞主线程。
# 这种机制使得异步迭代器非常适合处理大量数据或需要等待外部资源的情况，尤其是在有阻塞行为的数据获取场景中，使用异步迭代器可以提高效率。

class MyRange:
    def __init__(self, total=0):
        self.total = total
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.total:
            # 这和同步有啥区别呢？
            await asyncio.sleep(3)
            x = self.count
            self.count += 1
            return x
        else:
            raise StopAsyncIteration

async def func1(msg):
    await asyncio.sleep(5)
    print(msg)

async def main():
    # 与普通迭代器相比，异步迭代器的特点是它们的__anext__()方法必须返回一个awaitable对象，这样在每次迭代时，程序可以异步等待数据的到来，而不会阻塞主线程。
    # 这种机制使得异步迭代器非常适合处理大量数据或需要等待外部资源的情况，尤其是在有阻塞行为的数据获取场景中，使用异步迭代器可以提高效率。
    task1 = asyncio.create_task(func1("task1"))
    task2 = asyncio.create_task(func1("task2"))
    task3 = asyncio.create_task(func1("task3"))
    async for i in MyRange(10):
        print(i)

asyncio.run(main())