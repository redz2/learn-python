"""
关键字参数能让调用的意图更加明确
位置参数尽量类型要保持一致，超过2个位置参数，尽量使用*args
"""


# def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
def safe_division(number, divisor, *, ignore_overflow=False, ignore_zero_division=False, **kwargs):
    """ *标志位置参数就此终结，之后的参数只能是关键字参数"""
    
    # Python2没有明确的语法定义这种只能以关键字形式指定的参数
    # Python2这么写，只是给了个默认值，没有办法明确参数是关键字参数
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
        
# safe_division(number, divisor, ignore_overflow=False, ignore_zero_division=False)
# safe_division(1,2,3,4,5)
# TypeError: safe_division() takes from 2 to 4 positional arguments but 5 were given
# 函数认为ignore_overflow和ignore_zero_division都是有默认值的位置参数

# safe_division(number, divisor, *, ignore_overflow=False, ignore_zero_division=False)
# safe_division(1,2,3,4,5)
# TypeError: safe_division() takes 2 positional arguments but 5 were given
# 函数认为ignore_overflow和ignore_zero_division是关键字参数

# Python2
def safe_division_py2(number, divisor, **kwargs):
    # python2如何手动处理成只能使用关键字参数？
    ignore_overflow = kwargs.pop("ignore_overflow", False)
    ignore_zero_division = kwargs.pop("ignore_zero_division", False)
    if kwargs:
        raise TypeError("Unexpected **kwargs: %r" % kwargs)
    
# safe_division_py2(1,2,3)
# TypeError: safe_division_py2() takes 2 positional arguments but 3 were given

        
# 感受下关键字参数和位置参数的区别
def check_function_args(position_arg1, position_arg2=0, *args, key_word_arg1, key_word_arg2=None, **kwargs):
    print(f"无默认值的位置参数: {position_arg1}")
    print(f"有默认值的位置参数: {position_arg2}")
    print(f"数量不确定的位置参数: {args}")
    print(f"无默认值的关键字参数: {key_word_arg1}")
    print(f"有默认值的关键字参数: {key_word_arg2}")
    print(f"其他关键字参数: {kwargs}")
    
check_function_args(1, 2, 3, 4, 5, name="zhouyi", age=18, key_word_arg2=24, key_word_arg1=2)
# 无默认值的位置参数: 1
# 有默认值的位置参数: 2
# 数量不确定的位置参数: (3, 4, 5)
# 无默认值的关键字参数: 2
# 有默认值的关键字参数: 24
# 其他关键字参数: {'name': 'zhouyi', 'age': 18}

# check_function_args(1, 2, 3, 4, 5, name="zhouyi", 6)
# SyntaxError: positional argument follows keyword argument

# 函数定义中不包含**kwargs
# TypeError: check_function_args() got an unexpected keyword argument 'name'