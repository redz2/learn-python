# Python3.7+

harden_v1 = ('James Harden', 1, 'PG', 34)

from collections import namedtuple
Player = namedtuple('Player', ['name', 'number', 'field', 'age'])
harden_v2 = Player('James Harden', 1, 'PG', 34)

# what is dataclass? 
# dataclass is a decorator that generates a class with a default __init__ method, __repr__ method, and other useful features.

from dataclasses import dataclass
from typing import Optional

@dataclass
class PlayerV2():
    name: str
    number: Optional[int] = None
    field: Optional[str] = None
    age: Optional[int] = None
    
zy = PlayerV2(name="zy", age=30)    