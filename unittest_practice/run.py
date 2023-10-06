# 项目运行入口
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1. 自动加载所有的测试用例
# 到case文件夹下面去找名为test_*.py的所有测试用例
test_case = unittest.defaultTestLoader.discover('case', 'test_*.py')

# 2. 使用htmitestrunner自动运行所有的测试用例并且生成测试报告
file_path = 'report/report.html'
title = '测试报告'
descr = '这是unittest + selenium的测试报告'
with open(file=file_path, mode='wb') as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(test_case)


