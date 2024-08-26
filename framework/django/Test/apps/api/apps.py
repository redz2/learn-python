from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 因为在项目根目录创建子应用后，移动到了apps文件夹，需要把name从api修改为apps.api
    name = 'apps.api'
    
    # 当django应用就绪时，执行下面的代码
    def ready(self):
        pass
