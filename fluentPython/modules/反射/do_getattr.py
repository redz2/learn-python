import my_module

myfunc = getattr(my_module, "my_function")
mycls = getattr(my_module, "MyClass")

myfunc()
instance = mycls("ok")

# django框架中根据请求方法来执行不同的方法
# 通过字符串来调用方法
method = getattr(instance, "display_value") # 等价于 instance.display_value
print(getattr(instance, "display_value") == instance.display_value)

print(type(instance.display_value)) # <class 'method'>
print(id(instance.display_value)) # 4336532736
print(type(method)) # <class 'method'>
method() # self是何时传入的？

hasattr(my_module, "my_function")
setattr(my_module, "new_var", "NewVar")
print(getattr(my_module, "new_var"))
delattr(my_module, "new_var")

