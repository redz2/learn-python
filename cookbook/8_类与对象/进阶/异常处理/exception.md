# 异常处理
Exception(所有异常的父类)
ZeroDivisionError
IndexError
KeyError
NameError
SyntaxError 语法错误
ValueError
OSError
KeyboardInterrupt
SystemExit
RuntimeError

## try
try:
    可能触发错误的语句
except 错误类型1:
    处理错误
except 错误类型2:
    处理错误
else:
    未发生异常执行
finally:
    无论是否发生异常都要执行

## raise
raise抛出异常：向主函数传递错误信息一层层return比较麻烦，所以人为抛出异常

不要提前处理异常，让调用者自己处理