#用unittest写一个后台登录的测试用例
#1.导包

import unittest
#
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class loginTest(unittest.TestCase):
#重写
    @classmethod
    def setUpClass(self):
        #做web自动化测试，是不是所有的测试用例都要先打开
         self.driver = webdriver.Chrome()

         self.driver.implicitly_wait(10)
        #窗口最大化的代码，要求驱动版本必须和浏览器请准匹配
         self.driver.maximize_window()

    # 4个空格，在pycharm中可以用TAB键代替
    #对于初学者，或者找工作来讲，格式是最重要
    #算法是程序的灵魂，个人认为，格式是程序的外表
    #外表比灵魂重要
    @classmethod
    def tearDownClass(self):
        #为了保证看清测试结果，可以在teardown方法中加一个30秒的延时等待
        time.sleep(30)
        #每次执行完测试用例，应该把打开的浏览器关闭，释放内存，清除cookie和缓存，为下次执行测试用例做准备
        #这里面调用的driver是声明在setup方法中的局部变量，局部变量是不允许被其他方法访问的，
        # 所以我们应该把setup方法中的声明的driver改成一个全局变量
        #因为self表示类本身，所以我们只要在变量前加上self.，就表示这个变量是属于类的
        self.driver.quit()

    def test_login(self):
        #因为每次使用driver变量时，都需要前面加一个self.
        #为了简化代码，可以把成员变量self.driver,赋值给局部变量driver
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        #有些常用的键也可以用转义字符代替，其中\t表示TAB键，\n表示enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_add(self):
        driver = self.driver
        #添加商品的代码
     #如果第二个方法重新打开一个浏览器，登录就无效了，怎么办？
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_class_name("n11").click()
        driver.switch_to.frame(driver.find_element_by_id("mainFrame"))
        driver.find_element_by_name("name").send_keys("苹果X")
        driver.find_element_by_id("1").click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        #driver.find_element_by_id("7").click()
        #driver.find_element_by_id("jiafen").click()
        #双击
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        dropdown = driver.find_element_by_name("brand_id")
        select = Select(dropdown)
        select.select_by_visible_text("苹果 (Apple)")
        driver.find_element_by_class_name("button_search").click()

if __name__ == '__main__':
    unittest.main()