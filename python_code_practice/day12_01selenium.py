from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# driver.maximize_window()

e = driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]')
print(e)

# time.sleep(20)
# driver.quit()


