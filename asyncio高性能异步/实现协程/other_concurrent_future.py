from concurrent.futures import Future

# 使用线程池或线程池实现异步操作时用到的对象

import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

# 1. 创建线程池
# 2. 提交任务给线程池
def func(value):
    time.sleep(1)
    print(value)
    return "ok"
    
pool = ThreadPoolExecutor(max_workers=5)

for i in range(10):
    fut = pool.submit(func, i)
    print(fut)
    # <Future at 0x100fc6780 state=running>
    # <Future at 0x100fc69f0 state=pending>
    

def func2():
    time.sleep(5)
    print("sb")
    
import asyncio

# 如果第三方模块不支持协程，就使用线程池来处理
async def main():
    loop = asyncio.get_running_loop()
    # 1. 内部调用ThreadPoolExecutor的submit方法去线程池申请一个线程去执行func2，返回concurrent.futures.Future对象
    # 2. 调用asyncio.wrap_future将concurrent.futures.Future对象包装程asyncio.Future对象
    # await不支持concurrent.futures.Future对象
    fut = loop.run_in_executor(None, func2)
    result = await fut
    print("default thread pool", result)
    
asyncio.run(main())