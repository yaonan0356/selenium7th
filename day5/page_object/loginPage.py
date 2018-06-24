#这种框架的设计思想，叫做page-object设计模式，是一种高级框架设计思想

#这种思想的主旨是把业务逻辑和代码技术分离开
#测试用例的类，专门负责业务逻辑
#元素定位和操作交给网页对象page-object类
#在page-object这个类中，把每个网页看成一个类
#其中网页中的每个元素看成类中的一个属性
#针对这个元素的操作，看成类中的一个方法
#元素的信息等位是名词性的，所以可以看成属性（成员变量）
#元素的操作是动词性的，所以看成是方法
#那么，下面我们封装一下登录这个网页


#这个类主要做的就是把元素定位和操作改一个易于理解的名字

#     driver.get("http://localhost/index.php?m=user&c=public&a=login")
#     driver.find_element_by_id("username").send_keys("yaonan")
#     driver.find_element_by_id("password").send_keys("123456")
#     driver.find_element_by_class_name("login_btn").click()
#     time.sleep(5)
#     welcometext = driver.find_element_by_partial_link_text("您好").text
#     self.assertEqual("您好 yaonan",welcometext)
#     print(welcometext)

#——>——>——>把上面的代码封装成下面在样子
# 1.打开注册页面
# login_page.open()
# # 2.输入用户名
# login_page.input_username()
# # 3.输入密码
# login_page.input_password()
# # 4.点击登录按钮
# login_page.clcik_login_button()
# # 5.在我的会员中心页面验证用户名是否显示正确
# member_center_page.verify_username()
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #为这个类创建一个构造函数
    #在Python中构造函数固定名字__init__
    def __init__(self,driver):
        #因为setup方法中已经创建一个浏览器，
        # 所以这里不需要新建浏览器，直接用

        #self.driver = webdriver.Chrome()
        self.driver =driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"

    def open(self):
        self.driver.get(self.url)
    #给参数设置默认值，如果调用方法时，传入一个新的用户名，那么使用新的
    # 如果调用方法时，不传参，那么使用默认值

    #python的元组，类似于数组
    #这句话的意思是声明了一个数组，叫username_input_loc
    #这个数组中有两个元素，分别是By .ID，username
    username_input_loc= (By .ID,"username")
    password_input_loc = (By.ID, "password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def input_name(self,username='yaonan'):
        # 这个类中涉及三个元素定位，因为元素定位不太稳定，经常需要修改，
        # 所以应该把定位方式声明成类中的一个属性
        #self.driver.find_element(*self.username_input_loc).send_keys(username)


        self.driver.find_element(*self.username_input_loc).send_keys(username)



    def input_password(self,password='123456'):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def clcik_login_button(self):
        #self.find_element_by_class_name("login_btn").click()
        self.driver.find_element(*self.login_button_loc).click()
