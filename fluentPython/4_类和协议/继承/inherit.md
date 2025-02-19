# 继承

1. super(): super(type, object_or_type)
   - type: 从哪里开始搜索所需方法的父类，默认为 super()调用所在方法的类
   - object_or_type: 接收方法调用的对象，默认为 self

```python
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x) # 等价于 super(B, self).__init__(x) -> 在B的父类A中找一个方法，绑定到self上，并调用方法
        self.y = y
```

2. 子类化内置实例

   - 不要直接子类化内置类型，比如 list, dict, str
   - 使用 UserList, UserDict, UserString

```python
# 错误的做法
class MyList(list):
    pass

# 正确的做法
from collections import UserList
class MyList(UserList):
    pass
```

3. 多重继承和方法解析顺序
   - 深度优先还是广度优先？
