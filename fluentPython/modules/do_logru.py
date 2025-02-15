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

# 2024-09-02T14:13:19.990335+0800 - DEBUG - Debug message
# 2024-09-02T14:13:19.990536+0800 - INFO - Info message
# 2024-09-02T14:13:19.990620+0800 - WARNING - Warning message
# 2024-09-02T14:13:19.990683+0800 - ERROR - Error message
# 2024-09-02T14:13:19.990745+0800 - CRITICAL - Critical message


                        