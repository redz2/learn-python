# 元编程
* Don't repeat yourself -> 创建函数、类、包装已有的代码

1. 给函数添加一个包装
```python
def timethis(func):
    @wraps(func) # 此装饰器用来保存函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result
    return wrapper

@timethis # 当装饰器参数只有一个func
def countdown(n):
    while n > 0:
        n -= 1

origin_countdown = countdown.__wrapped__

# 编写有参数的装饰器
@logged(level=0) # 本质上就是调用logged(level=0)后会返回装饰器函数，这个装饰器函数再去包裹func
def countdown(n):
    while n > 0:
        n -= 1
```
1. 类工厂函数
* 类工厂函数 ---> 类 ---> 对象
* collections.namedtuple
```python
type(my_object) # 当成函数使用，等价于 
type(name, bases, dict) # 构造新类
```