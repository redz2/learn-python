## signals

Django包含一个“信号调度器”，帮助已解藕的应用程序在框架中的其它地方发生操作时可以得到通知
官网文档: https://docs.djangoproject.com/zh-hans/3.1/topics/signals/

1. 发送器
2. 信号
    * django.db.models.signals.pre_save & django.db.models.signals.post_save
        一个模型的 save() 方法被调用之前或之后发出
    * django.db.models.signals.pre_delete & django.db.models.signals.post_delete
        一个模型的 delete() 方法或查询结果集的 delete() 方法被调用之前或之后发出
3. 接收器

```
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished) # 接收器连接到信号
def my_callback(sender, **kwargs): # 接收器函数
    print("Request finished!")

@receiver(pre_save, sender=MyModel) # 连接到特定发送器发送的信号
def my_handler(sender, **kwargs):
    ...
```

### 定义和发送信号

何时使用信号？
信号是隐式函数调用，这使得调试更加困难。如果你的自定义信号的发送器和接收器都在你的项目内，最好使用显式函数调用。

```
import django.dispatch
pizza_done = django.dispatch.Signal()

class PizzaStore:
    def send_pizza(self, toppings, size):
        pizza_done.send(sender=self.__class__, toppings=toppings, size=size)

@receiver(pizza_done)
def my_handler(sender, **kwargs):
    ...
```
