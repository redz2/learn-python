# asyncio
1. asyncio事件循环（单线程）
    * 可以理解为一个死循环，去检测并执行某些代码
    * 事件循环的创建、获取、设置
        * asyncio.get_runing_loop()
        * asyncio.get_event_loop()
        * asyncio.set_event_loop()
        * asyncio.new_event_loop()
    * 事件循环的停止
        * loop.run_util_complete(future)
        * loop.run_forever()
        * loop.stop()
        * loop.is_running()
        * loop.is_closed()
        * loop.close()
    * 创建Future和Task
        * loop.create_future()
        * loop.create_task(coroutine)
```
伪代码

tasks = [task1, task2, task3]

while True:
    可执行任务列表, 已完成任务列表 = 去任务列表中检查所有任务，将可执行和已完成的任务返回

    for 就绪任务 in 可执行任务列表:
        执行已就绪的任务

    for 已完成任务 in 已完成任务列:
        在任务列表中移除已完成任务
    
    如果任务列表中的任务都已经完成，终止循环
```

2. await awaitable（coroutine，task，future）

    * 等待IO任务执行完成
    * 如果事件循环任务队列中有其他任务，可以先执行其他任务

3. task

    * 白话: 帮助你在事件循环中添加多个任务的
    * asyncio.create_task(协程对象)
        * loop.create_task()
        * ensure_future()
        * 不建议手动实例化Task对象

4. Future对象（更底层，一般不会直接用，task的基类）

    * 
    * _state （如何判断协程是否可以继续执行？）
    * 当future对象设置返回值，才能结束等待
    * task自动执行set_result，实现自动结束

5. concurrent.futures.Future

    * 线程池和进程池的Future对象

6. 异步和非异步模块（requests）