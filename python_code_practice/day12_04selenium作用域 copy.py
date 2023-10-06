'''
作用域: 新打开的窗口或者网页嵌套网页时, 需要切换作用域, 否则无法定位
    1. window:
            1) xxx = driver.window_handles 获取所有窗口的句柄
            2) driver.switch_to_window(xxx[-1]) 把作用域从原有窗口切换到最新的窗口, xxx[0]切回去
    2. iframe: 
            1) iframe = ('id', 'xxx')
            2) e = my_find_element(driver, iframe)
            3) driver.switch_to_frame(e) 把作用域从的网页切换到小网页
            4) driver.switch_to_default_content() 切回去
    3. alert:
        1) driver.switch_to_alert().accept() 确定按钮
        2) driver.switch_to_alert().dismiss() 取消按钮
'''
