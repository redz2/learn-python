# 不可变映射类型
from types import MappingProxyType


# my_dict_proxy是my_dict的只读视图，无法修改
# 如果my_dict改动了，my_dict_proxy可以观察到
my_dict = {"name": "zy"}
my_dict_proxy = MappingProxyType(my_dict)

