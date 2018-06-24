import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这是这个类不需要再写SetUp和tearDown方法了

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("yaonan")
        driver.find_element_by_id("password").send_keys("123456")
        old_title = driver.title
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(5)
        new_title = driver.title
        print("旧页面"+ old_title)
        print("新页面"+ new_title)
        self.assertNotEqual(old_title,new_title)





if __name__ == '__main__':
    unittest.main()