class MyType(type):
    """
    如何在创建一个类时，做一些额外的操作？
    """
    # 创建类时调用，可以添加类属性或类方法
    def __new__(cls, name, bases, attrs):
        print("MyType.__new__")
        attrs["my_name"] = name
        return type.__new__(cls, name, bases, attrs) # 创建并返回一个类

    # 创建类时调用: 目前不知道有啥用？
    def __init__(self, *args, **kwargs):
        # self就是元类创建的类，也可以添加类属性或类方法
        print("MyType.__init__")
        self.my_age = 30

    # 1. 类实例化对象时会调用元类的__call__
    def __call__(self, *args, **kwargs):
        """
        这里主要了解的是为什么会调用__new__和__init__方法？
        
        如何在使用类创建对象时，做一些额外的操作？在类的__new__和__init__中修改
        """
        # self -> 类Test
        print("MyType.__call__")
        # 2. 调用type的__call__
        return type.__call__(self, *args, **kwargs) # 创建一个该类的对象
    

        
    """
    如何创建该类的对象？具体实现过程是怎样的？以下是type中的大致实现
    type中的__call__做了哪些事情？调用了type.__new__创建了一个对象，调用type.__init__初始化一个对象
    如何修改创建对象的过程？在类中重写__new__和__init__
    也就是说，在类中我们可以不定义这两个方法，默认会使用object中的__new__和__init__
    """
    # def __call__(self, *args, **kwargs): 
    #     empty_obj = self.__new__(self, *args, **kwargs) # 调用类方法__new__，一般在类中不定义，到type中找该方法
    #     print(f"instance is {empty_obj}")
    #     self.__init__(empty_obj, *args, **kwargs) # 这里相当于调用类中的__init__()方法，并传入对象，一般在类中定义
    #     return empty_obj
    
# 创建一个类时，会调用元类的__new__方法
class Test(object, metaclass=MyType):
    # 如何实现单例？在__new__中判断是否创建过对象
    
    # 3. 调用Test的__new__
    def __new__(cls):
        print("Test.__new__")
        # super() -> object -> __new__()
        return super().__new__(cls)
    
    # 4. 调用Test的__init__
    def __init__(self):
        print("Test.__init__")
        super().__init__()

# 1. Test是MyType元类创建的，Test()会调用元类的__call__方法: type.__call__(Test, *args, **kwargs)
# 2. 元类中的__call__方法，参数是创建的类，通过类创建一个空对象，通过类和空对象进行初始化
# 3. Test.__new__(Test) -> 此方法是object提供的
# 4. Test.__init__(obj, *args, **kwargs) -> 此方法一般类中都会定义，如果没有定义，也由object提供
t = Test()
print(t.my_name)
print(t.my_age)

from prometheus_client import start_http_server