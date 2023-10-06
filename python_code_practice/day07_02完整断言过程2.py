import random
from httpRequest import *
from mysqlTools import *

# 登录请求
login_url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
login_data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res = httpRequest.request(url=login_url, json=login_data)
assert res.status_code == 200
assert res.json()['code'] == 1
print('登录成功')

# 获取token
user_token = res.json()['data'][0]['token']

# 添加用户请求
loginAccount = 'test{}'.format(random.randint(100000,999999))

add_user_url = 'http://43.138.178.63:81/haimo/sass/systemUser/addSystemUser'
add_user_header = {'token': user_token}
add_user_data = {"loginAccount":loginAccount,"loginPassword":"e10adc3949ba59abbe56e057f20f883e","realName":"test230926","categoryId":[]}
res = httpRequest.request(url=add_user_url, headers=add_user_header, json=add_user_data)
assert res.status_code == 200
assert res.json()['code'] == 1
# 数据库校验
add_user_sql = "select * from tb_system_user where login_account='{}'".format(loginAccount)
res = mysqlTools().query(add_user_sql)
assert len(res) != 0  # 如果查询到了, 长度就不为0; 如果查不到, 接口有问题(除非延迟入库, 这种查redis)
print('添加用户{}成功'.format(add_user_data['loginAccount']))

# 删除用户请求
# 删除用户前不知道id => 数据准备
# 根据用户的账号查id
get_user_id_sql = "select id from tb_system_user where login_account='{}'".format(loginAccount)
user_id_res = mysqlTools().query(get_user_id_sql)

delete_user_url = 'http://43.138.178.63:81/haimo/sass/systemUser/deleteUser/{}'.format(user_id_res[0][0])
delete_user_header = {'token': user_token}
res = httpRequest.request(url=delete_user_url, headers=delete_user_header)

assert res.status_code == 200
assert res.json()['code'] == 1

# 数据库校验
delete_user_sql = "select * from tb_system_user where id={} and login_account='{}' and is_true=0".format(user_id_res[0][0], loginAccount)
assert len(mysqlTools().query(delete_user_sql)) != 0
print('删除用户{}成功'.format(loginAccount))

