# yield关键字
# 后面不会通过这种方式实现协程

def func1():
    yield 1
    yield from func2()
    yield 2
    
def func2():
    yield 3
    yield 4
    
f1 = func1() # 生成器
for item in f1:
    print(item)