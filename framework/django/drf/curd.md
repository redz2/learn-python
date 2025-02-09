# 如何实现增删改查？
1. 使用django
```py
# models.py
class Student(models.Model):

    """学生信息"""
    name = models.CharField(verbose_name="姓名", max_length=255)
    sex = models.BooleanField(verbose_name="性别", default=True)
    age = models.IntegerField(verbose_name="年龄")
    classmate = models.CharField(verbose_name="班级编号", db_column="class", max_length=5)
    description = models.TextField(verbose_name="个性签名", max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "student"
        verbose_name = "学生" # 单数
        verbose_name_plural = verbose_name # 复数

    def __str__(self):
        return str({
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "classmate": self.classmate,
            "description": self.description
        })

# views.py
"""
POST /students/        添加一个学生信息
GET /students/         获取所有学生信息

GET /students/<pk>/    获取一个学生信息
PUT /students/<pk>/    更新一个学生信息
DELETE /students/<pk>/ 删除一个学生信息
"""
urlpatterns = [
    path('students/', Students.as_view()),
    path('students/<int:pk>/', StudentsInfoView.as_view()), 
]

class Students():
    def get(self, request):
        try:
            students_qs = models.Students.objects.all().values()
            return JsonResponse({
                "data": list(students_qs)
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "error": e
            }, status=400)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            models.Students.objects.create(
                name=data.get("name"),
                sex=data.get("sex"),
                age=data.get("age"),
                classmate=data.get("classmate"),
                description=data.get("description")
            )
            return JsonResponse({
                "message": "添加成功"
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "error": e
            }, status=400)

class StudentsInfoView():
    def get(self, request, pk):
        try:
            student = models.Students.objects.get(pk=pk)
            return JsonResponse({
                "data": {
                    "name": student.name,
                    "sex": student.sex,
                    "age": student.age,
                    "classmate": student.classmate,
                    "description": student.description
                }
            })
        except models.Students.DoesNotExist:
            return JsonResponse({                
                "error": "学生不存在"
            }, status=404)
    
    def put(self, request, pk):
        try:
            data = json.loads(request.body)
            student = models.Students.objects.get(pk=pk)
            student.name = data.get("name")
            student.sex = data.get("sex")
            student.age = data.get("age")
            student.classmate = data.get("classmate")
            student.description = data.get("description")
            student.save()
            return JsonResponse({
                "message": "更新成功"                
            }, status=200)
        except models.Students.DoesNotExist:
            return JsonResponse({                
                "error": "学生不存在"
            }, status=404)
        
        def delete(self, request, pk):
            try:
                student = models.Students.objects.get(pk=pk)
                student.delete()
                return JsonResponse({
                    "message": "删除成功"
                }, status=200)
            except models.Students.DoesNotExist:
                return JsonResponse({                
                    "error": "学生不存在"
                }, status=404)
```

2. 使用drf
    * 序列化器: ModelSerializer
    * 视图集: ModelViewSet
```py
# views.py中如何使用序列化器对数据进行校验?
class StudentSerializer(serializers.ModelSerializer):
    # 会根据模型的字段自动生成字段
    class Meta:
        model = models.Students
        fields = "__all__"

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = StudentSerializer

# class StudentsView(View):
#     def post(self, request, pk):
#         try:
#             student = models.Students.objects.get(pk=pk)
#             # 比较表单数据和数据库数据
#             serializer = StudentSerializer(student, data=request.data, partial=True) # 部分更新
#             if serializer.is_valid(raise_exception=True): # 判断数据是否合法
#                 # 如果序列化器有instance参数，执行update操作
#                 # 如果没有，执行create操作
#                 # 可以传递额外参数，serializer.save(age=30)
#                 serializer.save() # 验证通过，保存数据
#                 return JsonResponse({
#                     "message": "更新成功"
#                 }, status=200)
#             else:
#                 return JsonResponse({
#                     "error": serializer.errors # 验证不通过，返回错误信息
#                 }, status=400)
#         except models.Students.DoesNotExist:
#             return JsonResponse({                
#                 "error": "学生不存在"
#             }, status=404)
```