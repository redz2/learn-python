from loguru import logger
class Person(object):
    
    """
    1. __new__()开辟独立空间
    2. __init__()初始化实例属性
    3. 返回空间地址
    """
    _instance = None
    
    # 触发机制：创建对象，开辟地址空间时
    def __new__(cls, *args, **kwargs):
        if not cls._instance: 
            print("__new__ is running")
            cls._instance = object.__new__(cls)
        return cls._instance
        
    def __init__(self, name):
        self.name = name
        self._data = {}
        
    # 触发机制：str()
    def __str__(self):
        return str(self.name)
    
    # object中按照id来比较
    # 触发机制：== 
    def __eq__(self, other):
        return self.name  == other.name 
        
    # 触发机制：len()
    def __len__(self):
        return len(data)
    
    # 像操作字典一样操作对象
    # __item__系列
    def __getitem__(self, key):
        logger.info(f"查询某个键")
        return self._data[key]
    
    def __setitem__(self, key, value):
        logger.info(f"添加键值")
        self._data[key] = value
    
    def __delattr__(self, key):
        del self._data[key]
        
    def __contains__(self, key):
        return key in self._data.keys()
    

# 单例模式（对象都访问一块内存地址空间）
print(1) # print会先进行强转，print(str(1)) 
l1 = [1,2,3]
l2 = [1,2,3]
l1 == l2
l1 is l2

p = Person("xxx")
p["name"] = "zsy"
p["age"] = 3
# print(hasattr(p, "_data"))
# print(hasattr(p, "age"))



class Cache(object):
    
    def __init__(self):
        # self._data = {} 这里会有问题，使用__setattr__
        self.__dict__["data"] = {}
    
    # __attr__的触发机制导致无法直接使用self.data，会导致一直循环，只能都写self.__dict__["data"]，太tm丑陋了
    # 会报RecursionError: maximum recursion depth exceeded
    # 触发机制: obj.key = value
    def __setattr__(self, key, value):
        self.__dict__["data"][key] = value
        
    # 触发机制: obj.key
    def __getattr__(self, key):
        if key in self.__dict__["data"]:
            return self.__dict__["data"][key]
        else:
            raise KeyError("no key found")
    
    # 触发机制: del obj.key
    def __delattr__(self, key):
        self.__dict__["data"].pop(key)
    
cache = Cache()
cache.xxx = "z" # obj.xxx = yyy ---> __setattr__()
print(cache.xxx) # obj.xxx ---> __getattr__()



        