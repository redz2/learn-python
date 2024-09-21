# asyncio装饰器
import asyncio

# 我的python解释器不支持@asyncio.coroutine()装饰器了
# @asyncio.coroutine() # 普通函数 -> 协程函数
# def func1():
#     print(1)
#     yield from asyncio.sleep(1) # 遇到IO耗时操作，切换到其他tasks
#     print(2)

# @asyncio.coroutine
# def func2():
#     print(3)
#     yield from asyncio.sleep(1) # 遇到IO耗时操作，切换到其他tasks
#     print(4)
    
async def func1():
    print(1)
    await asyncio.sleep(1)
    print(2)
    
async def func2():
    print(3)
    await asyncio.sleep(1)
    print(4)
    
# 任务列表
tasks = [
    # 添加任务
    # create_task 和 ensure_future的区别？
    # 1. create_task时必须有一个已经存在的事件循环，内部调用loop.create_task()
    # 2. ensure_future时如果没有事件循环，内部会自动新建一个，内部也是调用loop.create_task()
    # 3. create_task可以给任务起名字
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
    # asyncio.create_task(func2()), # creat_task时必须存在一个事件循环，直接添加会报错
]


# 此处才创建event loop，上面无法使用create_task
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))