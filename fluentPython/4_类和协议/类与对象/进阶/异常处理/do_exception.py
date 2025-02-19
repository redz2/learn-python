# SyntaxError: expected ':'
# if forget_colon
# IndentationError: expected an indented block after 'if' statement on line 9
# pass

# NameError: name 'xxx' is not defined
# print(xxx)

# IndexError: list index out of range
# a = []
# a[10]

# KeyError: 'k'
# d = {}
# d["k"]

# ValueError: invalid literal for int() with base 10: 'sad
# int("sad")

# FileNotFoundError: [Errno 2] No such file or directory: 'filenotexist'
# open("filenotexist")

# ZeroDivisionError: division by zero
# 1/0

# AttributeError: 'Person' object has no attribute 'xx'
# class Person():
#     pass
# p = Person()
# p.xx

# IOError: 和输入输出相关的错误


try:
    # 试着执行
    1 / 0
# 通用异常（不推荐）
except Exception as e:
    # 捕获错误
    pass
# 指定异常
except ZeroDivisionError as e:
    pass
# 统一处理多个异常
except (ValueError, KeyError) as e:
    pass
# 未发生异常
else:
    pass
# 无论是否发生异常
finally:
    pass
    
# 主动抛出错误（业务错误，不是逻辑错误或者语法错误）
raise Exception("my exception")