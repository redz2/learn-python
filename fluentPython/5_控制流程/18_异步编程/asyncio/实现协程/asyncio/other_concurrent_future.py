from concurrent.futures import Future

# 使用线程池实现异步操作时用到的对象

import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

def func(value):
    time.sleep(1)
    print(value)
    return "ok"

# 1. 创建线程池
pool = ThreadPoolExecutor(max_workers=5)
# 2. 提交任务给线程池
for i in range(10):
    fut = pool.submit(func, i)
    print(fut)
    # <Future at 0x100fc6780 state=running>
    # <Future at 0x100fc69f0 state=pending>
    
def func2():
    time.sleep(5)
    print("sb")
    
import asyncio

# 如果第三方模块不支持协程（不能通过asyncio.create_task创建任务），就使用线程池来处理
async def main():
    # 1. 获取事件循环
    loop = asyncio.get_running_loop()
    
    # 2. 使用run_in_executor将同步函数构建成异步task
    # 内部调用ThreadPoolExecutor的submit方法去线程池申请一个线程去执行func2，返回concurrent.futures.Future对象
    # 调用asyncio.wrap_future将concurrent.futures.Future对象包装程asyncio.Future对象（await只支持这个Future对象）
    
    # 3. 我们自己包装了一个asyncio.Future对象，通过线程池添加了一个任务，可以认为和create_task没啥区别？
    fut = loop.run_in_executor(None, func2) # 协程通过create_task向队列中添加任务
    # 事件循环通过await关键字识别出耗时操作，尽可能快的完成非耗时操作
    # 多线程则通过IO阻塞来判断是否需要切换线程（避免IO阻塞浪费CPU）
    
    # 总结: 更像是事件循环处理不了耗时同步操作，就把这部分操作丢给线程去处理
    result = await fut
    print("default thread pool", result)

# async关键字将普通函数包装成一个协程函数
# await关键字标记耗时任务
# 事件循环处理任务列表中的所有任务，并且执行到await时会自动切换任务，防止事件循环被阻塞

# 如果一个耗时操作没有await，事件循环就会被卡住
asyncio.run(main())