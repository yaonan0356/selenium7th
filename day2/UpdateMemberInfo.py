#1.登录海盗商城
#讲登录功能封装成一个方法，这样以后每次登录就只需要一行代码调用就可以了
from webbrowser import browser


#文件名，类名，包名，变量名，所有的命名都应该以字母开头，可以有数字和下划线
#但是不能有空格和中文
import time
from selenium import webdriver
from day2.loginTest import Login

driver = webdriver.Chrome()
#每次创建浏览器时，固定写一次，对再这个浏览器上执行的所有代码都生效
#implicitly_wait主要是检测页面的加载时间，检测什么时候页面加载完，什么时候执行后续的操作
driver.implicitly_wait(20)

#实例化对象会占用内存，Pycharm会自动帮我们释放内存
#代码运行完，检测到Login（）这个对象，不再被使用，系统会自动释放内存
#把driver浏览器传入到登录方法中
#让登录方法和下面的点击账号设置使用同一个浏览器
#我们现在已经创建好了一个空白的浏览器，后续的所有的操作都应该在这个浏览器上执行
Login().LoginWithDefaultUser(driver)


# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://localhost")
# driver.get("http://localhost/index.php?m=user&c=public&a=login")
# driver.find_element_by_id("username").send_keys("yaonan")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_class_name("login_btn").click()
# #2.点击账号设置
#本来要点"账号设置"，需要使用driver这个变量，但是现在文件中没有driver变量了，怎么办？
#可以重新申请一个driver吗？不能


# time.sleep(4)
driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
# time.sleep(4)
#partial_link_text可以使用链接中的一部分进行元素定位
#当链接文本过长时，推荐partial_link_text
#使用partial_link_text方法时，可以用链接中的任意一部分，只要字在网页中唯一即可
#driver.find_element_by_link_text("个人资料").click()
#driver.find_element_by_partial_link_text("个人资料").click()
#xpath的方法比较通用，可以用工具自动生成，但是不推荐使用，做为一种没有方法时使用
#因为xpath的可读性，和可维护性比较差
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
# #4.修改真实姓名
#如果输入框中原本有内容，那么我们修改内容时，要先清空，用clear（）方法
#实际上，良好的编程习惯是在每次sendkeys之前，都应该先做clear（）操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("姚楠")
# #5.修改性别
#通过观察，可以发现，保密，男，女三者的唯一区别就是value属性值不同
#实际上我们可以通过任何属性来定位
#要想通过Value属性定位有两种方法：xpatch和css_selector
#通过css_selector定位元素，只需要在唯一属性的两边加一对中括号即可
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中//表示采用相对路径定位元素
#/单斜杠表示绝对路径，一般都是从/html开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般通过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到的节点比较多，当开发人员修改页面布局时，受到影响的可能性比较大代码的稳定性比较差
#相对路径，查询速度比较慢，因为可能需要遍历更多的节点
#工作中一般用绝对还是相对路径？工作中推荐用css_selector，因为查询速度比xpath快一点
#xpath在某些浏览器上支持不太好，比如IE8
#css_selector所有的前端开发都会用，易于沟通交流
#*星号表示任意节点
#[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()
#Javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
#然后下标选取其中的第n个元素，也可以用于定位，对不对
#selenium可不可以用这种思路在定位？
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
#一下一下点年，月，日是可以实现的
#但是稳定性比较差，很容易点错
#并且很难修改日期，尽量不要click（）点击日期
#我们右键检查，可以发现日历控件是一个文本输入框
#那么我们可不可以用sendkeys的方法来输入一下日期
#因为readonly属性，写一个javascript脚本
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')


driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1987-11-20")
#7.修改QQ
driver.find_element_by_id("qq").send_keys("927105935")
#8.点击确认按钮，保存成功
driver.find_element_by_class_name("btn4").click()
time.sleep(4)
driver.switch_to.alert.accept()