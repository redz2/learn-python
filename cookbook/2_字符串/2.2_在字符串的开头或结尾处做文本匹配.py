"""
startswith()
endswith()

当然也可以使用切片，或者使用re正则表达式来判断字符串开头或者结尾，但是不够优雅
"""

import os
filenames = os.listdir()
files = [name for name in filenames if name.startswith('2')]

# 检查目录中是否有py结尾的文件
py_exists = any(name.endswith('.py') for name in filenames)
# any(name.endswith(('.c', '.h')) for name in listdir(dirname))

# 参数必须是一个元组
choices = ['2.1', '2.3']
many_choices = [name for name in filenames if name.startswith(tuple(choices))]
print(many_choices)