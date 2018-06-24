#selenium执行javascript中的两个关键字：reture(返回值)和arguments(参数)
import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://172.31.15.27:8081/")

driver.implicitly_wait(20)



#点击登录链接
#用javascript的方法找登录链接的代码
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#selenium的方法找登录链接的代码：
#driver.find_element_by_link_text("登录")
#某些元素，用selenium的方法找元素比Javascript更容易
#虽然selenium不支持removeAttribute的方法
#但是selenium找到登录链接和javascript找到的是同一元素
#我们可不可以用selenium找到元素之后，转换成Javascript的元素？
#这样以后写JavaScript就容易很多，不需要childNodes这些方法了
#比如，driver.find_element_by_link_text("登录").removeAttribute()
login_link = driver.find_element_by_link_text("登录")

driver.execute_script("arguments[0].removeAttribute('target')",login_link)

login_link.click()


driver.find_element_by_id("username").send_keys("yaonan")
#driver.find_element_by_id("password").send_keys("123456")
#driver.find_element_by_class_name("login_btn").click()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()

driver.find_element_by_link_text("进入商城购物").click()

driver.find_element_by_name("keyword").send_keys("iphone")

driver.find_element_by_name("keyword").submit()

product_link_xpath = "/html/body/div[3]/div[2]/div[3]/div/div[1]/a"

iphone = driver.find_element_by_xpath(product_link_xpath)

driver.execute_script("arguments[0].removeAttribute('target')",iphone)

iphone.click()
#在商品详情页面点击加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
#练习
#driver.find_element_by_css_selector(".shopCar_T_span3")
#点击结算按钮
driver.find_element_by_class_name("shopCar_btn_03").click()
#
#driver.find_element_by_css_selector(".shopCar_btn_03.f1").click()

#点击添加新地址
driver.find_element_by_class_name("add-address").click()

#iframe = driver.find_element_by_class_name("aui_title")

#driver.switch_to.frame(iframe)

time.sleep(3)

driver.find_element_by_name("address[address_name]").send_keys("张三")
driver.find_element_by_name("address[mobile]").send_keys("1512345678")


#下拉框是一张特殊的网页元素，对下拉框的操作和普通网页元素

dropdown1 = driver.find_element_by_id("add-new-area-select")
#下拉框是一张特殊的网页元素，对下拉框的操作和普通网页元素
#selenium为这种特殊元素，专门创建了一个类Select
#dropdown1的类型是一个普通的页面元素，下面这句代码的意思是，把一个普通的网页类型，转换成一个下拉框的特殊网页元素
print(type(dropdown1)) #dropdown1是Web_element类型
#Web_element这个类中，只有click和send_keys这样的方法，没有选择下拉框选项的方法
select1 = Select(dropdown1)
print(type(select1)) #select1是Selcet

#转换成select类型之后，网页元素还是那个元素，但是Select类中有选择项的方法
select1.select_by_value("320000")   #这时，我们可以通过选项值来定位

time.sleep(2)
select1.select_by_visible_text("辽宁省")    #也可以通过选项的文本信息来定位

#可以用find_elements的方法，先找页面上所有的
#下标的方式选择第N个页面元素
dropdown2 = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("沈阳市")

#dropdown3 = driver.find_elements_by_class_name("add-new-area-select")[2] #等同于下面这句
#tag_name()这个方法，大多数情况都能找到一对元素，所以find_element_tag_name（）这个方法很少用
#但是find_elements_tag_name（）[n]这个方法
dropdown3 = driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("铁西区")

driver.find_element_by_name("address[address]").send_keys("辽宁省沈阳市铁西区")

driver.find_element_by_name("address[zipcode]").send_keys("300000")

driver.find_element_by_class_name("aui_state_highlight").click()



#输入收货人等信息（选择地区下午讲）
#点击保存收货人信息



