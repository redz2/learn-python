import threading
import time


def sample_job_every_5s():
    print("5s thread: ",threading.current_thread())
    
def sample_job_every_10s():
    print("10s thread: ",threading.current_thread())

timers = [
    threading.Timer(5, sample_job_every_5s),
    threading.Timer(10, sample_job_every_10s)
]

# 基于多线程
for timer in timers:
    timer.start()

while True:
    # 阻塞主线程，让其他线程执行任务
    time.sleep(3)
    print("main thread: ",threading.current_thread())