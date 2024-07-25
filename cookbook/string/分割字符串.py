import re
"""
re.split(pattern, string[, maxsplit=0, flags=0])
pattern: 匹配的字符串
string: 需要分割的字符串
maxsplit: 分隔次数
flags: 标志位，用于控制正则表达式匹配的方式，比如：是否区分大小写
"""

a = "good morning zhouyi"
b = "hello,zhouyi!abc;defg it is!   ok"

arr1 = a.split(' ')
# ['good', 'morning', 'zhouyi']

# 1. 允许你为分隔符指定多个正则模式（不包含分隔符）
arr2 = re.split(r'[,!;\s]\s*', b)
# ['hello', 'zhouyi', 'abc', 'defg', 'it', 'is', 'ok']

# 2. 捕获分组（包含分割符）
arr3 = re.split(r'(,|!|;|\s)\s*', b)
# ['hello', ',', 'zhouyi', '!', 'abc', ';', 'defg', ' ', 'it', ' ', 'is', '!', 'ok']
values = arr3[::2]
# ['hello', 'zhouyi', 'abc', 'defg', 'it', 'is', 'ok']
delimiters = arr3[1::2] + ['']
# [',', '!', ';', ' ', ' ', '!']

# 去掉多余的空格
result = ''.join((m+n for m,n in zip(values, delimiters)))

# 3. 不保留分割字符串到结果中（不包含分隔符）
arr4 = re.split(r'(?:,|!|;|\s)\s*', b)

