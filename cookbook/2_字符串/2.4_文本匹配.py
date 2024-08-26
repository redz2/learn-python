"""
看文本中是否包含特定的字符串
re.match
re.findall()
re.finditer()

简单场景使用
str.find()
str.startswith()
str.endswith
"""

import re

text = "1993/02/19 zhouyi 2022/02/10 zhousiyu"

# 匹配字符串默认是一个group
# 示例中匹配字符串中包含2个group
data_pattern = re.compile(r'(\d+)/\d+/\d+ (\w+)')

# 判断文本是否匹配pattern，如果匹配到返回一个对象，如果没匹配到返回None
have_pattern = re.match(data_pattern, text)
# 文本从头开始匹配，返回最先匹配到的文本
print(have_pattern.group())

# 如果匹配到多个pattern，返回list
# 如果每个pattern有多个分组，返回一个包含tuple的list
res = re.findall(data_pattern, text)
# 返回迭代器
res = re.finditer(data_pattern, text)
