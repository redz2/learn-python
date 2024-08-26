import time
from celery import shared_task

from .celery import app

"""
如何执行异步任务？
tasks.test.delay()
"""
@shared_task
def test():
    time.sleep(5)
    print("执行异步任务")

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

import this