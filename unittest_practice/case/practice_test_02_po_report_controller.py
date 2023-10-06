import time, unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import my_find_element
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage

class TestCaseReportController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('driver\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver.maximize_window
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)

    def setUp(self):
        # self.driver.get('http://43.138.178.63:81')
        self.admin_login_page.open_url()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_update_phone(self):
        
        # 登录
        self.admin_login_page.login('admin', '123456')

        # 进入修改页面
        self.admin_index_page.open_report_page()
        # 修改电话
        self.admin_index_page.phonenum_update()

        print('修改成功')

        time.sleep(3)
        self.driver.quit()

unittest.main()

