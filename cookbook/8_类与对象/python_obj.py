# 类对象：定义的类 Person
class Person():

    # 类属性：定义在__init__外的变量
    cls_attr = "类属性"

    def __init__(self, name):
        # 实例属性
        self.name = name # Calls the setter
        
    # 实例方法
    def self_func(self):
        # 如果方法中并未使用类属性，其实使用静态方法更合适
        print("self func")

    def _safe_self_func(self):
        pass

    # 类方法 
    # 无需实例化，类方法只能使用类属性，不能使用实例属性
    @classmethod
    def class_func(cls):
        print("class func")

    # 静态方法
    # 不需要对类实例化，可以直接调用，但是不能访问类属性和实例属性

    # 为什么需要静态方法呢？使代码更加组织化和模块化
    @staticmethod
    def static_func():
        print("static func")

    # 将类的方法转换成属性
    # 数据封装和保护、访问控制、属性计算
    @property
    def name(self):
        return self._name

    # 如果property不需要完成其他事，不要写成这个样子
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
        

if __name__ == "__main__":
    
    # 实例对象：类实例化后就是实例对象 person
    # 实例对象可以访问类属性，类方法，实例属性，实例方法

    # 实例化过程
    # 1. 创建一个新的对象
    # 2. self指向该对象
    # 3. 调用 __init__()，执行初始化代码
    # 4. 返回对象
    person = Person("zhouyi")
    person.class_func() # ===> class_func(Person, *args, **kwargs)
    person.static_func() # ===> static_func(*args, **kwargs)
    person.self_func() # ===> self_func(person, *args, **kwargs)
    