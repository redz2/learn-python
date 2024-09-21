# 
from typing import List, Tuple, Union, Optional, TypeVar, Callable, Sequence, Generator
# typing模块为代码提供静态类型注解的能力

# 类型别名
def process_numbers(numbers: List[int]) -> Optional[int]:
    pass

# Union类型
def double_or_square(number: Union[int, float]) -> Optional[int]:
    pass

# Optional类型：表示参数可以是指定类型或None
def greet(name: Optional[str]) -> Optional[str]:
    pass

# TypeVar：泛型
T = TypeVar('T') # 可以是任何类型
INT_OR_FLOAT = TypeVar("INT_OR_FLOAT", int, float) # 必须是int或者float
def get_first_element(items: List[T]) -> Optional[T]:
    pass

# 把动态类型语言写成静态类型语言的样子
def apply_function(
    f: Callable[[int, int], int],
    l: Sequence[int]
) -> Optional[List[int]]:
    pass


def generate_numbers(n: int) -> Optional[Generator[int, None, None]]:
    ...
    
    
if __name__ == "__main__":
    # This is how you declare the type of a variable
    age: int = 1

    # You don't need to initialize a variable to annotate it
    a: int  # Ok (no value at runtime until assigned)
    
    # Doing so can be useful in conditional branches
    child: bool
    if age < 18:
        child = True
    else:
        child = False
        
