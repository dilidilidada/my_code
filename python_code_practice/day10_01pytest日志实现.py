# 日志: 
# 记录接口运行的状态
# 出现异常后根据日志找出对应的原因
# logging: py自带包
# loguru: 三方包

from datetime import datetime

time = datetime.now()
print(time, type(time))

# 时间格式化
time1 = time.strftime('%Y%m%d%H%m')
time2 = time.strftime('%Y-%m-%d %H:%m')
print(time1, '\n', time2)


