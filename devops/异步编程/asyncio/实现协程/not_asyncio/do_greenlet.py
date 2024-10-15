from greenlet import greenlet

# 手动切换执行步骤

def func1():
    print(1)     # 2. 打印1
    gr2.switch() # 3. 切换到func2
    print(2)     # 5. 打印3
    gr2.switch() # 6. 切换到func2

def func2():
    print(3)     # 4. 打印2
    gr1.switch()
    print(4)     # 7. 打印4

gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch() # 1. 执行func1


# 为什么函数之间要进行切换？
