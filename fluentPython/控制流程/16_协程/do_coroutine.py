from inspect import getgeneratorstate

"""
如何控制函数的执行流程
"""

# 用作协程的生成器的基本行为
def simple_coroutine(): # 返回generator
    print("-> coroutine start")
    x = yield # 接收值，保存至x
    print("-> coroutine received: ", x)

my_coro = simple_coroutine() # GEN_CREATED
print(getgeneratorstate(my_coro))
# 激活协程，也可以使用my_coro.send(None)，如果未激活时，发送非None值，会报错
next(my_coro) # GEN_RUNNING -> GEN_SUSPENDED
print(getgeneratorstate(my_coro))
# my_coro.send(42) # GEN_CLOSED

# 协程的状态
# GEN_CREATED 等待开始执行
# GEN_RUNNING 解释器正在执行
# GEN_SUSPENDED 在yield表达式处暂停
# GEN_CLOSED 执行结束

# 产出两个值的协程
def simple_coro2(a):
    print("-> Startd: a=", a)
    b = yield a # 产出一个值a，接收一个值保存至b
    print("-> Received: b=", b)
    c = yield a + b
    print("-> Received: c=", c)
    
async def func3(): # 返回coroutine
    pass

# 如何激活协程？
def averager():
    total = 0.0
    count = 0 
    average = None 
    while True:
        term = yield average 
        total += term
        count += 1
        average = total/count
        


    
    
    