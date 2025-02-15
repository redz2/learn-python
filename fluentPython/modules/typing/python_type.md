1. simple types
* int
* float
* bool
* bytes

2. generic types(通用类型)
```
from typing import Dict, List, Set, Tuple, Union, Optiona
```
* dict
* list
* set
* tuple

3. Annotated
* 添加一些额外的metadata
```
from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```

4. 优势
* 编辑器支持
* 类型提示

5. 强类型 vs 弱类型
* 如果一门语言很少隐式转换类型，说明它是强类型，竟然把python认为是强类型语言

6. 静态类型 vs 动态类型
* 编译时检查类型的语言是静态类型
* 运行时检查类型的语言是动态类型
