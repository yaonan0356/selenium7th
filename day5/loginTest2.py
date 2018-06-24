import unittest

import time

from day5.myTestCase import MyTestCase
from day5.page_object.loginPage import LoginPage
from day5.page_object.memberCenterPage import MemberCenterPage


class LoginTest2(MyTestCase):
    #这是这个类不需要再写SetUp和tearDown方法了

     def test_login(self):
    #     driver = self.driver
    #     driver.get("http://localhost/index.php?m=user&c=public&a=login")
    #     driver.find_element_by_id("username").send_keys("yaonan")
    #     driver.find_element_by_id("password").send_keys("123456")
    #     driver.find_element_by_class_name("login_btn").click()
    #     time.sleep(5)
    #     welcometext = driver.find_element_by_partial_link_text("您好").text
    #     self.assertEqual("您好 yaonan",welcometext)
    #     print(welcometext)
    #

        #1.打开注册页面
        #要想调用封装好的login page类中封装好的open（），
        #首先必须实例化LoginPage的对象
        login_page  =  LoginPage(self.driver)
        login_page.open()
        #2.输入用户名
        login_page.input_name()
        #3.输入密码
        login_page.input_password()
        #4.点击登录按钮
        login_page.clcik_login_button()
        #5.在我的会员中心页面验证用户名是否显示正确



        member_center_page = MemberCenterPage(self.driver)

        self.assertEqual(member_center_page.get_welcome_link_text(),"您好 yaonan")




        #应该把代码写成和手工测试用例一样的感觉
        #这样别人一看你的代码就知道你测试用例设计的业务逻辑是否正确





if __name__ == '__main__':
    unittest.main()