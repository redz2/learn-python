# 如何使用特殊方法？

1. 特殊方法是 python 解释器调用的，不需要自己调用

   - 调用 len(myobject) -> myobject.**len**()
   - 内置类型 CPthon 还会抄近路，效率更高

2. 很多时候特殊方法调用是隐式的

   - for i in x -> iter(x) -> x.**iter**()

3. 千万不要自己添加特殊方法

4. 有哪些特殊方法？magic method、dunder method

```
__init__:构造函数,用于初始化对象的属性。
__str__:返回对象的字符串表示形式,用于打印对象时显示。
__repr__:返回对象的官方字符串表示形式,通常包含对象的关键信息。
__eq__:比较两个对象是否相等。
__lt__:比较两个对象的大小关系,实现小于比较。
__le__:比较两个对象的大小关系,实现小于等于比较。
__gt__:比较两个对象的大小关系,实现大于比较。
__ge__:比较两个对象的大小关系,实现大于等于比较。
__iter__:将对象转换为迭代器,实现for循环遍历。
__next__:返回迭代器的下一个值。
__getitem__:实现对象的下标访问,如obj[key]。
__setitem__:实现对象的下标赋值,如obj[key] = value。
__delitem__:实现对象的下标删除,如del obj[key]。
__len__:返回对象的长度,如len(obj)。
__contains__:实现对象的成员检查,如key in obj。
__add__:实现对象的加法操作,如obj1 + obj2。
__sub__:实现对象的减法操作,如obj1 - obj2。
__mul__:实现对象的乘法操作,如obj1 * obj2。
__truediv__:实现对象的除法操作,如obj1 / obj2。
__floordiv__:实现对象的整除操作,如obj1 // obj2。
__mod__:实现对象的取模操作,如obj1 % obj2。
__pow__:实现对象的幂运算操作,如obj1 ** obj2
```

5. 一摞纸牌

```py
import collections

# 具名元组
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # 可迭代，切片
    # 如果未实现__contains__方法，默认会做一次顺序扫描
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
import random

# 随机抽取一张牌
card = random.choice(deck)
Card("Q", "hearts") in deck
# 洗牌，FrenchDeck需要实现__setitem__方法
# random.shuffle(deck)
```

6. Vector

```python
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # repr()能把一个对象用字符串的形式表达出来，尽可能表达出对象是如何创建的
    # 如果只实现其中一个，那么实现__repr__是更好的选择（当需要调用__str__却找不到时，解释器会去调用__repr__）
    def __repr__(self):
        # !r 是一个格式化修饰符，表示调用 repr() 函数来获取 self.x 的“官方”字符串表示形式
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # 如果不实现，默认总是返回 True
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
```
