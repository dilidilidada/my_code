# 登录的请求
# haimo登录
import requests

url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res = requests.post(url=url, json=data)

# 常用方法
# assert 1==1
# print(res.text)  # .text, 获取返回值(字符串格式)
# print(res.status_code)  # .status_code, 返回状态码
print(res.json()) # .json(), 获取返回值(字典格式)
# 断言, assert条件语句
# 断言1==1, 如果断言通过, 继续执行代码
# 如果断言失败, 代码报错, 终止运行

# 1. 断言http状态码
assert res.status_code == 200  # 接口是正常工作的

# 2. 断言结果码
assert res.json()['code'] == 1  # 接口的结果码来判断本次请求


