from httpRequest import *

# 登录请求
url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res = httpRequest.request(url=url, json=data)

assert res.status_code == 200
assert res.json()['code'] == 1
print('登录成功')

# 获取token
user_token = res.json()['data'][0]['token']

# 第二个请求
# 构造请求
url = 'http://43.138.178.63:81/haimo/sass/systemUser/getSystemUser'
header = {'token': user_token}  # 关联
res= httpRequest.request(url=url, headers=header)  # headers=header2, 把请求头带给接口
# 判断结果
assert res.status_code == 200  
assert res.json()['code'] == 1
print('获取系统用户接口正常')

