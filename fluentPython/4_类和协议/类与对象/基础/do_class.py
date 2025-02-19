# 声明类
class Person():

    # 类属性：定义在__init__外的变量
    cls_attr = "类属性"

    # 构造方法
    def __init__(self, name):
        # 实例属性
        self.name = name # Calls the setter
        # 如何在实例中使用类属性
        print("init cls attr", self.__class__.cls_attr)
        
    # 实例方法
    def self_func(self):
        # 如果方法中未使用到self，其实使用静态方法更合适
        print(f"self func {self.name}")

    def _safe_self_func(self):
        pass

    # 类方法 
    @classmethod
    def class_func(cls):
        # 无需实例化，类方法只能使用类属性，不能使用实例属性
        print("class func", cls.cls_attr)

    # 静态方法（不需要使用实例属性或类属性）
    @staticmethod
    def static_func():
        # 为什么需要静态方法呢？使代码更加组织化和模块化
        print("static func")

    # 通过函数的方式返回属性值
    @property
    def name(self):
        # 数据封装和保护、访问控制、属性计算
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
    
    # 以上property等价于下面这行
    # name = property(fget=None, fset=None, fdel=None)
        

if __name__ == "__main__":
    # 类的实例化过程: 涉及到元类的__call__，具体可以参考how_type_works
    # 1. person = Person() ---> type.__call__(Person)
    # 2. 创建一个空对象: Person.__new__(Person) 
    # 3. 初始化该对象: Person.__init__(empty_object, *args, **kwargs) ---> empty_object.__init__(*args, **kwargs)
    # 4. 返回对象: return empty_object
    
    person = Person("zy")
    # 对象.类方法
    person.class_func() # ---> Person.class_func(cls)
    # 对象.实例方法
    person.self_func() # ---> Person.self_func(self)
    # 对象.静态方法: 
    person.static_func() # ---> Person.static_func()
    
    # 如何通过类来调用实例方法？
    Person.self_func(person) # 需要传入对象，对象.方法会默认传入对象
    
    # 如何证明两个实例使用的方法都是同一个？
    daughter = Person("zsy")
    print(id(person.self_func))
    print(id(daughter.self_func))
    
    # 如何找到方法或属性？
    # 1. 实例内存空间
    # 2. 类内存空间（为什么可以找到类？因为实例对象中有一块内存会指向类内存空间）

    # 如何给实例属性赋值？可以给类属性赋值或者修改类属性吗？
    # 1. 实例内存空间可以读写
    # 2. 类内存空间只读！！！不可以赋值，如果给一个实例内存空间不存在的变量赋值，会在实例空间创建该变量
    # 3. 如果一定要修改，通过cls.cls_attr可以修改
    def my_func(msg):
        print(msg)
    person.self_func = my_func
    person.self_func("some message")
    

    # 一切皆对象(python中的所有数据类型)
    # 字符串、列表都是解释器声明的，并且提供了简易表达来初始化
    # s = str("xxx")             <class 'str'>
    # l = list([1,2,3])          <class 'list'>
    # d = dict({"k": "v"})
    # 类实例化后是一个对象
    # 类本身也是一个对象
    
    # del a 
    # 变量可以被删除，对象无法被删除，需要GC（1不会被删除）
    
    # 如果一个对象只需要读取数据，不需要担心任何问题
    # 如果一个对象可以写入，需要考虑下这个可写入的对象会造成什么其他影响
    
