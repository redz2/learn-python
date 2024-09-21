from collections import deque

# 双向队列: 线程安全，可以快速从两端添加或删除元素
dq = deque(range(10), maxlen=10)

dq.rotate(3)

dq.appendleft(1)
dq.extendleft([1,2,3])

dq.append(2)
dq.extend([1,2,3])




from multiprocessing import Queue as m_q
from asyncio import Queue as a_q
import heapq
import queue # 队列满员时，会被锁住

