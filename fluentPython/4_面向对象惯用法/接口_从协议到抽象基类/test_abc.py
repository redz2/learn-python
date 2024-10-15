"""ABC
Abstract Base Class(抽象基类) -> 使接口更明确、能验证实现是否符合规定 -> 抽象类表示接口

"""

import abc

class Tombola(abc.ABC):
    """这是一个抽象基类，有两个抽象方法，有两个具体方法
    
    抽象方法可以有代码实现，不过子类必须覆盖抽象方法
    和常规父类的区别？会进行检查
    """
    
    # @classmethod # 如果有多个装饰器，abstractmethod必须在最里面
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素 """
        
    @abc.abstractmethod
    def pick(self):
        """随机删除元素，并返回 """
        
    def inspect(self):
        """返回一个有序数组，由当前元素组成
        
        我们不知道子类如何存储元素，不过我们可以调用pick()，把Tombola清空
        具体子类知道内部数据结构，可以更聪明的实现此功能，这里只是为了强调抽象基类可以提供具体的方法
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
    
    def loaded(self):
        """如果至少有一个元素，返回True，否则返回Fasle"""
        return bool(self.inspect())
    
    
import random

class BingoCage(Tombola):
    """继承了耗时的loaded和不太聪明的inspect方法，我们可以偷懒，可以直接继承不那么理想的具体方法"""
    
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")
    
    def __call__(self):
        self.pick()
    
    
from typing import List, Iterable

class LotteryBlower(Tombola):
    
    def __init__(self, iterable: Iterable):
        self._balls: List = list(iterable) # list()会创建副本
        
    def load(self, iterable: Iterable):
        self._balls.extend(iterable)
        
    def pick(self):
        """上面是先打乱"""
        try:
            position: int = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from empty BingoCage")
        return self._balls.pop(position)
    
    def loaded(self):
        return bool(self._balls)
    
    def inspect(self):
        return tuple(sorted(self._balls))
        
        
"""虚拟子类

虚拟子类不会继承注册的抽象基类，任何时候都不会检查它是否符合抽象基类，即便在实例化时也不会检查
虚拟子类需要实现抽象基类的所有方法

"""

@Tombola.register
class TomboList(list):
    
    # def __init__(self, *args):
    #     super().__init__(*args)
    #     self.other_info = "what happened"
    
    def pick(self):
        """TomboList是List的子类
        
        继承的本质就是方法的扩充和重写，所以TomboList就是添加了额外功能的list
        """
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pick from empty TomboList")
        
    load = list.extend
    
    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))
        
        

        print("sda")

if __name__ == "__main__":
    tl = TomboList(range(10))
    print(tl)
    tl.pick()


    
