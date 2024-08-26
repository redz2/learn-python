# async & await关键字

# 以协程方式实现的异步编程
import asyncio
# 判断一个函数是否是协程函数
# asyncio.iscoroutinefunction(do_some_work)
# 判断一个对象是否是协程对象
# asyncio.iscoroutine(do_some_work())

# 协程函数 返回 协程对象
async def func1(): # 最大的特点是会”谦让“
    print("3. Start func1")
    await asyncio.sleep(5) # 一个协程可以放弃执行，把机会让给其他协程
    print("6. Created task in func1")
    # 一定要搞清楚事件循环是什么时候创建的？
    # 任务可以在任何时候添加
    task4 = asyncio.create_task(asyncio.sleep(2))
    task5 = asyncio.create_task(func3())
    task5.add_done_callback(callback_func3)
    await task4 # 遇到IO自动切换
    print("8. task4 finished")
    await task5 # 等 可以等待的对象
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
    
    
# 对于每个协程来说，依旧是串行执行
# 对于多个协程来说，只要有IO阻塞，互相谦让，实现多个协程并发执行（让大家都阻塞在IO操作，而不是其他代码）
async def simple():
    # 错误使用await造成代码同步执行
    await asyncio.sleep(5) # 目前只是在傻傻地等 await coro
    await asyncio.sleep(5) # 依然还是在傻傻地等 await coro

async def main():
    
    # 为什么不这么写？因为还是同步执行
    # await func1()
    # await func2()

    # 和使用create_task没啥区别，一次性创建task，并且等待task执行
    # 返回一个Future对象
    # await asyncio.gather(func1(), func2(), func3())
    
    # 目前队列中只有task0，添加其他task到事件循环队列中（并发关键）
    print("1. begin")
    task2 = asyncio.create_task(func2()) # 返回一个task对象
    task1 = asyncio.create_task(func1()) 
    task3 = asyncio.create_task(asyncio.sleep(10))
    # 构造一种场景，task还未执行完成，main()继续往下执行了
    # 1. 当前协程放弃执行（task0），等待asyncio.sleep(1)执行完成
    # 2. 事件循环在队列中寻找其他可执行的任务（task1，task2）并开始执行
    # 3. 执行task1，task2时，遇到await时，也会放弃执行（如果仅仅是等待耗时IO操作，await就没什么卵用，还是串行执行）
    # 4. 事件循环发现asyncio.sleep(1)执行完成，会继续执行task0
    # 5. 这样会导致task1和task2执行不完
    # 6. 所以我补了await task1，告诉main()，需要等他两执行完
    await asyncio.sleep(1) # 依然在等待，不过不傻了，会找其他可以执行的任务
    print("4. asyncio sleep done")
    await task1 # 尽量要等待所有的task执行完成，task0才能继续执行
    print("12. task1 done")
    await task2
    print("13. task2 done") # 其实早执行完成了，await task1卡着了
    await task3 # 和task1，task2差不多时间开始执行，早就执行完了
    # 所有任务都执行完成，事件循环终止
    
    # task列表，必须放在main主线程中，不然会报错
    # task_list = [
    #     "task1",
    #     "task2",
    # ]
    # done, pending = await asyncio.wait(task_list, timeout=None)
    # done是个集合，任务的返回值
    
# 多线程，某个线程等待IO时，其他线程会执行（线程切换有开销）
# 协程，某个协程等到IO时，其他协程会执行（用户态）

if __name__ == "__main__":
    # 单个任务
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(func1) # 传进去的future结束后自动终止事件循环（内部调用run_forever）
    # asyncio.run(func1()) # 等价于上面两行代码
    
    # 事件循环一定会包含一个任务队列，如果任务队列中没有任务，那就只能傻傻地等
    # 单个任务task0中包含其他task1，task2
    coro = main()
    asyncio.run(coro)
    



# 如何运行协程？
# 启动事件循环
# 事件循环找队列中可以执行的任务
# 任务遇到IO阻塞，让出执行
# 事件循环找队列中可以执行的任务
# 任务遇到IO阻塞，让出执行
# ...
# 一个主task0，创建一堆任务 or 主进程直接创建一堆任务