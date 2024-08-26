from django.db import models
from rest_framework import serializers

class Student(models.Model):

    """学生信息"""
    name = models.CharField(max_length=255, verbose_name="姓名")
    sex = models.BooleanField(default=True, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    classmate = models.CharField(db_column="class", max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="个性签名")

    class Meta:
        db_table = "components_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
        
        
class StudentSerializer(serializers.ModelSerializer):

    """学生信息模型类序列化器"""

    class Meta:
        
        # 导入时会把id设置为read_only
        model = Student
        fields = "__all__"
        
        # 和字段声明里的写法做下对比
        extra_kwargs = {
            "name": {
                "max_length": 10,
                "error_messages": {
                    "max_length": "你太长了"
                }
            }
        }
        
        # ModelSerializer内置了update和create方法
        
        # 如果POST提交的数据，部分数据不需要存入数据库怎么办？
        # 是不是重写validate()方法就可以
        
        