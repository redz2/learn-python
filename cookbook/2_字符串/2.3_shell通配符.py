"""
该模块提供了对Unix shell风格的通配符的支持
fnmatch(file, pattern) 判断文件名是否和pattern匹配
fnmatchcase(file, pattern) 区分大小写
"""

import os
from fnmatch import fnmatchcase

filenames = os.listdir()
r = [name for name in filenames if fnmatchcase(name, "*.py")]