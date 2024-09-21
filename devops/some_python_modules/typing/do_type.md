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
