# 这个文件用来实现一个登录功能的自动化操作

# 1.打开浏览器
import time
from selenium import webdriver
#


driver = webdriver.Chrome()
#driver.implicitly_wait(20)
# 2.打开海盗商城网站
driver.get("http://localhost/")
# 3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("yaonan")
driver.find_element_by_id("password").send_keys("123456")
# 5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()
# 6.检查登录是否成功
time.sleep(5)
username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text

print(username_text)

if username_text =='您好 yaonan':
    print("pass")
else:
    print("error")

#7.click"acess shoping"

#driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/span/a").click()
driver.find_element_by_link_text("返回商城首页").click()

driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()
driver.close()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id("joinCarButton").click()
