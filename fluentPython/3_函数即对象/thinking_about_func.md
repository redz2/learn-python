# thinking in functions

- some principles to consider when designing functions
  1. do not repeat yourself (DRY)
  2. use default arguments to simplify the interface
  3. use keyword arguments to make the code more readable
  4. use docstrings to explain the purpose of the function and its arguments
  5. use assertions to check the input and output of the function
  6. use generators to lazily compute results
  7. use decorators to modify the behavior of a function
  8. use context managers to handle resources
  9. use multiple dispatch to handle different types of arguments

# Effective Python

- 尽量用异常来表示特殊情况，而不是返回 None

```python
# 一般通过异常来判断是否有异常
def divide(a, b):
    if b == 0:
        raise ValueError('division by zero')
    return a / b
```

```go
// 一般通过error来判断是否有异常
func divide(a, b int) (int, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
```

- 考虑使用生成器来改写直接返回列表的函数

```python
# 返回字符串中每个单词的首字母的位置
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter =='':
            result.append(index + 1)
    return result

def index_words_gen(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter =='':
            yield index + 1
```

- emuerate: 将迭代器包装成生成器

```python
# 枚举函数
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```

- 使用 None 来描述具有动态默认值的参数
  - 参数的默认值，不要使用可变数据类型，如列表、字典等（保持函数的不可变性）

```python
# when只在函数定义时执行一次
def log_not_good(message, when=datetime.now()):
    print(f"{when}: {message}")

def log(messsage, when=None):
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")
```

- 为什么我之前没有体会到函数的不可变性？
  - 因为 python 函数参数是引用传递的，所以就有可能会改变原来的对象
  - 确保函数不修改输入参数，可以让函数的行为更加可预测
