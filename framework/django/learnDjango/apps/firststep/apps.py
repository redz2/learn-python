from django.apps import AppConfig


class FirststepConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 多app放在一个目录下，需要加上目录名
    name = 'apps.firststep'
