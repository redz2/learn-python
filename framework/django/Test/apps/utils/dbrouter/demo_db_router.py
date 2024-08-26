# 多数据库，读写分离

class DemoRouter(object):
    def db_for_read(self, model, **hints):
        # print("read")
        # print(model._meta.app_label)
        # print(model._meta.model_name)
        # if model._meta.app_label == "app01":
        #     return 'app01'
        # if model._meta.app_label == "app01":
        #     return 'app02'
        return 'default'

    def db_for_write(self, model, **hints):
        # print("write")
        # print(model._meta.app_label)
        return 'default'

    # 执行 python manage.py migrate 时会执行
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if db == 'default':
    #         if model_name in ['role']:
    #             return True
    #         else:
    #             return False
        
    #     if db == 'bak':
    #         if model_name in ['users']:
    #             return True
    #         else:
    #             return False

