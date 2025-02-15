# 继承关系：根据mro依次在父类中寻找方法，直到找到为止
# super()找到自己的第一个父类节点，也是在父类节点中寻找方法

class GrandFather():
    
    name = "GrandFather"


class Father(GrandFather):
    
    namex = "Father"
    
    
class Mother(GrandFather):
    
    namex = "Mother"
    
    
class Son(Father, Mother):
    pass


# 相同点：都是找节点，不过super().__init__()中还嵌套super().__init__()，导致我们感觉super()循环遍历了一遍，实际上是一层层调用的关系
# 类似问题：如何不使用循环进行遍历呢？递归函数（一种高阶函数）

me = Son()
# 对象 ---> 实例空间 ---> 类空间 ---> 父类空间
# 如果没有super()，就是简单的一个个找，直到找到为止
# 如果有super()，就是找到下一个，如果下一个中还包含super()，继续找下一个，其实也是一个个找
print(me.name)
print(me.namex)