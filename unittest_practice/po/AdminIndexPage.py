import sys, time
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import my_find_element

class AdminIndexPage():
    def __init__(self, driver):
        self.driver = driver
        self.system_setting = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[2]/div')
        self.report_setting = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[2]/ul/li[1]/a')
        self.phone_del = ('id', 'form_in_modal_phone')
        self.phone_update = ('id', 'form_in_modal_phone')
        self.phone_save = ('xpath', '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div/div/div/form/div[8]/div/div/span/button')
        
    def open_report_page(self):
        my_find_element(self.driver, self.system_setting).click()
        time.sleep(1)
        my_find_element(self.driver, self.report_setting).click()
        time.sleep(1)

    def phonenum_update(self):    
        my_find_element(self.driver, self.phone_del).clear()
        my_find_element(self.driver, self.phone_update).send_keys('18677380000')
        my_find_element(self.driver, self.phone_save).click()
    

