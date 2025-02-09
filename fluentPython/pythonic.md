# pythonic

1. 确认自己所用的 python 版本

```python
import sys
print(sys.version)
print(sys.version_info)
```

2. 遵循 PEP8 风格指南

```python
import this
"""
1. 标准库模块
2. 第三方库模块
3. 自定义模块

PEP8:
1. 使用空格来表示缩进
2. 和语法相关的每一层都缩进4个空格
3. 每一行的字符数不超过79个
4. 占据多行的长表达式，除了首行，其他要再缩进4个空格
5. 函数和类应该2个空行隔开
6. 同一个类中，方法用一个空行隔开
7. 变量赋值时，赋值符号左右各加一个空格
8. 函数、变量、属性使用小写字母来拼写
"""
# 模块级别常量
MODULE_VAR = 0

# 类名使用大驼峰命名法
class Test():

    def __init__(self):
        self._leading_underscore = 1 # 受保护的实例属性
        self.__double_underscore = 2 # 私有的实例属性

    def do(self):
        a = 1
        b = 2
        if a is not b:
            print("a is not b")
        if not a:
            print("默认会把非空的值判断为True")

    @classmethod
    def cls_do(cls):
        pass

# 异常类名使用大驼峰命名法
class MyException(Exception):
    pass
```

3. 了解 bytes、str 与 unicode 的区别

```python
# bytes: 字节序列
# str: 字符串，包含Unicode字符的序列

a = b'hello'
b = '你好'

b.encode('utf-8') # 编码成bytes
a.decode('utf-8') # 解码成str

# 在内存中，一直是Unicode字符序列，但在磁盘、网络、数据库等存储介质中，必须要把Unicode字符序列编码成字节序列才能保存。
```
