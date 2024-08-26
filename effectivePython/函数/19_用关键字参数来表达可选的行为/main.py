# number和divisor都是位置参数
def remainder(number, divisor):
    return number / divisor

remainder(10, 2)

# 虽然是位置参数，但可以按关键字传递
remainder(divisor=2, number=10)

# 如果是关键字参数，就只能按关键字传递

