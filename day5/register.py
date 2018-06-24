import unittest

import time
from selenium import webdriver


from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


#2.继承unitest.Testcase



class RegisterTest(unittest.TestCase):
    #重写tearup和teardown
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        time.sleep(30)
        cls.driver.quit()

    #编写一个测试用例(以test开头)

    def test_register(self):
        for row in CsvFileManager4().reader('testdata.csv'):
            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #这两种方法没有任何区别，但是后面的 driver.find_element_by_name("username")扩展性更好，便于框架封装
            driver.find_element(By.NAME,"username")
            driver.find_element_by_name("username").send_keys([row[0]])
            driver.find_element(By.NAME,"password").send_keys([row[1]])
            driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
            driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME,"email").send_keys(row[4])

            check_tip = driver.find_element(By.CSS_SELECTOR,"form.registerform.sign > ul > li:nth-child(1) >div > span").text
            print(check_tip)
            '''
            if check_tip == "通过信息验证":
                print("passed")
            else:
                print("error")
            '''
            self.assertEqual("通过信息验证!", check_tip)

            #driver.find_element(By.CLASS_NAME,"reg_btn").click()

        #所以我们要采用ddt框架

if __name__ == '__main__':
    unittest.main()