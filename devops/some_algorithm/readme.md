1. 时间复杂度（这是一个大概的时间）
```
O(1)
print("hello world")

O(n)
for i in range(n):
    print("hello world")

O(n^2)
for i in range(n):
    for j in range(n):
        print("hello world")

O(n^3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            print("hello world")

O(n^2)
for i in range(n):
    print("hello world")
    for j in range(n):
        print("hello world")

O(logn)  循环减半，规模减小一半
while n > 2:
    print(n)
    n = n / 2
```