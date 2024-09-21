"""
doctest在docstring中寻找测试用例的时候，认为>>>是一个测试用例的开始，直到遇到空行或者下一个>>>
在两个测试用例之间有其他内容的话，会被doctest忽略（可以利用这个特性为测试用例编写一些注释）
"""

def average (values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len (values)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # automatically validate the embedded tests

