"""减少函数参数
1. 固定部分参数，返回新的函数
2. 使用场景：某些参数固定，不需要反复传入
"""

from functools import partial
def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1) # a = 1
s2 = partial(spam, c=2)

s2(a=1,b=1,d=1)