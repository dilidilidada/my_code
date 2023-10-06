'''
pageobjectmodel: 
selenium编程方法, 把页面中用到的元素和要执行的方法封装到类中, 测试用例通过去调用类的方式来实现自动化测试
方便脚本维护
'''
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\unittest_practice')
from utils.SeleniumTools import my_find_element

class AdminLoginPage():
    # 构造方法: 初始化成员变量
    # step1: 封装要用到的元素
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://43.138.178.63:81/login'
        self.name = ('id', 'name')
        self.password = ('id', 'password')
        self.login_btn = ('xpath', '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button')

        self.login_success = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
        self.login_fail = ('xpath', '/html/body/div[2]/span/div/div')

    # step2: 封装动作
    def open_url(self):
        self.driver.get(self.url)  # 打开登录网页

    # 登录的动作
    def login(self, name, password):
        my_find_element(self.driver, self.name).send_keys(name) 
        my_find_element(self.driver, self.password).send_keys(password)    
        my_find_element(self.driver, self.login_btn).click()

