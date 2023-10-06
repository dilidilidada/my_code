from selenium.webdriver.support.ui import WebDriverWait

def my_find_element(driver, locator, timeout=60):
    '''
        方法: 动态查找元素, 显式等待
        参数: 
            locator: 元素定位的方式和值
                -('id', 'kw')  # driver.find_element_by_id('kw')
                -('xpath', 'xxx')  
                -('name', 'xxx')
                -('css selector', 'xxx')
                -('class name', 'xxx')  # driver.find_element_by_class_name
                -('link text', 'xxx')  # driver.find_element_by_link_text
                -('partial', 'xxx')  # driver.find_element_by_partial_link_text
            timeout: 找元素的超时时间, 默认60   
        返回值: 找到则返回元素, 否则报错, 返回timeout
    '''

    # 匿名方法: 把一个方法当成参数来传递 
    return WebDriverWait(driver, timeout).until(lambda s:s.find_element(*locator))


