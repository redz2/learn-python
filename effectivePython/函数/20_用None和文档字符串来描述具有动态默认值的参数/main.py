import datetime

# datetime.now()只在函数定义时执行一次
def log(message, when=datetime.now()):
    print("%s %s" % (when, message))
    
def log(message, when=None):
    """
    message: ...
    when: ...
    """
    when = datetime.now() if when is None else when
    print("%s %s" % (when, message))

# 参数默认值，不要使用可变数据类型
# 如果参数是可变类型，比如{},[]，默认值都要使用None，否则所有函数会共享该数据，引发奇怪的问题
def decode(data, default={}):
    pass