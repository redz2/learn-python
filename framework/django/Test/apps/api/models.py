from django.db import models

# Create your models here.

# ORM
# 类 ---> SQL ---> 表结构（创建表、修改表、删除表）
# 对象 ---> SQL ---> 数据

# python3 manage.py makemigrations 生成配置文件（创建表的sql语句） # 注意: 不要手动修改数据库的表结构
# python3 manage.py migrate 读取每个注册的app的migrations，将配置文件转换成sql语句（用于生成表，更新表），连接到数据库运行sql语句
# 如何清理migrations表？python3 manage.py migrate --fake <app name> zero

# 常见字段和常见参数
# CharField(default="默认值",null=True,blank=True,\ 是否可以为空
#                           db_index=True,unique=True,\ 添加索引，经常查询，速度快；唯一索引
#                           choices=(("sh","上海"),("bj","北京"))) 数据库中只能存储sh和bj，页面上显示上海和北京
# PositiveIntegerField
# PositiveSmallIntegerField
# SmallIntegerField
# IntergerField 和 CharField参数基本一致
# BigIntegerField
# DateField(verbose_name="注册时间", auto_now=True) 不写就添加当前时间
# DateTimeField
# BooleanField
# DecimalField(verbose_name="余额", max_digits=10, decimal_places=2) 精确的小数

# 表结构关系
# 1. 单表
# 2. 一对多
    # 部门表
    # 用户表
    # depart = models.ForeignKey(verbose_name="部门id", to="Department", to_field="id", on_delete=models.CASCADE|SET_NULL|SET_DEFAULT)
# 3. 多对多
    # 男生表
    # 女生表
    # 需要第三张关系表: id boy_id girl_id（推荐使用这种方式，而不是ManyToManyField）
    # class BoyAndGirl(model.Model):
    #     gid = models.ForeignKey(to="Girl",to_field="id")
    #     bid = models.ForeignKey(to="Boy",to_field="id")
    # 简便写法: 在Boy或Girl任意一个中写上，缺点只能有三个字段，不能添加其他字段
    # 数据库中列名：relation_id
    # relation = models.ManyToManyField(to="Boy",verbose_name="男女关系")
# 4. 一对一: 分表
    # 一个表有100列
    # 拆分成2个50列的表
    # models.OneToOneField === 外键 + 唯一

# 类名：大驼峰
class UserInfo(models.Model):

    # 默认表名: api_userinfo（）

    # 类属性
    # id = models.BigAutoField()
    # 变量名：小写 or 下划线
    name = models.CharField(verbose_name="姓名",max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=128, unique=True, null=True)
    amount = models.DecimalField(verbose_name="余额", max_digits=5, decimal_places=2, null=True)
    depart = models.ForeignKey(to="Department", verbose_name="部门", on_delete=models.CASCADE, null=True, related_name="d1")

    # class Meta:
    #     db_table = "自定义表名"
    #     联合唯一索引
    #     index_togerther = [
    #     ("name", "age") 
    # ]

class Goods(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    detail = models.CharField(verbose_name="详细信息", max_length=128)


class Department(models.Model):
    title = models.CharField(verbose_name="部门名称", max_length=32)
    

# 数据操作
# 详见view.py


# 多数据库场景（目前我用不上）
# 注意：一定不要跨库做外键，django不支持，尽可能把有关联的表放在一个库

# 场景一：读写分离
# 初始化时只需要连接一个数据库
# 根据读写连接不同的数据库

# 场景二：分库（多app）
# 不同的app，连接到不同的数据库，执行初始化sql语句（创建表）
# python manage.py migrate app01 --database=default
# python manage.py migrate app02 --database=bak
# 视图函数中，连接数据库，默认都是default，如何知道连接哪个数据库进行操作呢？根据model._meta.app_label判断数据库属于哪个app

# 场景三：分库（单app）
# 命令行不支持，需要使用dbrouter中的allow_migrate，尽量使用场景二


# python manage.py shell 
