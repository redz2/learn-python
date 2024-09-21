# 类元编程
* 如何在运行时创建类？

1. 类工厂函数
* 类工厂函数 ---> 类 ---> 对象
* collections.namedtuple

```
type(my_object) # 当成函数使用，等价于 
type(name, bases, dict) # 构造新类

```