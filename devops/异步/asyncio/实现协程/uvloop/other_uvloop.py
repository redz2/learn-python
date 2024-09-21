import asyncio
import uvloop

# 如何使用uvloop？
# 1. 安装
# pip3 install uvloop

# 2. 设置事件循环
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# uvloop是什么？
# uvloop是asyncio事件循环的替代方案

# uvloop为什么快？
# uvloop基于libuv，这是一个使用C语言实现的高性能异步IO库，用来代替python的asyncio默认事件循环
