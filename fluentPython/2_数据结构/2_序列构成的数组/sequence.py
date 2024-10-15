"""
序列的分类
容器序列(存放不同类型的数据，存放的是引用)
list、tuple、collections.deque

扁平序列(只能容纳一种类型，存放的是值而不是引用)   扁平序列其实是一段连续的内存空间
str、bytes、bytearray、memoryview、array.array

可变序列（能否被修改）
list、bytearray、array.array、collections.deque、memoryview

不可变序列
tuple、str、bytes

序列的一些相同操作
迭代
切片
    为什么切片和区间会忽略最后一个元素？ 方便快速计算长度 end - start
排序
拼接
"""

"""
list: 列表是一个可变的容器序列
"""
symbols = 'abcdefg'
# 列表推导：用来创建列表
codes_1 = [ord(s) for s in symbols if ord(s) > 127] # python会忽略[],{},()中的换行！！！
# map和filter不好理解
codes_2 = list(filter(lambda c: c > 127, map(ord, symbols)))

# 生成其他类型的序列：生成器表达式
# 迭代器协议，逐个产出元素，而不是先建立一个完整的列表，避免内存占用
# 和列表推导的区别，使用小括号替代中括号
codes_3 = (ord(s) for s in symbols if ord(s) > 127) 
codes_4 = tuple(ord(s) for s in symbols if ord(s) > 127) # 如果生成器表达式是函数唯一参数，不需要再写括号了

# 常用方法
# append, insert, 

"""
tuple: 元组
尽量不要把元组理解为不可变的列表
尽量把元组当成一组记录（和具名元组的关系更加亲密一点）

namedtuple: 具名元组
City = namedtuple("City", "name country population")
1. 类名
2. 属性名
"""
# 元组拆包，可以用在任何可迭代对象上，也被称为可迭代元素拆包
_, x = (1, 2)
y = 1 , 2 # 其实,才是元组不可或缺的，括号并不是
a, b, *rest = (1, 2, 3, 4, 5)



# 对序列使用 + 和 *  --- 不修改原来的对象，而是创建一个新对象

# 序列就地加法
# a += b
# __iadd__()如果未实现，会调用__add__()
# 区别：__iadd__()在a对象基础上进行添加，__add__()创建新对象赋值给a


# 赋值操作（可以修改内容，但不能有赋值操作，所以尽量不要把可变对象放在元组里）
t = (1,2,[3,4])
t[2].append(5) # Yes

# 增量赋值不是一个原子操作，这就是为什么赋值能成功，同时也会报错！！！
t[2] += [6,7] # No
# 将t[2]的值存入TOS(Top Of Stack)
# 计算TOS += [6,7]，因为TOS指向一个可变对象，因此可以完成
# t[2] = TOS，因为s是元组，这一操作会报错

# 排序
# list.sort: 就地排序，python惯例会返回None
# sorted: 新建一个列表作为返回值






### 当列表不是首选
# 数组
# array.array
from array import array
from random import random
IntArray = array('i', (random() for i in range(100)))

# 二进制数据
# bytearry

# 内存视图
# memoryview

# 高阶数组和矩阵
# numpy
# scipy

# 双向队列
# collections.deque
