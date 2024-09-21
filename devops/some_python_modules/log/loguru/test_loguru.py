from loguru import logger
import sys

# 设置日志输出格式
logger.add('test.log', rotation="100 MB", format='{time} - {level} - {message}')

# 记录日志信息
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

                        