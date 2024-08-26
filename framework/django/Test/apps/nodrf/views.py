"""
POST /students/        添加一个学生信息
GET /students/         获取所有学生信息

GET /students/<pk>/    获取一个学生信息
PUT /students/<pk>/    更新一个学生信息
DELETE /students/<pk>/ 删除一个学生信息
"""

from django.views import View
from django.http.response import JsonResponse
from apps.nodrf.models import Student
import json


# 视图类
class Students(View):
    def get(self, request):
        """获取所有学生信息"""
        try:
            # 为什么要用values()
            students_list = Student.objects.values() # -> QuerySet[{},{}]
            # 如果是列表需要添加safe=False，如果是字典就不需要添加
            return JsonResponse({
                "data": list(students_list)
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "error": e
            }, status = 400)


    def post(self, request):
        """添加一个学生信息"""
        try:
            data = json.loads(request.body)
            # object
            student = Student.objects.create(
                name = data.get("name"),
                sex = data.get("sex"),
                age = data.get("age"),
                classmate = data.get("classmate"),
                description = data.get("description")
            )
            return JsonResponse(student.to_dict(), status=200)
        except Exception as e:
            return JsonResponse({
                "error": e
            }, status = 400)

class StudentsInfoView(View):

    def get(self, request, pk):
        # obj
        try:
            student = Student.objects.get(pk=pk) # -> obj
            return JsonResponse(student.to_dict())
        except Student.DoesNotExist:
            return JsonResponse({"error": "当前学生ID不存在"}, status=400)
        

    def put(self, request, pk):
        """
        修改一个学生的信息
        """
        try:
            student = Student.objects.get(pk=pk) # -> obj
        except:
            return JsonResponse({"error": "当前学生ID不存在"}, status=400)

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erros": "提交数据错误"}, status=400)

        try:
            student.name = data.get("name")
            student.age = data.get("age")
            student.sex = data.get("sex")
            student.classmate = data.get("classmate")
            student.description = data.get("description")
            student.save()
            return JsonResponse(student.to_dict())
        except:
            return JsonResponse({"erros": "提交数据错误"}, status=400)

    def delete(self, request, pk):
        """删除一个学生的信息"""
        try:
            Student.objects.filter(pk=pk).delete()
            return JsonResponse({"message": "删除成功"})
        except Exception as e:
            return JsonResponse({"erros": f"删除错误 {e}"}, status=400)
