import time, unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import my_find_element

class TestCaseReportController(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     s = Service('driver\chromedriver.exe')
    #     cls.driver = webdriver.Chrome(service=s)
    #     # cls.driver.maximize_window

    # def setUp(self):
    #     self.driver.get('http://43.138.178.63:81')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_01_update_phone(self):
        s = Service('driver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        # driver.maximize_window
        driver.get('http://43.138.178.63:81')

        name = ('id', 'name')
        password = ('id', 'password')
        login_click = ('xpath', '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button')
        my_find_element(driver, name).send_keys('admin')
        my_find_element(driver, password).send_keys('123456')
        my_find_element(driver, login_click).click()

        system_setting = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[2]/div')
        report_setting = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[2]/ul/li[1]/a')
        phone_del = ('id', 'form_in_modal_phone')
        phone_update = ('id', 'form_in_modal_phone')
        phone_save = ('xpath', '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div/div/div/form/div[8]/div/div/span/button')
        
        my_find_element(driver, system_setting).click()
        time.sleep(1)
        my_find_element(driver, report_setting).click()
        time.sleep(1)
        my_find_element(driver, phone_del).clear()
        my_find_element(driver, phone_update).send_keys('18677380000')
        my_find_element(driver, phone_save).click()

        print('修改成功')

        time.sleep(3)
        driver.quit()

unittest.main()

