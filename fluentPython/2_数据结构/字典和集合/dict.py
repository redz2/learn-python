### 常见的字典方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # zip接受多个可迭代对象，输出一系列元组
d = dict([('two', 2), ('three',3), ('one', 1)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e

# 字典推导
DIAL_CODES = [
    (91, 'India'),
    (1, 'Uniteed States')
]
country_code = { country: code for code, country in DIAL_CODES}

# d.clear()
# del d[k]

### 如何处理查不到的键
### 标准库中dict类型的变种
### set和frozenset
### 散列表的工作原理
### 
