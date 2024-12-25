"""
dict是python语言的基石（）
1. 模块的命名空间
2. 实例的属性
3. 函数的关键字参数
"""

# 判断某个数据是不是广义上的映射类型
from collections import abc
my_dict = {}
isinstance(my_dict, abc.Mapping)

# 如何创建字典？
## 1. 字面句法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3} # 常用
c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # zip接受多个可迭代对象，输出一系列元组
d = dict([('two', 2), ('three',3), ('one', 1)]) # 等价于zip
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e

## 2. 字典推导
DIAL_CODES = [
    (91, 'India'),
    (1, 'Uniteed States')
]
country_code = {country: code for code, country in DIAL_CODES}

# 字典常见方法（dict, collections.defaultdict, collections.OrderedDict）
my_dict.clear() # 移除所有元素
my_dict.__contains__("k") # 检查k是否在my_dict中
my_dict.__delitem__("k") # del my_dict["k"]，移除键为"k"的元素
my_dict.get("k", "default") # 返回键为"k"的值，如果没有返回"default"，比d["k"]好用！！！
my_dict.__getitem__("k") # d["k"]，若没有key，报KeyError
my_dict.items() # 返回所有键值对
my_dict.keys() # 获取所有的键
my_dict.values() # 获取所有的值
my_dict.__len__() # len(my_dict)
my_dict.setdefault("k", "default") # 如果存在key，返回key的值；如果不存在key，d["k"] = "default"，并返回默认值
my_dict.__setitem__("k", "v") # my_dict["k"] = "v"

# 案例：统计每个单词出现的位置
# words = "my name is zhouyi".strip()
# index = {}
# location = 0
# for word in words:
#     index.setdefault(word, []).append(location)
#     location += 1




