# type(元类) --- object(父类)
# MyType(自定义元类) --- Child(自定义类)

# 自定义元类
class MyType(type):
    
    _n = 0
    _m = 0
    
    # 通过MyType元类定义其他类时执行，比如定义Child类
    def __new__(cls, *args, **kwargs):
        """
        创建空类
        cls -> class '__main__.MyType'
        *args: 继承的父类
        **kwargs: class中定义的类属性以及所有方法
        """
        cls._n += 1
        # __mro__: (<class '__main__.MyType'>, <class 'type'>, <class 'object'>)
        # object.__new__(MyType) is not safe, use type.__new__()
        # 这不是个实例方法啊！！！
        # super() 找到父类节点，并且找到方法，如果方法是实例方法，会默认传入self
        # 如果是个类方法 type.__new__()
        return super().__new__(cls, *args, **kwargs)
    
    # 定义类时执行
    def __init__(self, *args, **kwargs):
        """
        初始化空类
        self: 就是__new__创建的空类 -> <class '__main__.Far'>
        *args: 继承的父类
        **kwargs: class中定义的类属性以及所有方法
        """
        print(f"class name is {self}")
        # 默认参数: <super: <class 'MyType'>, <MyType object>>
        # 找父类中的__init__()，其实就是object or MyObject
        # 使用super()调用父类的实例方法，会自动把self传进去！！！
        super().__init__(*args, **kwargs)
    
    # 类初始化实例会调用元类的 __call__()
    def __call__(self, *args, **kwargs): # 特殊一点会找父类相关的元类
        """
        self: <class '__main__.Far'>
        """
        # 创建空对象
        empty_obj = self.__new__(self, *args, **kwargs) # 调用类方法 -> cls.__new__(cls) -> obj.__new__(cls)
        # 初始化对象
        print(f"instance is {empty_obj}")
        self.__init__(empty_obj, *args, **kwargs) # 调用实例方法 -> cls.__init__(self)
        type(self)._m += 1
        # 返回对象
        return empty_obj
    
    @classmethod
    @property
    def n(cls):
        return cls._n
    
    @classmethod
    @property
    def m(cls):
        return cls._m
    
print(f"define classes\n===============")

# 自定义类
"""
定义类时:
如果定义了metaclass，那么该类就是由metaclass定义的类MyType创建的
如果继承的父类中，父类定义了metaclass，那么自己也是由MyType创建的

定义类时:
因为类是MyType创建的，会执行MyType的__new__()
"""
class MyClass(object, metaclass=type):
    pass


class MyObject(object):
    
    def __new__(cls, *args, **kwargs):
        """
        cls: <class '__main__.Child'>
        """
        print("MyObject __new__")
        # super(当前类, self)
        print(cls.__mro__)
        return super().__new__(cls, *args, **kwargs)

# 定义class
# 创建一个对象（class），初始化对象（instance） ---> 执行以及Far的__init__()
class Far(object, metaclass=MyType):
    
    # 初始化实例时，父类中的__call__()不会执行
    def __call__(cls):
        print("Far __call__")

class Child(MyObject, metaclass=MyType):
    
    child_var = "test"
    
    def __init__(self):
        # <super: <class 'Child'>, <Child object>>
        print("Child __init__")
        
    def __call__(self):
        print("Child __call__")
    
    @classmethod
    def my_func(cls):
        pass


# 类的实例化 ---> 会调用元类__call__() 为什么不会调用父类的__call__()?
# 创建一个对象（instance），初始化对象（instance）---> 执行Far的__new__()以及f的__init__()
print(f"\ndefine instances\n===============")
f = Far()
x = Far()
y = Far()
z = Far() # 直接从创建Far的元类中找__call__
Far.__call__(Far) # 从类中找__call__

# c = Child()
c = Child()
# c = Child() -> Child.__call__() -> MyType.__call__(Child)
#                                      为什么不是 ---> Far.__call__(Child)

# obj() ---> 类中的__call__()方法
# f()
# c()


# 元类的意义
# 定义一个类时：执行一些额外的逻辑
# 类实例化时：执行一些额外的逻辑
print(f"class number: {MyType.n}")
print(f"instance number: {MyType.m}")


# type掌管一切类型，而object是一切类的父类
print(MyClass.__bases__) # 查看一个类的父类 (<class 'object'>,)
print(MyClass.__class__) # 查看一个类的类型 <class 'type'>
print(Child.__bases__) # 父类 (<class '__main__.MyObject'>,)
print(Child.__class__) # 类型 <class '__main__.MyType'>    ===    type(Child)
print("实例对象c的类型", c.__class__)
print(type.__bases__) # object父类是object
print(type.__class__) # type类型是type
print(object.__bases__) # object没有父类
print(object.__class__) # object类型是type
print(int.__bases__)
print(int.__class__)

# 一个实例对象属于什么类型？属于哪个class？
# 一个类又属于什么类型？属于哪个type？

# 如何给类动态增加成员函数？
# type(object) -> the object's type 返回一个对象的类型
# type(name, bases, dict, **kwds) -> a new type 通过type创建类

# 给类增加一个成员函数
type.__setattr__(
    Child,
    "info",
    lambda self: print("hello, world")
)

Child().info()


