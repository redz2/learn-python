import datetime
import time

def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
    
def loop_monitor():
    while True:
        time_printer()
        # 暂停：；令主线程进入阻塞状态
        time.sleep(5) 
        
if __name__ == "__main__":
    loop_monitor()