import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumTools import my_find_element

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('http://43.138.178.63:81/login')

# 登录
driver.find_element(By.ID ,'name').send_keys('admin')
driver.find_element(By.ID ,'password').send_keys('123456')
# login_name_ipt = ('id', 'name')
# login_pass_ipt = ('id', 'password')
# my_find_element(driver, login_name_ipt).send_keys('admin')
# my_find_element(driver, login_pass_ipt).send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

# e = driver.find_element_by_xpath('//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
login_success = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
e = my_find_element(driver, login_success)
assert e.text == '系统首页'
print('登录成功')

# driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[4]/div/span').click()
# driver.find_element(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[4]/ul/li/a/text()').click()
case_manage = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[4]/div/span')
case_list = ('xpath', '//*[@id="popContainer"]/section/aside/div/ul/li[4]/ul/li/a')
my_find_element(driver, case_manage).click()
time.sleep(2)
my_find_element(driver, case_list).click()
# driver.find_element_by_xpath('//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[1]/form/div/div/div[1]/div/div[2]/div/span/input').send_keys('张三')
# driver.find_element_by_xpath('//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[1]/form/div/div/div[6]/div/div[1]/button').click()
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

