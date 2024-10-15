"""相对导入
在一个package中，模块导入非常有用，它提供了一种避免硬编码包名的方法，使得代码更加灵活和易于维护
但是，只有同一个package中的模块，才能使用相对导入
"""
import sys
from pathlib import Path


# django框架也设置了BASE_DIR，所以导入模块比较方便
# BASE_DIR = Path(__file__).resolve().parent.parent 不能直接加到sys.path
BASE_DIR = '/Users/tzhouyi_108087/Desktop/zhouyi/python/learn-python'
# BASE_DIR
# -- package1
#    -- __init__.py
#    -- module
#       -- function
#       -- class
#       -- var
# -- package2
# -- package3
sys.path.append(BASE_DIR)

# from cookbook.XXX import ZZZ # import应该是模块
# 首次导入包时，执行一次__init__.py，只有在使用模块或对象时才会执行响应的代码
# from cookbook.XXX.ZZZ import * # 和导入包效果一样
# from cookbook.XXX.ZZZ import test4 # 导入模块，不仅会执行__init__.py，还会执行test4.py

def say_hello():
    # from ..ZZZ import test4
    # from .test1 import say_hello
    from . import test1
    test1.say_hello() # 相对导入只能在包内部使用，不能用于顶层的脚本！！！
    # ImportError: attempted relative import with no known parent package
    from cookbook.XXX.YYY import test1 
    test1.say_hello()

# 这就是顶层脚本！！！
# if __name__ == '__main__':
#     for i  in range(2):
#         say_hello()

# 为什么在django中可以使用相对导入，开发其实只是在编写package，主程序会导入这些package和module进行使用
# 1. 相对导入只能在包内部使用，不能用于顶层的脚本。如果在顶层脚本中尝试使用相对导入，会抛出ValueError: Attempted relative import in non-package错误
# 2. 直接运行包含相对导入的模块会导致错误，因为相对路径无法解析。要运行这样的模块，可以使用python -m选项，如python -m mypackage.A.spam