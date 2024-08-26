from math import hypot

class Vector():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # 字符串表现形式
    def __repr__(self):
        # return "Vector(%r,%r) % (self.x, self.y)"
        return f"Vector({self.x},{self.y})"
    
    # def __str__(self):
    #     return repr(self)
    
    # 默认情况下，我们自己定义的类总是被认为是True，除非自己实现了判断逻辑
    def __bool__(self):
        # return hypot(self.x, self.y)
        return bool(self.x or self.y)
    
    # 中缀运算符的原则：不改变操作对象，而是产出一个新的对象
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
        
# 字符串表现形式: 
# __repr__
# repr()能把一个对象用字符串的形式表达出来
# <__main__.Vector object at 0x102ca7140> ---> Vector(2,3) ---> 尽可能表达出对象是如何创建的

# __str__
# 如果指向实现其中一个，那么实现__repr__是更好的选择（当需要调用__str__却找不到时，解释器会去调用__repr__）
# 何时调用？
# 1. print(obj)
# 2. str(obj)

if __name__ == "__main__":
    
    v = Vector(2,3)
    # 两种格式化字符串的方式
    # %
    # str.format
    f1 = "模运算符: %s" % v # python程序员更喜欢用这个 f1和f2会隐式调用__reper__()
    f2 = f"f-string: {v}" # 我更喜欢这么写
    # f3 = "str.format: {v:s}".format(v=v)
    print(f1)
    print(f2)
    # print(f3)

    print(v) # __str__ ---> __repr__