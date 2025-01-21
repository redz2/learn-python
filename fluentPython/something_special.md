1. 如何使用doctest来测试代码？
    * doctest在docstring中寻找测试用例的时候，认为>>>是一个测试用例的开始，直到遇到空行或者下一个>>>
    * 在两个测试用例之间有其他内容的话，会被doctest忽略（可以利用这个特性为测试用例编写一些注释）
```python
def average (values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len (values)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # automatically validate the embedded tests
```

2. overload是什么？
    * @overload是Python中的一个函数装饰器，它允许我们为同一个函数定义多个不同的签名
    * 在python中，overload并不是真的重载，只是为一个函数提供多个类型标注，用于提高代码的可读性
```python
from typing import overload

@overload
def add(a: str, b: str) -> str:
    ...

@overload
def add(a: int, b: int) -> int:
    ...
    
def add(a, b):
    return a + b
    
if __name__ == "__main__":
    print(add(1,2))
```

3. pass vs ...
```python
"""
... 和 pass 不会执行任何操作，通常情况下，...可以取代pass
... 在@overload中经常使用
"""
@overload
def add(a: int, b: int) -> int:
    ...
```


