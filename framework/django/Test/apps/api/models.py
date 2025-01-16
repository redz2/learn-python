from django.db import models

class UserInfo(models.Model):


    # 类属性
    # id = models.BigAutoField()
    name = models.CharField(verbose_name="姓名",max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=128, unique=True, null=True)
    amount = models.DecimalField(verbose_name="余额", max_digits=5, decimal_places=2, null=True)
    depart = models.ForeignKey(to="Department", verbose_name="部门", on_delete=models.CASCADE, null=True, related_name="d1")

class Goods(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    detail = models.CharField(verbose_name="详细信息", max_length=128)


class Department(models.Model):
    title = models.CharField(verbose_name="部门名称", max_length=32)
    


