"""if语句之外的else
先做这个，再做那个（按照语义，应该用then）

"""
# 仅当for循环运行完毕（未被break语句中止）才运行else
for i in range(10):
    if i < 8:
        print(i)
    else:
        break
else:
    print("for else")
    
# 仅当while循环为假值而推出（未被break语句中止）才运行else
v = 0
while v < 10:
    v += 1
    print(v)
    if v == 6:
        break
else:
    print("while else")
    
# try仅当没有异常时
try:
    # 1 / 0
    2 + 2
except:
    print("try except")
else:
    print("try else")
    
    
# 如果异常，break，continue语句导致控制权跳到了