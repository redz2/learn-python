# 多继承
# super()找到自己的父类（更准确的说法：根据mro找到自己的第一个父类 ）

# 感觉super()的机制和回调函数差不多，python解释器会自动寻找下一个执行代码，一个链式调用的结构


class GrandFather():
    
    def __init__(self):
        print("GrandFather")
    
class Father1(GrandFather):
    
    def __init__(self):
        # <super: <class 'Father1'>, <Child1 object>>
        super().__init__()
        print("Father1")

class Father2(GrandFather):
    
    def __init__(self):
        # <super: <class 'Father2'>, <Child1 object>>
        # Child1的MRO中找到Father2的后面一个
        super().__init__()
        print("Father2")
        
        
class Child1(Father1, Father2):
    def __init__(self):
        # <super: <class 'Child1'>, <Child1 object>>
        super().__init__()
        print("Child1")

# MRO是什么？
# 此案例中一直用的Child1的MRO，能找到后面的节点，归功于super(cls, obj)
print(Child1.__mro__)
# (<class '__main__.Child1'>, <class '__main__.Father1'>, <class '__main__.Father2'>, <class '__main__.GrandFather'>, <class 'object'>)
print(Father1.__mro__)
# (<class '__main__.Father1'>, <class '__main__.GrandFather'>, <class 'object'>)

# super()的作用是什么？
# super(cls, obj) 其中cls是MRO中的类，obj是MRO中类的对象
# super() -> super(cls, self) -> <super: <class 'Child1'>, <Child1 object>>
a = Child1()

# 为什么是深度优先，先进后出？GrandFather -> Father2 -> Father1
# Child1 -> super().__init__
#           Father1.__init__ -> super().__init__()
#                               Father2.__init__() -> super().__init__()
#                                                     GrandFather.__init__()

# 如果Father1中没有写super().__init__()呢？执行到Father1，代码机就返回了，不会继续向下执行
# Father1
# Child1

# 如果Father2中没有写super().__init__()呢？
# Father2
# Father1
# Child1


