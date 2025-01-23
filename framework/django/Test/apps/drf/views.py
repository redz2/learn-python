# Create your views here.


# 创建Serializer对象
# 序列化器(instance=None, data=empty, many=False, context=None, **kwargs)

# 1. 序列化（读取数据）: instance = models.Model对象 -> stu = StudentSerializer(instance=stu_obj)
# 2. 反序列化（写入数据）: data = JSON字符串 
# 3. 当instance是一个QuerySet时，需要声明many=True -> stu = StudentSerializer(instance=stu_list, many=True)
# 4. 传递数据到序列化器中: -> stu = StudentSerializer(instance=stu_obj, context={"name": "zhouyi"})

from django.http.response import HttpResponse,JsonResponse
from django.views import View
from apps.drf.models import Student
from apps.drf.serializers import StudentSerializer


class StudentsView(View):

    def get(self, request):

        """序列化器的基本使用"""
        
        # 没有序列化器时，数据写入是在视图函数中实现的，现在是在序列化器中实现的

        # 读取数据（流程比较简单）
        
        # 序列化单个模型对象: obj -> {} -> json
        # student_obj = Student.objects.first()
        # student_serializer = StudentSerializer(instance=student_obj)
        # return JsonResponse(student_serializer.data)
        
        # 序列化多个模型对象: QuerySet[obj, obj] -> [{},{}] -> unsafe json
        # student_list = Student.objects.all()
        # student_list_serializer = StudentSerializer(instance=student_list, many=True)
        # return JsonResponse(student_list_serializer.data, safe=False)


        # 写入数据（比较麻烦，需要校验数据）
        
        # 反序列化
        # json ---> {} ---> serializer ---> is_valid() ---> validated_data ---> obj
        
        # 1. 模拟客户端提交数据，validate执行顺序和这里的顺序有关
        stu_object = Student.objects.get(pk=9)
        
        data = {
            "name": "zxx",
            "sex": False,
            "age": 20,
            "classmate": 101,
            "description": "son"
        }
        
        # 2. 实例化serializer对象
        ser = StudentSerializer(instance=stu_object, data=data)
        
        # 3. 数据格式校验
        # is_valid = ser.is_valid() # 验证失败不会抛出异常 True or False
        # if is_valid:
        #     print("验证通过")
        # else:
        #     print("验证失败")
        #     print(ser.errors)
        #     print(ser.error_messages)
        ser.is_valid(raise_exception=True) # 会抛出异常，工作中常用
        # 4. 写入数据
        ser.save()
        return JsonResponse(ser.data)




    
