1. Python文化中的接口和协议
    * 接口是实现特定角色的方法集，而一个类可以实现多个协议（接口），扮演多个角色
    * 协议：非正式的接口
        * 类与协议（隐式 or 假隐式）
            * 迭代协议，序列协议
            * 只需要实现某个方法即可
        * 类与抽象基类（显式）
            * 需要实现抽象方法（抽象基类和golang的interface比较像，不过golang中实现接口是隐式的）
        * 类与父类（显式，严格意义上不应该放这，接口和协议更像一种规范，更上层；类与类之间是同一层次的）
            * 继承父类的方法
            * 重写父类的方法
    * 协议 vs 父类
        * 协议更能体现你能做什么？
        * 父类更加注重代码重用（家产继承）

2. Python喜欢序列
    * 序列协议是Python最基础的协议之一
    * Python哲学：尽量支持基本协议
    * __getitem__
        * 如果没有实现__iter__和__contains__，python会设法调用__getitem__

3. 为什么引入抽象基类？
* 让协议具象化（我怎么证明自己实现了某个协议呢？那协议长什么样子？）

4. 如何继承抽象基类？如何实现某个协议或接口？
* 如果是标准库中的抽象基类，只需要实现对应的方法就行了
* 自定义的抽象基类，必须要显式继承，并且必须实现抽象方法
    * 定义抽象基类的子类，如果没有实现方法会报TyperError
* 怎么就区别对待呢？
    * 标准库中的抽象基类比较少，方法比较固定，所以通过方法就可以找到
    * golang是真隐式实现接口的
    * python还是显式实现接口的
```
class Struggle:
    def __len__(self):
        return 23

from collections import abc
isinstance(Struggle(), abc.Sized)
```

5. 标准库中的抽象基类
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
