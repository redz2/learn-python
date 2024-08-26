import asyncio

# 示例一
async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务（future对象），任务什么都不干
    fut = loop.create_future()
    # 等待任务最终结果（future对象），没有结果会一直等下去
    await fut
    
# asyncio.run(main())
    
# 示例二
# task对象的本质
async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")
    
async def main_2():
    
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 没有绑定任何行为，这个任务永远不知道什么时候结束
    fut = loop.create_future()
    # 创建一个任务，2s后给fut赋值，让future返回值
    # task执行完成后会自动赋值，让task变成完成状态（我们一般只会用task，不会使用future）
    await loop.create_task(set_after(fut))
    data = await fut
    print(data)
    
asyncio.run(main_2())

