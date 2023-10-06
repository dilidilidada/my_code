import pytest
import os, sys
import json
import random

# 把当前文件夹添加到环境变量中实现跨文件夹导入
sys.path.append(os.getcwd())
from utils.HttpRequest import *
from utils.MysqlTools import *
from utils.ExcelTools import *

# 从excel读出数据, 存放到类外面作为公共变量
excel_datas = ExcelTools.read_excel(r'data\haimo_api.xlsx', '病例管理')

class TestCaseList():
    '''
        病例管理
    '''  
    @pytest.mark.skip('test_02_list_case')  # 跳过执行
    @pytest.mark.parametrize('datas', eval(excel_datas[0][5]))
    def test_02_list_case(self, user_login, datas):
        '''
            病例列表
        '''
        url = excel_datas[0][2]
        headers = eval(excel_datas[0][3])
        res = HttpRequest.request(url=url, headers=headers, json=datas)
        assert res.status_code == eval(excel_datas[0][6])
        assert res.json()['code'] == eval(excel_datas[0][7])

    def test_03_add_case_success(self, user_login):
        url = excel_datas[1][2]
        headers = eval(excel_datas[1][3])
        datas = eval(excel_datas[1][5])
        res = HttpRequest.request(url=url, headers=headers, json=datas)

        assert res.status_code == eval(excel_datas[1][6])
        assert res.json()['code'] == eval(excel_datas[1][7])

        add_case_ok_sql = """
                        SELECT * FROM tb_case WHERE
                            patient_name = '{}'
                            AND gender ={}
                            AND age ={}
                            AND `month` ={}
                            AND specimen_barcode = '{}'
                            AND test_number = '{}'
                            AND hospital_id = {}
                            AND department_id = {}
                    """.format(
                        datas["patientName"], 
                        datas["gender"], 
                        datas["age"], 
                        datas["month"],
                        datas["specimenBarcode"],
                        datas["testNumber"],
                        datas["hospitalId"],
                        datas["departmentId"],
                        )
        # print(add_case_ok_sql)






