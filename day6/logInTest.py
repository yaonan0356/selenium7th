from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("yaonan")
driver.find_element_by_id("password").send_keys("123456")
        # 5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()

#WebDriverWait(driver,20,0.5).until(expected_conditions.)
WebDriverWait(driver,20,0.5).until(EC._element_if_visible(driver.find_element_by_link_text("进入商城购物")))
driver.find_element_by_link_text("进入商城购物").click()


