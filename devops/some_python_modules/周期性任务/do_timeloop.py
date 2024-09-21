import time
from timeloop import Timeloop
from datetime import timedelta
import threading

tl = Timeloop()

@tl.job(interval=timedelta(seconds=2))
def sample_job_every_2s():
    # print("2s job current time : {}".format(time.ctime()))
    print("2s thread: ",threading.current_thread())
    # 2s thread:  <Job(Thread-1, started daemon 6114439168)>
    
@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    # print("5s job current time : {}".format(time.ctime()))
    print("5s thread: ",threading.current_thread())
    # 5s thread:  <Job(Thread-2, started daemon 6131265536)>
    
@tl.job(interval=timedelta(seconds=10))
def sample_job_every_10s():
    # print("10s job current time : {}".format(time.ctime()))
    print("10s thread: ",threading.current_thread())
    # 10s thread:  <Job(Thread-3, started daemon 6148091904)>

# 启动定时器(每个任务都在独立的线程中执行)
tl.start()

while True:
    # 阻塞主线程，让其他线程执行任务
    time.sleep(2)
    print("main thread: ",threading.current_thread())

# 关闭定时器
tl.stop()

