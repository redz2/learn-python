import importlib

module_name = "do_getattr"
# 等价于import do_getattr
# 但是带来了灵活性，可以在代码执行过程中动态导入模块了
module = importlib.import_module(module_name) 


