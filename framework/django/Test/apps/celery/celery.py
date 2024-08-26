from celery import Celery
import os

"""
1. 定义celery配置
    * broker
    * backend
    * tasks
2. 启动celery进程
3. 感觉更适合处理异步任务，周期性任务不太适合
"""

# 如何启动celery worker？
# celery -A lijobs worker -l INFO -c 控制并发数

# 如何启动celery beat？
# celery -A lijobs beat -l INFO 

# 运行在后台
# celery multi start w1 -A proj -l INFO
# celery multi restart w1 -A proj -l INFO


broker='redis://127.0.0.1:6379/0'
backend='redis://127.0.0.1:6379/1'

# 通过celery-worker监听broker中的任务
app = Celery('lijobs', 
            broker=broker, 
            backend=backend, 
            # 注册任务
            include=['lijobs.tasks']
        )

# Optional configuration, see the application user guide.
app.conf.update(
    # 时区
    timezone='Asia/Shanghai',
    # 是否使用UTC
    use_UTC=False,
    # 任务结果过期时间
    result_expires=3600,
    broker_connection_retry_on_startup=True,
)

# 通过celery-beat周期性地添加任务到broker中
app.conf.beat_schedule = {
    'hello-every-3-seconds0': {
        'task': 'lijobs.tasks.test',
        'schedule': 3.0,
    },
    'hello-every-3-seconds1': {
        'task': 'lijobs.tasks.test',
        'schedule': 3.0,
    },
    'hello-every-3-seconds2': {
        'task': 'lijobs.tasks.test',
        'schedule': 3.0,
    },
}
    
