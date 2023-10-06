# 测试用例:
# 1. excel, 分模块, 按照页面划分
# 2. test文件和测试方法
# 3. 接口测试用例设计:
#   1) 正常
#   2) 逆向场景:
#       ① 未登录: token失效/错误
#       ② 参数错误: 长度/内容/空值/未传

# 框架描述:
# 1. 采用脚本驱动的方式, 使用python+pytest+requests+pymysql+xlrd+allure完成框架的开发
#   1) pytest: 组织测试用例, 将普通脚本以类的形式集成, 实现测试报告
#   2) requests: 发送请求, 接收返回数据
#   3) pymysql: 数据库校验, 连接并操作数据库
#   4) xlrd: 读取excel文件, 将要测试的数据插入脚本中
#   5) allure: 实现测试报告
#   6) 接⼝⾃动化测试采⽤分层设计思想, 将不同作⽤的代码放到不同的⽂件夹下, 使⽤excel封装接⼝的信息，实现数据和脚本分离
#   7) 关联: 使用pytest的fixtrues实现接口参数之间的关联(让这个方法针对于方法有效)
#   8) 开发完测试用例后再做报告的集成

# 测试报告:
# 1. pytest-html: python -m pytest -s --html=./report/xxx/report.html, 太丑了, 一般不用
# 2. allure(配合jenkins集成):
#   1) java环境
#   2) 安装allure-commandline工具:
#       ① 解压
#       ② 配置环境变量: 全局/系统
#   3) 安装allure-pytest的第三方包: pip3 install allure-pytest 
#   4) 管理员身份重启vscode
#   5) 运行pytest命令: python -m pytest -s --aluredir=./report/result
#   6) 把测试结果编译成测试报告: allure generate ./report/result -o ./report/report
#   7) 打开测试报告: allure open ./report/report 






