# Python3.7+

harden_v1 = ('James Harden', 1, 'PG', 34)

from collections import namedtuple
Player = namedtuple('Player', ['name', 'number', 'field', 'age'])
harden_v2 = Player('James Harden', 1, 'PG', 34)


from dataclasses import dataclass
from typing import Optional

# 帮你定义__init__，__repr__
@dataclass
class PlayerV2():
    name: str
    number: Optional[int] = None
    field: Optional[str] = None
    age: Optional[int] = None
    
zy = PlayerV2(name="zy", age=30)
print(zy)
    