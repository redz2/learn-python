# pydantic
* pydantic会对类型做自动转换，无法识别的值或转换失败会抛出ValidationError

## 类型说明
```
typing.Any 任何类型，包括None
typing.TypeVar 泛型
    T = TypeVar("T", int, float) # 定义类型T，必须是int或者float
typing.Optional[T] === typing.Union(T, None)
typing.Pattern

```