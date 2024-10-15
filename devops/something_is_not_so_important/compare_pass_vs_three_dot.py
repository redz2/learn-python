"""
... 和 pass 不会执行任何操作，通常情况下，...可以取代pass
... 在@overload中经常使用
"""

@overload
def add(a: int, b: int) -> int:
    ...
    
def add(a, b):
    return a + b