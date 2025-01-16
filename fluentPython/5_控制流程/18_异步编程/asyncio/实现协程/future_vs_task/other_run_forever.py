# run_forever 已经不用了

"""
loop.run_until_complete: 因为传进去的future会绑定一个回调函数
loop.run_forever
"""

import asyncio
from asyncio import Future


async def func1():
    await asyncio.sleep(3)
    return "this is func1"

# run_until_complete 实现原理
def callback(f: Future):
    print(f"func1 done: {f.result()}")
    # Return the event loop the Future is bound to
    # Then stop it
    f.get_loop().stop()

# 1. 创建事件循环
loop = asyncio.get_event_loop()
# 2. 创建任务
task = loop.create_task(func1())
task.add_done_callback(callback)
# loop.run_until_complete(task) # 添加任务，事件循环开始执行，直到任务完成
loop.run_forever() # 事件循环开始执行


