from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.find_element_by_link_text("登录").click()

#driver.switch_to.window(second window name)

#driver.window_handles

#driver.window_handles[1]
driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_name("keyword").send_keys("iphone")