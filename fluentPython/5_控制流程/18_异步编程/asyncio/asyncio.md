# 协程
1. 协程是什么？
    * 协程不是计算机提供的，是程序员人为创造，也被称为微线程，是一种用户态上下文切换技术。
2. 如何实现协程？
    * greenlet，早期模块
    * yield关键字
    * asyncio装饰器（py3.4）
    * async、await关键字（py3.5）目前最主流！！！
3. 协程的意义
    * 在一个线程中如果遇到IO等待时间，线程不会傻傻等，会利用空闲时间再去干点别的事情
    * [一文搞懂python async/await异步编程](https://zhuanlan.zhihu.com/p/698683843)
    * [python进阶asyncio](https://www.kancloud.cn/xiaoran/python_asyncio/3043126)
4. 我对于协程的理解
    * 单线程，事件循环
    * await显式标记耗时操作
    * 深入理解协程的代码执行过程

# asyncio
1. 事件循环: 单线程、死循环
    * 事件循环的创建、获取、设置
        * asyncio.get_runing_loop()
            * 创建event loop，若已经存在，返回当前event loop
        * asyncio.get_event_loop()
            * 返回当前event loop，若未创建抛出异常
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
    * 等 awaitable 对象返回
    * 如果有IO阻塞，事件循环会从任务队列中找其他可以执行的任务

3. Task对象
    * 白话: 帮助你在事件循环中添加多个任务
    * asyncio.create_task(协程对象) 
        * 尽量使用协程对象创建一个任务添加到事件循环中
        * 其他创建任务的方式（更底层，不建议手动实例化Task对象）
            * loop.create_task()
            * ensure_future()

4. Future对象（更底层，一般不会直接用，是task的基类/父类）
    * _state （如何判断协程是否可以继续执行？）
    * 当future对象设置返回值时，await结束等待，代码继续执行
        * Task会自动执行set_result，实现自动结束

5. concurrent.futures.Future
    * 线程池和进程池的Future对象
        * -> 可以包装成asyncio的Future对象

# 场景
1. 顺序执行同步任务: 阻塞主线程
2. 顺序执行异步任务: 
3. 并发执行异步任务: asyncio.gather
4. 并发执行非异步任务: asyncio.run_in_executor