import this
"""
0. import总是要放在开头，注意顺序
1. 标准库模块
2. 第三方库模块
3. 自用模块
"""

"""
2. 遵循PEP8风格指南

* 使用空格来表示缩进，而不是tab（我的vscode已经设置过了）
* 和语法相关的每一层都缩进4个空格
* 每一行的字符数不应该超过79个
* 占据多行的长表达式，除了首行，其他要在此基础上再缩进4个空格
* 函数和类应该2个空行隔开
* 同一个类中，方法用1个空行隔开
* 变量赋值时，赋值符号左右各加一个空格
* 函数、变量、属性使用小写字母来拼写，lowercase_underscore

"""

# 模块级别的常量
MODULE_VAR = 0

class Test(): # 类 --- 大驼峰
    
    def __init__(self):
        self._leading_underscore = 1 # 受保护的实例属性
        self.__double_leading_underscore = 2 # 私有的实例属性
    
    def do(self): # self -> 对象
        a = 1
        b = 2
        # if not a is b
        if a is not b: # 采用内联形式的否定词
            print("a is not b")
        # if len(list_a) == 0
        if not list_a:
            print("默认会把非空的值判断为True")
    
    @classmethod
    def cls_do(cls): # cls -> 类
        pass
    
class MyException(Exception): # 异常 --- 大驼峰
    pass




