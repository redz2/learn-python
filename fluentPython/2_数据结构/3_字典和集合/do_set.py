# 集合的本质是许多唯一对象的聚集（去重）
l = [1,2,3,4,1]
no_repeat_l = list(set(l))

# a | b 合集
# a & b 交集
# a - b 差集

s = {1} # 集合字面量
s0 = set() # 空集，{}表示空字典

# frozenset # 本身可散列
# set # 本身不可散列，元素必须是可散列的


# 集合推导
from unicodedata import name
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
# {'§', '=', '¢', '#', '¤', '<', '¥', 'μ', '×', '$', '¶', '£', '©', '°', '+', '÷', '±', '>', '¬', '®', '%'}