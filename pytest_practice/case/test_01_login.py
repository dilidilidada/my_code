import pytest
import os, sys

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import *

# 登录页面所有接口的测试用例
class TestLogin:
    # 接口请求代码
    def test_01_login_success(self, user_login):
        assert len(user_login) != 0





