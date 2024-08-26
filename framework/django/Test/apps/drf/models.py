from django.db import models

# Create your models here.

class Student(models.Model):

    """学生信息"""
    name = models.CharField(max_length=255, verbose_name="姓名")
    sex = models.BooleanField(default=True, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    classmate = models.CharField(db_column="class", max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="个性签名")

    class Meta:
        db_table = "drf_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "classmate": self.classmate,
            "description": self.description
        })

    def to_dict(self):
        return {
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "classmate": self.classmate,
            "description": self.description
        }

        
