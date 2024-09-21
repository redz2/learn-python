import datetime
import time
import sched
import threading

def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
    print("printer1: ",threading.current_thread())
    loop_monitor() # 递归
    
def time_printer2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
    print("printer2: ",threading.current_thread())
    loop_monitor() # 递归
    
def loop_monitor():
    s = sched.scheduler(time.time, time.sleep)  # 生成调度器
    s.enter(5, 1, time_printer, ())
    # s.enter(5, 1, time_printer2, ()) # 不会执行
    s.run()

    
if __name__ == "__main__":
    """sched并没有多线程，一直在主线程中执行，感觉不好用"""
    loop_monitor()