import time, unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import find_element

class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('driver\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver.maximize_window

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://43.138.178.63:81/login')

    def test_01_login_success(self):
        self.driver.find_element(By.ID, 'name').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

        time.sleep(3)
        e = self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
        assert e.text == '系统首页'
        print('登录成功')

    def test_02_login_fail(self):
        self.driver.find_element(By.ID, 'name').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('1234567')
        self.driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

        time.sleep(3)
        e = self.driver.find_element(By.XPATH, '/html/body/div[2]/span/div/div')
        assert e.text == '用户名或密码错误'
        print('登录失败')

# unittest.main()
