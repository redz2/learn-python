from array import array
import reprlib
import numbers

# 如果说类是你抽象出来的一个笼统概念，对象就是把笼统概念又进行了具体化，具体化的结果叫对象，这个过程叫实例化
class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        # 底层存储为array
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # 有限长度表现形式
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return "Vector({})".format(components)

    # 序列协议需要实现__len__和__getitem__方法
    # 鸭子类型语言使用非正式接口
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # 获取 object 的 class
        cls = type(self)
        if isinstance(index, slice):
            # 创建Vector对象
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

        # return Vector(self._components[index])

    # 通过名称访问向量的前四个分量
    def __getattr__(self, name):
        # 获取Vector
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0<= pos < len(self._components):
                return self._components[pos]

    def do_something(self):
        return

    # def __setattr__(self, name, value):
    #     return 

if __name__ == "__main__":
    v1 = Vector(range(10))
    v2 = Vector(range(2))
    # 说明不同对象使用的方法是同一个(JS中的原型对象)
    print(id(v1.do_something) == id(v2.do_something))
    

