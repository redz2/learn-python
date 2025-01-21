import logging

# 创建Logger对象
logger = logging.getLogger(__name__)
# 设置标准日志等级
logger.setLevel(logging.DEBUG)

# 创建FileHandler对象，将日志写入文件
file_handler = logging.FileHandler('test.log', mode='w')
# 设置文件中写入的日志等级
file_handler.setLevel(logging.DEBUG)

# 创建StreamHandler对象，将日志输出到控制台
stream_handler = logging.StreamHandler()
# 设置控制台显示的日志等级
stream_handler.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将处理器添加到Logger对象中（注册）
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# 记录日志信息
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')