# 可接受任意数量的位置参数的函数

# 参数传递都是对象的引用传递（python所有变量都是引用，重点要看该数据是否可以修改）

from typing import Tuple
# 函数的参数注解
def avg(first:int, *rest:Tuple[int]) -> int: 
    return (first + sum(rest)) / (1 + len(rest))

# 同时接收任意数量的位置参数和关键字参数
def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict

# 注意：*args只能作为最后一个位置参数出现，**kwargs只能作为最后一个参数出现
# *args和**kwargs中间出现的参数只能是关键字参数 === keyword-only


# 编写只接受关键字参数的函数
def recv(maxsize, *, block):
    pass

# 从函数中返回多个值
# 实际上返回了一个元组，元组是通过逗号组成的，不是圆括号？？？


# 定义带有默认参数的函数
def spam(a, b=42):
    pass

def spam1(a, b=None):
    # 注意：对默认参数的赋值只会在函数定义的时候绑定一次
    # 默认参数赋值绝对不要用引用类型，不然有点闭包的意思，所有调用函数都在用同一份数据
    if b is None:
        b = []

# object类没有任何属性或方法
_no_value = object()
def spam2(a, b=_no_value):
    if b is _no_value:
        pass