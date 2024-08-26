class Father():
    
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.deleter
    def name(self):
        raise AttributeError("Can not delete attribute")
        
class Child(Father):
    
    def __init__(self, name):
        super().__init__(name) # 如何调用父类中的实例方法？
        # Father.__init__(self, name)
    
    # 在子类中扩展属性
    @property
    def name(self):
        print("Getting Name")
        return super().name
    
    @name.setter
    def name(self, value):
        print("Setting Name")
        # 为什么要这么写
        super(Child, Child).name.__set__(self, value)
        
    @name.deleter
    def name(self, value):
        print("Deleting Name")
        super(Child, Child).name.__delete__(self)
        
        
    # 如果只修改get方法，需要写成下面这样，属性的其他方法会被拷贝过来，getter方法会被替换掉
    # @Person.getter
    # def name(self):
    #     return super().name
        