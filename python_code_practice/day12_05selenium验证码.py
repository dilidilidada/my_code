'''
登录验证码:
    1. 万能码 开发留后门(出事要寄)
    2. 打码平台: 贵
    3. 机器学习: 技术要牛逼
    4. cookie绕过
        1) 手动登录并且获取到已登录账号的cookie
        2) 使用已经登录的cookie去访问网站 
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumTools import my_find_element

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('http://43.138.178.63:81/login')

# 登录
time.sleep(10)
# 手动输入账号密码
cookies = driver.get_cookies()
print(cookies)
# driver.delete_all_cookies()  # 因为每次访问服务器都会给客户端一个cookie, 第一次访问cookie是未登录
# cookie = {'domain': '43.138.178.63', 'httpOnly': False, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'T9iDoQCHHeH1dmfnJt7CkI5R7Av6N4bfwHTbp3d/z3E='}
# driver.add_cookie(cookie)
# driver.refresh()  # 带着已经登 录的cookie去刷新网站, 服务器会接收到这个登录的cookie并允许访问


login_success = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
e = my_find_element(driver, login_success)
assert e.text == '系统首页'
print('登录成功')

case_manage = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[4]/div/span')
case_list = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[4]/ul/li/a')
my_find_element(driver, case_manage).click()
time.sleep(2)
my_find_element(driver, case_list).click()
time.sleep(2)

search_ipt = ('xpath', '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[1]/form/div/div/div[1]/div/div[2]/div/span/input')
search_btn = ('xpath', '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[1]/form/div/div/div[6]/div/div[1]/button')
my_find_element(driver, search_ipt).send_keys('张三')
my_find_element(driver, search_btn).click()

search_result = ('xpath', '//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[3]/td[2]')
e = my_find_element(driver, search_result)
assert e.text == '张三'
print('搜索成功')

time.sleep(5)
driver.quit() 

