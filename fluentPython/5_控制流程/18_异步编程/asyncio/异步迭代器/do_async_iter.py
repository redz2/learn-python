import asyncio
import time
"""
1. 与普通迭代器相比，异步迭代器的特点是它们的__anext__()方法必须返回一个awaitable对象，这样在每次迭代时，程序可以异步等待数据的到来，而不会阻塞主线程。
2. 这种机制使得异步迭代器非常适合处理大量数据或需要等待外部资源的情况，尤其是在有阻塞行为的数据获取场景中，使用异步迭代器可以提高效率。
"""

class MyRange:
    def __init__(self, total=0):
        self.total = total
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.total:
            await asyncio.sleep(1)
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration
        
class MyRange2(MyRange):
    # 目前还没理解async for的价值和意义
    async def __anext__(self):
        if self.count < self.total:
            # task = asyncio.create_task(print_msg(f"{self.count}"))
            print(f"now handle something wasting time")
            await asyncio.sleep(1)
            print(f"now handle data got")
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration
            

async def print_msg(msg):
    await asyncio.sleep(5)
    print(f"now running print_msg: {msg}")

async def main():
    # task1 = asyncio.create_task(func1("task1"))
    # task2 = asyncio.create_task(func1("task2"))
    # task3 = asyncio.create_task(func1("task3"))
    
    # 如果单纯地使用for，并不会产生task的切换
    # async for i in MyRange(3):
    #     print(i)
    
    # 不会创建任务，而是顺序执行异步任务，目前我认为的好处就是还能执行任务队列中的其他任务
    # 每次迭代时，类似于书写await代码，能够确保其他的task能够顺利执行
    async for j in MyRange2(10):
        print(j)

asyncio.run(main())