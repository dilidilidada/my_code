# 框架入口
# 数据驱动不采用pytest/unittest脚本驱动方式
# 手写驱动
from re import L
import traceback
from utils.LogTools import logger
from utils.ExcelTools import ExcelTools
from utils.HttpRequest import HttpRequestV2

# p1: 每次都要写case_sheet，      - ok
# p2: 每次都要自己填token，       - ok
# p3: 测试报告怎么实现？        - 明天继续：邮件、短信、微信推送。。
# p4: 数据查询怎么办？

def get_all_case(case_path='./case/haimo_api.xlsx'):
    """
        读取excel中所有的测试用例
        返回值: {"病例原理":[[row1], [row2]], "首页":[[row1], [row2]]}
    """
    results = {}
    for sheet in ExcelTools.get_excel_sheets(case_path):
        results[sheet] = ExcelTools.read_excel(case_path, sheet)        #{"病例原理页面":[]}

    return results

def user_login():
    """
        每个方法登录前都要运行
    """
    url = "http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin"
    data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    res = HttpRequestV2(url, data).request()
    assert res.status_code == 200
    assert res.json()["code"] == 1
    return res.json()["data"][0]["token"]   # 返回登录成功的token

def case_runner(all_case):
    """    
        请求引擎
        循环请求所有的case
    """
    for sheet in all_case:
        logger.warning('-----------------------------------------------------------------------')
        logger.info("开始处理【{}】页面的接口,共发现{}条测试用例".format(sheet, len(all_case[sheet])))

        for case in all_case[sheet]:
            # 处理请求头和参数
            if case[5] == "-":
                case_data = {}
            else:
                case_data = eval(case[5])

            # 处理header，自动调用user_login，实现token的获取
            if case[3] == "-":
                case_header = {}
            else:
                case_header = eval(case[3])

                for k, v in case_header.items():
                    if k == "token":
                        case_header[k] = v()    # python反射调用 v = user_login v() == user_login()
            
            # 具体的参数
            case_id, case_url , case_name = case[0], case[2],  case[1]
            case_method, case_http_code, case_resu_code = case[4], int(case[6]), int(case[7])
            logger.info("开始处理测试用例【{}】".format(case_name))

            # try里面的代码报错，跳到excel执行，否则跳到else
            try:
                res = HttpRequestV2(case_url, case_data, case_header, case_method).request()
                assert res.status_code == case_http_code
                assert res.json()["code"] == case_resu_code
            except Exception as e:
                logger.error("测试用例【{}】执行失败, 失败原因：【{}】".format(case_name, traceback.format_exc()))
            else:
                logger.info("测试用例【{}】执行成功".format(case_name))

            # 数据库校验先放着

            logger.info("结束处理测试用例【{}】".format(case_name))
        logger.info("结束处理【{}】页面的接口".format(sheet))
        

if __name__ == "__main__":
    all_case = get_all_case()
    case_runner(all_case)

    # print(eval("user_login"))
    