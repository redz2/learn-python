# yield关键字
# 我们不会通过这种方式实现协程

def func1():
    yield 1
    # await告诉python自己应该等待，并让出执行权，具体执行哪个函数，事件循环自己去找
    # yield from告诉python该去执行哪个函数，我tm直接调用函数不行吗？可能不同之处在于后面跟了个生成器
    yield from func2()
    yield 2
    
def func2():
    yield 3
    yield 4
    
f1 = func1() # 生成器
for item in f1:
    print(item)