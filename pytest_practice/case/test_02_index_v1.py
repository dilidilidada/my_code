import pytest
import os, sys
import json 

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import *

# 登录页面所有接口的测试用例
class TestIndex():
    # 1. 获取首页
    # 运行test前自动登录并且获取对应的返回值, 方法名就是返回值
    # 相当于关联
    def test_01_home_page(self, user_login):
        url = 'http://43.138.178.63:81/haimo/sass/homePage/sassHomePage'
        heasers = {'token':user_login}
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == 200
        assert res.json()['code'] == 1

    # 2. 获取系统用户
    def test_02_get_system_user(self, user_login):
        url = 'http://43.138.178.63:81/haimo/sass/systemUser/getSystemUser'
        heasers = {'token':user_login}
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == 200
        assert res.json()['code'] == 1
    
    # 3. 今日录入报告
    def test_03_report_entry_daily(self, user_login):
        url = 'http://43.138.178.63:81/haimo/sass/homePage/reportEntryDaily'
        heasers = {'token':user_login}
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == 200
        assert res.json()['code'] == 1    

    # 4. 月度录入报告
    def test_04_report_entry_monthly(self, user_login):
        url = 'http://43.138.178.63:81/haimo/sass/homePage/reportEntryMonthly'
        heasers = {'token':user_login}
        data = {"date":1695730499000}
        res = HttpRequest.request(url=url, headers=heasers, json=data)
        assert res.status_code == 200
        assert res.json()['code'] == 1



