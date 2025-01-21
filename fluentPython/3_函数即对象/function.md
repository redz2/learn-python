# 函数
1. 所有函数都是是 __一等对象__（为什么说函数是对象？函数是function类的实例，使用type验证）
    * 运行时创建
    * 能赋值给变量
    * 能作为参数传给函数
    * 能作为函数的返回值
    ```py
    # 高阶函数: 接受函数为参数，或者把函数作为结果返回(map、filter、reduce)
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    sorted(fruits, key=len)

    # 装饰器

    # 匿名函数: sorted(fruits,key=lambda x: x[::-1])
    # 除了作为参数传给高阶函数，python 中很少使用 lambda
    # 补充: js 中的箭头函数 ()=>{}

    # 为什么列表推导可以取代map？
    a = list(map(factorial, range(20)))
    b = [factorial(n) for n in range(20)]

    # 归约函数(最后返回一个值): sum、reduce
    all(iterable) # 元素都为True，返回True，否则False
    any(iterable) # 元素中有True，返回True，否则False
    ```

2. 什么是可调用对象？如何判断对象是否可以调用？callable(obj)
    * 用户定义的函数: def lambda
    * 内置函数: len
    * 内置方法: dict.get
    * 方法
    * 类: Person()
    * 类的实例(如果类中定义了__call__方法): person()
        * python 函数是对象，任何对象也可以表现得像函数
    * 生成器函数

3. 编写函数时，输入输出尽量明确，条件判断放到主流程中（函数要求: 专注于一个功能）

4. 函数参数（golang中只有位置参数，不支持关键字参数）
    * 位置参数: name（位置参数最多两个，不要太多，args只能作为最后一个位置参数出现，类型保持一致）
        * 如果位置参数很多，可以考虑传入一个字典，在函数内进行解析
    * 关键字参数: cls（keyword-only）
    ```py
    def tag(name, *content, cls=None, **attrs):
        ...
    # block只接受关键字参数
    def recv(maxsize, *, block):
        pass

    # 返回多个数据: 实际上是返回一个元组

    # 定义带有默认参数的函数（那b是位置参数还是关键字参数呢？其实都可以）
    # 默认参数千万不要是引用类型，容易出问题
    def spam(a, b=42):
        pass
    ```

5. 注解中可用的类型: 注解不会做任何处理，只是存储在函数的__annotations__属性中，网络框架可以根据注解执行类型检查
    * Any
    * 简单类型: int、float、str、bytes
    * Optional、Uniion
    * typing.List、typing.Set
    ```py
    from typing import Tuple
    def avg(first:int, *rest:Tuple[int]) -> int: 
        return (first + sum(rest)) / (1 + len(rest))
    ```

6. 装饰器: 一种特殊的高阶函数，参数是一个函数，并且只返回一个函数
    * 闭包: 能访问主体之外的非全局变量
    * 因为保持了输入输出一致(都是函数)，因为可以叠放装饰器
    * 参数化装饰器: 通过 __装饰器工厂函数__，生成一个装饰器函数
```py
# 使用装饰器
@decorator
def target():
    ...

target = decorator(target)

# 实现一个装饰器
def decorator(func):
    @functools.wraps(func) # 添加被装饰函数的__name__和__doc__属性
    def wrapp(*args, **kwargs):
        # do something
        return func(*args, **kwargs)
    return wrap
```

7. 回调函数: callback
    * 同步: 让干什么就去干什么，喊一声就去干了
    * 异步: 让干什么就去本子上记一下，人看见了就去干
    * 两个概念
        1. 面向事件的GUI
        2. 基于回调处理异步IO

8. 策略模式:
    * 抽象基类和具体实现
    * 使用函数实现策略模式: 添加一个可选的参数，用于传入一个实现具体算法的函数（程序 = 数据 + 逻辑，如何包裹这两种概念？）
