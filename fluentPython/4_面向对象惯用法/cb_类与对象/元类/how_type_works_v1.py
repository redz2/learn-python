# 自定义元类
class MyType(type):
    
    # 可以统计创建了多少个MyType类型的类
    _n = 0
    _m = 0
    
    # 为何__new__不需要加@classmethod？特殊方法，用于创建类的实例
    def __new__(cls, *args, **kwargs):
        """
        创建类时调用此方法
        cls -> MyType元类
        """
        cls._n += 1
        # __mro__: (<class '__main__.MyType'>, <class 'type'>, <class 'object'>)
        # object.__new__(MyType) is not safe, use type.__new__()
        print(f"type is {cls}")
        # type.__new__(cls, name, bases, attrs)
        return super().__new__(cls, *args, **kwargs) # 创建类
    
    def __init__(self, *args, **kwargs):
        """
        创建类时调用此方法: 当我们声明一个类时，会依次执行元类中的__new__和__init__
        通过类创建一个对象时，调用的是object中的__init__ !!!
        """
        print(f"class is {self}")
        # 默认参数: <super: <class 'MyType'>, <MyType object>>
        # 找父类中的__init__()，其实就是object or MyObject
        # 使用super()调用父类的实例方法，会自动把self传进去！！！
        super().__init__(*args, **kwargs) # 初始化类
    
    def __call__(self, *args, **kwargs):
        """
        通过类创建一个对象时，会调用此方法
        此方法描述了创建类的实例的过程
        """
        # Foo(): 调用创建类Foo的元类的__call__方法 -> 创建一个空对象 -> 初始化这个对象
        # foo(): 调用创建对象foo的Foo类的__call__方法
        empty_obj = self.__new__(self, *args, **kwargs) # 调用类方法__new__，一般在类中不定义，到type中找该方法
        print(f"MyType.__call__: instance is {empty_obj}")
        self.__init__(empty_obj, *args, **kwargs) # 这里相当于调用类中的__init__()方法，并传入对象，一般在类中定义
        type(self)._m += 1 # 其他操作
        return empty_obj # 返回对象
    
    @classmethod
    @property
    def n(cls):
        return cls._n
    
    @classmethod
    @property
    def m(cls):
        return cls._m
    
print(f"0. 定义类")
# 定义一个普通的类
class MyObject(object):
    
    def __new__(cls, *args, **kwargs):
        """
        cls: <class '__main__.Child'>
        """
        print("MyObject.__new__")
        print(cls.__mro__) # (<class '__main__.Child'>, <class '__main__.MyObject'>, <class 'object'>)
        print(super())
        return super().__new__(cls, *args, **kwargs)

# 通过元类创建两个类: Father、Child
"""
metaclass: 该类由哪个元类创建（如果父类中包含metaclass，子类也由父类中的元类创建）
"""
class Father(object, metaclass=MyType):
    
    def __new__(cls, *args, **kwargs):
        print(f"Father.__new__")
        return super().__new__(cls)
    
    def __call__(self):
        print(f"object is {self}, now run Father.__call__")

class Child(MyObject, metaclass=MyType):
    
    child_var = "test"
    
    def __init__(self):
        # <super: <class 'Child'>, <Child object>>
        print("Child.__init__")
        
    def __call__(self):
        print("Child.__call__")
    
    @classmethod
    def my_func(cls):
        pass
print(f"\n")

# 创建一个对象（instance），初始化对象（instance）---> 执行Far的__new__()以及f的__init__()
print(f"1. f = Father() 的执行过程")
f = Father() # 调用元类中MyType的__call__
print(f"\n")

print(f"2. 如何调用Father中的__call__")
Father.__call__(f) # 等价于 f()
f()
print(f"\n")

print(f"3. c=Child() 的执行过程")
c = Child() # 调用MyType的__call__ -> MyObject.__new__ -> Child.__init__
print(f"\n")

print(f"4. 通过元类统计创建的类、对象的数量")
print(f"class number: {MyType.n}")
print(f"instance number: {MyType.m}")
print(f"\n")

print(f"5. 查看一个类的父类以及元类")
# type -> class -> instance
print("type掌管一切类型，而object是一切类的父类")
print(f"Father的父类: {Father.__bases__}") 
print(f"Father的类型: {Father.__class__}")
print(f"Child的父类: {Child.__bases__}") 
print(f"Child的类型: {Child.__class__}")
print(f"Child对象的类型: {c.__class__}")
print(f"type的父类: {type.__bases__}") 
print(f"type的类型: {type.__class__}") 
print(f"object的父类: {object.__bases__} object 没有父类") 
print(f"object的元类: {object.__class__}")
print(f"int的父类: {int.__bases__}")
print(f"int的类型: {int.__class__}")
print("\n")

# type(object) -> 返回一个对象的类型
# type(name, bases, dict, **kargs) -> 通过type创建一个class

print(f"6. 给类增加一个成员函数")
type.__setattr__(
    Child,
    "info",
    lambda self: print("hello, world")
)

Child().info()
print("\n")