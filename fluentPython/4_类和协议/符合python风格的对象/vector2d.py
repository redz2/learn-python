import math

class Vector2D:

    # 使用__slots__类属性节约内存，一般不需要使用
    # __slots__ = ('__x', '__y')

    # 1. 创建一个对象
    # 2. self指向对象
    # 3. 调用构造函数进行初始化
    # 4. 返回对象
    def __init__(self, x, y):
        # 名称改写：__x ==> _Vector2D__x
        # 属性是”私有的“，并且是”不可变的“
        # 默认情况下，python在__dict__存储实例属性，创建大量实例时会比较浪费内存
        self.__x = float(x)
        self.__y = float(y)

    # 把读值方法标记为特性: getter方法
    @property
    def x(self):
        return __x

    @property
    def y(self):
        return __y

    # 实例方法
    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r},{!r})".format(class_name, *self)

    def __str__(self):
        # 必须返回字符串
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    # 可散列的Vector2D
    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)

    def do_something(self):
        return

if __name__ == '__main__':
    v1 = Vector2D(3,4)
    v2 = Vector2D(6,8)
    # 解构赋值和可迭代之间有啥关系
    print(id(v1.do_something) == id(v2.do_something))
    print(id(v1._Vector2D__x) == id(v2._Vector2D__x))
