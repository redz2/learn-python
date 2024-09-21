# import知识点
1. 中文名称的目录import有问题（所以我改成XXX,YYY,ZZZ了）
2. 如何对所有符号的导入精确控制
* from module import * 
    * 虽然强烈反对，定义大量符号的模块中，还是需要使用
* __all__ = ["spam", "grok"]   
    * 只有显式列出的符号才会被导出
3. 当一个模块被导入时，模块中的代码会被执行
* 然而，模块中的代码只会在第一次导入时执行一次，如果再次导入同一个模块，python解释器会直接加载已经加载的模块，不会再次执行模块中的代码
4. import: 导入模块和模块中定义的变量，函数，类
    1. 导入模块: import math
    2. 导入模块中特定内容: from module import name
    3. 给导入的模块或内容起别名: import module as alias 或 from module import name as alias
    4. 导入模块中的所有内容: from module import * （不建议这么做，命名可能冲突）
    5. 千万不要导入一个包，没法用！！！import package 
5. 关于相对导入
* 只能在包中使用，顶层脚本中不识别，可以参考test2.py
* https://stackoverflow.com/questions/16981921/relative-imports-in-python-3