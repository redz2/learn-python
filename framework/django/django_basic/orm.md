# ORM
***
* 主要描述如何连接数据库创建表？表结构有哪些常见字段？表与表之间有几种关系？如何创建多数据库？
***

* 本质: 将对象操作 __翻译__ 为 SQL语句
    * 类 -> 表结构
    * 对象 -> 记录
```python
class UserInfo(models.Model):
    # 名称不要使用拼音
    name = models.CharField(verbose_name="姓名",max_length=16) # 变量名是小写 + 下划线
    age = models.IntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=128, unique=True, null=True)
    amount = models.DecimalField(verbose_name="余额", max_digits=5, decimal_places=2, null=True)
    depart = models.ForeignKey(to="Department", verbose_name="部门", on_delete=models.CASCADE, null=True, related_name="d1") # 默认使用id做关联，to_field="id"

    class Meta:
        # 默认表名: appname_userinfo
        db_table = "自定义表名"
        # 联合索引
        index_togerther = [("name", "age"),]
        # 联合唯一索引
        unique_together = (("name", "age"),)
        # admin中显示的表名称
        verbose_name = "单数名称"
        verbose_name_plural = "复数名称"
```

* 表结构常见字段和参数
```python
# 字符串
CharField(verbose_name="城市", max_length="16", 
                        default="默认值",            # 默认值
                        null=True,                  # 数据库是否可以为空
                        blank=True,                 # 管理页面数据是否可以为空
                        db_index=True,              # 该字段添加索引，查询速度快
                        unique=True,                # 唯一约束
                        choices=(
                            ("sh","上海"), 
                            ("bj","北京")
                        )) # 数据库中只能存储sh和bj，页面上显示上海和北京
# IntergerField: 整型（SmallIntegerField、BigIntegerField、PositiveSmallIntegerField、PositiveIntegerField）
DateField(verbose_name="注册时间", auto_now=True)  # 不写就添加当前时间
# DateTimeField: 时间
# BooleanField: 布尔 -> SmallIntegerField
DecimalField(verbose_name="余额", max_digits=10, decimal_places=2)  # 精确的小数
```

* 表关系（自己画一个结构图）
    * 单表
    * 一对多
        * 每个部门包含多个用户
        * 每个用户属于一个部门（多个用户能在一个部门中，用户中需要有外键，每个用户都可以在一个部门中）
        * 如果一个用户可以属于多个部门，一个部门也可以包含多个用户，那就是多对多的关系
    * 多对多
    ```python
    # 第三张关系表: 除了id、bid、gid，还能自己添加其他字段
    class BoyAndGirl(model.Model):
        gid = models.ForeignKey(to="Girl",to_field="id")
        bid = models.ForeignKey(to="Boy",to_field="id")

    # 或者在其中一个类中添加，会自动创建第三张表，但只有id、bid、gid三个字段，推荐使用上面的方式创建
    # relation = models.ManyToManyField(verbose_name="关系表", to="Girl")
    ```
    * 一对一
        * 字段太多，将单表拆分成多个表（100列的一张表拆分成2张50列的表）
        * 本质: 
        ```py
        class Blog(models.Model):
            user = models.OneToOneField(to="UserInfo")
            # user = models.ForeignKey(to="UserInfo", unique=True)
        ```

***
***

* 编写ORM的步骤
1. settings.py连接数据库
2. settings.py注册app
3. 编写models类
4. 执行命令
```bash
python3 manage.py makemigrations # 会找到所有已注册app中的models.py生成数据库操作的配置文件（就是创建表的sql语句）
                                    # 注意: 千万不要手动修改数据库的表结构
python3 manage.py migrate        # 连接到数据库运行sql语句
python3 manage.py migrate --fake <app name> zero # 如何清理migrations表？
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 默认：文件类数据库
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 如何连接mysql
import pymysql # 只提供了引擎，如果要连接数据库还需要安装第三方库
               # mysqlclient
pymysql.install_as_MySQLdb() # 默认使用MySQLdb

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxxxxxx',  # 数据库名字，和sqlite3不同，需要提前手动创建数据库
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST': '127.0.0.1', # ip
        'PORT': 3306
    }
}

# 为什么需要连接池？避免重复创建连接，关闭连接，减少性能损耗
# django默认没有数据库连接池的功能
# DBUtils ---> 连接池 pip3 install django-db-connection-pool，此库底层使用SQLAchemy来创建连接池
DATABASES = {
    "bak":{
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'xxx',
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST':'xxx', 
        'PORT': 3306,
        'POOL OPTIONS': {
            'POOL_SIZE': 10, # 连接数量
            'MAX_OVERFLOW': 10, # 在最小的基础上,还可以增加10个,即:最大20个。
            'RECYCLE': 24 * 60, # 连接可以被重复用多久,超过会重新创建,-1表示永久。
            'TIMEOUT': 30, # 池中没有连接最多等待的时间。  
        }
    }
}
```

* 多数据库场景
1. 读写分离（单app）
```bash
# 192.168.1.1 master 数据库做主从同步
# 192.168.1.2 slave
# 相同的app，连接到不同的数据库，执行初始化sql语句
python manage.py migrate app01 --database=default
python manage.py migrate app01 --database=bak # 在两个数据库中创建相同的表结构
```

```py
# 在 utils/dbrouter.py 中编写router类
# 在 settings 中配置router类
DATABASE_ROUTERS = ["apps.utils.dbrouter.DemoRouter"]

"""
编写router类，
1. 单app读写分离
2. 多app分库（按照app区分: model._meta.app_label）
3. 单app分库（按照表名区分: model._meta.mode_name）
    * 注意: 一定不要跨库做关联，数据库支持，但是django不支持
"""
class DemoRouter(object):
    # 读操作
    def db_for_read(self, model, **hints): 
        # 多app如何使用不同的数据库？
        # if model._meta.app_label == "app01":
        #     return 'bak01'
        # if model._meta.app_label == "app01":
        #     return 'bak02'
        return "bak"
    
    # 写操作
    def db_for_write(self, model, **hints): # 返回数据库连接，默认使用default
        return "default" 

    # 执行 python manage.py migrate 会执行，默认返回true
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # 如果一个app有100张表，如何控制其中50张表放在default中，另外50张表放在bak中？
        if db == 'default':
            if model_name in ['role']: # 哪些表放default
                return True
            else:
                return False
        
        if db == 'bak':
            if model_name in ['users']: # 哪些表放bak
                return True
            else:
                return False
```

2. 分库（多app）
    * 多个app，连接不同的数据库
```bash
# 如何在不同的数据库中创建不同app的表？
python manage.py migrate app01 --database=default
python manage.py migrate app02 --database=bak
```

```py
# 在视图函数中，连接数据库默认都是default，可以手动指定数据库连接
def index(request):
    models.UserInfo.objects.using("bak").create(name="zz")

# 可以在DemoRouter中，针对app返回不同的数据库连接
# 根据model._meta.app_label判断数据库属于哪个app
```