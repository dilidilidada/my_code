from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 定位方式: 八大定位, 面试95%问定位
# 能用id就id, 不能就xpath
# id值唯一, 快, 准; xpath: 方便, 慢
# id定位
driver.find_element(By.ID,'kw').send_keys('大海')  # 输入文本值
driver.find_element(By.ID, 'su').click()  # 点击
time.sleep(100)
driver.close()

'''
● 1. ID定位 find_element(By.ID,value='')
优点: ID是唯一的, 定位速度快。
缺点: 有些元素没有ID, 不适用。

● 2. Name定位  find_element(By.NAME,value=" ")
优点: Name属性通常是唯一的, 定位速度快。
缺点: 有些元素没有Name属性, 不适用。

● 3. Class Name定位  find_element(By.CLASS_NAME,value=" ")
优点: Class Name属性通常是唯一的, 定位速度快。
缺点: 有些元素没有Class Name属性, 不适用。

● 4. Tag Name定位 find_element(By.TAG_NAME,value=" ")
优点: Tag Name属性通常是唯一的, 定位速度快。
缺点: 有些元素没有Tag Name属性, 不适用。

● 5. Link Text定位  find_element(By.LINK_TEXT,value=" ")
优点: Link Text属性通常是唯一的, 定位速度快。
缺点: 只适用于链接。

● 6. Partial Link Text定位  find_element(By.PARTIAL_LINK_TEXT,value=" ")
优点: Partial Link Text属性通常是唯一的, 定位速度快。
缺点: 只适用于链接。

● 7. CSS Selector定位  find_element(By.CSS_SELECTOR,value=" ")	
优点: CSS Selector可以通过多个属性组合定位元素, 定位灵活。
缺点: CSS Selector语法较为复杂, 学习成本较高。

● 8. XPath定位  find_element(By.XPATH,value=" ")
优点: XPath可以通过多个属性组合定位元素, 定位灵活。
缺点: XPath语法较为复杂, 定位速度较慢。
'''

