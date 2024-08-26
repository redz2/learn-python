import subprocess

# 创建子进程
proc = subprocess.Popen(
    ["echo", "hello world"],
    stdout=subprocess.PIPE
)
# 运行子进程
out, err = proc.communicate()
print(out.decode("UTF-8"))


# 先不看了，有空再看subprocess模块