from collections import defaultdict

# 给构造方法提供一个可调用对象
# dd["new-key"]明显找不到"new-key"
# 调用list()创建一个列表
# 把列表作为值，"new-key"作为键，放入dd
# 返回这个列表的引用
dd = defaultdict(list)
# 相当于setdefault
dd["new-key"]

# 特殊方法__missing__()
# 当__getitem__()找不到键时，不会抛出KeyError，而是会调用该方法
# 注意：__missing__()只会被__getitem__()调用



# 字典的变种
from collections import OrderedDict # 有序字典
from collections import ChainMap
from collections import Counter # 用于统计可迭代对象中元素出现的次数
from collections import UserDict # 把标准dict使用纯Python实现一遍

ct = Counter("abcdsadsadasidsadas") # -> {"a": 6, ...}
ct.update("aaaaabbbbbb") # -> {"a": 11, ...}