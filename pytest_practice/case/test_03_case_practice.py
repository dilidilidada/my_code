import pytest
import os, sys
import json
import random

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import *

patientName = 'test{}'.format(random.randint(100000,999999))  # 随机生成用户名
print(patientName)

class TestCaseList():
    '''
        病例管理
    '''
    def test_01_search_case(self, user_login):
        '''
            用户名搜索
        '''
        url = 'http://43.138.178.63:81/haimo/sass/case/sassListCase/10/1'
        heasers = {'token':user_login}
        datas = {"patientName":"牛"}
        res = HttpRequest.request(url=url, headers=heasers, json=datas)
        assert res.status_code == 200
        assert res.json()['code'] == 1         

    def test_02_search_case(self, user_login):
        '''
            电话号码搜索
        '''
        url = 'http://43.138.178.63:81/haimo/sass/case/sassListCase/10/1'
        heasers = {'token':user_login}
        datas = {"phone":"412"}
        res = HttpRequest.request(url=url, headers=heasers, json=datas)
        assert res.status_code == 200
        assert res.json()['code'] == 1

    def test_03_search_case(self, user_login):
        '''
            性别搜索
        '''
        url = 'http://43.138.178.63:81/haimo/sass/case/sassListCase/10/1'
        heasers = {'token':user_login}
        datas = {"gender":2}
        res = HttpRequest.request(url=url, headers=heasers, json=datas)
        assert res.status_code == 200
        assert res.json()['code'] == 1

    def test_04_search_case(self, user_login):
        '''
            新增病例
        '''
        url = 'http://43.138.178.63:81/haimo/sass/case/saveCase'
        heasers = {'token':user_login}
        datas = {"patientName":patientName,"gender":1,"age":"4","month":"2","samplingTime":"2023-09-27","hospitalId":34,"departmentId":83,"testNumber":"12","specimenBarcode":"1234","caseReportDTOS":[]}
        res = HttpRequest.request(url=url, headers=heasers, json=datas)
        assert res.status_code == 200
        assert res.json()['code'] == 1

        # 数据库校验
        add_case_sql = "select * from tb_case where patient_name='{}'".format(patientName)
        res = MysqlTools().query(add_case_sql)
        assert len(res) != 0

    # @pytest.mark.skip('test_05_search_case')  # 跳过执行
    def test_05_search_case(self, user_login):
        '''
            删除病例
        '''
        # 取病例id
        get_csase_id_sql = "select id from tb_case where patient_name='{}'".format(patientName)
        case_id_res = MysqlTools().query(get_csase_id_sql)

        url = 'http://43.138.178.63:81/haimo/sass/case/deleteCase/{}'.format(case_id_res[0][0])
        heasers = {'token':user_login}
        res = HttpRequest.request(url=url, headers=heasers)
        assert res.status_code == 200
        assert res.json()['code'] == 1

        # 数据库校验
        delete_case_sql = "select * from tb_case where id={} and is_true=0".format(case_id_res[0][0])
        assert len(MysqlTools().query(delete_case_sql)) != 0



