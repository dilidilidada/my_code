from loguru import *

# 日志级别
logger.info('123')  # 显示信息: 登录接口, 参数
logger.debug('123')  # 调试信息
logger.warning('123') # 警告, 比较重要的提示信息
logger.error('123')  # 错误信息: bug, 异常信息

# 日志保存
# encoding='utf-8': 支持中文, 防止乱码
logger.add('./prictice_code/log_add_test.log', encoding='utf-8')  # 文件路径

logger.info('信息')  
logger.debug('调试')  
logger.warning('警告') 
logger.error('错误')
