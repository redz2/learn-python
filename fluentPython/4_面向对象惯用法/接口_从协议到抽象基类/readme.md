1. Python文化中的接口和协议
    * 接口是实现特定角色的方法集
    * 一个会实现多个接口，扮演多个角色（迭代协议，序列协议）

2. Python喜欢序列
    * 序列协议是Python最基础的协议之一
    * Python哲学：尽量支持基本协议
    * __getitem__
        * 如果没有实现__iter__和__contains__，python会设法调用__getitem__

3. 为什么引入抽象基类？

4. 如何继承抽象基类？
* 只需要实现方法就行
```
class Struggle:
    def __len__(self): return 23

from collections import abc
isinstance(Struggle(), abc.Sized)
```

5. 定义抽象基类的子类
* 如果没有实现方法会报TyperError

6. 标准库中的抽象基类
* collections.abc
    * Iterable
        * Iterator
    * Container
        * Sequence
            * MutableSequence
        * Mapping
            * MutableMapping
        * Set
            * MutableSet
    * Sized

* numbers
    1. Number
    2. Complex
    3. Real
    4. Rational
    5. Integral

