# 全局解释器锁并不会保护程序员自己写的代码
# 一个线程操作某一数据操作到一半，可能另外一个线程会打断并开始执行

# 互斥锁
from threading import Lock

class LockingCounter(object): 
    def init (self):
        self.lock = Lock () 
        self.count = 0
    def increment (self, offset):
        # 如何让一个操作变成原子操作 
        with self.lock:
            # 看上去是原子操作，实际上python会分成3步
            self.count += offset 