"""
f: Formatted String
r: Raw String
b: Byte String
u: Unicode String Python3中默认
"""
name = zhouyi
age = 25

f_str = f"my name is {name}"
r_str = r"c:\Program Files\Python"

# 模运算符
a_str = "my name is %s, I am %d" % (name, age)
b_str = "my name is %(name)s, I am %(age)d" % {"name": name, "age": age}

# 使用格式化方法
c_str = "my name is {name:s}, I am {age:d}".format(name=name,age=age)
e_str = "my name is {!s}"

# 使用f-string
d_str = f"my name is {name}, I am {age}"
