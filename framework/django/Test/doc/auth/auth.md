# 什么是认证？

1. Django自带认证功能auth模块和User对象的基本操作
    * https://www.cnblogs.com/wcwnina/p/9246228.html
    * auth.authenticate(username, password) -> User or None (账号密码是否正确？)
    * 如何重写authenticate方法？可以自己定义登录时应该如何验证
```
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

# 继承ModelBackend类，重写authenticate()方法
class CustomBackend(ModelBackend):

    """
    自定义用户验证后端：支持用户名或邮箱登录。
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# settings.py添加配置
AUTHENTICATION_BACKENDS = ['yourfilepath.CustomBackend'] 
```
    * session框架
        * login(request, user)
        * logout(request) 
    * user.is_authenticated() -> True or False
    * User.object.create_user
    * check_password(password) # 检查密码
    * auth.hashers.make_password(password) # 修改密码
    * 自定义auth User模型
```
from django.contrib.auth.models import AbstractUser

# 继承AbstractUser类
class UserInfo(AbstractUser):　　　　
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    
    def __str__(self):
        return self.username

# settings.py中添加配置
AUTH_USER_MODEL = "app名.UserInfo"
```
