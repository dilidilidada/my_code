import pytest
import os, sys
import json 

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import *
from utils.ExcelTools import *

# 从excel读出数据, 存放到类外面作为公共变量
excel_datas = ExcelTools.read_excel(r'data\haimo_api.xlsx', '首页')

# 登录页面所有接口的测试用例
class TestIndex():
    # 1. 获取首页
    # 运行test前自动登录并且获取对应的返回值, 方法名就是返回值
    # 相当于关联
    def test_01_home_page(self, user_login):
        url = excel_datas[0][2]
        heasers = eval(excel_datas[0][3])
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == eval(excel_datas[0][6])
        assert res.json()['code'] == eval(excel_datas[0][7])

    # 2. 获取系统用户
    def test_02_get_system_user(self, user_login):
        url = excel_datas[1][2]
        heasers = eval(excel_datas[1][3])
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == eval(excel_datas[1][6])
        assert res.json()['code'] == eval(excel_datas[1][7])
    
    # 3. 今日录入报告
    def test_03_report_entry_daily(self, user_login):
        url = excel_datas[2][2]
        heasers = eval(excel_datas[2][3])
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == eval(excel_datas[2][6])
        assert res.json()['code'] == eval(excel_datas[2][7])    

    # 4. 月度录入报告
    def test_04_report_entry_monthly(self, user_login):
        url = excel_datas[3][2]
        heasers = eval(excel_datas[3][3])
        datas = eval(excel_datas[3][5])
        res = HttpRequest.request(url=url, headers=heasers, json=datas)
        assert res.status_code == eval(excel_datas[3][6])
        assert res.json()['code'] == eval(excel_datas[3][7])
    



