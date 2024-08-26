# 将部分参数固定，返回新的函数
from functools import partial
def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1) # a = 1
s2 = partial(spam, c=2)


# 使用场景
# 函数因为一些原因添加了参数，调用函数时可以使用partial