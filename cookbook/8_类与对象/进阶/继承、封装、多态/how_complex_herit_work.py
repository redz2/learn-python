class MyGranMaType(type):
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
    
    def test_type(self):
        print("MyGrandMaType test_type")
        
    def test_class(self):
        print("MyGrandMaType test_class")

class MyType(MyGranMaType):
    
    def __new__(cls, *args, **kwargs):
        # 创建类时，可以添加类属性和方法
        cls.name = "MyType Name"
        return super().__new__(cls, *args, **kwargs)
    
    def test_type(self):
        print("MyType test_type")
        
    # def test_class(self):
    #     print("MyType test_class")

class GrandMa(metaclass=MyGranMaType):
    
    def __init__(self, name):
        print("GrandMa __init__")
        self.name = name
        
    def test_type(self):
        print("GrandMa test_type")
        
        
class Mother(GrandMa):
    
    # 代码复用
    pass

class Son(Mother, metaclass=MyType):
    
    # super()一般用在重写方法，扩展代码功能时
    def __init__(self, name):
        # self.__init__(name) 不过__init__()是父类中的方法，本质上是obj.method()
        super().__init__(name)
        
    def test(self):
        print("son test")


me = Son("zy")
# print(me.name)
# print(Son.name) # 创建类时由元类创建

# 不涉及元类，只讨论类的继承关系
# super()找到父类 Mother，调用实例方法
# Mother 没有__init__()，从父类 GrandMa 中找




# 如何找到object调用的方法？如何找到类调用的方法？
# 自己的内存空间，创建自己的类的内存空间（还会从父类中去找）
# 语法糖: object.method() -> cls.method(self)

# 对象.方法
# 1. 实例对象内存空间 -> 创建该实例的类
# 2. Son class类内存空间
# 3. Mother class类内存空间
# 4. GrandMa class类内存空间
print("object.method ==========")
me.test_type() # GrandMa.test_type(me)
# me.test_class() # 'Son' object has no attribute 'test_class'
print("class.method ==========")
# 类.方法
# 1. 类内存空间
# 2. 父类内存空间: mro顺序找
# 3. 元类MyType内存空间
# 4. 元类MyGrandMa内存空间
Son.test(me)
Son.test_type(me)
Son.test_class() # 这里Son就是MyType创建的实例对象，只不过是个class罢了


print(dir(Son))
print(Son.__class__)
print(Son.__dict__)
print(Son.__bases__)
print(Son.__mro__) # 每个类都有一个mro，告诉python，属性和方法应该按照什么顺序找
# print(me.__mro__)

print(MyType.__mro__)
print(type.__mro__)




