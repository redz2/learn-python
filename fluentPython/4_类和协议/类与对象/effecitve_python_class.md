22. 尽量用辅助类来维护程序的状态，而不是用字典或元组（我觉得说的很对，自定义类方便扩展功能）

    - 不要使用包含字典的字典
    - 不要使用过长的元组 (name, age, classmate)
    - 辅助类更容易留空，更容易扩展

23. 简单的接口应该接受函数，而不是类的实例（有啥用啊？）

    - 闭包无非就是函数保存了其他的变量，那我为啥不用类的实例来做，同样可以保存变量，而且实现**call**方法时，也可以调用（一模一样啊！）

24. 以@classmethod 形式去构建对象

```python
    class Person():

        def __init__(self, name):
            self.name = name

        @classmethod
        def generate_instances(cls config):
            for c in config:
                yield cls(c) # 类实例化对象
```
