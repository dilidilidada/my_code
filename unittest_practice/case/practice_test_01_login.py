import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 类的继承: unittest.TestCase
class TestCaseLogin(unittest.TestCase):
    # setUpclass: 解决浏览器重复打开的问题
    # 修饰符, 表示下面的第一个方法是类方法(成员方法)
    @classmethod
    # 类的前置方法
    # cls = self: 目的是为了把driver变成全局变量, 使driver可以在不同的方法里使用
    def setUpClass(cls):
        s = Service('driver\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver.maximize_window

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 固定的, 前置方法
    def setUp(self):
        self.driver.get('http://43.138.178.63:81/login')

    def test_01_login_success(self):
        # selenium代码
        # s = Service('driver\chromedriver.exe')
        # driver = webdriver.Chrome(service=s)
        # driver.maximize_window
        # self.driver.get('http://43.138.178.63:81/login')

        self.driver.find_element(By.ID, 'name').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

        time.sleep(3)
        e = self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
        print(e.text)
        assert e.text == '系统首页'
        print('登录成功')

    @unittest.skip
    def test_02_login_fail(self):
        # s = Service('driver\chromedriver.exe')
        # self.driver = webdriver.Chrome(service=s)
        # driver.maximize_window
        # self.driver.get('http://43.138.178.63:81/login')

        self.driver.find_element(By.ID, 'name').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('1234567')
        self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

        time.sleep(3)
        e = self.driver.find_element(By.XPATH, '/html/body/div[2]/span/div/div')
        assert e.text == '用户名或密码错误'
        print('登录失败')

        # time.sleep(2)
        # self.driver.quit()

# unittest.main(), 需要在类的外面
unittest.main()

'''
测试结果:
1. .: 成功
2. F: 断言失败
3. E: 代码有问题, 抛出异常

生命周期:
setUpClass(类开始运行时运行一次) -> 
setUp(每个test方法运行时运行一次) -> 
test_01 ->
tearDown01(每个test方法运行后运行一次) ->
setUp02 ->
test_02 ->
tearDown02 ->
... ->
tearDownClass

'''

'''
# 方法:
# 1. 普通方法
def add(a, b):
    return a + b

# 2. 类中的方法
# 1) 成员方法: 实例化对象后调用的方法
# 例:
# x = A()
# x.a()
class A():
    def a(self):
        pass
# 2) 类方法: 不直接用    
    @classmethod
    def b(cls):
        pass
# 3) 静态方法: 通过类名去调用
# 例:
# A.c()
    @staticmethod
    def c():
        pass  

# 3. 匿名方法: 把方法作为参数传递
# lambda s   
'''

