# async & await关键字

# 以协程方式实现的异步编程
import asyncio
# 判断一个函数是否是协程函数: asyncio.iscoroutinefunction(do_some_work)
# 判断一个对象是否是协程对象: asyncio.iscoroutine(do_some_work())

# 协程函数 返回 协程对象
async def func1(): # 最大的特点是会“谦让”
    print("3. Start func1")
    await asyncio.sleep(5) # 让出执行，等待IO
    print("6. Created task in func1")
    # 任务可以在任何时候添加
    task4 = asyncio.create_task(asyncio.sleep(2))
    task5 = asyncio.create_task(func3())
    task5.add_done_callback(callback_func3)
    await task4
    print("8. task4 finished")
    await task5
    print("10. task5 finished")
    print("11. Finish func1")
    # 可以有返回值
    
async def func2():
    print("2. Start func2")
    await asyncio.sleep(3)
    print("5. Finish func2")
    
async def func3():
    print("7. Start func3")
    await asyncio.sleep(3)
    print("9. Finish func3")
    return "hello world"

# 在任务执行完毕的时候可以获取任务的结果，然后进行处理
# 回调函数最后一个参数一定是Future对象
from asyncio import Future
def callback_func3(future: Future):
    print("  * callbakc_func3 can get func3 reuslt: ", future.result())
    
    
# 如果任务队列中只有一个task，没法并发
# 对于任务对垒中包含多个task的，只要有IO阻塞，协程会互相谦让，实现并发执行（不要阻塞在IO操作上）
async def simple():
    # 错误使用await造成代码同步执行
    await asyncio.sleep(5) # 目前只是在傻傻地等 await coro
    await asyncio.sleep(5) # 依然还是在傻傻地等 await coro

async def main():
    """
    main()就是任务队列中的task0

    """
    
    # 1. 为什么不这么写？因为还是同步执行
    # await func1()
    # await func2()

    # 2. 如何创建一个任务队列？
    # asyncio.gather（一次性创建tasks，返回Future对象）
    # await asyncio.gather(func1(), func2(), func3())

    # 3. 如何添加任务？并发关键，任务队列中一定要有多个任务（否则谈p的并发）
    # 目前队列中只有一个任务task0，需要添加其他task到任务队列中
    print("1. begin")
    task2 = asyncio.create_task(func2()) # 返回一个task对象
    task1 = asyncio.create_task(func1()) # 添加task的顺序和执行顺序没啥关系
    task3 = asyncio.create_task(asyncio.sleep(10))
    
    # create_task的实现
    # loop = asyncio.get_event_loop()
    # loop.create_task()
    
    # 4. 构造一种场景，task还未执行完成，main()继续往下执行了
        # 1. 当前协程放弃执行（task0），等待asyncio.sleep(1)执行完成
        # 2. 事件循环在队列中寻找其他可执行的任务（task1，task2）并开始执行
        # 3. 执行task1，task2时，遇到await时，也会放弃执行
        # 4. 事件循环发现asyncio.sleep(1)执行完成，会继续执行task0
        # 5. 这样会导致task1和task2执行不完
        # 6. 所以我补了await task1，await task2，await task3，告诉main()，需要等他两执行完
    await asyncio.sleep(1) # 依然在等待，不过不傻了，会找其他可以执行的任务
    print("4. asyncio sleep done")
    await task1 # 一定要等待所有的task执行完成，task0才能继续执行
    print("12. task1 done")
    await task2
    print("13. task2 done") # 其实早执行完成了，await task1卡着了
    await task3 # 和task1，task2差不多时间开始执行，早就执行完了
    # 所有任务都执行完成，事件循环终止
    
    # 5. task列表，必须放在main主线程中，不然会报错
    # task_list = [
    #     "task1",
    #     "task2",
    # ]
    # done, pending = await asyncio.wait(task_list, timeout=None)
    # done 是个集合，是任务的返回值
    
    # asyncio.wait vs asyncio.gather（看上去差不多，都是创建一个任务队列，一个传入列表，一个传入task）
    # await asyncio.wait(tasks)
    # await asyncio.gather(task1, task2, task3)
    # 如果传入的是写成对象，会自动包装成task
    


if __name__ == "__main__":
    
    # 协程 vs 多线程
    # 多线程，某个线程等待IO时，其他线程会执行（线程切换有开销，内核态切换）
    # 协程，某个协程等待IO时，其他协程会执行（用户态切换）
    
    # 单个任务
    # 1. 创建并得到一个事件循环
    # loop = asyncio.get_event_loop()
            # asyncio.get_event_loop: 创建event loop，若已经存在，返回当前event loop
            # asyncio.get_running_loop: 返回当前event loop，若未创建抛出异常
    # 2. 何时结束事件循环
    # 传进去的future对象结束后自动终止事件循环（内部调用run_forever，）
    # 自动把协程对象包装成future对象 
    # loop.run_until_complete(func1()) # ---> loop.run_until_complete(asyncio.ensure_future(func1()))
    
    # 等价于上面两行代码
    # asyncio.run(func1())
    
    # 单个任务 vs 多个任务
    # loop.run_until_complete(func1()) # 只执行一个协程函数
    # loop.run_until_complete(asyncio.gather(*tasks))
    # loop.run_until_complete(asyncio.wait(tasks))
    
    
    # 多个任务
    # 1. 一个主协程对象
    coro = main() 
    # 2. 创建并得到一个事件循环，并且传入主协程对象
    # 主协程对象包含任务队列
    asyncio.run(coro)