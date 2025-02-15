# 丰富的序列

1. 序列

   - 容器序列(可存放不同类型的 item): list, tuple, collections.deque
   - 扁平序列(可存放一种简单类型的 item): str, bytes, array.array

2. 列表推导式: 用来创建列表

```python
symbols = '$¢£¥€¤'
code = [ord(s) for s in symbols if ord(s) > 127] # python会忽略[],{},()中的换行符

code_use_filter_map = list(filter(lambda c: c > 127, map(ord, symbols)))
```

3. 生成器表达式: 逐个产出元素，而不是返回完整的列表，避免占用过多内存

```python
symbols = '$¢£¥€¤'
code = (ord(s) for s in symbols if ord(s) > 127)
```

4. 元组

   - 元组的用途
     - 作为记录，每一项对应一个字段的数据，位置决定数据意义
       - 具名元组
     ```python
     Point = namedtuple('Point', ['x', 'y'])
     p = Point(1, 2)
     x, y = p
     ```
     - 作为不可变的列表
   - 元组拆包
     ```python
     x, y = (1, 2)
     a, b, *rest = range(5) # 剩余元素用*rest表示
     s = 1, 2 # 元组的简写
     ```

5. 一个有趣的例子

```python
t = (1,2,[3,4])
t[2].append(5) # YES
t[2] += [6,7] # NO
# 增量操作不是一个原子操作，所以修改能成功，赋值会失败
# t[2] = t[2] + [6,7] 没有办法赋值
```

6. 排序

```python
list.sort(list) # 原地排序，返回 None
sorted(list) # 返回排序后的新列表
```

7. 双向队列

```python
from collections import deque

d = deque(range(10), maxlen=10)
d.rotate(3) # 向右旋转 3 步
d.appendleft(0) # 左侧添加元素
d.extendleft([1,2,3]) # 左侧添加列表
d.append(10) # 右侧添加元素
d.extend([11,12]) # 右侧添加列表
```
