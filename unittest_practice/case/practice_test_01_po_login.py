import time, unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import my_find_element
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage

class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('driver\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver.maximize_window
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.admin_login_page.open_url()

    def test_01_login_success(self):
        self.admin_login_page.login('admin', '123456')
        e = my_find_element(self.driver, self.admin_login_page.login_success)
        assert e.text == '系统首页'
        print('登录成功')

    def test_02_login_fail(self):
        self.admin_login_page.login('admin', '12345')
        e = my_find_element(self.driver, self.admin_login_page.login_fail)
        assert e.text == '用户名或密码错误'
        print('登录失败')

unittest.main()
