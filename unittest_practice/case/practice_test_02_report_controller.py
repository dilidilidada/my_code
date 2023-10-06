import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestCaseReportController(unittest.TestCase):
    
    def test_01_update_phonenum(self):
        s = Service('driver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        # driver.maximize_window
        driver.get('http://43.138.178.63:81')

        driver.find_element(By.ID, 'name').send_keys('admin')
        driver.find_element(By.ID, 'password').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

        time.sleep(2)
        # e = driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
        # assert e.text == '系统首页'
        # print('登录成功')
        driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[2]/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[2]/ul/li[1]/a').click()
        time.sleep(2)
        driver.find_element(By.ID, 'form_in_modal_phone').clear()
        driver.find_element(By.ID, 'form_in_modal_phone').send_keys('18677380000')
        driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div/div/div/form/div[8]/div/div/span/button').click()
        
        # time.sleep(2)
        # e = driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div/div/div/form/div[3]/div[2]/div/span')
        # print(e.text)
        # assert e.text == '18677380000'
        print('修改成功')

        time.sleep(5)
        driver.quit()

unittest.main()

