from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) # 创建进程对象
    print('Child process will start.')
    p.start()
    p.join() # 等待子进程结束后继续执行，通常用于进程间同步
    print('Child process end.')