"""
函数遇到特殊情况时，需要抛出异常，而不是返回None，尽量让调用者去处理异常
"""


# 第一种
def divide1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# 容易写出错误的代码，因为None和0做判断时，都是False
result = divide1(0, 5)
if not result:
    print("Invalid Inputs")

# 第二种 
# 和golang有点像，状态和值作为两个结果返回
def divide2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None
    
# 不过使用者还是可能会写出错误的代码
_, result = divide2(0, 5)
if not result:
    print("Invalid Inputs 2")
    
# 第三种
def divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs 3') from e
    
divide3(1, 0)  

# raise: 抛出新的异常
# raise ... from ...: 抛出新的异常，新的异常是由旧的异常导致
# raise ... from None: 抛出新的异常，不会打印旧的异常（禁止异常关联）