# 容器序列(存放的是包含的任意类型的对象的引用)
# list
# tuple
# collections.deque

# 扁平序列(存放的是值而不是引用)
# str
# bytes
# bytearray
# memoryview
# array.array

# 相同操作
# 迭代
# 切片
# 排序
# 拼接


# list
# 列表是一个可变序列
# 列表推导: 创建一个新的列表
# symbols = 'abcdefg'
# codes = [ord(symbol) for symbol in symbols]

# 生成器表达式
# 迭代器协议，逐个产出元素，而不是先建立一个完整的列表，避免内存占用
# 和列表推导的区别，使用小括号替代中括号
# 如果生成器表达式是函数唯一参数，不需要再写括号了

# tuple
# 尽量不要把元组理解为不可变的列表
# 尽量把元组当成一组记录（和具名元组的关系更加亲密一点）
# 元组拆包，可以用在任何可迭代对象上，也被称为可迭代元素拆包
_, x = (1, 2)
x, y, *rest = (1, 2, 3, 4, 5)


### 赋值
"""
1. 不要把可变对象放在元组里
2. 增量赋值不是一个原子操作，这就是为什么赋值能成功，同时也会报错
"""
t = (1,2,[3,4])
# 可以修改内容，但不能有赋值操作
t[2].append(5)

# 将s[a]的值存入TOS
# 计算TOS += b，因为TOS指向一个可变对象，因此可以完成
# s[a] = TOS，因为s是元组，这一操作会报错
t[2] += [6,7]

### 排序
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
