# import random
# import pytest

# @pytest.fixture(scope='function')  # 这个方法针对于方法有效
# def f1(request):
#     patientName = 'test{}'.format(random.randint(100000,999999))  # 随机生成用户名
#     return patientName
    
# def f2(f1):
#     a = f1
#     print(a)

a = {'patientName': '张三', 
     'gender': 1, 
     'age': '4', 
     'month': '2', 
     'samplingTime': '2023-09-27', 
     'hospitalId': 34, 
     'departmentId': 83, 
     'testNumber': '1234', 
     'specimenBarcode': '1234', 
     }
