import asyncio
import time

"""
执行IO耗时操作时自动切换
"""

# 一个函数由async def定义，就是一个coroutine，内部可以使用await
async def hello_world(): # 返回一个coroutine对象
    """coroutine"""
    # await awaitable 如果不使用task或future，而是使用coroutine，依旧是顺序执行的
    await asyncio.sleep(1) # 目前当成一个黑盒来看待
    print("hello world")
    print(time.ctime(time.time()))
    task1 = asyncio.create_task(asyncio.sleep(3))
    task2 = asyncio.create_task(asyncio.sleep(3))
    await task1
    await task2
    print(time.ctime(time.time()))
    print("hello world again")
    
async def main():
    # 哪些任务是并发执行的
    print("start gather")
    # run a collection of awaitables
    # get a future that represents multiple awaitables
    # 一旦创建了Futures对象，就会在事件循环中自动调度，等这些任务执行完成
    await asyncio.gather(hello_world(), hello_world(), hello_world())
    # Tasks是Futures的一个子类
    print("wait task1 done")
    await asyncio.create_task(hello_world())
    # 创建了2个任务
    print("create task")
    task2 = asyncio.create_task(hello_world())
    task3 = asyncio.create_task(hello_world())
    print("task created")
    # 中断task0的执行，开始执行task2，执行到内部的await，eventloop寻找下一个可执行的task3
    # 当task2执行完成后才会往下执行
    await task2
    print("task2 done")
    time.sleep(3)
    # 执行到这里时，task3早执行完了，实际上不需要等待
    await task3
    # await: 中断主线程，等待当前任务执行完成
    
    


# coro_hello_word = hello_world()
# asyncio.run(coro_hello_word)

# 返回一个coroutine对象
coro = main()
# python会将coroutine对象包装程一个task0
# 
asyncio.run(coro)



# 什么是可暂停等待的对象？awaitable
# coroutine对象（调用coroutine函数返回），await coroutine对象直接执行对应的coroutine函数，直到返回
# task
# future


async def sleep(delay, result=None):
    """Coroutine that completes after a given time (in seconds)."""
    if delay <= 0:
        await __sleep0()
        return result

    loop = events.get_running_loop()
    future = loop.create_future()
    h = loop.call_later(delay,
                        futures._set_result_unless_cancelled,
                        future, result)
    try:
        return await future
    finally:
        h.cancel()