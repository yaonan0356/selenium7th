#1.登录后台
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")



driver.find_element_by_name("userverify").send_keys("1234")

driver.find_element_by_class_name("Btn").click()

#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品模块
driver.find_element_by_class_name("n11").click()
#4.输入商品名称
#driver.find_element_by_name("name").send_keys("苹果X")
#driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > "
 #                                   "dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("pingguo ")


driver.switch_to.frame(driver.find_element_by_id("mainFrame"))
driver.find_element_by_name("name").send_keys("苹果X")
#5.选择商品分类（双击或单击”选择当前分类“）
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
driver.find_element_by_id("jiafen").click()
#6.在下拉框中选择商品品牌
dropdown = driver.find_element_by_name("brand_id")
select = Select(dropdown)
select.select_by_visible_text("苹果 (Apple)")
#7.点击提交按钮
driver.find_element_by_class_name("button_search").click()
#根据以上7步编码，找出第一个不能实现的地方