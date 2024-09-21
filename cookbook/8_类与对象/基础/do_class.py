# 面向对象编程是如何把算法复杂性隔离开来，而保留接口和其他的代码不变

# 声明类
class Person():

    # 类属性：定义在__init__外的变量
    cls_attr = "类属性"

    # 构造方法
    def __init__(self, name):
        # 实例属性
        self.name = name # Calls the setter
        print("init cls attr", self.__class__.cls_attr)
        
    # 实例方法
    def self_func(self):
        # 如果方法中未使用到self，其实使用静态方法更合适
        print("self func")

    def _safe_self_func(self):
        pass

    # 类方法 
    # 无需实例化，类方法只能使用类属性，不能使用实例属性
    @classmethod
    def class_func(cls):
        print("class func", cls.cls_attr)

    # 静态方法（不需要使用实例属性或类å属性）
    @staticmethod
    def static_func():
        print("static func")
    # 为什么需要静态方法呢？使代码更加组织化和模块化


    # 将类的方法转换成属性
    # 数据封装和保护、访问控制、属性计算
    @property
    def name(self):
        return self._name

    # 如果赋值操作不需要其他处理，那么不要用property
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value # 数据实际保存在_name中

    @name.deleter
    def name(self):
        del self._name
        
    # 使用property定义计算属性
    @property
    def hello(self):
        return f"hello, {self._name}"
    
    # name = property(fget=None, fset=None, fdel=None)
        

if __name__ == "__main__":
    
    # 实例对象：类实例化后就是实例对象 person（类不实例化只声明的话毫无意义）
    # 实例对象可以访问实例属性 ---> 类属性，实例方法 ---> 类方法(有顺序)
    
    # 实例化过程
    # 1. 创建一个新的对象（开辟独立内存空间，包含一个字段指向类）
    # 2. self指向该对象
    # 3. 调用__init__()，执行初始化代码（自动调用）
    # 4. 返回对象
    person = Person("zy")
    # 对象.类方法（自动传入self.__class__，即cls）
    # 对象.实例方法（自动传入self）
    person.class_func() # ===> class_func(Person, *args, **kwargs)
    person.static_func() # ===> static_func(*args, **kwargs)
    person.self_func() # ===> self_func(person, *args, **kwargs)
    
    daughter = Person("zsy")
    # 先找person自己的空间，没找到，通过指针找到Person类，找到公共属性和方法
    # 如何证明两个实例使用的方法都是同一个？
    print(id(person.self_func))
    print(id(daughter.self_func))
    
    # 实例属性赋值（类与对象的内存空间是分开的，对象中有字段指向类空间，类没法知道有哪些对象）
    # 1. 实例内存空间可以读写
    # 2. 类内存空间只读！！！
    # 赋值一定是写入实例内存空间（思考下读写的差异）
    def my_func(msg):
        print(msg)
    person.self_func = my_func
    person.self_func("some message")
    
    # 如何修改类属性？
    # 通过self.cls_attr可以读类属性
    # 通过self.cls_attr修改，只会在self中新增cls_attr实例属性
    # 所以必须通过cls.cls_attr才可以修改类属性
    
    # 类.实例方法（需要手动传入对象）
    # 有类不一定有实例，有实例一定知道类
    Person.self_func(person)
    
    # 一切皆对象(python中的所有数据类型)
    # 字符串、列表都是解释器声明的，并且提供了简易表达来初始化
    # s = str("xxx")             <class 'str'>
    # l = list([1,2,3])          <class 'list'>
    # d = dict({"k": "v"})
    # 类实例化后是一个对象
    # 类本身也是一个对象
    
    
    
    # del a 
    # 变量可以被删除，对象无法被删除（1不会被删除）
    
    
    
    # 如果一个对象只需要读取数据，不需要担心任何问题
    # 如果一个对象可以写入，需要考虑下这个可写入的对象会造成什么其他影响
    
