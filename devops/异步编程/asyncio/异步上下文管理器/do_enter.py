import time

class ContextManager:
    def __init__(self):
        self.conn = None

    def action(self):
        return self.conn

    def __enter__(self):
        # 链接数据库
        time.sleep(1)
        self.conn = "OK"
        return self

    def __exit__(self, exc_type, exc, tb):
        # 关闭数据库链接
        self.conn = "CLOSE"


def main():
    with ContextManager() as cm:
        result = cm.action()
        print(result)


main()