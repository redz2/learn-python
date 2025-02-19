"""
多重继承

self是什么？类实例化后的对象
self调用父类中的方法？方法本质上就是函数调用，只不过第一个参数是self
"""
class A:
    def ping(self):
        print('A ping', self)

class B(A):
    def pong(self):
        print('B pong', self)

class C(A):
    def pong(self):
        print('C PONG', self)

class D(B,C):
    def ping(self):
        # 调用A的ping方法
        A.ping(self)
        # 调用A的ping方法
        super().ping()
        print("D ping", self)

    def pingpong(self):
        # 实例方法
        self.ping()
        # 调用父类的ping方法
        super().ping()
        # 在class中使用super()，python黑魔法做了两件事情，等价于 super(D, self).ping()
        # 1. 找到自己属于哪个class，作为自己的第一个参数
        # 2. 找到自己属于哪个函数，并把函数的第一个参数，作为自己的第二个参数

        # super()的用法
        # 1. 获取self对象所属class的mro列表
        # 2. 获取class D在mro中的位置
        # 3. 从class D的后面一个开始找，哪个class中有ping这个方法
        # 4. 把ping这个方法bind到self上
        # 5. 等价于 A.ping(self)

        # pong方法继承自B，调用B的pong方法
        self.pong()
        # 使用父类中的pong方法
        super().pong()
        # 直接使用类方法
        C.pong(self)

if __name__ == "__main__":
    print(D.__mro__)
    d = D()
    d.pingpong()
        
