"""fork()调用一次，返回两次，操作系统会自动把当前进程复制一份，分别在父进程和子进程内返回
"""

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
# 子进程也会执行一次
print("executing now")

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))