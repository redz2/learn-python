from typing import overload

"""@overload是Python中的一个函数装饰器，它允许我们为同一个函数定义多个不同的签名

overload并不是真的重载，只是为一个函数提供多个类型标注，用于提高代码的可读性

... 和 pass 不会执行任何操作，通常情况下，...可以取代pass
"""
@overload
def add(a: str, b: str) -> str:
    ...

@overload
def add(a: int, b: int) -> int:
    ...
    
def add(a, b):
    return a + b

def xxx(a, b):
    ...
    
if __name__ == "__main__":
    print(add(1,2))
    xxx(1,2)