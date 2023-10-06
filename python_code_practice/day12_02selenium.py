from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://43.138.178.63:81/login')

driver.find_element(By.ID, 'name').send_keys('admin')
driver.find_element(By.ID, 'password').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="popContainer"]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()

# 断言
# time.sleep(15)
# assert driver.title == '海默医学报告管理系统 | 系统首页'

driver.implicitly_wait(5)  # 隐式等待
# find_elements()查找多个元素
# e = driver.find_elements(By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
# assert len(e) != 0

e = driver.find_element_by_xpath('//*[@id="popContainer"]/section/aside/div/ul/li[1]/a')
# print(e.text)
assert e.text == '系统首页'

print('登录成功')

time.sleep(15)
driver.quit()  # 关闭浏览器并退出测试

# 断言:
# 1. 判断元素是否存在
# 2. 判断文本值(推荐)

# 等待: 一般网页有跳转/元素动态加载时需要等待
# 1. 固定等待: time.sleep(5)
# 2. 隐式等待: driver.implicitly_wait(5)
# 3. 显式等待


