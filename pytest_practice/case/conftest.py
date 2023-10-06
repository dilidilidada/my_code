import pytest
import os, sys

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import * 

# 实现user_login公用
@pytest.fixture(scope='function')  # 这个方法针对于方法有效
def user_login(request):
    url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
    data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    res = HttpRequestV2(url, data).request()
    # 或者:
    # res = HttpRequest.request(url=url, json=data)
    
    assert res.status_code == 200
    assert res.json()['code'] == 1

    return res.json()['data'][0]['token']
