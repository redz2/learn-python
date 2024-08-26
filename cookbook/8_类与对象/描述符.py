# 属性描述符
# 控制对属性的访问，添加额外的处理逻辑(属性托管这个词比较形象！)

# V1版本
class Integer():
    
    """
    描述符: 实现了特定协议的类，包括__get__、__set__、__delete__方法（可以只实现部分协议）
    
    property、classmothed、staticmethod都用到了描述符
    """
    
    
    def __init__(self, name):
        self.name = name # 托管实例存储值的属性的名称
    
    # obj底层使用dict保存属性
    def __get__(self, instance, cls):
        print("Calls __get__()")
        if instance is None:
            return self
        else:
            # {'x': 2, 'y': 4}
            return instance.__dict__[self.name]
        
    # 先做类型判断，再将属性保存到obj的字典中
    def __set__(self, instance, value):
        print("Calls __set__()")
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name] = value
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]
        
class Point():
    
    # 这是语法糖吗？
    
    # 使用Integer描述符管理Point的属性
    # 如何使用一个描述符？需要把描述符的实例放在类的定义中作为变量使用
    # 针对描述符属性的访问都会被__get__()、__set__()、__delete__()方法捕获
    x = Integer('x')
    y = Integer('y')
    
    def __init__(self, x:int, y:int, z:str=""):
        
        # 我也不清楚为什么会调用类属性x的方法？
        self.x = x # Calls x.__set__(p, 5) -> __dict__中添加x
        self.y = y
        self.z = 'other' # -> __dict__中添加z






# V2版本: 自动获取储存属性的名称
# 1. 定义一个描述符类
class IntegerV2():
    
    # 为了管理属性写这么多代码值得吗？
    __count = 0
    
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__count
        self.storage_name = "_{}#{}".format(prefix, index)
        cls.__count += 1
            
    def __get__(self, instance, cls):
        if instance is None:
            return self
        print(self.storage_name)
        return getattr(instance, self.storage_name)
        
    def __set__(self, instance, value):
        print("Calls v2 __set__")
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        setattr(instance, self.storage_name, value)
        print(instance.__dict__)
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]
        
class PointV2():
    
    # 2. 描述符类实例化 -> 类属性
    x = IntegerV2() # -> _IntegerV2#0
    y = IntegerV2() # -> _IntegerV2#1
    
    def __init__(self, x:int, y:int, z:str=""):
        
        # obj底层已经是这个鬼样子了: {'_IntegerV2#0': 365, '_IntegerV2#1': 4, 'z': 'other'}   
        self.x = x
        self.y = y
        self.z = 'other'
        
        
# V3版本
class AutoStorage():
    pass

import abc
class Validated(abc.abstractmethod, AutoStorage):
    pass

class A(Validated):
    pass

class B(Validated):
    pass

if __name__ == "__main__":
    
    # p = Point(1, 4)
    # p.x = 5 # Calls Point.x.__set__(p, value)
    # print(p.x) # Calls Point.x.__get__(p, Point)
    # print(p.z) # Calls p.z
    # del p.x # Calls Point.x.__delete__(p)
    # print(p.__dict__) # Get all instance attrs
    
    p2 = PointV2(3, 4)
    print(p2.x)
    p2.x = 365
    print(p2.__dict__)